# Text-Based RPG Game

## Objective

Create an engaging text-based RPG game that offers a dynamic and immersive experience, allowing players to make impactful choices.

## Requirements

### General Requirements

1. **Multiple Locations:** Minimum of three significant locations with unique interactions and experiences.
2. **Scalable Design:** Flexible, organized, and modular code for easy future expansion.
3. **Choice:** path selection, and decision-making affecting the game's outcome.

<!-- #region drawnote -->
<svg id="svg" xmlns="http://www.w3.org/2000/svg" viewbox="31.86,89,360.5,341.2" style="height:341.2"><rect x="41.86" y="219" fill="none" stroke="#6190e8" stroke-width="2" width="94" height="83" d="M 41.86 219 h 94 v 83 h -94 Z"></rect><line x1="136.86" y1="260" x2="181.86" y2="260" fill="none" stroke="#6190e8" stroke-width="2" d="M 136.86 260 L 181.86 260"></line><line x1="180.86" y1="261" x2="180.86" y2="181" fill="none" stroke="#6190e8" stroke-width="2" d="M 180.86 261 L 180.86 181"></line><line x1="181.86" y1="261" x2="180.86" y2="341" fill="none" stroke="#6190e8" stroke-width="2" d="M 181.86 261 L 180.86 341"></line><rect x="139.86" y="99" fill="none" stroke="#6190e8" stroke-width="2" width="82" height="81" d="M 139.86 99 h 82 v 81 h -82 Z"></rect><rect x="139.86" y="339" fill="none" stroke="#6190e8" stroke-width="2" width="81" height="79" d="M 139.86 339 h 81 v 79 h -81 Z"></rect><text font-family="inherit" font-size="14" fill="#6190e8" x="60.86" y="245">START</text><text font-family="inherit" font-size="14" fill="#6190e8" x="151.86" y="114">ROOM 1</text><text font-family="inherit" font-size="14" fill="#6190e8" x="148.86" y="350">ROOM 2</text><rect x="182.86" y="347" fill="rgba(240, 240,240, 0.4)" stroke="#BBB" stroke-width="1"></rect><rect x="191.86" y="348" fill="rgba(240, 240,240, 0.4)" stroke="#BBB" stroke-width="1"></rect><rect x="191.86" y="348" fill="rgba(240, 240,240, 0.4)" stroke="#BBB" stroke-width="1"></rect><rect x="190.86" y="340" fill="rgba(240, 240,240, 0.4)" stroke="#BBB" stroke-width="1"></rect><rect x="190.86" y="340" fill="rgba(240, 240,240, 0.4)" stroke="#BBB" stroke-width="1"></rect><rect x="225.86" y="383" fill="rgba(240, 240,240, 0.4)" stroke="#BBB" stroke-width="1"></rect><rect x="179.86" y="344" fill="rgba(240, 240,240, 0.4)" stroke="#BBB" stroke-width="1"></rect><rect x="202.36" y="347.8" fill="rgba(240, 240,240, 0.4)" stroke="#BBB" stroke-width="1"></rect><rect x="185.36" y="145.8" fill="rgba(240, 240,240, 0.4)" stroke="#BBB" stroke-width="1"></rect><rect x="179.86" y="346" fill="rgba(240, 240,240, 0.4)" stroke="#BBB" stroke-width="1"></rect><line x1="220.36" y1="379.2" x2="298.36" y2="380.2" fill="none" stroke="#6190e8" stroke-width="2" d="M 220.36 379.2 L 298.36 380.2"></line><rect x="299.36" y="339.2" fill="none" stroke="#6190e8" stroke-width="2" width="83" height="81" d="M 299.36 339.2 h 83 v 81 h -83 Z"></rect><text font-family="inherit" font-size="14" fill="#6190e8" x="311.36" y="355.2">ROOM 3</text><line x1="342.36" y1="339.2" x2="341.36" y2="259.2" fill="none" stroke="#6190e8" stroke-width="2" d="M 342.36 339.2 L 341.36 259.2"></line><text font-family="inherit" font-size="14" fill="#6190e8" x="312.36" y="199.2">ROOM 4</text><text font-family="inherit" font-size="14" fill="#6190e8" x="320.36" y="220.2">END</text><line x1="212.36" y1="295.2" x2="232.36" y2="295.2" fill="none" stroke="#6190e8" stroke-width="2"></line><rect x="300.36" y="183.2" fill="none" stroke="#6190e8" stroke-width="2" width="80" height="77" d="M 300.36 183.2 h 80 v 77 h -80 Z"></rect><line x1="186.36" y1="294.2" x2="202.36" y2="293.2" fill="none" stroke="#6190e8" stroke-width="2" d="M 186.36 294.2 L 202.36 293.2"></line><text font-family="inherit" font-size="14" fill="#6190e8" x="246.36" y="298.2">?</text><rect x="239.36" y="279.2" fill="none" stroke="#6190e8" stroke-width="2" width="39" height="38" d="M 239.36 279.2 h 39 v 38 h -39 Z"></rect></svg>  
<!-- #endregion -->

### Functional Requirements

1. **Unique Interactions:** Each location should offer specific interactions like using objects, conversing with characters, or moving to different areas.
2. **Navigation:** Allow players to move between locations.
3. **Impactful Outcomes:** Interactions should influence the game's progress, such as acquiring items or altering the storyline.

## Gameplay Experience

1. **Engaging and Immersive:** A balance of challenges and rewards, promoting a sense of progression and achievement.
2. **Choice and Exploration:** Freedom for players to make choices and explore different outcomes for replayability.
3. **Surprises:** Incorporate unexpected outcomes for exciting gameplay.

<!-- #region drawnote -->
<svg id="svg" xmlns="http://www.w3.org/2000/svg" viewbox="110,70,240,160" style="height:160">  <text font-family="inherit" font-size="14" fill="#6190e8" x="140" y="100">START</text><text font-family="inherit" font-size="14" fill="#6190e8" x="131.86" y="124">- Options for travel to room 1 or 2</text><text font-family="inherit" font-size="14" fill="#6190e8" x="131.86" y="144">- Option to inspect the room</text><rect x="120" y="80" fill="none" stroke="#6190e8" stroke-width="2" width="240" height="140" d="M 120 80 h 220 v 140 h -220 Z"></rect><rect x="400" y="80" fill="none" stroke="#6190e8" stroke-width="2" width="240" height="140" d="M 120 80 h 220 v 140 h -220 Z"></rect><text font-family="inherit" font-size="14" fill="#6190e8" x="411.86" y="104">ROOM 1</text><text font-family="inherit" font-size="14" fill="#6190e8" x="411.86" y="124">- Possible enemy to fight</text><text font-family="inherit" font-size="14" fill="#6190e8" x="411.86" y="144">- Option to inspect the room</text><text font-family="inherit" font-size="14" fill="#6190e8" x="411.86" y="164">- Options to go to start or room 2</text></svg>  
<!-- #endregion -->

## Evaluation Criteria

1. **Functional Requirements Fulfillment:** Compliance with specified functional requirements.
2. **Gameplay Experience:** Engagement, immersion, fun, replayability, and balance in gameplay.
3. **Code Organization and Modularity:** Well-structured, organized, modular code.
4. **Creativity and Innovation:** Originality and unique gameplay features or mechanics.
