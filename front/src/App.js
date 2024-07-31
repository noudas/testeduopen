import React, { useState } from 'react';
import './App.css';

function App() {
  const [cpf, setCpf] = useState('');
  const [idade, setIdade] = useState(null); 
  const [aceitaTermos, setAceitaTermos] = useState(false); 
  
  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = {
        cpf: cpf,
        idade: parseInt(idade),
        aceita_termos: aceitaTermos
    };
  
    try {
        const response = await fetch('/pessoas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });
  
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
  
        const result = await response.json();
        console.log(result);
    } catch (error) {
        console.error('Error:', error);
    }
  };
  
  return (
    <div className="formulario">
      <form onSubmit={handleSubmit}>
        <label>
          CPF:
          <input type="text" value={cpf} onChange={(e) => setCpf(e.target.value)} />
        </label>
        <label>
          Idade:
          <input type="number" value={idade} onChange={(e) => setIdade(e.target.value)} />
        </label>
        <label>
          Aceita Termos:
          <input type="checkbox" checked={aceitaTermos} onChange={(e) => setAceitaTermos(e.target.checked)} />
        </label>
        <button type="submit">Enviar</button>
      </form>
    </div>
  );
}

export default App;
