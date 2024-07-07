import { z } from "zod";

export const usernameSchema = z.string()
  .min(4, { message: "Username must be at least 4 characters long" })
  .max(64, { message: "Username cannot exceed 64 characters" })
  .regex(/^[^&=+"'|]{4,64}$/, { message: "Username cannot contain special characters like & = + \" ' |" });

export const passwordSchema = z.string()
  .min(8, { message: "Password must be at least 8 characters long" })
  .max(50, { message: "Password cannot exceed 50 characters" })
  .refine((password) => /[a-z]/.test(password), { message: "Password must contain at least one lowercase letter" })
  .refine((password) => /[A-Z]/.test(password), { message: "Password must contain at least one uppercase letter" })
  .refine((password) => /\d/.test(password), { message: "Password must contain at least one digit" })
  .refine((password) => /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password), { message: "Password must contain at least one special character" });
