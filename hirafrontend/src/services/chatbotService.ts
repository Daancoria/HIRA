const USE_MOCK = true; // 👈 Toggle this to false when you're ready for real backend

export async function getBotResponse(prompt: string): Promise<string> {
  if (USE_MOCK) {
    // 🔁 Mocked response with simulated delay
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(`📊 (Mock) AI says: "${prompt}" real AI coming soon.`);
      }, 1000);
    });
  }

  // 🔌 Real backend call
  const response = await fetch('http://localhost:5000/analyze', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ prompt }),
  });

  if (!response.ok) throw new Error('Server error');

  const data = await response.json();
  return data.reply || 'No reply from server.';
}
