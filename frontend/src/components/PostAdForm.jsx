import React, { useState } from 'react';

export default function PostAdForm({ onAdPosted }) {
  const [formData, setFormData] = useState({
    title: '',
    platform: 'Telegram',
    subscribers: '',
    views: '',
    price: '',
    description: ''
  });
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage(null);

    try {
      const response = await fetch('http://127.0.0.1:8000/api/v1/marketplace/create', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        setMessage({ type: 'success', text: data.message || 'ማስታወቂያው በተሳካ ሁኔታ ተለጠፈ!' });
        setFormData({ title: '', platform: 'Telegram', subscribers: '', views: '', price: '', description: '' });
        if (onAdPosted) onAdPosted();
      } else {
        setMessage({ type: 'error', text: data.detail || 'ማስታወቂያውን መለጠፍ አልተቻለም!' });
      }
    } catch (err) {
      setMessage({ type: 'error', text: 'ከ ሰርቨር ጋር መገናኘት አልተቻለም። ሰርቨሩ መነሳቱን ያረጋግጡ!' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto bg-slate-900 border border-slate-800 rounded-2xl p-8 shadow-2xl text-white my-8">
      <h2 className="text-2xl font-bold mb-6 text-amber-400 border-b border-slate-800 pb-4">
        ዲጂታል ቻናል ወይም አካውንት መሸጫ መለጠፊያ ፎርም
      </h2>

      {message && (
        <div className={`p-4 mb-6 rounded-lg text-sm font-medium ${message.type === 'success' ? 'bg-emerald-900/50 text-emerald-300 border border-emerald-700' : 'bg-rose-900/50 text-rose-300 border border-rose-700'}`}>
          {message.text}
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-5">
        <div>
          <label className="block text-sm font-medium text-slate-300 mb-2">የቻናሉ ወይም አካውንቱ ስም (Title / Handle)</label>
          <input
            type="text"
            name="title"
            required
            value={formData.title}
            onChange={handleChange}
            placeholder="ለምሳሌ: Crypto Hub Habesha"
            className="w-full bg-slate-800 border border-slate-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-amber-500"
          />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">ፕላትፎርም (Platform)</label>
            <select
              name="platform"
              value={formData.platform}
              onChange={handleChange}
              className="w-full bg-slate-800 border border-slate-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-amber-500"
            >
              <option value="Telegram">Telegram</option>
              <option value="YouTube">YouTube</option>
              <option value="TikTok">TikTok</option>
              <option value="Instagram">Instagram</option>
              <option value="Facebook">Facebook</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">የተከታዮች ብዛት (Subscribers / Followers)</label>
            <input
              type="text"
              name="subscribers"
              required
              value={formData.subscribers}
              onChange={handleChange}
              placeholder="ለምሳሌ: 15K ወይም 5000"
              className="w-full bg-slate-800 border border-slate-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-amber-500"
            />
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">እይታዎች / እንቅስቃሴ (Views / Engagement)</label>
            <input
              type="text"
              name="views"
              required
              value={formData.views}
              onChange={handleChange}
              placeholder="ለምሳሌ: 45K views per post"
              className="w-full bg-slate-800 border border-slate-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-amber-500"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">የመሸጫ ዋጋ በብር (Price in ETB)</label>
            <input
              type="text"
              name="price"
              required
              value={formData.price}
              onChange={handleChange}
              placeholder="ለምሳሌ: 15,000 ETB"
              className="w-full bg-slate-800 border border-slate-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-amber-500"
            />
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-slate-300 mb-2">ተጨማሪ መግለጫ (Description)</label>
          <textarea
            name="description"
            rows="4"
            value={formData.description}
            onChange={handleChange}
            placeholder="ስለ ቻናሉ ገቢ፣ ዕድሜ እና ሌሎች ዝርዝር መረጃዎችን እዚህ ይጻፉ..."
            className="w-full bg-slate-800 border border-slate-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-amber-500"
          ></textarea>
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-gradient-to-r from-amber-500 to-orange-600 text-slate-950 font-bold py-4 rounded-lg shadow-lg hover:from-amber-400 hover:to-orange-500 transition duration-200 disabled:opacity-50"
        >
          {loading ? 'በመለጠፍ ላይ...' : 'ማስታወቂያውን በደህንነት ለጥፍ (Post Ad)'}
        </button>
      </form>
    </div>
  );
}