# Cyber Security Base 2023 Project

## Instructions:
1. `python3 manage.py migrate`
2. `python3 manage.py runserver`

---

## FLAW 1:
[Flaw in settings.py](https://github.com/sannituomisto/csb-project1/blob/master/csb_project1/settings.py#L93) (Line 93 in settings.py)

### Description of flaw 1:
The first flaw is that the application does not implement any password validation. The link pinpointing this flaw indicates that validators are not in use. Consequently, when a user creates a new account on the signup page, they can use weak, well-known, and unsecured passwords, posing a security risk. This flaw falls under A2-Broken Authentication. As stated in the OWASP Top Ten list, it is crucial to confirm the user's identity to protect against authentication-related attacks.

### How to fix the flaw:
This flaw can be addressed by implementing password checks during the password creation process. Django provides pluggable password validation, and incorporating these checks can prevent users from using weak passwords. The fix can be found in [here](https://github.com/sannituomisto/csb-project1/blob/master/csb_project1/settings.py#L93) (Lines 93-106 in settings.py). The fix includes validators that check whether the password and user attributes are not too similar, the password is not too short (in this case, the minimum length is nine characters), the password is not on the list of 20,000 common passwords (created by Royce Williams), and the password is not entirely numeric. However, it is essential to note that even the most advanced validation cannot guarantee that the password is 100% secure.

---

## FLAW 2:
[Flaw in views.py](https://github.com/sannituomisto/csb-project1/blob/master/app/views.py#L37) (Line 37 in views.py)      

### Description of flaw 2:
The second flaw is that an attacker, once logged in, can delete tasks belonging to other users stored in the system by passing a task ID as a URL parameter (e.g., domain:port/delete/54). This vulnerability falls under A2-Broken Access Control. Not only is the task ID exposed to the user in the URL (and also as a "hidden" form value), making it vulnerable to tampering, but the task IDs are also very predictable because they have sequential values. This could be seen as a part of the flaw.

### How to fix the flaw:
This flaw can be addressed by making sure that the user attempting to delete a task is the same user who created it. Additionally, to increase security, task IDs can be made less predictable by randomizing or masking them. However, the primary focus in fixing this type of flaw should be on controlling access to resources. The fix can be found in [here](https://github.com/sannituomisto/csb-project1/blob/master/app/views.py#L45) (Line 45 in views.py is the crucial part of the fix). This line checks if the currently logged-in user is the creator of the task, and only if this condition is true, the task can be deleted.

---

## FLAW 3:
[Flaw in views.py](https://github.com/sannituomisto/csb-project1/blob/master/app/views.py#L55) (Line 55 in views.py)

### Description of flaw 3:
Third flaw is that the SQL query is vulnerable to SQL injection because it includes the 'userid' variable directly in the query without proper sanitation. An attacker could potentially manipulate the 'userid' variable to inject arbitrary SQL code into the database. In this case, the attacker could, for example, get access to all tasks from all users. On the OWASP top ten list, this flaw is A1- Injection.

### How to fix the flaw:
This flaw can be addressed by using Django's built-in ORM methods, as they use query parametrization. The fix can be found in [here](https://github.com/sannituomisto/csb-project1/blob/master/app/views.py#L63) (Line 63 in views.py is the main part of the fix). The filter method handles parametrization automatically, making the SQL query protected from SQL injection.

---

## FLAW 4:
[Flaw in settings.py](https://github.com/sannituomisto/csb-project1/blob/master/csb_project1/settings.py#L26) (Line 26 in settings.py)

### Description of flaw 4:
The fourth flaw is an A6- Security Misconfiguration flaw listed on the OWASP Top Ten. In this case, the debug mode is enabled in the settings file. When an error occurs, the application provides detailed error pages containing sensitive information about the application, which attackers can potentially exploit.

### How to fix the flaw:
To address this flaw, it is crucial to turn off debugging. The fix can be found in [here](https://github.com/sannituomisto/csb-project1/blob/master/csb_project1/settings.py#L27) (Line 27 in settings.py). Disabling debug mode ensures that if a flaw occurs, the error message will be more general and not reveal sensitive details.

---

## FLAW 5:
[Flaw in index.html](https://github.com/sannituomisto/csb-project1/blob/master/app/templates/index.html#L10)  
[Flaw in index.html](https://github.com/sannituomisto/csb-project1/blob/master/app/templates/index.html#L25)  
(Line 10 and 25 in index.html)

### Description of flaw 5:
The fifth flaw is that there is no CSRF protection when creating and deleting tasks. CSRF attacks trick authenticated users on the website into sending malicious requests. The malicious requests can be created to include cookies, parameters, and other data in a way that the server processing the requests perceives them as legitimate. While this very simple application may not in this form pose serious threats exploitable through CSRF attacks, the lack of CSRF protection exposes the possibility of malicious users, for instance, creating and deleting tasks on behalf of the authenticated user, potentially leading to abuse of the user's account. CSRF was not mentioned in the OWASP top ten list but accepted as a flaw in the project.

### How to fix the flaw:
To address this flaw, CSRF tokens should be implemented. A CSRF token is an unpredictable and unique value generated by the application for each user session. When the user makes a request, the server-side application verifies the existence and validity of the CSRF token and compares it to the token used in the user session. If the token is not found or is not valid, the request is rejected. The use of tokens prevents attackers from making unauthorized requests on behalf of legitimate users. The fixes can be found in [here](https://github.com/sannituomisto/csb-project1/blob/master/app/templates/index.html#L11) and [here](https://github.com/sannituomisto/csb-project1/blob/master/app/templates/index.html#L26) (Line 11 and 26 in index.html).

---

## References:
1. Django documentation, [https://docs.djangoproject.com/en/5.0/](https://docs.djangoproject.com/en/5.0/)
2. OWASP Cheat Sheets, [https://cheatsheetseries.owasp.org/IndexTopTen.html](https://cheatsheetseries.owasp.org/IndexTopTen.html)
3. OWASP Top Ten list 2017, [https://owasp.org/www-project-top-ten/2017/](https://owasp.org/www-project-top-ten/2017/)
