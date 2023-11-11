import bcrypt


# Function to hash a password
def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    encrypted_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
    return encrypted_pass


# Function to check if a plain password matches the hashed password
def check_password(entry, checker):
    # Check if the hashed version of the plain password matches the stored hashed password
    return bcrypt.checkpw(entry.encode('utf-8'), checker)


'''

# Example usage
# User registration: Hash the password and store it in the database
plain_password = "user_password"  # entry
hashed_password = hash_password(plain_password)  # checker
print("Hashed Password:", hashed_password)

# User login: Check if the provided plain password matches the stored hashed password
login_password = "user_password"
is_password_correct = check_password(login_password, hashed_password)

if is_password_correct:
    print("Password is correct. Allow access.")
else:
    print("Incorrect password. Deny access.")

'''