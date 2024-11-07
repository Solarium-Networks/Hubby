import Private
from Private import g
from github import Github

# set up the static variables
# None

class hubby:
    @staticmethod
    def setup():
        Private.AuthUser()

    @staticmethod
    def UserRepos():
        global user
        for repo in g.getuser().getrepos():
            print(repo.name)
    
    @staticmethod
    def GetStars(Owner, RepoName):
        RepoToGetStars = g.get_repo(f"{Owner}/{RepoName}")
        RepoToGetStars.stargazers_count

    @staticmethod
    def GetTopics(Owner, RepoName):
        RepoToGetTopics = g.get_repo(f"{Owner}/{RepoName}")
        RepoToGetTopics.get_topics()
    
    @staticmethod
    def GetIssues(Owner, RepoName):
        RepoToGetIssues = g.get_repo(f"{Owner}/{RepoName}")
        open_issues = RepoToGetIssues.get_issues(state='open')
        for issue in open_issues:
            print(issue)
    
    @staticmethod
    def GetAlerts(Owner, RepoName):
        RepoToGetAlerts = g.get_repo(f"{Owner}/{RepoName}")
        codescan_alerts = RepoToGetAlerts.get_codescan_alerts()
        for alert in codescan_alerts:
            print(alert.number, alert.created_at, alert.dismissed_at)
            print("  ", alert.tool.name, alert.tool.version, alert.tool.guid)
            print("  ", alert.rule.name, alert.rule.security_severity_level, alert.rule.severity)
            print("    ", alert.rule.description)
            print("  ", alert.most_recent_instance.ref, alert.most_recent_instance.state)
            print("    ", alert.most_recent_instance.location)
            print("    ", alert.most_recent_instance.message['text'])

    @staticmethod
    def GetLabels(Owner, RepoName):
        RepoToGetLabels = g.get_repo(f"{Owner}/{RepoName}")
        labels = RepoToGetLabels.get_labels()
        for label in labels:
            print(label)

    @staticmethod
    def GetRootContent(Owner, RepoName):
        RepoToGetRootContent = g.get_repo(f"{Owner}/{RepoName}")
        contents = RepoToGetRootContent.get_contents("")
        for content_file in contents:
            print(content_file)
    
    @staticmethod
    def GetRepoContent(Owner, RepoName):
        RepoToGetContent = g.get_repo(f"{Owner}/{RepoName}")
        contents = RepoToGetContent.get_contents("")
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":

                contents.extend(RepoToGetContent.get_contents(file_content.path))
            else:
                print(file_content)
    
    @staticmethod
    def GetFile(Owner, RepoName, FileName):
        RepoToGetFile = g.get_repo(f"{Owner}/{RepoName}")
        contents = RepoToGetFile.get_contents(FileName)
        print(contents)
    
    @staticmethod
    def NewFile(Owner, RepoName, FileName, CommitMessage, Contents, Branch):
        RepoToMakeFile = g.get_repo(f"{Owner}/{RepoName}")
        RepoToMakeFile.create_file(FileName, CommitMessage, Contents, branch=Branch)
    
    @staticmethod
    def DeleteFile(Owner, RepoName):
        RepoToDelFile = g.get_repo(f"{Owner}/{RepoName}")
        contents = RepoToDelFile.get_contents("test.txt", ref="test")
        RepoToDelFile.delete_file(contents.path, "remove test", contents.sha, branch="test")

    @staticmethod
    def MarkNotifsRead(Owner, RepoName):
        RepoToMarkNotifsRead = g.get_repo(f"{Owner}/{RepoName}")
        RepoToMarkNotifsRead.mark_notifications_as_read()