---
titulo: "Una IA puede haber resuelto Navier–Stokes. ¿Qué significa y cuál será el próximo Problema del Milenio?"
resumen: "OpenAI ha presentado una demostración de uno de los grandes problemas abiertos de las matemáticas. Qué se ha resuelto, cómo lo ha hecho una IA y qué nos dice sobre cuál podría ser el siguiente."
fecha: 2026-09-17
categoria: ciencia
imagen: /images/navier-stokes-portada.jpg
imagenAlt: "PENDIENTE"
imagenCredito: "PENDIENTE"
---

OpenAI ha presentado una demostración de uno de los grandes problemas abiertos de las matemáticas. Si supera el escrutinio de la comunidad, sería el segundo de los siete Problemas del Milenio en caer. ¿Qué se ha resuelto exactamente? ¿Cómo ha podido hacerlo una IA? ¿Y nos dice este caso algo sobre cuál podría ser el siguiente?

El 8 de septiembre de 2026 [OpenAI anunció](https://openai.com/index/navier-stokes-solution/) que uno de sus sistemas experimentales de inteligencia artificial había encontrado una solución al problema de Navier–Stokes, uno de los siete célebres Problemas del Milenio.

La noticia es extraordinaria, pero todavía requiere una cautela.

El Clay Mathematics Institute, la institución que creó los Problemas del Milenio, [ha dicho](https://www.claymath.org/news/navier-stokes-announcement/) que Navier–Stokes «aparentemente ha sido resuelto», no que el proceso haya concluido. Sus reglas exigen publicación, tiempo para el escrutinio y aceptación general de la solución entre la comunidad matemática antes de reconocer formalmente un resultado.

OpenAI, por su parte, ha dicho que no pretende reclamar el millón de dólares asociado al problema.

Por tanto, la formulación prudente por ahora es: una IA puede haber resuelto Navier–Stokes.

## ¿Qué problema ha resuelto exactamente?

Las ecuaciones de Navier–Stokes describen cómo se mueven los fluidos.

Y un fluido no es solamente el agua. También lo es el aire. Por eso estas ecuaciones aparecen detrás de fenómenos tan distintos como el agua circulando por una tubería, la aerodinámica de un avión o determinados modelos de la atmósfera.

Las ecuaciones se utilizan desde hace muchísimo tiempo. El problema no era saber escribirlas ni aplicarlas, sino comprender algo mucho más básico sobre ellas.

Supongamos que partimos de un fluido completamente regular: su velocidad es finita y cambia suavemente de un punto a otro.

La pregunta era:

¿garantizan las ecuaciones que esa regularidad se mantendrá para siempre o puede aparecer, en un tiempo finito, una singularidad?

En la solución presentada por OpenAI sucede esto último.

El movimiento se concentra progresivamente en una región cada vez más pequeña. Al acercarse a un determinado instante, la velocidad máxima del fluido crece sin límite, aunque la energía total permanece acotada. La solución deja entonces de ser suave: aparece una singularidad.

Hay un detalle importante.

En la construcción de OpenAI actúa sobre el fluido una fuerza externa suave.

A primera vista puede parecer una trampa: si estamos empujando al fluido desde fuera, ¿hemos resuelto realmente Navier–Stokes?

Sí, si la demostración es correcta.

El enunciado oficial del Problema del Milenio contemplaba expresamente esta posibilidad como una de las formas válidas de resolverlo. Por tanto, no sería una solución parcial: resolvería el problema tal como Clay lo formuló.

Seguiría abierta otra cuestión distinta y todavía más fuerte: si una singularidad semejante puede aparecer también sin ninguna fuerza externa.

Pero ése sería otro problema.

## Miles de agentes investigando a la vez

Probablemente lo más interesante de la historia sea cómo se llegó a la demostración.

OpenAI no puso a un único chatbot delante de las ecuaciones y esperó a que tuviera una inspiración.

El experimento se parece más a haber creado un gigantesco instituto de investigación artificial.

La compañía desplegó grupos de agentes capaces de consultar literatura, ejecutar código, desarrollar argumentos y explorar estrategias diferentes. Los resultados prometedores podían transmitirse después a otros grupos.

El equipo que terminó produciendo la solución llegó a involucrar del orden de 10.000 agentes concurrentes.

Y la historia tuvo un paso intermedio fundamental.

OpenAI había enviado agentes no solo contra Navier–Stokes, sino contra otros Problemas del Milenio y problemas relacionados. Cerca de cien agentes trabajaron durante unas 50 horas sobre las ecuaciones de Euler, emparentadas con Navier–Stokes, y consiguieron primero resolver un problema de formación de singularidades sin fuerza externa.

Ese avance hizo pensar que Navier–Stokes era especialmente prometedor.

OpenAI concentró entonces muchos más recursos allí y proporcionó el resultado de Euler a los agentes que estaban trabajando en el problema.

La solución apareció unas 88 horas después de iniciar los experimentos. Solo el ataque a Navier–Stokes generó unos 2,7 millones de mensajes y aproximadamente 130.000 millones de tokens de salida.

Después, la demostración fue formalizada en Lean, un sistema capaz de comprobar mecánicamente que, una vez fijadas las definiciones y los axiomas, cada paso lógico se deriva correctamente de los anteriores.

Eso aporta una garantía muy potente, aunque no elimina el trabajo humano: los matemáticos todavía tienen que comprobar que la formulación introducida en Lean representa exactamente el problema original y estudiar qué ideas contiene realmente la prueba.

## La IA no empezó desde cero

La estrategia utilizada tampoco nació de la nada dentro de las máquinas.

La European Mathematical Society ha señalado que la solución está estrechamente relacionada con una línea de investigación desarrollada previamente por Diego Córdoba, Luis Martínez-Zoroa y Fan Zheng, apoyada a su vez en décadas de trabajo sobre singularidades en ecuaciones de fluidos.

Dos de esos investigadores, Córdoba y Martínez-Zoroa, son españoles.

Habían desarrollado durante años una estrategia basada en estructuras de vorticidad a escalas progresivamente menores. Una estructura amplifica otra más pequeña, ésta hace lo propio con la siguiente y el movimiento va concentrándose cada vez más.

Ese programa acercó progresivamente a los matemáticos al tipo de singularidad que necesitaba el Problema del Milenio.

La importancia de esa contribución no es una reivindicación patriótica posterior. Charles Fefferman, autor del enunciado oficial de Navier–Stokes para el Clay Mathematics Institute, ha señalado a Córdoba y Martínez-Zoroa como figuras centrales de esta historia.

Por tanto, sería engañoso presentar el resultado como si diez mil agentes hubieran recibido una hoja en blanco y descubierto de repente una nueva forma de pensar los fluidos.

Pero también sería incorrecto decir que simplemente copiaron una demostración existente.

La demostración completa no existía.

Lo que existía era un camino prometedor.

La IA tuvo que desarrollarlo, intentar construcciones, encontrar argumentos, descartar caminos y completar finalmente algo que los investigadores humanos todavía no habían conseguido demostrar.

La diferencia fundamental parece haber estado en la escala.

Un matemático puede preguntarse si dedicar varias semanas a una estrategia A o abandonarla para probar B.

Aquí podían existir cientos de agentes explorando simultáneamente variantes de A, otros cientos trabajando en B y otros tantos intentando C.

No es simplemente «pensar diez mil veces más rápido».

Es hacer una parte de la investigación matemática de forma masivamente paralela.

## Una carrera que ya había comenzado

OpenAI tampoco era el único grupo utilizando IA sobre esta línea.

Los matemáticos Tristan Buckmaster, de la Universidad de Nueva York, y Levent Alpöge, de Anthropic, llevaban tiempo trabajando con modelos de inteligencia artificial para extender las ideas anteriores y habían obtenido un resultado relacionado para las ecuaciones de Euler con fuerza externa.

OpenAI reconoce su prioridad en ese resultado y admite además que comenzó su gran ofensiva del 1 de septiembre después de conocer rumores de importantes avances matemáticos que posteriormente relacionó con su trabajo.

La coincidencia originó una discusión sobre prioridad y sobre si el trabajo privado de Buckmaster, realizado en parte con productos de OpenAI, podría haber influido de alguna manera en el sistema. OpenAI lo niega y afirma que una investigación interna concluyó que esos prompts no pudieron influir en el modelo ni siquiera a través del entrenamiento.

No hace falta resolver aquí esa controversia.

Lo importante para nuestra historia es otra cosa: varios grupos humanos, utilizando también inteligencia artificial, estaban empezando a recorrer una línea de investigación que acababa de volverse especialmente fértil.

## ¿Puede una IA producir conocimiento nuevo?

Aquí aparece una pregunta mucho mayor que Navier–Stokes.

Durante años ha sido habitual imaginar los modelos generativos como sistemas encerrados dentro de una especie de círculo.

Aprenden a partir de textos, imágenes, código o música previamente creados por humanos. Después pueden recombinar y generalizar ese conocimiento de maneras sorprendentes.

Pero ¿pueden realmente cruzar la frontera de lo conocido?

Navier–Stokes ofrece una respuesta parcial.

Si la demostración termina siendo validada, la IA habrá contribuido a obtener un resultado matemático que ningún ser humano había conseguido demostrar todavía, aunque los avances inmediatamente anteriores habían llevado ya a especialistas como Terence Tao a considerar muy probable que una construcción de este tipo fuese posible.

Eso sería conocimiento matemático nuevo.

Pero no significa necesariamente que la IA haya inventado una nueva forma conceptual de pensar el problema.

Podemos distinguir tres niveles.

El primero es obtener un resultado que antes era desconocido. Navier–Stokes parece estar ya en ese nivel, condicionado a la validación.

El segundo sería inventar un método matemático fundamentalmente nuevo para conseguirlo. Aquí la respuesta es mucho menos clara: la estrategia principal tenía raíces profundas en investigaciones humanas anteriores.

Y el tercero sería todavía más ambicioso: inventar un nuevo paradigma intelectual.

No sabemos si la IA actual puede hacer eso.

Además, un teorema nuevo no equivale necesariamente a una nueva comprensión humana. Una máquina podría producir una demostración correcta y extremadamente compleja sin que los matemáticos comprendiesen todavía cuáles son las ideas esenciales que hacen funcionar el argumento.

Así que el resultado es impresionante sin necesidad de exagerarlo.

Si se confirma, mostrará que una IA puede utilizar el conocimiento humano existente como punto de partida y llevarlo hasta un resultado que nosotros todavía no habíamos conseguido alcanzar.

La gran incógnita es si también puede inventar por sí sola los marcos conceptuales que permiten abrir caminos completamente nuevos.

## ¿Qué son los Problemas del Milenio?

En el año 2000, el Clay Mathematics Institute seleccionó siete problemas que representaban algunas de las grandes fronteras abiertas de las matemáticas y reservó siete millones de dólares: uno por cada problema.

El instituto había sido fundado dos años antes por el empresario estadounidense Landon T. Clay y su esposa, Lavinia D. Clay, que dedicaron parte de su fortuna a impulsar las matemáticas.

No existe un límite de tiempo para resolver los problemas.

Hasta ahora solo uno había caído: la conjetura de Poincaré, demostrada por el matemático ruso Grigori Perelman.

Clay le concedió en 2010 el millón de dólares.

Perelman lo rechazó.

No parece que fuese simplemente una extravagancia. Entre otras cosas, consideraba que la aportación de Richard Hamilton —el matemático que había desarrollado el programa sobre el que se apoyó su solución— no había sido menor que la suya. Cuatro años antes ya había rechazado también la Medalla Fields.

Hay una curiosa resonancia con el caso actual.

Hamilton abrió una vía que Perelman consiguió culminar.

Ahora Córdoba, Martínez-Zoroa, Zheng y otros investigadores han construido buena parte del camino que sistemas de inteligencia artificial pueden haber terminado de recorrer.

En matemáticas, como en buena parte de la ciencia, el último paso raramente nace de la nada.

## ¿Qué problemas quedarían?

Si Navier–Stokes termina siendo aceptado, quedarían cinco Problemas del Milenio.

La **hipótesis de Riemann** busca demostrar una propiedad de la función zeta estrechamente relacionada con la distribución de los números primos. Los ceros de la función no son los números primos, pero su posición contiene información profunda sobre cómo éstos se distribuyen.

**P frente a NP** pregunta, simplificando muchísimo, si todo problema cuya solución puede comprobarse rápidamente puede también resolverse rápidamente. Su respuesta tendría enormes consecuencias para la informática, la optimización y la criptografía.

La **conjetura de Birch y Swinnerton-Dyer** conecta las soluciones racionales de unas ecuaciones llamadas curvas elípticas con el comportamiento de una función analítica asociada a ellas.

La **conjetura de Hodge** intenta establecer un profundo puente entre diferentes formas de describir los objetos geométricos, especialmente la geometría algebraica y la topología.

Y **Yang–Mills y el salto de masa** pretende proporcionar una fundamentación matemática rigurosa a una teoría utilizada con enorme éxito en la física de partículas.

Resolver alguno de ellos no tiene por qué producir una nueva tecnología al día siguiente. Buena parte de su importancia reside en las herramientas y conexiones matemáticas que habría que descubrir durante el camino.

Pero Navier–Stokes plantea ahora una pregunta inevitable.

## ¿Cuál podría resolver después una IA?

No lo sabemos.

Y cualquier lista ordenada sería poco más que una apuesta.

Pero el caso Navier–Stokes sí permite preguntarnos qué características parecen favorecer las capacidades que acaba de demostrar la inteligencia artificial.

Había una gran cantidad de conocimiento previo, una línea humana reciente especialmente prometedora, problemas intermedios que podían utilizarse como escalones y un enorme espacio técnico de posibilidades que podía dividirse entre miles de agentes.

Además, Navier–Stokes tenía una ventaja particular: una de las formas válidas de resolverlo consistía en construir un solo ejemplo que desarrollase una singularidad.

Eso encaja especialmente bien con una estrategia capaz de explorar muchas construcciones diferentes.

Para varias de las conjeturas restantes, si son ciertas como generalmente se espera, el reto sería distinto: habría que demostrar una afirmación válida para infinitos casos. Encontrar millones de ejemplos favorables nunca sería suficiente.

Aun así, Birch–Swinnerton-Dyer y la hipótesis de Riemann resultan especialmente interesantes.

Ambas disponen de enormes cantidades de conocimiento previo, resultados parciales, problemas intermedios y una importante dimensión computacional. Son precisamente el tipo de ecosistema donde miles de agentes pueden intentar caminos diferentes y compartir avances.

Pero Riemann muestra también el límite de esta estrategia: puedes comprobar diez billones de ceros y seguir sin haber demostrado qué sucede con todos los demás. En algún momento hace falta una idea capaz de controlar infinitos casos de una sola vez.

P vs NP presenta otro obstáculo. Décadas de investigación han demostrado que familias enteras de técnicas no son suficientes para resolverlo. Diez mil agentes explorando variantes de una estrategia que sabemos insuficiente no solucionan necesariamente nada.

Hodge es más difícil de clasificar: existe muchísimo conocimiento previo, pero no está claro que su principal cuello de botella sea el tipo de exploración masivamente paralela que ha funcionado ahora.

Y Yang–Mills parece todavía menos parecido a Navier–Stokes. Su resolución parece requerir construir nuevas ideas y parte de la propia infraestructura matemática necesaria para formular rigurosamente la teoría.

Eso nos devuelve a la cuestión realmente importante.

## La verdadera pregunta después de Navier–Stokes

Quizá lo más interesante de esta historia no sea acertar si el siguiente problema será Riemann o Birch–Swinnerton-Dyer.

Es saber qué clase de ciencia puede hacer una inteligencia artificial.

Si la demostración termina siendo validada, una IA habrá utilizado el conocimiento humano existente como punto de partida para alcanzar un resultado matemático que nosotros todavía no habíamos conseguido demostrar.

Habrá contribuido, por tanto, a desplazar la frontera del conocimiento.

Pero queda la pregunta más difícil.

¿Qué ocurrirá cuando no exista una buena estrategia humana que desarrollar?

¿Podrá la IA inventarla?

¿Será capaz no solo de recorrer caminos nuevos, sino de imaginar una forma completamente distinta de mirar el territorio?

El equivalente matemático a inventar el cubismo antes de Picasso.

Navier–Stokes todavía no nos permite responder.

Pero si algún día la respuesta es sí, la pregunta sobre cuál será el siguiente Problema del Milenio empezará a quedarse pequeña.

Porque entonces ya no estaremos preguntándonos simplemente si la inteligencia artificial puede ayudarnos a avanzar más deprisa por las fronteras de la ciencia.

Estaremos preguntándonos hasta dónde puede desplazarlas.
