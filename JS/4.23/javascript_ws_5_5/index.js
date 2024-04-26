const searchBtn = document.querySelector('.search-box__button');
const URL = 'http://ws.audioscrobbler.com/2.0/';
const resultTag = document.querySelector('.search-result');
const resultend = document.createElement('p')
resultend.classList.add('search-result-end')
const search = document.querySelector('.search')
search.appendChild(resultend)
const loading = document.querySelector('.search-result--loadingList')

let page = 1;

const fetchAlbums = async function (keyword) {
  loading.style.display = 'block'
  try {
    const response = await axios({
      method: 'get',
      url: URL,
      params: {
        format: 'json',
        method: 'album.search',
        api_key: '0277611e3e5f6cf53c76ad0904a971c7',
        album: keyword,
        page: page,
        limit: 10,
      },
    });

    const albums = response.data.results.albummatches.album;
    console.log(albums);

    for (let i = 0; i < albums.length; i++) {
      const divCardTag = document.createElement('div');
      const imgTag = document.createElement('img');
      const divTextTag = document.createElement('div');
      const h2Tag = document.createElement('h2');
      const pTag = document.createElement('p');
      const aTag = document.createElement('a');

      divCardTag.classList.add('search-result__card');
      divTextTag.classList.add('search-result__text');

      aTag.setAttribute('href', albums[i].url);
      imgTag.setAttribute('src', albums[i].image[1]['#text']);
      h2Tag.textContent = albums[i].artist;
      pTag.textContent = albums[i].name;

      aTag.appendChild(divCardTag);
      divCardTag.appendChild(imgTag);
      divCardTag.appendChild(divTextTag);
      divTextTag.appendChild(h2Tag);
      divTextTag.appendChild(pTag);
      resultTag.appendChild(aTag);
    }

    page++;
    loading.style.display = 'None'
  } catch (error) {
    alert('잠시 후 다시 시도해주세요');
  }
};


const io = new IntersectionObserver((entries, observer) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      fetchAlbums(keyword);
    }
  });
}, { threshold: 0.5 });

let keyword;

searchBtn.addEventListener('click', function (event) {
  event.preventDefault();
  keyword = document.querySelector('.search-box__input').value;
  page = 1;
  resultTag.innerHTML = '';
  fetchAlbums(keyword);
  io.observe(document.querySelector('.search-result-end'));
});