import { createFeatureSelector, createSelector } from '@ngrx/store';
import { UserState } from './userInfo.reducer';

export const selectUser = createFeatureSelector<UserState>('user');

export const selectUsername = createSelector(
  selectUser,
  (state: UserState) => state.username
);

export const selectIsAdmin = createSelector(
  selectUser,
  (state: UserState) => state.isAdmin
);
