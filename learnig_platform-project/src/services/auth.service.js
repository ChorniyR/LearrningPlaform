import axios from "axios";

export const login = async (username, password) => {
  const { data } = await axios.post("/auth/jwt/create/", {
    username: username,
    password: password,
  });
  console.log(data.access);
  localStorage.setItem("access-token", data.access);
  localStorage.setItem("refresh-token", data.refresh);
};

export const refreshToken = async () => {
  const { data } = await axios.post("/auth/jwt/refresh/", {
    refresh: localStorage.getItem("refresh-token"),
  });
  localStorage.setItem("access-token", data.access);
  console.log("refresh");
};

export const logout = async () => {
  localStorage.removeItem("access-token");
};
