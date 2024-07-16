import { TestBed } from '@angular/core/testing';

import { SharedAllService } from './shared-all.service';

describe('SharedAllService', () => {
  let service: SharedAllService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SharedAllService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
