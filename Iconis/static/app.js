function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

mic = document.getElementById('mic');
on = document.getElementById('on');
mic.addEventListener('click', async function () {
  mic.classList.add('disable');
  on.classList.remove('disable');
  on.classList.add('block');
  await sleep(8000);
  mic.classList.remove('disable');
  on.classList.add('disable');
  on.classList.remove('block');
});
