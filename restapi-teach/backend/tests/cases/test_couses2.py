import pytest
from ApiLib import AdminOperationSession



@pytest.fixture(scope='module')
def adminOpSession():
    print('\n======创建空白数据环境2======')
    aos = AdminOperationSession()
    aos.adminlogin('auto','sdfsdfsdf')

    aos.delete_all_course()

    return aos


class TestCourse:

    def test_listCourse(self,adminOpSession,couse1):
        # 先列出课程
        addRet = adminOpSession.list_course()
        assert addRet == {'retcode': 0, 'retlist': [], 'total': 0}


    def test_delCourse(self,adminOpSession):
        # 先添加课程
        addRet = adminOpSession.add_course(
            'python9', 'python 课程', 3)
        assert addRet['retcode'] == 0

        #再删除课程
        delRet = adminOpSession.delete_course(addRet['id'])
        assert  delRet['retcode'] == 0
