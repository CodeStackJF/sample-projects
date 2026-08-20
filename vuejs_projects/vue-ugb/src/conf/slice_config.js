import { createSlice } from "@reduxjs/toolkit";

export const userSlice = createSlice({
    name: 'user',
    initialState: {
        user: {
            isAuthenticated: false
        }
    },
    reducers: {
        login: (state, action) => {
            state.user = action.payload;
        },
        logout: (state) => {
            state.user = {
                isAuthenticated: false
            };
            localStorage.removeItem('persist:root');
            localStorage.removeItem('token');
        }
    }
});

export const {login, logout} = userSlice.actions;
export const selectUser = (state) => state.user; 
export default userSlice.reducer;