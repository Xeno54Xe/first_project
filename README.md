<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">SARC_BACKEND_TASK</h1></p>
<p align="center">
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Xeno54Xe/SARC_Backend_task?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Xeno54Xe/SARC_Backend_task?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Xeno54Xe/SARC_Backend_task?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Xeno54Xe/SARC_Backend_task?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Screenshots](#-screenshots)
- [ Instructions](#-instructions)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)


---
##  Notice 
I tried going for the brownie task but ended up with some issue, i.e in the view budget page- the saved goal amount is not being displayed(fetched from the db prolly). This issue might majorly be something in the HTML. I've copied the HTML files for view budget and addsavinggoal from Chatgpt as frontend is not my cup of tea. I assure you the rest html files and the other code is not at all been pasted from any source. I've completed a course in the past week on django (certifications can be found on my linkedin: vansh-dhillon-b9238131a 
Also this readme is generated from a readme generator at the last moment of submission so pls dont mind the poop ive put in here.
Regards
Vansh Dhillon
2024B3PS0923P

##  Screenshots

Make sure to check out the screenshots folder for example screenshots for the project.

---

##  Instructions

Make sure to firstly do [py manage.py flush] to avoid any rookie issues that are beyond my knowledge, then makemigrations and migrate followed by py manage.py runserver

---

##  Project Structure

```sh
└── SARC_Backend_task/
    ├── db.sqlite3
    ├── first_project
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── plan.txt
    ├── templates
    │   └── tracker
    └── tracker
        ├── __init__.py
        ├── __pycache__
        ├── admin.py
        ├── apps.py
        ├── migrations
        ├── models.py
        ├── tests.py
        ├── update.py
        ├── urls.py
        └── views.py
```


###  Project Index
<details open>
	<summary><b><code>SARC_BACKEND_TASK/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/manage.py'>manage.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/db.sqlite3'>db.sqlite3</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/plan.txt'>plan.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- templates Submodule -->
		<summary><b>templates</b></summary>
		<blockquote>
			<details>
				<summary><b>tracker</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/templates/tracker/home.html'>home.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/templates/tracker/budget.html'>budget.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/templates/tracker/add_saving_goal.html'>add_saving_goal.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/templates/tracker/trans_new.html'>trans_new.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/templates/tracker/budget_update.html'>budget_update.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/templates/tracker/trans_update.html'>trans_update.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/templates/tracker/alltrans.html'>alltrans.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/templates/tracker/newbudget.html'>newbudget.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- tracker Submodule -->
		<summary><b>tracker</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/tests.py'>tests.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/views.py'>views.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/apps.py'>apps.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/update.py'>update.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/urls.py'>urls.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/admin.py'>admin.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/models.py'>models.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
			<details>
				<summary><b>migrations</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/migrations/0001_initial.py'>0001_initial.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/migrations/0002_transaction_budget_id_alter_budget_transtot_and_more.py'>0002_transaction_budget_id_alter_budget_transtot_and_more.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/migrations/0006_alter_transaction_budget_alter_transaction_trans_id_and_more.py'>0006_alter_transaction_budget_alter_transaction_trans_id_and_more.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/migrations/0007_alter_savingsgoal_budget.py'>0007_alter_savingsgoal_budget.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/migrations/0005_alter_transaction_budget_alter_transaction_trans_id.py'>0005_alter_transaction_budget_alter_transaction_trans_id.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/migrations/0003_remove_transaction_id_transaction_trans_id.py'>0003_remove_transaction_id_transaction_trans_id.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/tracker/migrations/0004_remove_transaction_budget_id_transaction_budget.py'>0004_remove_transaction_budget_id_transaction_budget.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- first_project Submodule -->
		<summary><b>first_project</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/first_project/settings.py'>settings.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/first_project/urls.py'>urls.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/first_project/asgi.py'>asgi.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Xeno54Xe/SARC_Backend_task/blob/master/first_project/wsgi.py'>wsgi.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

