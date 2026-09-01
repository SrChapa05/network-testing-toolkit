import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import ConsolePanel from './components/ConsolePanel';
import { getModules } from './services/api';

export default function App() {
  const [modules, setModules] = useState([]);
  const [selectedModule, setSelectedModule] = useState(null);
  const [loadingModules, setLoadingModules] = useState(true);

  // Cargar la lista de módulos al iniciar la aplicación
  useEffect(() => {
    async function fetchModules() {
      try {
        const data = await getModules();
        setModules(data.modules || []);
        // Opcional: Seleccionar el primer módulo por defecto si existe
        if (data.modules && data.modules.length > 0) {
          setSelectedModule(data.modules[0]);
        }
      } catch (error) {
        console.error('Error al cargar los módulos desde el backend:', error);
      } finally {
        setLoadingModules(false);
      }
    }

    fetchModules();
  }, []);

  return (
    <div className="flex h-screen bg-slate-955 text-slate-100 overflow-hidden font-sans">
      {/* Barra lateral con la lista de herramientas */}
      <Sidebar
        modules={modules}
        selectedModule={selectedModule}
        onSelectModule={setSelectedModule}
        loading={loadingModules}
      />

      {/* Panel principal de ejecución y consola */}
      <ConsolePanel selectedModule={selectedModule} />
    </div>
  );
}