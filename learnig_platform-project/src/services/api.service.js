import axios from "axios";
import { refreshToken } from "./auth.service";

export const axiosWithJWT = axios.create({
  headers: {
    Authorization: `Bearer ${localStorage.getItem("access-token")}`,
  },
});

export const error401Handler = async (error) => {
  if (error.response.status === 401) {
    refreshToken();
  }
};
