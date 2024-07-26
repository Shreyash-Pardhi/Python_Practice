import { createReducer, on, Action } from '@ngrx/store';
import { loginSuccess, logout } from './userInfo.action';

export interface UserState {
  username: string;
  isAdmin: boolean;
}

export const initialState: UserState = {
  username: '',
  isAdmin: false,
};

const _userReducer = createReducer(
  initialState,
  on(loginSuccess, (state, { username, isAdmin }) => ({ ...state, username, isAdmin })),
  on(logout, () => initialState)
);

export function userReducer(state: UserState | undefined, action: Action) {
  return _userReducer(state, action);
}
