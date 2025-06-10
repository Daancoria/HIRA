
# HIRA Frontend Component Tree & Design Notes

## Component Tree (Simplified)

```
App
├── AuthProvider
├── Routes
│   └── ProtectedRoute
│       └── ChatbotPage
│           ├── FileUploader
│           ├── MessageBubble (mapped list)
│           ├── ChatInput
│           ├── HelpModal (conditional)
│           ├── RoleBanner (conditional styling)
│           └── InsightSummary (conditional)
```

## Page Flow Description

### LoginPage
- Auth form
- Calls AuthContext login handler
- Redirects on success

### ChatbotPage
- Displays user role and personalized message
- Uploads file (validated client-side)
- Chat window renders messages and bot responses
- Chat input sends messages to `getBotResponse()`
- Insight summary updates based on keyword scan
- Help modal with instructions available at bottom right

### UI Role Adaptations
- `user?.role === 'Director'` shows budget prompts and banner
- `user?.role === 'Manager'` shows staffing-related prompts
- Suggestions and insights update accordingly

## Styling
- Uses `ChatbotPage.module.css` for all layout and theming
- Fully supports dark/light mode via root variables
- All inline styles refactored into CSS modules
