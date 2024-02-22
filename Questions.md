# Preguntas

### Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste.
Si aún no he hecho git push, usaría --amend:

```bash
git add archivo
git commit --amend -m "Nuevo mensaje del commit"

```

Si ya hice git push, usaría git commit --amend y push --force para sobrescribir el commit. Sin embargo, debo tener cuidado de que alguien más haya hecho push a la misma rama en la que estoy trabajando para evitar borrar su trabajo:



```bash
git add archivo
git commit --amend -m "Nuevo mensaje del commit"
git push --force
```


### Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado?
He trabajo con varios workflow de git mucho muy parecedios con diferente nombre, 
bitbucket y github y gitlab dan la opciones para personalizar y configuar eso workflow.
Al final lo importante que es el equipo( los desarrolladores) entiendas de donde salen las rama y hacia donde van los pull request 

* Git Flow: dos ramas principales: master y develop. Se crean ramas de características, ramas de liberación y ramas de corrección de errores.
* GitHub Flow: rama principal (master o main) y fomenta la creación de ramas para nuevas características o correcciones. Los cambios se fusionan a la rama principal a través de pull requests
* Master-only Flow: Como su nombre lo indica una sola rama puede ser adecuado para proyectos más pequeños o situaciones donde la simplicidad es clave como este proyecto de TalanaKombat

### ¿Cuál ha sido la situación más compleja que has tenido con esto?
Fue en alrededor de marzo del 2019, trabajaba en un proyecto de monorepo donde el backend y frontend compartían el mismo repo pero en carpetas diferentes. El equipo de frontend tenía un proyecto en otra rama llamada "proyecto-z", la cual no había sido actualizada con las ramas master o develop desde hacía 3 meses.
Al momento de hacer el pull request, había una cantidad de conflictos tanto en el backend como en el frontend. Dado que los otros equipos habían ido mezclando sus proyectos y tareas terminadas,
tuvimos que contar con la ayuda de ese equipo de frontend y utilizar un IDE como PyCharm para poder comparar y revisar la historia de cada archivo, permitiendo así mezclar uno por uno.



### ¿Qué experiencia has tenido con los microservicios?
Mi experiencia con los microservicios ha sido entusiasta, aunque limitada en el ámbito profesional. He desarrollado APIs sin utilizar bases de datos para colaborar con desarrolladores de frontend, exponiendo un API en Heroku mediante json-server. Además, he jugando Google Cloud Functions para implementar funciones Python sencillas.

###  ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?
Los dos servicios son excelentes y cubren muchas de las necesidades, presupuestos y proyectos. Me gusta GCP, sobre todo para la interfaz de usuario de la web, ya que tiene menos servicios que AWS. Por lo tanto, resulta menos abrumador al momento de aprender y explotar todos sus servicios.





