import axios from 'axios'

// TMDB v3 API KEY 방식 (권장)
const tmdb = axios.create({
	baseURL: 'https://api.themoviedb.org/3',
	params: {
		api_key: import.meta.env.VITE_TMDB_API_KEY,
	},
})

// v4 인증 방식 (참고)
// headers: { Authorization: `Bearer ${import.meta.env.VITE_TMDB_V4_TOKEN}` }

export function getTopRated(page = 1) {
	return tmdb.get('/movie/top_rated', { params: { page } })
}

export function getMovieDetail(id) {
	return tmdb.get(`/movie/${id}`)
}

export function getImageUrl(path, size = 'w500') {
	return `https://image.tmdb.org/t/p/${size}${path}`
}
