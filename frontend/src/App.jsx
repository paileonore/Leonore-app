import React, { useState } from 'react';
import axios from 'axios';
import { Search, Shield } from 'lucide-react';

export default function App() {

  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {

    if (!query) return;

    setLoading(true);

    try {

      const res = await axios.get(
        `http://127.0.0.1:5000/api/username/${query}`
      );

      setResults(res.data.results);

    } catch (err) {
      console.log(err);
    }

    setLoading(false);
  }

  return (
    <div className="min-h-screen bg-black text-white p-8">

      <div className="max-w-4xl mx-auto">

        <div className="flex items-center gap-3 mb-10">
          <Shield className="text-purple-500" />

          <h1 className="text-3xl font-bold">
            LEONORE.ROCKS
          </h1>
        </div>

        <div className="flex gap-3">

          <input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="username"
            className="flex-1 bg-zinc-900 border border-zinc-700 rounded-xl p-4"
          />

          <button
            onClick={handleSearch}
            className="bg-purple-600 px-6 rounded-xl flex items-center gap-2"
          >
            <Search size={18} />
            SEARCH
          </button>

        </div>

        {
          loading && (
            <div className="mt-6 text-purple-400">
              Scanning target...
            </div>
          )
        }

        <div className="mt-8 space-y-4">

          {
            results.map((r, i) => (
              <div
                key={i}
                className="bg-zinc-900 border border-zinc-800 rounded-xl p-4 flex justify-between"
              >
                <div>{r.site}</div>
                <div>
                  {r.status}
                </div>
              </div>
            ))
          }

        </div>

      </div>

    </div>
  )
}
