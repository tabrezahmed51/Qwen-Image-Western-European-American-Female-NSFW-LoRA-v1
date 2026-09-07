---
license: other
license_name: qwen-image-western-european-american-female-nsfw-lora-v1-non-commercial
license_link: https://huggingface.co/perpetual3x/Qwen-Image-Western-European-American-Female-NSFW-LoRA-v1/blob/main/LICENSE
base_model:
  - Qwen/Qwen-Image-2512
base_model_relation: adapter
library_name: diffusers
pipeline_tag: text-to-image
tags:
  - qwen-image
  - qwen-image-2512
  - lora
  - text-to-image
  - photorealistic
  - realistic-photography
  - western-european-woman
  - american-woman
  - environmental-portrait
  - body-diversity
  - experimental
  - nsfw
language:
  - en
  - fr
  - es
---

<div style="display:flex; flex-wrap:nowrap; gap:6px; align-items:center; overflow-x:auto;"><a href="#" style="display:inline-flex; align-items:center; height:22px; vertical-align:middle;"><img alt="Visitors" src="https://visitor-badge.laobi.icu/badge?page_id=perpetual3x.Qwen-Image-Western-European-American-Female-NSFW-LoRA-v1" style="display:block; height:22px; vertical-align:middle;"></a><a href="#" style="display:inline-flex; align-items:center; height:22px; vertical-align:middle;"><img alt="Base Model" src="https://img.shields.io/badge/Base-Qwen%20Image%202512-blue" style="display:block; height:22px; vertical-align:middle;"></a><a href="#" style="display:inline-flex; align-items:center; height:22px; vertical-align:middle;"><img alt="GPU" src="https://img.shields.io/badge/GPU-RTX%20PRO%206000%20Blackwell%2096GB-blue" style="display:block; height:22px; vertical-align:middle;"></a><a href="#" style="display:inline-flex; align-items:center; height:22px; vertical-align:middle;"><img alt="Training" src="https://img.shields.io/badge/Training-10K%20Steps-purple" style="display:block; height:22px; vertical-align:middle;"></a><a href="#" style="display:inline-flex; align-items:center; height:22px; vertical-align:middle;"><img alt="Trigger" src="https://img.shields.io/badge/Trigger-None-success" style="display:block; height:22px; vertical-align:middle;"></a></div>

### Language / Langue / Idioma

**🇬🇧 English - displayed below**

-----------

<details name="language-version">
<summary><strong>🇫🇷 Français - afficher la version complète</strong></summary>

---------

# LoRA NSFW féminin ouest-européen et américain pour Qwen Image v1

### De la pierre atlantique à la lumière du Pacifique - des identités occidentales sans prétendre réparer l'anatomie.

> **Avertissement - contenu pour adultes :** ce dépôt contient des images explicites générées par IA et s'adresse exclusivement aux adultes. Toutes les personnes représentées ou décrites dans les exemples et les prompts de référence sont clairement adultes.

![Couverture](assets/c0.png)

## Une distinction importante avant de commencer

**Ce LoRA n'est pas un LoRA de correction anatomique.** Il a été entraîné pour représenter une large gamme visuelle de femmes adultes d'Europe occidentale et des États-Unis : visages, corps, âges, présence, caractère photographique et environnements. Il ne prétend pas corriger seul l'anatomie intime dans les poses difficiles. Un modèle peut comprendre un phare de Nouvelle-Angleterre et rester philosophiquement indécis devant le bassin humain.

Si la correction anatomique est prioritaire, combinez-le prudemment avec l'une de mes versions spécialisées, en particulier [**Female Anatomy Fix NSFW LoRA - Triggerless v2**](https://huggingface.co/perpetual3x/Qwen-Image-Female-Anatomy-Fix-NSFW-LoRA-Triggerless-v2) ou son compagnon plus explicite [**Triggered v2**](https://huggingface.co/perpetual3x/Qwen-Image-Female-Anatomy-Fix-NSFW-LoRA-Triggered-v2). Le LoRA anatomique peut surveiller la structure pendant que celui-ci s'occupe de la personne, de l'atmosphère et du contexte culturel. Commencez avec des poids modérés : deux spécialistes qui crient à pleine puissance améliorent rarement une réunion.

**Qwen Image Western European American Female NSFW LoRA v1** est un LoRA photoréaliste expérimental pour **Qwen/Qwen-Image-2512 Text-to-Image**. Il se concentre sur des femmes clairement adultes d'Europe occidentale et des États-Unis, dans des environnements urbains, ruraux, côtiers, montagneux, domestiques et artistiques. Le jeu de données comprend différents âges adultes, morphologies, traits du visage et contextes régionaux, plutôt qu'un seul visage poli qui change constamment d'adresse.

Le titre décrit le jeu de données et son champ de références visuelles ; il n'affirme pas que l'Europe ou l'Amérique possèdent une apparence canonique. Les continents ne sont pas des agences de casting, et les passeports ne sont pas livrés avec un préréglage obligatoire des pommettes.

## Points forts

- Entraîné sur **8 417** images d'adultes
- Large représentation visuelle de femmes adultes ouest-européennes et américaines
- Diversité d'âges adultes, de morphologies, de traits du visage et de textures cutanées naturelles
- Lofts urbains, intérieurs historiques, fermes, côtes, forêts, montagnes, déserts et motels routiers
- Caractère photographique artistique, documentaire, environnemental, argentique couleur et monochrome
- Contrôle en langage naturel sans mot déclencheur obligatoire
- **2 000** prompts réutilisables pour tester la diversité et les contextes régionaux
- Conçu et testé pour Qwen-Image-2512 T2I

## Ce que ce modèle est - et ce qu'il n'est pas

Cette version porte sur **la diversité des identités, l'atmosphère, les lieux et la présence humaine adulte**. Elle vise à produire des images moins proches d'une beauté synthétique générique et davantage reliées à des personnes crédibles et à des environnements ouest-européens ou américains reconnaissables.

Elle n'est volontairement pas présentée comme spécialiste de l'anatomie. Les vues frontales, arrière, assises, allongées, fortement occultées ou physiquement difficiles peuvent encore produire une anatomie intime, des mains, des pieds ou des articulations incorrects. Lorsque ces détails comptent, utilisez un LoRA anatomique, un prompt adapté ou une autre seed.

### Le pendant, pas le remplacement

Ce projet forme un contraste volontaire avec [**Eastern European Female Anatomy NSFW LoRA v1**](https://huggingface.co/perpetual3x/Eastern-European-Female-Anatomy-NSFW-LoRA-v1) :

| | Cette version | Eastern European Anatomy v1 |
|:--|:--|:--|
| Objectif principal | Identité, morphologies, décors et caractère photographique ouest-européens/américains | Précision et diversité de l'anatomie féminine adulte |
| Champ géographique | Europe occidentale et États-Unis | Jeu photographique est-européen |
| Spécialisation anatomique | Non | Oui |
| Mot déclencheur | Aucun | `zl_nubiles_v1` |
| Usage idéal | Base de personnage et de contexte visuel | Génération et correction orientées anatomie |

Ils répondent à deux questions différentes. L'un demande : « Qui est cette personne, et dans quel monde vit-elle ? » L'autre demande : « Toutes les structures visibles sont-elles arrivées à la même réunion ? » Selon l'image, les deux questions peuvent être utiles.

## Une brève note de l'humain chargé des tests

Ces dernières semaines, j'ai examiné davantage de photographies de corps féminins et masculins qu'un service de radiologie légèrement désorienté. Je souffre maintenant de vertiges occasionnels. Le diagnostic actuel est un **surapprentissage de l'opérateur aux grilles comparatives**.

Après la fin du projet d'anatomie coréenne, je compte prendre une vraie pause, regarder des arbres sans estimer leur poids LoRA et vérifier que les nuages existent toujours sans huit étapes d'inférence. Si je commence à voir des numéros de seed au-dessus des passants, les vacances auront déjà trop attendu.

## Informations d'entraînement

| Élément | Valeur |
|:---|---:|
| Modèle de base | Qwen Image 2512 |
| Images d'entraînement | 8 417 |
| GPU | NVIDIA RTX PRO 6000 Blackwell / 96 Go |
| Rank | 64 |
| Taille du lot | 8 |
| Étapes d'entraînement | 10 000 |
| Déclencheur | Aucun - langage naturel uniquement |

## Réglages recommandés

- **Pipeline recommandé :** Qwen Image 2512 T2I
- **Poids conseillé :** commencez entre `0.8-1.2`, puis ajustez selon le prompt et les autres LoRA
- **Empilement de LoRA :** commencez autour de `0.8-1.0` pour celui-ci et utilisez un poids modéré pour le spécialiste anatomique
- **Prompt :** décrivez en langage naturel l'âge adulte, l'apparence, la morphologie, le lieu, l'humeur, la pose, la lumière et le traitement photographique
- **Déclencheur :** aucun mot fixe n'est requis

Les poids élevés peuvent renforcer l'identité et les tendances photographiques apprises, mais aussi répéter certains visages, lisser la peau ou imposer une composition familière.

## Compatibilité

Ce LoRA est destiné à **Qwen/Qwen-Image-2512** pour la génération Text-to-Image. La compatibilité avec Qwen-Image-Edit ou des architectures sans rapport n'est pas garantie.

## Limites connues

- aucune garantie dédiée de correction de l'anatomie intime
- mains, doigts, pieds, membres, articulations ou poses difficiles parfois incorrects
- répétition de certains traits du visage ou stéréotypes régionaux à poids excessif
- peau trop lissée, biais glamour ou style photographique plus fort que demandé
- âge ou morphologie variables entre les seeds
- conflits avec des adaptateurs de personnage, de style ou d'anatomie très directifs
- erreurs de géométrie dans l'architecture, les balustrades, les fenêtres et les intérieurs
- indices régionaux faibles lorsque le prompt ne décrit pas l'environnement

Le modèle doit être traité comme une tendance visuelle étendue, non comme un recensement, une définition ethnographique ou une machine à délivrer des certificats de nationalité. Testez plusieurs seeds et baissez le poids si une tendance apprise commence à parler au nom d'un continent entier.

## Exemples

La couverture est volontairement présentée sans prompt. Les huit exemples suivants conservent leurs prompts anglais complets. Toutes les personnes représentées sont adultes.

## Exemple 1 - Ruines de pierre

| ![Exemple 1](assets/w1.png) |
|:---:|

**Prompt original (anglais)**

> A museum-minded portrait observes an adult nude woman in a composed but spontaneous-looking portrait pausing beside rough stone ruins while listening to the wind beside pale stone outcrops overlooking a distant patchwork of fields. Her hair is gathered away from her face, leaving the gesture clearly readable. A distant medium-format composition lets weather and place occupy most of the frame. Open shade beneath the trees provides even illumination while the distance remains luminous. The photograph has the tonal restraint of medium-format film, subtle grain and carefully held highlights. The scene feels candid, meditative and grounded in ordinary physical reality. Avoid plastic skin, exaggerated symmetry or fashion retouching; retain natural variation and small imperfections.

---

## Exemple 2 - Ancienne bibliothèque

| ![Exemple 2](assets/w2.png) |
|:---:|

**Prompt original (anglais)**

> This poetic environmental portrait features an adult nude woman treated as a classical figure study sitting sideways on a weathered wooden bench with one knee raised and both shoulders relaxed within an old library hall with empty shelves and diffuse window light. Her hair remains natural and minimally styled. A gently compressed telephoto view layers the figure, architecture and distant space. Late-day window light meets soft reflection from the timber floor. The photograph has the tonal restraint of medium-format film, subtle grain and carefully held highlights. The environment and figure share equal visual importance, producing a calm sense of scale. Keep the gesture physically achievable and the relationship between body, gravity and support convincing.

---

## Exemple 3 - Grange du Midwest

| ![Exemple 3](assets/w3.png) |
|:---:|

**Prompt original (anglais)**

> A clearly adult Italian-American woman age 30 with olive-toned skin, dark wavy hair and a soft curvy build, standing fully nude in profile while wind moves her hair and the surrounding vegetation in a weathered Midwestern barn with hay dust, timber rafters and open fields beyond. A low but restrained viewpoint that preserves realistic proportions. Crisp winter sunlight with cool ambient fill. The mood is calm, mature and emotionally present. Cinematic environmental portraiture with realistic material textures and gentle lens softness. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

---

## Exemple 4 - Cour en adobe du Nouveau-Mexique

| ![Exemple 4](assets/w4.png) |
|:---:|

**Prompt original (anglais)**

> A clearly adult French-American woman age 33 with chestnut hair, subtle freckles and an elegant average build, stretching fully nude after a walk with both arms raised in a physically believable gesture in a private New Mexico adobe courtyard with vigas, clay walls and desert sunlight. A medium-format three-quarter composition connecting face, body and place. Cool dawn light balanced by a small area of warm interior illumination. The mood is solitary and contemplative, with no commercial beauty performance. Restrained 35 mm color-negative realism with subtle grain and no beauty smoothing. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

---

## Exemple 5 - Loft du Lower East Side

| ![Exemple 5](assets/w5.png) |
|:---:|

**Prompt original (anglais)**

> A clearly adult Danish-American woman age 34 with sandy hair and a soft unretouched body, standing fully nude in a relaxed contrapposto with both arms resting naturally in a rain-darkened Lower East Side loft beside a metal fire escape and wet rooftop reflections. A full-body eye-level environmental frame with generous space around the figure. Crisp winter sunlight with cool ambient fill. The mood is playful in a restrained documentary manner. Cinematic environmental portraiture with realistic material textures and gentle lens softness. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

---

## Exemple 6 - Motel enneigé

| ![Exemple 6](assets/w6.png) |
|:---:|

**Prompt original (anglais)**

> A clearly adult Welsh-American woman age 36 with short dark hair and a slender angular frame, kneeling fully nude on a folded blanket while looking quietly into the distance in a snowbound mountain motel with pine forest and warm tungsten window light. A frame-within-a-frame view through a doorway, window or foreground structure. Rainy blue-hour light reflected from wood, stone or pavement. The mood is solitary and contemplative, with no commercial beauty performance. Unretouched documentary-style fine-art photography with believable hands, feet and weight distribution. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

---

## Exemple 7 - Prairie du mont Rainier

| ![Exemple 7](assets/w7.png) |
|:---:|

**Prompt original (anglais)**

> A clearly adult Croatian-American woman age 39 with dark blonde hair and a strong hourglass build, lying fully nude on her side with one knee slightly forward and her head supported by one hand in a Mount Rainier meadow with lupines, snowfields and moving summer cloud. A slightly elevated diagonal composition with calm geometric balance. Coastal haze producing subtle flare and low micro-contrast. The mood is candid and absorbed in the surrounding place. Cinematic environmental portraiture with realistic material textures and gentle lens softness. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

---

## Exemple 8 - Phare du Maine

| ![Exemple 8](assets/w8.png) |
|:---:|

**Prompt original (anglais)**

> A clearly adult woman age 39 of mixed Northern European heritage with pale skin and a powerful athletic build, sitting fully nude on a low bench with one knee raised and shoulders relaxed on a granite shoreline in Maine beneath a working lighthouse and fast Atlantic clouds. A full-body eye-level environmental frame with generous space around the figure. Clean overcast daylight with soft modeling and honest skin texture. The mood is slightly melancholic without becoming theatrical. Museum-minded black-and-white figure photography with a full tonal range. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

## À propos des 2 000 prompts de test

Le fichier [`western_european_american_diversity_2000.txt`](western_european_american_diversity_2000.txt) contient **2 000** prompts réservés aux adultes, couvrant les âges de 29 à 40 ans, différentes morphologies, plusieurs branches d'apparence ouest-européenne et américaine, ainsi que New York, les côtes de Nouvelle-Angleterre, les forêts du Nord-Ouest Pacifique, le Sud-Ouest américain, les fermes, les granges, les motels et les paysages ruraux.

Il est conçu pour des tests systématiques plutôt que pour une seule seed héroïque. Il coûte aussi moins cher que de visiter personnellement 2 000 lieux, même s'il n'offre malheureusement ni miles aériens ni café de motel fiable.

## Code de référence - Qwen Image 2512 T2I

Les fichiers [`reference.py`](reference.py) et [`reference_low_vram.py`](reference_low_vram.py) chargent Qwen Image 2512 en BF16, fusionnent l'adaptateur Lightning communautaire et appliquent ce LoRA sans déclencheur. La version standard convient aux GPU CUDA disposant d'une VRAM généreuse ; la version faible VRAM active l'offload CPU séquentiel ainsi que le tiling et le slicing du VAE.

## Installation

```bash
pip install -U diffusers transformers accelerate peft safetensors
```

## Exigences d'utilisation responsable

- Réservé aux adultes. N'utilisez pas ce modèle pour représenter des mineurs ou des personnes paraissant mineures.
- Ne créez pas d'images intimes non consenties, de deepfakes sexuels, de harcèlement, d'exploitation ou d'abus.
- Ne représentez pas une personne réelle identifiable dans un contexte sexuel ou intime sans son consentement explicite.
- Respectez les lois applicables, les règles des plateformes et les droits des personnes représentées dans les sources ou les générations.
- Les résultats peuvent rester incorrects ou trompeurs. Ne les utilisez pas comme preuves médicales, pédagogiques ou médico-légales.

## Licence

Cette version utilise la [licence de recherche non commerciale personnalisée](LICENSE) du dépôt. Les usages personnels, pédagogiques, artistiques et de recherche non commerciale sont autorisés sous réserve de ses conditions. Toute utilisation commerciale nécessite une autorisation écrite distincte.

## Contact

Pour toute question, rapport technique, demande d'attribution ou licence commerciale, contactez le propriétaire du dépôt via Hugging Face.

---

*Il s'agit d'un LoRA expérimental consacré aux femmes adultes d'Europe occidentale et des États-Unis pour Qwen Image 2512. Évaluez-le avec plusieurs seeds, poids, âges, morphologies, régions et styles photographiques avant de tirer des conclusions.*

</details>

<details name="language-version">
<summary><strong>🌎 Español - mostrar la versión completa</strong></summary>

---------

# LoRA NSFW de mujeres de Europa Occidental y Estados Unidos para Qwen Image v1

### De la piedra atlántica a la luz del Pacífico: identidad occidental sin fingir que repara la anatomía.

> **Advertencia de contenido para adultos:** este repositorio contiene imágenes explícitas generadas por IA y está destinado exclusivamente a personas adultas. Todas las personas mostradas o descritas en los ejemplos y prompts de referencia son claramente adultas.

![Portada](assets/c0.png)

## Una distinción importante antes de empezar

**Este no es un LoRA de reparación anatómica.** Fue entrenado para representar una amplia gama visual de mujeres adultas de Europa Occidental y Estados Unidos: rostros, cuerpos, edades, presencia, carácter fotográfico y los lugares que las rodean. No promete corregir por sí solo la anatomía íntima en posturas difíciles. Un modelo puede comprender un faro de Nueva Inglaterra y seguir filosóficamente indeciso ante la pelvis humana.

Si la corrección anatómica es prioritaria, combínelo con cuidado con una de mis versiones especializadas, especialmente [**Female Anatomy Fix NSFW LoRA - Triggerless v2**](https://huggingface.co/perpetual3x/Qwen-Image-Female-Anatomy-Fix-NSFW-LoRA-Triggerless-v2) o su compañero más explícito [**Triggered v2**](https://huggingface.co/perpetual3x/Qwen-Image-Female-Anatomy-Fix-NSFW-LoRA-Triggered-v2). El LoRA anatómico puede ocuparse de la estructura mientras este modelo atiende a la persona, la atmósfera y el contexto cultural. Empiece con pesos moderados: dos especialistas gritando al máximo rara vez mejoran una reunión.

**Qwen Image Western European American Female NSFW LoRA v1** es un LoRA fotorrealista experimental para **Qwen/Qwen-Image-2512 Text-to-Image**. Se centra en mujeres claramente adultas de Europa Occidental y Estados Unidos en entornos urbanos, rurales, costeros, montañosos, domésticos y artísticos. El conjunto incluye distintas edades adultas, constituciones, rasgos faciales y contextos regionales, en lugar de una sola cara pulida que cambia constantemente de domicilio.

El título describe el conjunto de datos y su rango de referencia visual; no afirma que Europa o Estados Unidos tengan una apariencia canónica. Los continentes no son agencias de casting y los pasaportes no incluyen un preajuste obligatorio de pómulos.

## Características

- Entrenado con **8.417** imágenes de personas adultas
- Amplia representación visual de mujeres adultas de Europa Occidental y Estados Unidos
- Diversidad de edades adultas, físicos, rasgos faciales y textura natural de la piel
- Lofts urbanos, interiores históricos, granjas, costas, bosques, montañas, desiertos y moteles de carretera
- Carácter fotográfico artístico, documental, ambiental, de negativo en color y monocromo
- Control mediante lenguaje natural sin palabra de activación obligatoria
- **2.000** prompts reutilizables para probar diversidad y contextos regionales
- Diseñado y probado para Qwen-Image-2512 T2I

## Lo que este modelo es y lo que no es

Esta versión trata sobre **variedad de identidades, atmósfera, lugares y presencia humana adulta**. Busca que las generaciones se parezcan menos a fotografía genérica de belleza sintética y estén más conectadas con personas creíbles y entornos reconocibles de Europa Occidental o Estados Unidos.

No se presenta como especialista en anatomía. Las vistas frontales, posteriores, sentadas, reclinadas, muy ocluidas o físicamente difíciles todavía pueden producir anatomía íntima, manos, pies o articulaciones incorrectas. Cuando esos detalles importen, utilice un LoRA anatómico, un prompt apropiado u otra seed.

### La contraparte, no el reemplazo

Este proyecto contrasta deliberadamente con [**Eastern European Female Anatomy NSFW LoRA v1**](https://huggingface.co/perpetual3x/Eastern-European-Female-Anatomy-NSFW-LoRA-v1):

| | Esta versión | Eastern European Anatomy v1 |
|:--|:--|:--|
| Objetivo principal | Identidad, constituciones, escenarios y carácter fotográfico de Europa Occidental/Estados Unidos | Precisión y diversidad de anatomía femenina adulta |
| Alcance geográfico | Europa Occidental y Estados Unidos | Conjunto fotográfico de Europa Oriental |
| Especialización anatómica | No | Sí |
| Palabra de activación | Ninguna | `zl_nubiles_v1` |
| Mejor uso | Base de personaje y contexto visual | Generación y corrección orientadas a la anatomía |

Responden a preguntas diferentes. Uno pregunta: «¿Quién es esta persona y qué mundo habita?» El otro pregunta: «¿Todas las estructuras visibles llegaron a la misma reunión?» Dependiendo de la imagen, conviene hacer ambas preguntas.

## Una breve nota del humano que realiza las pruebas

Durante las últimas semanas he revisado más fotografías de cuerpos femeninos y masculinos que un departamento de radiología ligeramente confundido. Ahora tengo mareos ocasionales. El diagnóstico provisional es **sobreajuste del operador a las cuadrículas comparativas**.

Cuando termine el proyecto de anatomía coreana, pienso tomarme un verdadero descanso, mirar árboles sin calcular su peso LoRA y confirmar que las nubes todavía existen sin ocho pasos de inferencia. Si empiezo a ver números de seed sobre los peatones, las vacaciones ya habrán llegado tarde.

## Información de entrenamiento

| Elemento | Valor |
|:---|---:|
| Modelo base | Qwen Image 2512 |
| Imágenes de entrenamiento | 8.417 |
| GPU | NVIDIA RTX PRO 6000 Blackwell / 96 GB |
| Rank | 64 |
| Tamaño de batch | 8 |
| Pasos de entrenamiento | 10.000 |
| Activador | Ninguno - solo lenguaje natural |

## Ajustes recomendados

- **Pipeline recomendado:** Qwen Image 2512 T2I
- **Peso sugerido:** empiece entre `0.8-1.2` y ajuste según el prompt y los demás LoRA
- **Combinación de LoRA:** empiece alrededor de `0.8-1.0` para este modelo y utilice un peso moderado para el especialista anatómico
- **Prompting:** describa en lenguaje natural la edad adulta, apariencia, constitución, lugar, ambiente, postura, luz y tratamiento fotográfico
- **Activador:** no se requiere ninguna palabra fija

Los pesos altos pueden reforzar la identidad y las tendencias fotográficas aprendidas, pero también repetir rasgos faciales, alisar la piel o imponer composiciones familiares.

## Compatibilidad

Este LoRA está pensado para **Qwen/Qwen-Image-2512** en generación Text-to-Image. No se garantiza la compatibilidad con Qwen-Image-Edit ni con arquitecturas no relacionadas.

## Limitaciones conocidas

- no ofrece una garantía específica de anatomía íntima correcta
- manos, dedos, pies, extremidades, articulaciones o posturas difíciles pueden ser incorrectos
- rasgos faciales repetidos o estereotipos regionales con pesos excesivos
- piel demasiado suavizada, sesgo de glamour o estilo fotográfico más fuerte de lo solicitado
- edad o constitución inconsistentes entre seeds
- conflictos con adaptadores de personaje, estilo o anatomía muy dominantes
- errores geométricos en arquitectura, barandillas, ventanas e interiores
- señales regionales débiles cuando el prompt no aporta información ambiental

Este modelo debe entenderse como una tendencia visual amplia, no como un censo, una definición etnográfica ni una máquina para expedir certificados de nacionalidad. Pruebe varias seeds y reduzca el peso si una tendencia aprendida empieza a hablar en nombre de un continente entero.

## Ejemplos

La portada se muestra deliberadamente sin prompt. Los ocho ejemplos siguientes conservan sus prompts completos en inglés. Todas las personas representadas son adultas.

## Ejemplo 1 - Ruinas de piedra

| ![Ejemplo 1](assets/w1.png) |
|:---:|

**Prompt original (inglés)**

> A museum-minded portrait observes an adult nude woman in a composed but spontaneous-looking portrait pausing beside rough stone ruins while listening to the wind beside pale stone outcrops overlooking a distant patchwork of fields. Her hair is gathered away from her face, leaving the gesture clearly readable. A distant medium-format composition lets weather and place occupy most of the frame. Open shade beneath the trees provides even illumination while the distance remains luminous. The photograph has the tonal restraint of medium-format film, subtle grain and carefully held highlights. The scene feels candid, meditative and grounded in ordinary physical reality. Avoid plastic skin, exaggerated symmetry or fashion retouching; retain natural variation and small imperfections.

---

## Ejemplo 2 - Biblioteca antigua

| ![Ejemplo 2](assets/w2.png) |
|:---:|

**Prompt original (inglés)**

> This poetic environmental portrait features an adult nude woman treated as a classical figure study sitting sideways on a weathered wooden bench with one knee raised and both shoulders relaxed within an old library hall with empty shelves and diffuse window light. Her hair remains natural and minimally styled. A gently compressed telephoto view layers the figure, architecture and distant space. Late-day window light meets soft reflection from the timber floor. The photograph has the tonal restraint of medium-format film, subtle grain and carefully held highlights. The environment and figure share equal visual importance, producing a calm sense of scale. Keep the gesture physically achievable and the relationship between body, gravity and support convincing.

---

## Ejemplo 3 - Granero del Medio Oeste

| ![Ejemplo 3](assets/w3.png) |
|:---:|

**Prompt original (inglés)**

> A clearly adult Italian-American woman age 30 with olive-toned skin, dark wavy hair and a soft curvy build, standing fully nude in profile while wind moves her hair and the surrounding vegetation in a weathered Midwestern barn with hay dust, timber rafters and open fields beyond. A low but restrained viewpoint that preserves realistic proportions. Crisp winter sunlight with cool ambient fill. The mood is calm, mature and emotionally present. Cinematic environmental portraiture with realistic material textures and gentle lens softness. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

---

## Ejemplo 4 - Patio de adobe de Nuevo México

| ![Ejemplo 4](assets/w4.png) |
|:---:|

**Prompt original (inglés)**

> A clearly adult French-American woman age 33 with chestnut hair, subtle freckles and an elegant average build, stretching fully nude after a walk with both arms raised in a physically believable gesture in a private New Mexico adobe courtyard with vigas, clay walls and desert sunlight. A medium-format three-quarter composition connecting face, body and place. Cool dawn light balanced by a small area of warm interior illumination. The mood is solitary and contemplative, with no commercial beauty performance. Restrained 35 mm color-negative realism with subtle grain and no beauty smoothing. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

---

## Ejemplo 5 - Loft del Lower East Side

| ![Ejemplo 5](assets/w5.png) |
|:---:|

**Prompt original (inglés)**

> A clearly adult Danish-American woman age 34 with sandy hair and a soft unretouched body, standing fully nude in a relaxed contrapposto with both arms resting naturally in a rain-darkened Lower East Side loft beside a metal fire escape and wet rooftop reflections. A full-body eye-level environmental frame with generous space around the figure. Crisp winter sunlight with cool ambient fill. The mood is playful in a restrained documentary manner. Cinematic environmental portraiture with realistic material textures and gentle lens softness. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

---

## Ejemplo 6 - Motel nevado

| ![Ejemplo 6](assets/w6.png) |
|:---:|

**Prompt original (inglés)**

> A clearly adult Welsh-American woman age 36 with short dark hair and a slender angular frame, kneeling fully nude on a folded blanket while looking quietly into the distance in a snowbound mountain motel with pine forest and warm tungsten window light. A frame-within-a-frame view through a doorway, window or foreground structure. Rainy blue-hour light reflected from wood, stone or pavement. The mood is solitary and contemplative, with no commercial beauty performance. Unretouched documentary-style fine-art photography with believable hands, feet and weight distribution. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

---

## Ejemplo 7 - Pradera del monte Rainier

| ![Ejemplo 7](assets/w7.png) |
|:---:|

**Prompt original (inglés)**

> A clearly adult Croatian-American woman age 39 with dark blonde hair and a strong hourglass build, lying fully nude on her side with one knee slightly forward and her head supported by one hand in a Mount Rainier meadow with lupines, snowfields and moving summer cloud. A slightly elevated diagonal composition with calm geometric balance. Coastal haze producing subtle flare and low micro-contrast. The mood is candid and absorbed in the surrounding place. Cinematic environmental portraiture with realistic material textures and gentle lens softness. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

---

## Ejemplo 8 - Faro de Maine

| ![Ejemplo 8](assets/w8.png) |
|:---:|

**Prompt original (inglés)**

> A clearly adult woman age 39 of mixed Northern European heritage with pale skin and a powerful athletic build, sitting fully nude on a low bench with one knee raised and shoulders relaxed on a granite shoreline in Maine beneath a working lighthouse and fast Atlantic clouds. A full-body eye-level environmental frame with generous space around the figure. Clean overcast daylight with soft modeling and honest skin texture. The mood is slightly melancholic without becoming theatrical. Museum-minded black-and-white figure photography with a full tonal range. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.

## Acerca de los 2.000 prompts de prueba

El archivo [`western_european_american_diversity_2000.txt`](western_european_american_diversity_2000.txt) contiene **2.000** prompts solo para adultos, con edades de 29 a 40 años, distintos físicos, ramas de apariencia de Europa Occidental y Estados Unidos, y escenarios como lofts de Nueva York, costas de Nueva Inglaterra, bosques del Noroeste del Pacífico, el Suroeste estadounidense, granjas, graneros, moteles y paisajes rurales.

Está diseñado para pruebas sistemáticas, no para una única seed heroica. También cuesta menos que visitar personalmente 2.000 lugares, aunque lamentablemente no ofrece millas de viajero frecuente ni café de motel fiable.

## Código de referencia - Qwen Image 2512 T2I

Los archivos [`reference.py`](reference.py) y [`reference_low_vram.py`](reference_low_vram.py) cargan Qwen Image 2512 en BF16, fusionan el adaptador comunitario Lightning y aplican este LoRA sin activador. La versión estándar está indicada para GPU CUDA con VRAM abundante; la versión de poca VRAM activa descarga secuencial a CPU, tiling y slicing del VAE.

## Instalación

```bash
pip install -U diffusers transformers accelerate peft safetensors
```

## Requisitos de uso responsable

- Solo para adultos. No utilice este modelo para representar menores ni personas que parezcan menores.
- No cree imágenes íntimas sin consentimiento, deepfakes sexuales, acoso, explotación ni abuso.
- No represente a una persona real identificable en contenido sexual o íntimo sin su consentimiento explícito.
- Respete la legislación aplicable, las reglas de las plataformas y los derechos de las personas representadas en material de origen o generado.
- Los resultados pueden seguir siendo incorrectos o engañosos. No los utilice como evidencia médica, educativa ni forense.

## Licencia

Esta versión utiliza la [licencia personalizada de investigación no comercial](LICENSE) del repositorio. Se permiten usos personales, educativos, artísticos y de investigación no comercial sujetos a sus condiciones. El uso comercial requiere autorización escrita por separado.

## Contacto

Para preguntas, informes técnicos, cuestiones de atribución o licencias comerciales, contacte con el propietario del repositorio a través de Hugging Face.

---

*Este es un LoRA experimental dedicado a mujeres adultas de Europa Occidental y Estados Unidos para Qwen Image 2512. Evalúelo con varias seeds, pesos, edades, constituciones, regiones y estilos fotográficos antes de extraer conclusiones.*

</details>

-----------

---

# Qwen Image Western European American Female NSFW LoRA v1

## From Atlantic stone to Pacific light—Western character without anatomical overreach.

First, an important distinction: **this is not an anatomy-repair LoRA**. It was
trained to model a broad Western European and American adult-female visual
range—faces, bodies, age, presence, photographic character, and the places
around them. It does not claim to make difficult intimate anatomy correct by
itself. A model can understand a New England lighthouse and still become
philosophically uncertain about the human pelvis.

If anatomical correction is the priority, combine it carefully with one of my
existing anatomy-focused releases, especially
[**Female Anatomy Fix NSFW LoRA — Triggerless v2**](https://huggingface.co/perpetual3x/Qwen-Image-Female-Anatomy-Fix-NSFW-LoRA-Triggerless-v2)
or its more explicit
[**Triggered v2 companion**](https://huggingface.co/perpetual3x/Qwen-Image-Female-Anatomy-Fix-NSFW-LoRA-Triggered-v2).
The anatomy LoRA can look after structural detail while this model looks after
the person, atmosphere, and cultural setting. Start with moderate weights when
stacking; two specialists shouting at full volume rarely improve a meeting.

![Cover](assets/c0.png)

**Qwen Image Western European American Female NSFW LoRA v1** is an
experimental photorealistic LoRA for **Qwen/Qwen-Image-2512 Text-to-Image**.
It focuses on clearly adult Western European and American women across urban,
rural, coastal, mountain, domestic, and fine-art environments. The dataset
includes varied adult ages, body types, facial characteristics, and regional
visual contexts rather than one polished face endlessly changing addresses.

The title describes the dataset and its visual reference range, not a claim
that Europe or America has one canonical appearance. Continents are not casting
agencies, and passports do not come with a mandatory cheekbone preset.

> **Adult-content notice:** This repository contains explicit adult material
> and is intended only for adults. All subjects represented by the training
> objective and all people described in the examples are adults.

---

# ✨ Features

- Trained on **8,417** adult images
- Broad Western European and American adult-female visual representation
- Varied adult ages, physiques, facial characteristics, and natural skin detail
- Urban lofts, historic interiors, farms, coastlines, forests, mountains, deserts, and roadside settings
- Fine-art, documentary, environmental, color-negative, and monochrome photographic character
- Natural-language prompting with no required trigger word
- Includes **2,000** reusable diversity and regional-context testing prompts
- Designed and tested for Qwen-Image-2512 T2I

---

# 🎯 What This Model Is—and Is Not

This release is about **identity range, atmosphere, place, and adult human
presence**. It is meant to help generations feel less like generic synthetic
beauty photography and more connected to believable people and recognizable
Western European or American environments.

It is deliberately not presented as an anatomy specialist. Difficult frontal,
rear, seated, reclining, or heavily occluded poses can still produce incorrect
intimate anatomy, hands, feet, or joints. When those details matter, use an
anatomy-assist LoRA, an appropriate prompt, or another seed.

## The Counterpart, Not the Replacement

This project forms a deliberate contrast with
[**Eastern European Female Anatomy NSFW LoRA v1**](https://huggingface.co/perpetual3x/Eastern-European-Female-Anatomy-NSFW-LoRA-v1):

| | This release | Eastern European Anatomy v1 |
|:--|:--|:--|
| Primary goal | Western European/American identity, body range, setting, and photographic character | Adult female anatomy accuracy and diversity |
| Geographic scope | Western Europe and the United States | Eastern European photographic dataset |
| Anatomy specialization | No | Yes |
| Trigger word | None required | `zl_nubiles_v1` |
| Best use | Character and visual-context foundation | Anatomy-oriented generation and correction |

They answer different questions. One asks, “Who is this person, and what world
does she inhabit?” The other asks, “Did every visible structure arrive at the
same meeting?” Depending on the image, both questions may be worth asking.

---

# 🌀 A Brief Note From the Human Running the Tests

During recent testing I have reviewed more photographs of female and male
bodies than a mildly confused radiology department. I now experience occasional
dizziness. The current diagnosis is **operator overfitting to comparison
grids**.

After the Korean anatomy project is finished, I plan to take a proper break,
look at trees without estimating their LoRA weight, and confirm that clouds
still exist without eight inference steps. If I begin seeing seed numbers above
pedestrians, the holiday will already be overdue.

---

# 🖥️ Training Details

## Hardware

- GPU: **NVIDIA RTX PRO 6000 Blackwell 96GB**

## Dataset and Network

- Base model: **Qwen/Qwen-Image-2512**
- Training images: **8,417**
- Dataset type: **Western European and American adult female photography**
- LoRA rank: **64**
- Batch size: **8**
- Training steps: **10,000**

## Trigger Words and Weight

No fixed trigger word is required. Describe the adult subject, regional
background, age, body type, mood, pose, light, and photographic treatment in
natural language.

Recommended starting range:

```text
0.8–1.2
```

Start around `0.8–1.0` when stacking with another LoRA. Higher values can make
the learned identity and photographic tendencies more assertive, but may also
increase repeated facial traits, oversmoothed skin, or composition bias.

---

# ⚠️ Base Model Compatibility

This LoRA is intended for:

- **Qwen/Qwen-Image-2512** for Text-to-Image generation

Compatibility with Qwen-Image-Edit or unrelated model architectures is not
guaranteed. A different base checkpoint may produce weak effects, artifacts,
incorrect colors, or a loading error.

---

# 🔍 Scope and Limitations

Possible limitations include:

- no dedicated guarantee of correct intimate anatomy
- incorrect hands, fingers, feet, limbs, joints, or physically difficult poses
- repeated facial traits or learned regional stereotypes at excessive weight
- oversmoothed skin, glamour bias, or stronger-than-requested photographic styling
- inconsistent age or body characteristics between seeds
- conflicts between this LoRA and strongly opinionated character, style, or anatomy adapters
- background geometry errors in architecture, railings, windows, and interiors
- weak regional cues when the prompt provides no environmental information

The model should be treated as a broad visual tendency, not a census, an
ethnographic definition, or a machine for issuing nationality certificates.
Review generated output, test several seeds, and reduce the weight if one
learned tendency begins speaking for an entire continent.

---

# 🖼️ Examples

The cover image is intentionally shown without a prompt. The eight samples
below include their complete prompts. All depicted people are adults.

---

## Example 1

![Example 1](assets/w1.png)

**Prompt**

```text
A museum-minded portrait observes an adult nude woman in a composed but spontaneous-looking portrait pausing beside rough stone ruins while listening to the wind beside pale stone outcrops overlooking a distant patchwork of fields. Her hair is gathered away from her face, leaving the gesture clearly readable. A distant medium-format composition lets weather and place occupy most of the frame. Open shade beneath the trees provides even illumination while the distance remains luminous. The photograph has the tonal restraint of medium-format film, subtle grain and carefully held highlights. The scene feels candid, meditative and grounded in ordinary physical reality. Avoid plastic skin, exaggerated symmetry or fashion retouching; retain natural variation and small imperfections.
```

---

## Example 2

![Example 2](assets/w2.png)

**Prompt**

```text
This poetic environmental portrait features an adult nude woman treated as a classical figure study sitting sideways on a weathered wooden bench with one knee raised and both shoulders relaxed within an old library hall with empty shelves and diffuse window light. Her hair remains natural and minimally styled. A gently compressed telephoto view layers the figure, architecture and distant space. Late-day window light meets soft reflection from the timber floor. The photograph has the tonal restraint of medium-format film, subtle grain and carefully held highlights. The environment and figure share equal visual importance, producing a calm sense of scale. Keep the gesture physically achievable and the relationship between body, gravity and support convincing.
```

---

## Example 3

![Example 3](assets/w3.png)

**Prompt**

```text
A clearly adult Italian-American woman age 30 with olive-toned skin, dark wavy hair and a soft curvy build, standing fully nude in profile while wind moves her hair and the surrounding vegetation in a weathered Midwestern barn with hay dust, timber rafters and open fields beyond. A low but restrained viewpoint that preserves realistic proportions. Crisp winter sunlight with cool ambient fill. The mood is calm, mature and emotionally present. Cinematic environmental portraiture with realistic material textures and gentle lens softness. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.
```

---

## Example 4

![Example 4](assets/w4.png)

**Prompt**

```text
A clearly adult French-American woman age 33 with chestnut hair, subtle freckles and an elegant average build, stretching fully nude after a walk with both arms raised in a physically believable gesture in a private New Mexico adobe courtyard with vigas, clay walls and desert sunlight. A medium-format three-quarter composition connecting face, body and place. Cool dawn light balanced by a small area of warm interior illumination. The mood is solitary and contemplative, with no commercial beauty performance. Restrained 35 mm color-negative realism with subtle grain and no beauty smoothing. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.
```

---

## Example 5

![Example 5](assets/w5.png)

**Prompt**

```text
A clearly adult Danish-American woman age 34 with sandy hair and a soft unretouched body, standing fully nude in a relaxed contrapposto with both arms resting naturally in a rain-darkened Lower East Side loft beside a metal fire escape and wet rooftop reflections. A full-body eye-level environmental frame with generous space around the figure. Crisp winter sunlight with cool ambient fill. The mood is playful in a restrained documentary manner. Cinematic environmental portraiture with realistic material textures and gentle lens softness. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.
```

---

## Example 6

![Example 6](assets/w6.png)

**Prompt**

```text
A clearly adult Welsh-American woman age 36 with short dark hair and a slender angular frame, kneeling fully nude on a folded blanket while looking quietly into the distance in a snowbound mountain motel with pine forest and warm tungsten window light. A frame-within-a-frame view through a doorway, window or foreground structure. Rainy blue-hour light reflected from wood, stone or pavement. The mood is solitary and contemplative, with no commercial beauty performance. Unretouched documentary-style fine-art photography with believable hands, feet and weight distribution. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.
```

---

## Example 7

![Example 7](assets/w7.png)

**Prompt**

```text
A clearly adult Croatian-American woman age 39 with dark blonde hair and a strong hourglass build, lying fully nude on her side with one knee slightly forward and her head supported by one hand in a Mount Rainier meadow with lupines, snowfields and moving summer cloud. A slightly elevated diagonal composition with calm geometric balance. Coastal haze producing subtle flare and low micro-contrast. The mood is candid and absorbed in the surrounding place. Cinematic environmental portraiture with realistic material textures and gentle lens softness. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.
```

---

## Example 8

![Example 8](assets/w8.png)

**Prompt**

```text
A clearly adult woman age 39 of mixed Northern European heritage with pale skin and a powerful athletic build, sitting fully nude on a low bench with one knee raised and shoulders relaxed on a granite shoreline in Maine beneath a working lighthouse and fast Atlantic clouds. A full-body eye-level environmental frame with generous space around the figure. Clean overcast daylight with soft modeling and honest skin texture. The mood is slightly melancholic without becoming theatrical. Museum-minded black-and-white figure photography with a full tonal range. Preserve a single coherent clearly adult body, realistic joints, natural breasts, hands and feet, authentic age and body variation; no clothing, no additional people, no text, no logo, no watermark.
```

---

# 🗺️ About the 2,000 Testing Prompts

This repository includes
[`western_european_american_diversity_2000.txt`](western_european_american_diversity_2000.txt),
containing **2,000** adult-only prompts covering ages 29–40, varied physiques,
Western European and American appearance branches, and settings including New
York lofts, New England coasts, Pacific Northwest forests, the American
Southwest, farms, barns, motels, and rural landscapes.

The file is designed for systematic testing rather than one heroic seed. It is
also cheaper than personally visiting 2,000 locations, although regrettably it
provides neither frequent-flyer miles nor reliable motel coffee.

---

# 🚀 Reference Code — Qwen-Image-2512 T2I

The downloadable [`reference.py`](reference.py) loads Qwen-Image-2512 in BF16,
fuses the official community Lightning 4-step adapter, and applies this LoRA.
A high-memory CUDA GPU is recommended.

For consumer GPUs, use
[`reference_low_vram.py`](reference_low_vram.py). It enables sequential CPU
offloading plus tiled and sliced VAE decoding. This saves substantially more
VRAM at the cost of slower generation and higher system-RAM usage.

## Installation

```bash
pip install -U diffusers transformers accelerate peft safetensors
```

## Python

```python
import math

import torch
from diffusers import DiffusionPipeline, FlowMatchEulerDiscreteScheduler


BASE_MODEL_ID = "Qwen/Qwen-Image-2512"
LIGHTNING_MODEL_ID = "lightx2v/Qwen-Image-2512-Lightning"
LIGHTNING_WEIGHT_NAME = (
    "Qwen-Image-2512-Lightning-4steps-V1.0-bf16.safetensors"
)
LORA_MODEL_ID = (
    "perpetual3x/Qwen-Image-Western-European-American-Female-NSFW-LoRA-v1"
)
LORA_WEIGHT_NAME = "Western-European-American-Female.safetensors"

scheduler_config = {
    "base_image_seq_len": 256,
    "base_shift": math.log(3),
    "invert_sigmas": False,
    "max_image_seq_len": 8192,
    "max_shift": math.log(3),
    "num_train_timesteps": 1000,
    "shift": 1.0,
    "shift_terminal": None,
    "stochastic_sampling": False,
    "time_shift_type": "exponential",
    "use_beta_sigmas": False,
    "use_dynamic_shifting": True,
    "use_exponential_sigmas": False,
    "use_karras_sigmas": False,
}

scheduler = FlowMatchEulerDiscreteScheduler.from_config(scheduler_config)
pipe = DiffusionPipeline.from_pretrained(
    BASE_MODEL_ID,
    scheduler=scheduler,
    torch_dtype=torch.bfloat16,
).to("cuda")

pipe.load_lora_weights(
    LIGHTNING_MODEL_ID,
    weight_name=LIGHTNING_WEIGHT_NAME,
    adapter_name="lightning",
)
pipe.fuse_lora(adapter_names=["lightning"], lora_scale=1.0)
pipe.unload_lora_weights()

pipe.load_lora_weights(
    LORA_MODEL_ID,
    weight_name=LORA_WEIGHT_NAME,
    adapter_name="western_female_v1",
)
pipe.set_adapters(["western_female_v1"], adapter_weights=[1.0])

# Natural language only. No trigger word is required.
prompt = (
    "A realistic environmental portrait of a clearly adult Western European "
    "American woman, natural unretouched appearance, mature presence, "
    "believable body variation, Atlantic coastal landscape, fine-art photography"
)
negative_prompt = (
    "child, minor, underage, youthful-looking, low quality, blurry, "
    "distorted anatomy, malformed hands, extra limbs, plastic skin, "
    "watermark, logo, text"
)

image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    width=928,
    height=1328,
    num_inference_steps=8,
    true_cfg_scale=1.0,
    generator=torch.Generator(device="cuda").manual_seed(42),
).images[0]

image.save("western_european_american_female_v1.png")
```

---

# 🔞 Responsible Use

This model is intended exclusively for lawful, consensual, adult creative
work. Do not use it to:

- create or sexualize minors or youthful-looking persons
- create non-consensual or exploitative sexual content
- depict an identifiable real person without permission
- harass, threaten, exploit, or defame another person
- create illegal content or bypass platform rules

Users are responsible for ensuring that their prompts, source material, and
generated content comply with applicable laws and platform policies.

---

# License & Copyright Notice

This LoRA may be used for personal and non-commercial purposes only. See the
repository [LICENSE](LICENSE) file for the complete terms.

For commercial licensing inquiries, please contact the author.
