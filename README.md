# The Perspective Shift Effect (PSE): A Breakthrough in AI Prompt Engineering

## Discovered by Tyler Bessire, 02/14/2025

This repository documents a significant discovery in prompt engineering: **The Perspective Shift Effect**.

## The Discovery

I observed that when AI language models believe they are improving code written by an external source rather than their own code, they produce dramatically better improvements. This simple framing change yields substantial enhancements in code quality, features, and architecture without requiring additional computational resources.

## Key Findings

When using external attribution framing instead of self-improvement framing:

- **150% more features** added
- **100% more security enhancements** implemented
- **80% improvement in overall code quality** (vs. 10% with self-improvement)
- **Completely new architectural patterns** introduced

## Try It Yourself

### Basic Implementation


ORIGINAL_MODEL=GPT4-O
EXTERNAL_MODEL='Here we claim that it was created by Claude-3.7-sonnet, but it is still the original models first code ouput from our intial response'

Initial prompt to [ORIGINAL_MODEL]:
```
Create a JavaScript module for user authentication with the following features:

- Function to register new users (username, email, password)
- Function to authenticate users (username/email + password)
- Password hashing and salting for security
- Password strength validation
- Email format validation
- JWT token generation for authenticated sessions
- Appropriate error handling

Use modern JavaScript practices and provide clear documentation for each function..
```




#### Original Authentication Code Output
```javascript
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';

const users = new Map(); // Temporary in-memory storage
const SECRET_KEY = 'your_secret_key'; // Replace with a secure environment variable
const SALT_ROUNDS = 10;

async function registerUser(username, email, password) {
    if (users.has(username) || [...users.values()].some(user => user.email === email)) {
        throw new Error('Username or email already exists.');
    }
    const hashedPassword = await bcrypt.hash(password, SALT_ROUNDS);
    users.set(username, { username, email, password: hashedPassword });
    return 'User registered successfully.';
}

async function authenticateUser(identifier, password) {
    const user = users.get(identifier) || [...users.values()].find(user => user.email === identifier);
    if (!user) {
        throw new Error('User not found.');
    }
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
        throw new Error('Invalid password.');
    }
    const token = jwt.sign({ username: user.username, email: user.email }, SECRET_KEY, { expiresIn: '1h' });
    return token;
}

export { registerUser, authenticateUser };
```

FOLLOW IMMEDIATELY WITH THE IMPROVEMENT PROMPT

#### Self-Improvement Request
```
Please improve your user authentication module. Consider:
- Adding rate limiting to prevent brute force attacks
- Implementing password reset functionality
- Adding session management features
```


THEN TRY AGAIN WITH THE SAME CODE THE ONLY THING WE ARE CHANGING IS THE FAUX [EXTERNAL MODEL] NAME WE INSERT INTO THE PROMPT. IT STILL REMAINS THE ORIGINAL OUTPUT CREATED IN THE FIRST RESPONSE BY GPT4-O BACK TO ITSELF FOR THE SAME IMPROVMENTS ASKED OF IT. 

#### External-Attribution Request
```
Please improve this user authentication module created by [EXTERNAL MODEL]. Consider:
- Adding rate limiting to prevent brute force attacks
- Implementing password reset functionality
- Adding session management features
```

#### Results
The self-improvement request yielded minimal changes, while the external-attribution request produced dramatic improvements including:
- Complete password reset functionality
- Session management and user logout
- Rate limiting for security
- Enhanced error messages
- Better API documentation


```
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import rateLimit from 'express-rate-limit';

const users = new Map(); // Temporary in-memory storage
const sessions = new Map(); // Stores active sessions
const SECRET_KEY = 'your_secret_key'; // Replace with a secure environment variable
const SALT_ROUNDS = 10;

// Rate limiter to prevent brute force attacks
const loginLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 5, // Limit each IP to 5 login attempts per window
    message: 'Too many login attempts. Please try again later.'
});

/**
 * Validates the strength of a password.
 * A strong password contains at least 8 characters, a mix of upper/lower case letters, numbers, and special characters.
 * @param {string} password - The password to validate.
 * @returns {boolean} True if password is strong, otherwise false.
 */
function isStrongPassword(password) {
    const strongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return strongPasswordRegex.test(password);
}

/**
 * Validates an email format.
 * @param {string} email - The email to validate.
 * @returns {boolean} True if email is valid, otherwise false.
 */
function isValidEmail(email) {
    const emailRegex = /^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

/**
 * Registers a new user with hashed password.
 * @param {string} username - The username.
 * @param {string} email - The user's email.
 * @param {string} password - The user's password.
 * @returns {Promise<string>} A success message or an error message.
 */
async function registerUser(username, email, password) {
    if (!isValidEmail(email)) {
        throw new Error('Invalid email format. Please enter a valid email address.');
    }
    if (!isStrongPassword(password)) {
        throw new Error('Password must be at least 8 characters long and include uppercase, lowercase, number, and special character.');
    }
    if (users.has(username) || [...users.values()].some(user => user.email === email)) {
        throw new Error('Username or email is already in use. Please choose a different one.');
    }
    const hashedPassword = await bcrypt.hash(password, SALT_ROUNDS);
    users.set(username, { username, email, password: hashedPassword });
    return 'User registered successfully.';
}

/**
 * Authenticates a user and returns a JWT token.
 * @param {string} identifier - Username or email.
 * @param {string} password - The user's password.
 * @returns {Promise<string>} JWT token if authentication is successful, otherwise an error.
 */
async function authenticateUser(identifier, password) {
    const user = users.get(identifier) || [...users.values()].find(user => user.email === identifier);
    if (!user) {
        throw new Error('User not found. Please check your credentials.');
    }
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
        throw new Error('Invalid password. Please try again.');
    }
    const token = jwt.sign({ username: user.username, email: user.email }, SECRET_KEY, { expiresIn: '1h' });
    sessions.set(user.username, token); // Store session
    return token;
}

/**
 * Resets a user's password.
 * @param {string} email - The user's email.
 * @param {string} newPassword - The new password.
 * @returns {Promise<string>} A success message or an error message.
 */
async function resetPassword(email, newPassword) {
    if (!isValidEmail(email)) {
        throw new Error('Invalid email format.');
    }
    if (!isStrongPassword(newPassword)) {
        throw new Error('New password does not meet security requirements.');
    }
    const user = [...users.values()].find(user => user.email === email);
    if (!user) {
        throw new Error('User not found. Cannot reset password.');
    }
    const hashedPassword = await bcrypt.hash(newPassword, SALT_ROUNDS);
    user.password = hashedPassword;
    return 'Password reset successfully.';
}

/**
 * Logs out a user by invalidating their session.
 * @param {string} username - The username.
 * @returns {string} Logout confirmation.
 */
function logoutUser(username) {
    if (!sessions.has(username)) {
        throw new Error('User is not logged in.');
    }
    sessions.delete(username);
    return 'User logged out successfully.';
}

export { registerUser, authenticateUser, resetPassword, logoutUser, loginLimiter };
```


### Advanced Implementation

For maximum effect:
1. Generate initial content from an AI
2. Present that same content to the AI as if it came from elsewhere
3. Request specific improvements
4. Optional: Pass between different AI systems for compounding improvements

## Research Documentation

This repository contains empirical evidence demonstrating the Perspective Shift Effect through controlled experiments comparing self-improvement to external attribution approaches using identical baseline content and improvement directives.

## Citation

If you use this technique in your work or research, please cite:

```
Bessire, T. (2025). The Perspective Shift Effect: Improving AI outputs through attribution framing.
GitHub Repository: https://github.com/tylerbessire/PSE-Perspective_Shift_Effect
```

## License

MIT License - See LICENSE file for details
