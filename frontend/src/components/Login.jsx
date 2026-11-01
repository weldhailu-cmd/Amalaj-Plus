import React, { useState } from 'react';

export default function Login({ onSwitchToRegister, onLoginSuccess }) {
  const [formData, setFormData] = useState({
    phone: '',
    password: '',
  });
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setErrorMessage('');

    try {
      const response = await fetch('http://127.0.0.1:8000/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          phone: formData.phone.strip ? formData.phone.strip() : formData.phone,
          password: formData.password,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        if (data.token) {
          localStorage.setItem('token', data.token);
        }
        if (onLoginSuccess) onLoginSuccess(data);
      } else {
        setErrorMessage(data.detail || 'የስልክ ቁጥር ወይም ሚስጥር ቁጥር ተሳስቷል!');
      }
    } catch (err) {
      setErrorMessage('ከሰርቨር ጋር መገናኘት አልተቻለም! እባክዎ ሰርቨሩ መነሳቱን ያረጋግጡ።');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto bg-slate-900 border border-slate-800 rounded-2xl p-6 text-white shadow-2xl mt-10">
      {/* ቱግል ቁልፎች (Log In / Create Account) */}
      <div className="flex bg-slate-800 p-1 rounded-xl mb-6">
        <button
          type="button"
          className="flex-1 py-2.5 text-sm font-semibold rounded-lg bg-amber-500 text-slate-950 shadow transition"
        >
          Log In
        </button>
        <button
          type="button"
          onClick={onSwitchToRegister}
          className="flex-1 py-2.5 text-sm font-semibold rounded-lg text-slate-400 hover:text-white transition"
        >
          Create Account
        </button>
      </div>

      <h2 className="text-xl font-bold mb-1 text-amber-400">ወደ አካውንትዎ ይግቡ (Log In)</h2>
      <p className="text-xs text-slate-400 mb-6">ቀደም ብሎ የተመዘገበ አካውንትዎ ከሆነ በስልክ ቁጥርዎ ይግቡ።</p>

      {errorMessage && (
        <div className="mb-4 p-3 bg-rose-950/80 border border-rose-600 text-rose-200 rounded-lg text-sm font-semibold">
          ⚠️ {errorMessage}
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-xs text-slate-300 mb-1">Phone Number (የስልክ ቁጥር)</label>
          <input
            type="text"
            name="phone"
            required
            value={formData.phone}
            onChange={handleChange}
            placeholder="0917175800"
            className="w-full bg-slate-800 border border-slate-700 rounded-lg p-3 text-sm focus:border-amber-500 outline-none"
          />
        </div>

        <div>
          <label className="block text-xs text-slate-300 mb-1">Password (የሚስጥር ቁጥር)</label>
          <input
            type="password"
            name="password"
            required
            value={formData.password}
            onChange={handleChange}
            placeholder="••••••••"
            className="w-full bg-slate-800 border border-slate-700 rounded-lg p-3 text-sm focus:border-amber-500 outline-none"
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-3 rounded-lg text-sm transition duration-200 shadow-lg disabled:opacity-50"
        >
          {loading ? 'በመግባት ላይ...' : 'Log In Now 🚀'}
        </button>
      </form>
    </div>
  );
}