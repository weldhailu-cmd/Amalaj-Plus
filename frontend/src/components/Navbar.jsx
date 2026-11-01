import React, { useState } from 'react';
import { Menu, X, User } from 'lucide-react';

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="bg-slate-950 border-b border-slate-800 text-white px-6 py-4 flex justify-between items-center relative">
      <div className="text-xl font-bold text-amber-400">
        አማላጅ ፕላስ <span className="text-xs text-slate-400">Amalaj Plus</span>
      </div>

      {/* ዩዘር ሜኑ ቁልፍ (Dropdown Menu Toggle) */}
      <div className="relative">
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="flex items-center gap-2 bg-slate-900 border border-slate-700 hover:border-slate-600 px-3 py-2 rounded-xl transition"
        >
          <Menu className="w-5 h-5 text-slate-300" />
          <div className="w-8 h-8 bg-slate-800 rounded-full flex items-center justify-center border border-slate-700">
            <User className="w-4 h-4 text-slate-300" />
          </div>
        </button>

        {/* ፕል ዳውን (Dropdown Box) */}
        {isOpen && (
          <div className="absolute right-0 mt-2 w-56 bg-white text-slate-900 rounded-2xl shadow-2xl border border-slate-200 py-2 z-50 overflow-hidden">
            <a
              href="/join"
              className="block px-5 py-3 text-sm font-semibold hover:bg-slate-100 transition"
            >
              Join now
            </a>
            <a
              href="/login"
              className="block px-5 py-3 text-sm font-semibold hover:bg-slate-100 transition"
            >
              Log In
            </a>
            <div className="border-t border-slate-200 my-1"></div>
            <a
              href="/help-center"
              className="block px-5 py-3 text-sm text-slate-600 hover:bg-slate-100 transition"
            >
              Help center
            </a>
            <a
              href="/blog"
              className="block px-5 py-3 text-sm text-slate-600 hover:bg-slate-100 transition"
            >
              Blog
            </a>
          </div>
        )}
      </div>
    </nav>
  );
}