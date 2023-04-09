const characters = [
    document.getElementById('character1'),
    document.getElementById('character2'),
    document.getElementById('character3'),
    document.getElementById('character4'),
    document.getElementById('character5')
  ];
  
  function animateCharacter(character) {
    const x = Math.random() * (window.innerWidth - character.clientWidth);
    const y = Math.random() * (window.innerHeight - character.clientHeight);
    const duration = Math.random() * 3000 + 3000;
  
    character.animate([
      { transform: `translate(${x}px, ${y}px)` },
    ], {
      duration: duration,
      easing: 'linear',
      fill: 'forwards',
    });
  
    setTimeout(() => {
      animateCharacter(character);
    }, duration);
  }
  
  characters.forEach(character => animateCharacter(character));
  