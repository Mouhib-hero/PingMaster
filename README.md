<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="images/PingMaster.png" alt="Project logo"></a>
</p>

<h3 align="center">PingMaster</h3>

<div align="center">

</div>

---

<p align="center"> 
PingMaster is a connectivity testing application that allows you to ping a list of IP addresses, monitor their availability and save the results into a database sqlite3 that you can backup, restore and send any operation that happens on databases to a specific email that you define. 
<br></p>
<div align="center">

</div>

---


## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Database](#database)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

In any entreprise, there's an important need to check for the availability of its devices and if they're properly integrated into the network. Which means, there must be a scheduled task of regularly checking for the availability of these

PingMaster can be scheduled to run at specific times and dates, and it can save the results to a database. PingMaster can also send the results to email, so that you can be alerted of any connectivity issues.

PingMaster is a powerful and versatile tool that can be used by businesses of all sizes to monitor their network connectivity and ensure that the corresponding devices to the defined ip addresses are always available.

The main philosophy behind the application is to develop a simple powershell script for a windows scheduled task that scans the available IP adresses of our choice. That script is organized inside our GUI application. 

To see a graphical demonstration of this application please visit :
https://tinyurl.com/2z3rz24n

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need to Clone the repo locally :

```
git clone https://github.com/Mouhib-hero/PingMaster
```

### Installing


install the needed python modules by running :
```
python install_depencies.py
```
### Running


Run the main application with this command :
```
python ping_master.py
```

End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Features, Benefits & Perspectives <a name = "tests"></a>

### Features:

- Ping multiple IP addresses at once.
- Schedule pings to run at specific times and dates.
- Save ping results to a database.
- Send ping results to email.
- Generate reports on ping results.

### Benefits:

- Improve network reliability.
- Identify and resolve connectivity issues quickly.
- Save time and money on network troubleshooting.

### Perspectives:
- Support for multiple ping protocols.
- Integration with other monitoring tools.
- Support for cloud-based deployments.
## 🎈 Usage <a name="usage"></a>

**How to use PingMaster :**

<li>Clone PingMaster on your computer and run it.</li>
<li>Create a list of IP addresses to ping by modifying <i>" AdresseIP.txt "</i>.</li>
<li>Schedule a ping job.</li>
<li>Run the connectivity test & View the results.</li>
<li>Save into sqlite3 database and backup.</li>
<li>Restore and delete database.</li>
<li>Receive alerts of any database operation through email.</li>
<br>

**Email Notification Configuration :**

To receive email notifications related to any operation on the database, you need to configure the following parameters in a JSON configuration file:

- `receiver_email`: The email address where you want to receive notifications.
- `sender_email`: Your email address for sending notifications.
- `sender_password`: The password for your sender email.
- `smtp_server`: The SMTP server address for sending emails.
- `smtp_port`: The SMTP port number for email service.

Edit the `config.json` file to set these parameters before using the email notification feature.

**Note:**

* Please be aware that certain files, such as <i><b>"config.txt, PingResults.txt, restore.txt"</b></i> should not be modified or deleted. These files are essential for the proper functioning of the application and should be left untouched.
<br>
* You can visually view the sqlite3 database using third-party software, personally I used <i><b>"DB Browser for SQLite (DB4S)"</b></i>.

## 🗃️ Database <a name = "tests"></a>
### Backup and Restore
I'm implementing backup and restore functionality in two distinct ways within this application:

<b>1- Backup/Restore to/from Another SQLite Database:</b>

- Creating a separate database for the backup which will also be the same database from which we'll do the restore. Both databases are be of the same type (SQLite).
- This approach offers simple, local data transfer and management. And it's very important in case we need to perform SQLite-to-SQLite operations.

<b> 2- Backup/Restore to/from SQL Query (Cross-Platform): </b>

- The backups and retores are made by the exportation of data as SQL queries that are compatible with many databases like SQLite and SQL Server.
- This approach is suitable for cross-platform data migration and synchronization. We can run the SQL queries generated by the application in different database management systems.

These two methods offer flexibility and compatibility for different data management scenarios. Depending on your specific use case, you can choose the most suitable approach for your data backup and restore needs.
## 🚀 Deployment <a name = "deployment"></a>

No deployment for the moment.

## ⛏️ Built Using <a name = "built_using"></a>

- [Python3](https://www.python.org/download/releases/3.0/) - The code.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - The GUI.
- [Sqlite3](https://docs.python.org/3/library/sqlite3.html) - Database.

## ✍️ Authors <a name = "authors"></a>

- [@Mouhib-hero](https://github.com/Mouhib-hero/) - Idea & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- All image credits are for their rightful owners.
- Inspiration came from my first internship supervisor.
- References: Python documentation & Stackoverflow.
