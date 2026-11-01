import React, { useState } from 'react';

export default function SellerVerification({ onSuccess }) {
  const [formData, setFormData] = useState({
    full_name: '',
    mother_name: '',
    phone: '',
    fayida_num: '',
  });
  const [idFront, setIdFront] = useState(null);
  const [idBack, setIdBack] = useState(null);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setErrorMessage('');
    setSuccessMessage('');

    const data = new FormData();
    data.append('full_name', formData.full_name);
    data.append('mother_name', formData.mother_name);
    data.append('phone', formData.phone);
    data.append('fayida_num', formData.fayida_num);
    if (idFront) data.append('id_front', idFront);
    if (idBack) data.append('id_back', idBack);

    try {
      const response = await fetch('http://127.0.0.1:8000/api/auth/verify', {
        method: 'POST',
        body: data,
      });

      const result = await response.json();

      if (response.ok) {
        setSuccessMessage(result.message || 'ማረጋገጫዎ በተሳካ ሁኔታ ተጠናቋል!');
        if (onSuccess) onSuccess();
      } else {
        setErrorMessage(result.detail || 'የተሳሳተ መረጃ አስገብተዋል። እባክዎ እንደገና ይሞክሩ!');
      }
    } catch (err) {
      setErrorMessage('ከሰርቨር ጋር መገናኘት አልተቻለም! እባክዎ ሰርቨሩ መነሳቱን ያረጋግጡ።');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl mx-auto bg-slate-900 border border-slate-800 rounded-2xl p-6 text-white shadow-2xl">
      <h2 className="text-xl font-bold mb-1 text-amber-400">One-Time Seller National ID Verification</h2>
      <p className="text-xs text-slate-400 mb-6">Enter your details once. Existing sellers bypass automatically.</p>

      {errorMessage && (
        <div className="mb-4 p-3 bg-rose-950/80 border border-rose-600 text-rose-200 rounded-lg text-sm font-semibold">
          ⚠️ {errorMessage}
        </div>
      )}

      {successMessage && (
        <div className="mb-4 p-3 bg-emerald-950/80 border border-emerald-600 text-emerald-200 rounded-lg text-sm font-semibold">
          ✅ {successMessage}
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-xs text-slate-300 mb-1">Full Name (የሙሉ ስም)</label>
            <input
              type="text"
              name="full_name"
              required
              value={formData.full_name}
              onChange={handleChange}
              placeholder="HAILU WOLDEKIDAN WOLDAMANUAL"
              className="w-full bg-slate-800 border border-slate-700 rounded p-2.5 text-sm"
            />
          </div>
          <div>
            <label className="block text-xs text-slate-300 mb-1">Mother's Full Name (የእናት ስም)</label>
            <input
              type="text"
              name="mother_name"
              required
              value={formData.mother_name}
              onChange={handleChange}
              placeholder="Zenbechi"
              className="w-full bg-slate-800 border border-slate-700 rounded p-2.5 text-sm"
            />
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-xs text-slate-300 mb-1">Phone Number (የስልክ ቁጥር)</label>
            <input
              type="text"
              name="phone"
              required
              value={formData.phone}
              onChange={handleChange}
              placeholder="0917175800"
              className="w-full bg-slate-800 border border-slate-700 rounded p-2.5 text-sm"
            />
          </div>
          <div>
            <label className="block text-xs text-slate-300 mb-1">Fayida ID (16 Digits)</label>
            <input
              type="text"
              name="fayida_num"
              required
              value={formData.fayida_num}
              onChange={handleChange}
              placeholder="2176159169245063"
              className="w-full bg-slate-800 border border-slate-700 rounded p-2.5 text-sm"
            />
          </div>
        </div>

        <div className="p-4 bg-slate-800/50 border border-slate-700 rounded-lg space-y-3">
          <p className="text-xs font-semibold text-amber-400">🪪 National ID / Fayida Photo Verification</p>
          <div className="grid grid-cols-2 gap-4 text-xs">
            <div>
              <label className="block mb-1 text-slate-300">ID Front Side *</label>
              <input
                type="file"
                required
                accept="image/*"
                onChange={(e) => setIdFront(e.target.files[0])}
                className="w-full text-slate-400 text-xs"
              />
            </div>
            <div>
              <label className="block mb-1 text-slate-300">ID Back Side *</label>
              <input
                type="file"
                required
                accept="image/*"
                onChange={(e) => setIdBack(e.target.files[0])}
                className="w-full text-slate-400 text-xs"
              />
            </div>
          </div>
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-3 rounded-lg text-sm transition duration-200 disabled:opacity-50"
        >
          {loading ? 'በማረጋገጥ ላይ...' : 'Verify Identity & Continue 🛡️'}
        </button>
      </form>
    </div>
  );
}