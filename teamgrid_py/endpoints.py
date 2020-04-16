#        _                         __    __           __   __      __         __
#       (_)___  ____  ____  __  __/ /_  / /___ ______/ /__/ /___ _/ /_  ___  / /
#      / / __ \/ __ \/ __ \/ / / / __ \/ / __ `/ ___/ //_/ / __ `/ __ \/ _ \/ /
#     / / /_/ / / / / / / / /_/ / /_/ / / /_/ / /__/ ,< / / /_/ / /_/ /  __/ /
#  __/ /\____/_/ /_/_/ /_/\__, /_.___/_/\__,_/\___/_/|_/_/\__,_/_.___/\___/_/
# /___/                  /____/
#
#
# author: Johannes Kunze
# date: 2018-05-01
# web: http://www.jonnyblacklabel.de/
# twitter: @jonnyblacklabel
#

from time import sleep


class EndpointBase():
    endpoint = ''

    def __init__(self, tg_base, *args, **kwargs):
        self.service = tg_base


class ReadOnly(EndpointBase):
    def get(self):
        """Get data from API
        Returns
        -------
        Response-Object
            TeamGridPyResponse
        """
        response = self.service.get(self.endpoint)
        self.service.params = {}
        return response


class ReadWrite(ReadOnly):
    def create(self, data):
        return self.service.create(self.endpoint, data)

    def update(self, id_, data):
        return self.service.update(self.endpoint, id_, data)

    def delete(self, id_):
        self.service.delete(self.endpoint, id_)


class Selectable(EndpointBase):
    def by_id(self, id_):
        """Get data from API for id
        Parameters
        ----------
        id_ : {int}
            Unique identifier
        Returns
        -------
        Response-Object
            TeamGridPyResponse
        """
        response = self.service.get(self.endpoint, id_=id_)
        self.service.params = {}
        return response


class Paginatable(EndpointBase):
    def get(self, page=1, limit=50):
        """Get data from API for requestet page
        Parameters
        ----------
        page : {number}, optional
            page for pagination (the default is 1, which is the first page)
        limit : {number}, optional
            number of results per page (the default is 50)
        Returns
        -------
        Response-Object
            TeamGridPyResponse
        """
        self.service.params = {
            **self.service.params,
            **{'page': page, 'limit': limit}
        }
        response = self.service.get(self.endpoint)
        self.service.params = {}
        return response

    def all(self):
        """Get all data from API
        Returns
        -------
        Response-Object
            TeamGridPyResponse
        """
        page = 1
        while True:
            print('request page ', page)
            self.service.params = {
                **self.service.params,
                **{'page': page, 'limit': self.service.limit}
            }
            response = self.service.get(self.endpoint)
            if hasattr(response, 'error'):
                result = response
                print(f'Error at page {page}.')
                break
            elif hasattr(response, 'data'):
                print(f'Page {page} | Rows {len(getattr(response, "data"))}')
                if page == 1:
                    result = response
                else:
                    result.__dict__['data'].extend(response.__dict__['data'])
            else:
                if response.statusCode == 204:
                    if page == 1:
                        result = response
                    print(f'No Data at page {page}.')
                    break
            page += 1
            sleep(0.6)
        sleep(2)
        self.service.params = {}
        return result


class Teams(ReadOnly):
    endpoint = 'teams'


class Users(ReadOnly):
    endpoint = 'users'

    def where(self, email):
        """filter users
        Parameters
        ----------
        email : {string}
            filter by email
        """
        self.service.params = {'email': email}
        return self


class Contacts(Paginatable, Selectable, ReadWrite):
    endpoint = 'contacts'


class Projects(Paginatable, Selectable, ReadWrite):
    endpoint = 'projects'


class Tasks(Paginatable, Selectable, ReadWrite):
    endpoint = 'tasks'

    def where(
            self,
            userId=None,
            contactId=None,
            projectId=None,
            completed=None):
        """filter request
        Parameters
        ----------
        userId : {int}, optional
            filter by userId
        contactId : {int}, optional
            filter by contactId
        projectId : {int}, optional
            filter by projectId
        completed : {bool}, optional
            filter by state
        """
        self.service.params = {
            'userId': userId,
            'contactId': contactId,
            'projectId': projectId,
            'completed': completed
        }
        return self


class Services(Paginatable, Selectable):
    endpoint = 'services'

    def where(
        self,
        name=None,
        billable=None,
        hourlyRate=None,
        createdAt=None,
        createdBy=None
    ):
        """filter services

        Args:
            name (string, optional): Display name of the Service. Defaults to None.
            billable (bool, optional): wether time entries assigned are billable. Defaults to None.
            hourlyRate (int, optional): hourly rate. Defaults to None.
            createdAt (string, optional): date '%Y-%m-%d'. Defaults to None.
            createdBy (string, optional): UID of User. Defaults to None.
        """
        self.service.params = {
            'name': name,
            'billable': billable,
            'hourlyRate': hourlyRate,
            'createdAt': createdAt,
            'createdBy': createdBy
        }
        return self

class Times(Paginatable, Selectable, ReadWrite):
    endpoint = 'times'

    def where(
            self,
            userId=None,
            taskId=None,
            serviceId=None,
            contactId=None,
            projectId=None,
            billed=None,
            startFrom=None,
            startTo=None,
            taskCompleted=None,
            projectCompleted=None,
            taskArchived=None,
            projectArchived=None):
        """filter times
        Parameters
        ----------
        userId : {int}, optional
        taskId : {int}, optional
        serviceId : {int}, optional
        contactId : {int}, optional
        projectId : {int}, optional
        billed : {string}, optional
            'true' 'false'
        startFrom : {string}, optional
            'yyyy-mm-dd'
        startTo : {string}, optional
            'yyyy-mm-dd'
        taskCompleted : {string}, optional
            'true' 'false'
        projectCompleted : {string}, optional
            'true' 'false'
        taskArchived : {string}, optional
            'true' 'false'
        projectArchived : {string}, optional
            'true' 'false'
        """
        self.service.params = {
            'userId': userId,
            'taskId': taskId,
            'serviceId': serviceId,
            'contactId': contactId,
            'projectId': projectId,
            'billed': billed,
            'startFrom': startFrom,
            'startTo': startTo,
            'taskCompleted': taskCompleted,
            'projectCompleted': projectCompleted,
            'taskArchived': taskArchived,
            'projectArchived': projectArchived
        }
        return self


if __name__ == '__main__':
    pass
