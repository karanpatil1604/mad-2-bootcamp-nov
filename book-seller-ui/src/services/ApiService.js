import axios from 'axios'

class ApiService {
  constructor(baseURL) {
    this.client = axios.create({
      baseURL,
    })
  }

  async request(method, url, data = null, params = null) {
    try {
      const response = await this.client({
        method,
        url,
        data,
        params,
      })
      return response.data
    } catch (error) {
      return error.response
      // this.handleError(error)
    }
  }

  get(url, params = null) {
    return this.request('get', url, null, params)
  }

  post(url, data) {
    return this.request('post', url, data)
  }

  put(url, data) {
    return this.request('put', url, data)
  }

  delete(url) {
    return this.request('delete', url)
  }

  handleError(error) {
    if (error.response) {
      // Request made and server responded
      console.error('Error Response:', error.response.data)
      console.error('Error Status:', error.response.status)
      console.error('Error Headers:', error.response.headers)

      switch (error.response.status) {
        case 400:
          throw new Error('Bad Request')
        case 401:
          throw new Error('Unauthorized')
        case 403:
          throw new Error('Forbidden')
        case 404:
          throw new Error('Not Found')
        case 500:
          throw new Error('Internal Server Error')
        default:
          throw new Error('An unknown error occurred')
      }
    } else if (error.request) {
      // Request made but no response received
      console.error('Error Request:', error.request)
      throw new Error('No response from the server')
    } else {
      // Something happened in setting up the request
      console.error('Error Message:', error.message)
      throw new Error('Error in setting up request')
    }
  }
}

export default new ApiService('http://localhost:5000')
