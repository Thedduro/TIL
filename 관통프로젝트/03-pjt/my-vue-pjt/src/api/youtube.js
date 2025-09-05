import axios from 'axios'

export async function searchYoutube(q, max = 10) {
	const { data } = await axios.get('https://www.googleapis.com/youtube/v3/search', {
		params: {
			key: import.meta.env.VITE_YOUTUBE_API_KEY,
			part: 'snippet',
			q,
			maxResults: max,
			type: 'video',
			videoEmbeddable: 'true',
		},
	})
	return data
}
