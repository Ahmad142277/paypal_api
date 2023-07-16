// App.js

import React, { useState, useEffect } from 'react';

const App = () => {
  const [formHtml, setFormHtml] = useState('');

  useEffect(() => {
    const createPayment = async () => {
      const paymentData = {
        description: 'Product purchase',
        amount: '100.00',
        invoice: 'A7892sasas4',
      };
      try {
        const response = await fetch('http://localhost:8000/api/paypal/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(paymentData),
        });
        const data = await response.json();

        if (response.ok) {
          setFormHtml(data.form);
        } else {
          console.log('Error:', data.error);
        }
      } catch (error) {
        console.log('Error:', error);
      }
    };

    createPayment();
  }, []);

  return (
    <div>
      {formHtml ? (
        <div dangerouslySetInnerHTML={{ __html: formHtml }} />
      ) : (
        <div>Loading...</div>
      )}
    </div>
  );
};

export default App;
