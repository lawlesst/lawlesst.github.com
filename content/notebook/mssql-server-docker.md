Title:Fix the docs - SQL Server and Docker on a Mac
Date:01-07-22
Slug:mssql-server-docker

I recently setup Microsoft SQL Server on a Macbook and found a simple error in Microsoft's documentation. Since I didn't quickly find an answer in the normal places (Google -> Stack Overflow), I thought I would post it here in case it saves someone a few minutes. 

From Microsoft's "Get started with SQL Server" documentation, which is otherwise quite good and nicely organized, Step 1.1 ((https://www.microsoft.com/en-us/sql-server/developer-get-started/python/mac/)) lists two commands for pulling a Docker image from Docker Hub and running it. The path to the Docker location is incorrect and you will receive an error message when trying to pull the image. 

The `docker pull` command:

```
sudo docker pull microsoft/mssql-server-linux:2017-latest
```

Should be changed to:
```
sudo docker pull mcr.microsoft.com/mssql/server:2017-latest
```

Note: Microsoft does have a chat window embedded on this site and I thought that I could submit an error report that way but the chat window requires you to authenticate with Gitter, which points you to Oauth via Github, and the Oauth message is kind of scary regarding the amount of access you will be giving Gitter, as Oauth with Github usually is. So I stopped there.