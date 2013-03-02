# -*- coding: utf-8 -*-
# User role
ADMIN = 0
STAFF = 1
USER = 2
ROLE = {
    ADMIN: "admin",
    STAFF: "staff",
    USER: "user",
}

# user status
INACTIVE = 0
NEW = 1
ACTIVE = 2
STATUS = {
    INACTIVE: "inactive",
    NEW: "new",
    ACTIVE: "active",
}

# Registration messages
USERNAME_TAKEN = "That username has already been registered. Pick a new one, loosah."
PASSWORDS_DO_NOT_MATCH = "Those passwords don't match! The buck were you thinking?"
TOS_AGREEMENT = "I agree to be fine and nice."
INVALID_CREDS = "You bucked up. That username and password combo isn't valid."

# Login messages
LOGIN_WELCOME_MESSAGE = "Welcome back, {username}."
