// 初始化


frameApp.controller('studentCtrl', function ($scope,$http,$state) {

    $scope.trainingList = null;
    var trainingTable = null;

    $scope.traininggradeListOri = null;
    $scope.traininggradeList = null;
    var traininggradeTable = null;

    $scope.theList = null;

    $scope.currentPage = 1;
    $scope.totalNum = 0;
    $scope.pageSize = 10;

    $scope.isOneEditing = false; // 是否当前正在编辑一个信息，只允许一个正在编辑

    $scope.trainingSelected = null;
    $scope.traininggradeSelected = null;

    $scope.filter = {
        training_id      : null,
        traininggrade_id : null,
        name : null

    };

    function listToTable(thelist){
        var table = {};
        for (var i=0; i<thelist.length;i++){
            var one = thelist[i];
            table[one.id] = one;
        }
        return table;
    }

    $scope.pageChangeTo = function(pageNumber) {
        var url = '/api/mgr/sq_mgr/?action=list_student&pagenum='+pageNumber  + '&pagesize='+$scope.pageSize;
        if ($scope.filter.training_id)
            url += '&training_id='+ $scope.filter.training_id;
        if ($scope.filter.traininggrade_id)
            url += '&traininggrade_id='+ $scope.filter.traininggrade_id;
        if ($scope.filter.name)
            url += '&name='+ $scope.filter.name;

        Util.angular_get($http,
            url,
            function (ret) {

                if (ret.total==0 && $scope.currentPage>1){
                    $scope.currentPage-=1;
                    return;
                }


                $scope.theList = ret.retlist;
                $scope.totalNum = ret.total;



                // 解码 starttime, endtime
                for (var i=0; i<$scope.theList.length;i++){

                    var stStr = $scope.theList[i].startcoursedate;
                    $scope.theList[i].startcoursedate = new Date(stStr);

                }

            }
        );

    };


    $scope.startSearch = function() {
        $scope.pageChangeTo(1);
        $scope.clearCheckins()
    }


    // 得到培训班/班期 列表,成功后获取学生列表

    Util.angular_get($http,
        '/api/mgr/sq_mgr/?action=list_training&pagenum=1&pagesize=100',
        function (ret) {

            $scope.trainingList = ret.retlist;
            trainingTable = listToTable(ret.retlist);
            Util.angular_get($http,
                '/api/mgr/sq_mgr/?action=list_training_grade&pagenum=1&pagesize=100',
                function (ret) {
                    $scope.traininggradeList = ret.retlist;
                    $scope.traininggradeListOri = ret.retlist;
                    traininggradeTable = listToTable(ret.retlist);
                    $scope.pageChangeTo(1);
                }
            );
        }
    );

    $scope.filter_trainingchanged = function() {

        var newTraininggradeList=[];
        for (var i=0;i<$scope.traininggradeListOri.length;i++){
            if($scope.traininggradeListOri[i].training__id == $scope.filter.training_id){
                newTraininggradeList.push($scope.traininggradeListOri[i])
            }
        }
        $scope.traininggradeList = newTraininggradeList;
        
        $scope.pageChangeTo(1);

    }





    // ************* add one  *************

    $scope.showAddOne=false;

    $scope.addEditData={

        username:'',
        realname:'',
        training_id:null,
        traininggrade_id:null,
        desc:'',
        startcoursedate:new Date(),
        password:'sq888',



    };


    $scope.addOne = function() {

        $scope.addEditData.username = $scope.addEditData.username.trim();
        $scope.addEditData.realname = $scope.addEditData.realname.trim();
        if ($scope.addEditData.username.length==0){
            BootstrapDialog.alert('请填写登录名');
            return
        }
        if ($scope.addEditData.realname.length==0){
            BootstrapDialog.alert('请填写真实姓名');
            return
        }
        var paramStr =  'action=add_student&data='+ encodeURIComponent(angular.toJson($scope.addEditData));


        Util.angular_post($http,
            '/api/mgr/sq_mgr/',
            paramStr,
            function(ret){
                $scope.pageChangeTo(1);
            });
    };


    // ************* edit one *************



    $scope.editOneBegin = function(one) {

        if($scope.isOneEditing){
            BootstrapDialog.alert('同时只能编辑一个，请先完成当前编辑!!');
            return
        }
        $scope.isOneEditing = true;
        one.editing=true;

        $scope.addEditData.username=one.username;
        $scope.addEditData.courses=one.courses;
        $scope.addEditData.realname=one.realname;
        $scope.addEditData.desc=one.desc;
        $scope.addEditData.graduated=one.graduated;

        // $scope.addEditData = JSON.parse(JSON.stringify(one))
    };
    $scope.editOneCancel = function(one) {

        one.editing=false;
        $scope.isOneEditing = false;
    };

    $scope.editOneSubmit = function(one) {

        one.editing = false;
        $scope.isOneEditing = false;


        var paramStr =  'action=modify_student&id='+one.id;
        paramStr += '&newdata='+encodeURIComponent(angular.toJson($scope.addEditData));


        Util.angular_put($http,
            '/api/mgr/sq_mgr/',
            paramStr,
            function(ret){
                $scope.pageChangeTo($scope.currentPage);
            });
    };



    $scope.delOne = function(one) {

        BootstrapDialog.confirm('确定删除吗?', function (result) {

            if (!result) {
                return;
            }

            var paramStr =  'action=delete_student&id='+one.id;
            Util.angular_delete($http,
                '/api/mgr/sq_mgr/',
                paramStr,
                function(ret){
                    $scope.pageChangeTo($scope.currentPage);
                });
        });


    };


    $scope.resetPasswd = function(one) {

        BootstrapDialog.confirm('确定重置密码?', function (result) {

            if (!result) {
                return;
            }

            var paramStr =  'action=changeuserpassword&uid='+one.userid;
            Util.angular_put($http,
                '/api/mgr/sq_mgr/',
                paramStr,
                function(ret){
                    BootstrapDialog.alert('重置密码成功，新密码为sq666')
                });
        });


    };

    $scope.showCheckins = function(one) {

        $state.go('student.checkin_history', { uid: one.id });

    };

    $scope.showCheckinsByCourse = function(one) {

        $state.go('student_checkin_by_course',{ uid: one.id } );

    };

    $scope.clearCheckins = function(one) {

        $state.go('student');

    };





});

