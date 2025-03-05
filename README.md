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

See the full research documentation for complete code samples.

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
