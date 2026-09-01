import React from 'react';
import { Terminal, Shield, Activity, Cpu } from 'lucide-react';

export default function Sidebar({ modules, selectedModule, onSelectModule, loading }) {
  return (
    <aside className="w-80 bg-slate-900 border-r border-slate-800 flex flex-col h-screen">
      {/* Cabecera de la barra lateral */}
      <div className="p-5 border-b border-slate-800 flex items-center space-x-3">
        <div className="bg-emerald-500/10 border border-emerald-500/30 p-2 rounded-lg text-emerald-400">
          <Shield className="w-6 h-6" />
        </div>
        <div>
          <h1 className="font-bold text-slate-100 tracking-wide">Network Toolkit</h1>
          <p className="text-xs text-slate-400">Panel de Ciberseguridad</p>
        </div>
      </div>

      {/* Lista de Módulos */}
      <div className="flex-1 overflow-y-auto p-4 space-y-2">
        <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider px-2 mb-2">
          Módulos Disponibles ({modules.length})
        </div>

        {loading ? (
          <div className="space-y-2 p-2">
            {[...Array(6)].map((_, i) => (
              <div key={i} className="h-10 bg-slate-800/50 rounded-md animate-pulse"></div>
            ))}
          </div>
        ) : modules.length === 0 ? (
          <div className="text-sm text-slate-500 px-2 py-4 text-center">
            No se encontraron módulos disponibles o sin conexión al backend.
          </div>
        ) : (
          modules.map((mod) => {
            const isSelected = selectedModule?.id === mod.id;
            return (
              <button
                key={mod.id}
                onClick={() => onSelectModule(mod)}
                className={`w-full text-left px-3 py-2.5 rounded-lg text-sm font-medium transition-all flex items-center justify-between group ${
                  isSelected
                    ? 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30 shadow-sm'
                    : 'text-slate-400 hover:bg-slate-800/60 hover:text-slate-200'
                }`}
              >
                <div className="flex items-center space-x-3 truncate">
                  <Activity className={`w-4 h-4 flex-shrink-0 ${isSelected ? 'text-emerald-400' : 'text-slate-500 group-hover:text-slate-300'}`} />
                  <span className="truncate">{mod.name}</span>
                </div>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-950 text-slate-500 border border-slate-800">
                  {mod.id}
                </span>
              </button>
            );
          })
        )}
      </div>

      {/* Pie de la barra lateral */}
      <div className="p-4 border-t border-slate-800 bg-slate-950/40 text-xs text-slate-500 flex items-center justify-between">
        <span className="flex items-center gap-1.5">
          <Cpu className="w-3.5 h-3.5 text-emerald-500" /> Backend FastAPI
        </span>
        <span className="text-[10px] bg-emerald-500/10 text-emerald-400 px-1.5 py-0.5 rounded border border-emerald-500/20 font-mono">
          v1.0
        </span>
      </div>
    </aside>
  );
}