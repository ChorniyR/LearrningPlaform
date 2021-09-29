import { axiosWithJWT } from "./api.service";

export const enroll = async (course_id) => {
  console.log(course_id);
  const res = await axiosWithJWT
    .post(`/courses/${course_id}/enroll/`)
    .catch((err) => {
      if (err.response.status === 401) {
        console.log("error");
      }
    });
  console.log(res);
};
