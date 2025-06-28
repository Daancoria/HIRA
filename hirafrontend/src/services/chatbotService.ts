const USE_MOCK = false; // 👈 Toggle this to true for local testing without backend

export async function getBotResponse(prompt: string): Promise<string> {
  if (USE_MOCK) {
    
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(`📊 (Mock) AI says: "${prompt}" — real AI coming soon.`);
      }, 1000);
    });
  }

  try {
    const response = await fetch('https://flask-env.eba-xyz123.us-east-1.elasticbeanstalk.com/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt }),
    });
    

    if (!response.ok) {
      throw new Error(`Server returned ${response.status}`);
    }

    const data = await response.json();
    return data.reply || '🛑 No response received from the server.';
  } catch (error: any) {
    console.error('Chatbot error:', error);
    return '⚠️ There was a problem connecting to the chatbot.';
  }
}
