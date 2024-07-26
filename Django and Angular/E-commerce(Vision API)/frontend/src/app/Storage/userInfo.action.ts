import { createAction, props } from '@ngrx/store';

export const loginSuccess = createAction(
  '[Auth API] Login Success',
  props<{ username: string; isAdmin: boolean }>()
);

export const logout = createAction('[Auth] Logout');