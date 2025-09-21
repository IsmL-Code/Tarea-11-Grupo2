###  Sistema de Gestión de Pacientes para una Clínica
Comparación entre Solución 1 y Solución 2
1. ¿Se separaron adecuadamente las responsabilidades (pacientes, citas, historiales)?

Solución 1:  No. Todo está en un solo módulo, con listas y funciones que manejan todo junto.

Solución 2:  Sí. Se usan clases (Paciente, Cita, Historia) y managers específicos (PacienteManager, CitaManager, HistoriaManager, FacturacionManager), cada uno con su responsabilidad.

2. ¿Qué sucede si se intenta programar una cita en un horario ya ocupado?

Solución 1:  Se valida que no exista otra cita en la misma fecha, hora y con el mismo doctor.

Solución 2:  También se valida en CitaManager.programar(), pero además lanza una excepción (ValueError) para un mejor manejo de errores.

3. ¿El sistema puede extenderse fácilmente para añadir nuevas especialidades médicas?

Solución 1:  No fácilmente. Habría que modificar las funciones y la estructura de los diccionarios manualmente.

Solución 2:  Sí. Es sencillo extender la clase Cita o añadir nuevos atributos y métodos en los managers. La arquitectura está pensada para crecer.

4. ¿Los nombres de las funciones y variables describen claramente su propósito?

Solución 1:  Sí. Funciones como registrar_paciente(), programar_cita() son claras y descriptivas.

Solución 2:  Sí, e incluso mejora la claridad con clases y métodos (PacienteManager.registrar(), CitaManager.programar()).

5. ¿Se documentaron adecuadamente las funciones y métodos críticos?

Solución 1:  No hay docstrings ni comentarios explicativos.

Solución 2:  Mejor estructurado, pero tampoco incluye docstrings. Se recomienda añadirlos en métodos críticos.

6. ¿Se eligieron estructuras de datos apropiadas para cada tipo de información?

Solución 1:  Uso de listas de diccionarios. Correcto para un prototipo, pero limitado a largo plazo.

Solución 2:  Uso de clases y listas de objetos, lo que mejora organización, reutilización y extensibilidad.

-------------------------------------------------------------------------------------------------------------
###  Plataforma de Comercio Electrónico 
1. ¿Se implementaron prácticas seguras para el manejo de información sensible?

Solución 1:  No. Datos como correos, pagos, etc. se manejan en variables simples sin protección ni validación.

Solución 2:  Todavía no hay cifrado ni anonimización de datos, pero sí hay separación de responsabilidades, lo que facilita agregar seguridad después.

2. ¿El sistema mantiene la integridad de los datos durante procesos críticos (como pagos)?

Solución 1:  No. Solo descuenta stock y confirma el pago de forma secuencial, sin validaciones adicionales ni rollback.

Solución 2:  Sí, hay validaciones de stock antes de confirmar el pedido y el proceso de pago se ejecuta como un paso obligatorio. Si falla, el pedido no se crea.

3. ¿Cómo maneja el sistema intentos simultáneos de compra del mismo producto?

Solución 1:  No contempla compras simultáneas. Podría sobrescribir stock si dos usuarios compran a la vez.

Solución 2:  Mejor, porque valida stock antes de crear el pedido, pero no implementa bloqueos de concurrencia (como asyncio.Lock o transacciones distribuidas).

4. ¿Existe una clara división entre lógica de negocio, presentación y acceso a datos?

Solución 1:  No. Todo está en funciones con listas y diccionarios mezclados, sin capas claras.

Solución 2:  Sí. Está organizado en modelos (Producto, Usuario, Pedido), managers/servicios (Catalogo, Inventario, Pago, SistemaPedidos), y la interacción de usuario está en la parte final (main_program).

5. ¿Qué tan fácil es modificar parámetros como impuestos, métodos de envío, etc.?

Solución 1:  Muy difícil. Habría que cambiar funciones y diccionarios manualmente.

Solución 2:  Fácil. Solo habría que añadir atributos o métodos en las clases Pago o Pedido (por ejemplo, un método calcular_impuestos() o seleccionar_envio()).
