import axios from 'axios'

export const login = async(username, password) => {
        const res = await axios.post(
            '/auth/jwt/create/', {
                username: username,
                password: password
            }
        )
        .then(r => {
            console.log(r.data)
            localStorage.setItem('access-token', r.data.access)
            localStorage.setItem('refresh-token', r.data.refresh)
        }) 
    }


