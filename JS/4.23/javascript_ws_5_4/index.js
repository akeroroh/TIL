/* 
  아래에 코드를 작성해주세요.
*/
const searchBtn = document.querySelector('.search-box__button')
const URL = 'http://ws.audioscrobbler.com/2.0/'
const resultTag = document.querySelector('.search-result')

const fetchAlbums = function(keyword) {
  axios({
    method: 'get',
    url: URL,
    params: {
      format: 'json',
      method: 'album.search',
      api_key: '0277611e3e5f6cf53c76ad0904a971c7',
      album: keyword,
      page: 1,
      limit: 10,
    }
  })
    .then((response) => {
      const albums = response.data.results.albummatches.album
      console.log(albums)
      for (i=0; i<albums.length; i++) {
        const divcardTag = document.createElement('div')
        const imgTag = document.createElement('img')
        const divtextTag = document.createElement('div')
        const h2Tag = document.createElement('h2')
        const pTag = document.createElement('p')
        const aTag = document.createElement('a')

        divcardTag.classList.add('search-result__card')
        divtextTag.classList.add('search-result__text')
        
        aTag.setAttribute('href', albums[i].url)
        imgTag.setAttribute('src', albums[i].image[1]['#text'])
        h2Tag.textContent = albums[i].artist
        pTag.textContent = albums[i].name

        aTag.appendChild(divcardTag)
        divcardTag.appendChild(imgTag)
        divcardTag.appendChild(divtextTag)
        divtextTag.appendChild(h2Tag)
        divtextTag.appendChild(pTag)
        resultTag.appendChild(aTag)
      }
    })
    .catch((error) => {
      alert('잠시 후 다시 시도해주세요')
    })
  
}

searchBtn.addEventListener('click', function(event) {
  event.preventDefault()
  const keyword = document.querySelector('.search-box__input').value
  fetchAlbums(keyword)
})
