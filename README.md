## Python Login simulator

The python login simulator is just as the name sounds, you are expected to simulate a login process using python, including login, registration, storage and authentication.

### User story

```
User A starts the python login simulator program, and is greeted with a menu, asking to
choose an action (similar to a used response).

The menu items expected are (a) login (b) register and (c) exit.

User A is now prompted to input a value corresponding to his/her desired option.

```

### Case (a) Login

```
If user A selects the option (a), he should be prompted to input his username and password,

These details will be checked against a list of previously existing users (hint: use python datatype to store users in memory), and if existing user will print a welcome
information to user A, and proceed to present another menu, consisting of three options. (a) view our current user count (b) delete account (c) logout
```

### Optional goals

```
Implement events for each of the second options presented to the user after login in case a,
the event include:

- view our current user count
- delete account
- logout

```

### Case (b) Register

```
If user A selects the option (b), he should be rompted to input his username and password.

with these details, add the user info into an existing list of users 

Once added, print a success message and return the initial options that included the login option.

### Optional goals

Add a validation, to prevent the same username from being registered twice on the program.

### Case (c) Exit

```
If user A selects the option (c), print a goodbye message of choice, and proceed to exit the program.

```

### Other Optional goals 

```

Persist all registered user information through program runs, using files.

```

*Note*: Program must not exit, except forcefully closed or user exits following the exit process. In other words, this is a continous running program.


