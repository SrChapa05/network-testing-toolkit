const API_BASE_URL = 'http://127.0.0.1:8000/api';

/**
 * Obtiene la lista de todos los módulos registrados en el backend.
 */
export async function getModules() {
  try {
    const response = await fetch(`${API_BASE_URL}/modules`);
    if (!response.ok) {
      throw new Error('Error al conectar con el servidor para listar módulos');
    }
    return await response.json();
  } catch (error) {
    console.error('API Error (getModules):', error);
    throw error;
  }
}

/**
 * Envía una solicitud para ejecutar un módulo específico con un parámetro opcional.
 * @param {string} moduleId - Identificador único del módulo (ej: "ping-sweep")
 * @param {string} param - Parámetro o objetivo de red (ej: "192.168.1.0/24")
 */
export async function executeModule(moduleId, param = '') {
  try {
    const response = await fetch(`${API_BASE_URL}/execute/${moduleId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ param }),
    });

    if (!response.ok) {
      throw new Error(`Error en la ejecución del módulo ${moduleId}`);
    }

    return await response.json();
  } catch (error) {
    console.error('API Error (executeModule):', error);
    throw error;
  }
}