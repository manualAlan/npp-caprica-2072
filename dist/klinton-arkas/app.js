const menu=document.querySelector('.menu-toggle');
const nav=document.querySelector('#navigation');
function closeMenu(){menu.setAttribute('aria-expanded','false');nav.classList.remove('open')}
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open)});
nav.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu()});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){closeMenu();menu.focus()}});
function revealSpeech(){const section=document.getElementById(location.hash.slice(1));if(section?.tagName==='DETAILS'){section.open=true;section.scrollIntoView({block:'start'})}}
window.addEventListener('hashchange',revealSpeech);revealSpeech();
document.getElementById('share').addEventListener('click',async()=>{const status=document.getElementById('share-status');const url=location.origin+location.pathname;try{if(navigator.share){await navigator.share({title:'Klinton Arkas — 2068 campaign archive',text:'Explore the archive of Klinton’s 2068 campaign for Carnapol MP.',url});status.textContent='Thank you for sharing.'}else if(navigator.clipboard&&window.isSecureContext){await navigator.clipboard.writeText(url);status.textContent='Archive link copied. Ready to share.'}else{status.textContent='Copy this address to share: '+url}}catch(e){if(e.name!=='AbortError')status.textContent='Copy this address to share: '+url}});
