import React, { useState, useEffect } from 'react';
import { Play, Terminal, Clock, CheckCircle2, AlertCircle, RefreshCw } from 'lucide-react';
import { executeModule } from '../services/api';

export default function ConsolePanel({ selectedModule }) {
  const [param, setParam] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  // Limpiar estados al cambiar de módulo
  useEffect(() => {
    setParam('');
    setResult(null);
    setError(null);
  }, [selectedModule]);

  const handleExecute = async (e) => {
    e.preventDefault();
    if (!selectedModule) return;

    setLoading(true);
    setResult(null);
    setError(null);

    try {
      const data = await executeModule(selectedModule.id, param);
      setResult(data);
    } catch (err) {
      setError('No se pudo completar la ejecución del módulo. Verifique la conexión con el backend FastAPI.');
    } finally {
      setLoading(false);
    }
  };

  if (!selectedModule) {
    return (
      <div className="flex-1 flex flex-col items-center justify-center bg-slate-950 text-slate-500 p-6">
        <Terminal className="w-16 h-16 mb-4 text-slate-700 stroke-1" />
        <p className="text-lg font-medium">Selecciona un módulo de la barra lateral</p>
        <p className="text-sm text-slate-600 mt-1">Elige una herramienta de red para configurar sus parámetros y ejecutarla.</p>
      </div>
    );
  }

  return (
    <div className="flex-1 flex flex-col bg-slate-950 h-screen overflow-hidden">
      {/* Cabecera del módulo activo */}
      <div className="bg-slate-900 border-b border-slate-800 p-6 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <span className="text-xs font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
              {selectedModule.id}
            </span>
            <span className="text-xs text-slate-500">• Módulo Activo</span>
          </div>
          <h2 className="text-xl font-bold text-slate-100 mt-1">{selectedModule.name}</h2>
          <p className="text-xs text-slate-400 mt-0.5">Configura los parámetros de ejecución para este script de red.</p>
        </div>
      </div>

      {/* Formulario de Parámetros */}
      <div className="p-6 border-b border-slate-800/60 bg-slate-900/40">
        <form onSubmit={handleExecute} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">
              Parámetro de Entrada / Objetivo
            </label>
            <div className="flex gap-3">
              <input
                type="text"
                value={param}
                onChange={(e) => setParam(e.target.value)}
                placeholder="Ej: 192.168.1.1 o 127.0.0.1 (dejar vacío si no requiere)"
                className="flex-1 bg-slate-900 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-slate-200 placeholder-slate-600 focus:outline-none focus:border-emerald-500 font-mono"
              />
              <button
                type="submit"
                disabled={loading}
                className="bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-semibold px-6 py-2.5 rounded-lg text-sm flex items-center space-x-2 transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-lg shadow-emerald-950/20 cursor-pointer"
              >
                {loading ? (
                  <>
                    <RefreshCw className="w-4 h-4 animate-spin" />
                    <span>Ejecutando...</span>
                  </>
                ) : (
                  <>
                    <Play className="w-4 h-4 fill-slate-950" />
                    <span>Ejecutar</span>
                  </>
                )}
              </button>
            </div>
          </div>
        </form>
      </div>

      {/* Consola de Salida Estilo Terminal */}
      <div className="flex-1 flex flex-col p-6 overflow-hidden">
        <div className="flex items-center justify-between mb-2">
          <div className="flex items-center space-x-2 text-xs font-semibold text-slate-400 uppercase tracking-wider">
            <Terminal className="w-4 h-4 text-emerald-400" />
            <span>Consola de Salida (Stdout)</span>
          </div>
          {result && (
            <div className="flex items-center space-x-4 text-xs">
              <span className="flex items-center gap-1 text-slate-400 font-mono">
                <Clock className="w-3.5 h-3.5 text-slate-500" /> {result.duration_seconds}s
              </span>
              <span className={`flex items-center gap-1 font-medium px-2 py-0.5 rounded ${result.success ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' : 'bg-red-500/10 text-red-400 border border-red-500/20'}`}>
                {result.success ? <CheckCircle2 className="w-3.5 h-3.5" /> : <AlertCircle className="w-3.5 h-3.5" />}
                {result.success ? 'Completado' : 'Fallido'}
              </span>
            </div>
          )}
        </div>

        <div className="flex-1 bg-slate-950 border border-slate-800 rounded-lg p-4 font-mono text-xs text-emerald-400 overflow-y-auto shadow-inner select-text whitespace-pre-wrap">
          {loading ? (
            <div className="h-full flex flex-col items-center justify-center text-slate-500 space-y-2">
              <RefreshCw className="w-8 h-8 animate-spin text-emerald-500/50" />
              <p>Ejecutando script de red en el backend... Esto puede tardar según el objetivo.</p>
            </div>
          ) : error ? (
            <div className="text-red-400 flex items-center space-x-2">
              <AlertCircle className="w-4 h-4 flex-shrink-0" />
              <span>{error}</span>
            </div>
          ) : result ? (
            result.output || <span className="text-slate-600">// El script finalizó sin texto impreso en stdout.</span>
          ) : (
            <span className="text-slate-600">// Esperando ejecución. Ingrese un parámetro y haga clic en "Ejecutar"...</span>
          )}
        </div>
      </div>
    </div>
  );
}