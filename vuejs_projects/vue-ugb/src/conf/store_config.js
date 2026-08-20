import { configureStore } from "@reduxjs/toolkit";
import  useReducer  from "./slice_config";
import storage from 'redux-persist/lib/storage'
import { persistStore, persistReducer } from 'redux-persist'

const persistConfig = {
    key: 'root',
    storage,
  }

const persistedReducer = persistReducer(persistConfig, useReducer)

const store = configureStore({
    reducer: {
        user: persistedReducer
    },
    middleware: getDefaultMiddleware =>
        getDefaultMiddleware({
            immutableCheck: false,
            serializableCheck: false,
    }),
});

const resetStore = async () => {
    await persistor.purge();
    await persistor.flush();
    localStorage.removeItem('persist:root');
}

const persistor =  persistStore(store)
export {store, persistor, resetStore}