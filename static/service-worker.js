'use strict';

// Update cache names any time any of the cached files change.
const CACHE_NAME = 'static-cache-v2';
const DATA_CACHE_NAME = 'data-cache-v1';

// Add list of files to cache here.
const FILES_TO_CACHE = [
  'templates/home/home.html',
  'templates/users/login.html',
  'templates/users/register.html',
  'manifest.json',
  'css/pwa/bootstrap.min.css',
  'css/pwa/style.css',
  'css/pwa/circle.css',
  'css/pwa/jquery.datepicker2.css',
  'plugins/fontawesome/css/fontawesome.min.css',
  'plugins/fontawesome/css/all.min.css',
  'plugins/swiper/css/swiper.min.css',
  'plugins/fancybox/jquery.fancybox.min.css',
  'img/pwa/open-account-logout.svg',
  'img/pwa/kidneys.svg',
  'img/pwa/brain.svg',
  'img/pwa/cardiology.svg',
  'img/pwa/dentist.svg',
  'img/pwa/doctors/doctor-02.jpg',
  'img/pwa/doctors/doctor-thumb-01.jpg',
  'img/pwa/doctors/doctor-thumb-02.jpg',
  'img/pwa/doctors/doctor-thumb-03.jpg',
  'img/pwa/doctors/doctor-thumb-07.jpg',
  'img/pwa/specialities/specialities-05.png',
  'img/pwa/favicon.png',
  'img/pwa/icons/icon-144x144.png',
  'img/pwa/add-icon.svg',
  'img/pwa/Back.png',
  'img/pwa/calender-icon.svg',
  'img/pwa/call-bg.png',
  'img/pwa/call-close.svg',
  'img/pwa/chat.svg',
  'img/pwa/chat-icon.svg',
  'img/pwa/check-circle-big.svg',
  'img/pwa/credit-card.svg',
  'img/pwa/dentist-1.svg',
  'img/pwa/doctofemr.svg',
  'img/pwa/email.svg',
  'img/pwa/facebook.svg',
  'img/pwa/facebook-letter.svg',
  'img/pwa/filter.svg',
  'img/pwa/google-plus.svg',
  'img/pwa/google-plus-letter.svg',
  'img/pwa/green-tick.svg',
  'img/pwa/grid-icon.svg',
  'img/pwa/icon-awesome-eye.svg',
  'img/pwa/icon-awesome-user.svg',
  'img/pwa/icon-book.svg',
  'img/pwa/icon-checkmark.svg',
  'img/pwa/icon-clinic-medical.svg',
  'img/pwa/icon-feather-check-circle.svg',
  'img/pwa/icon-metro-calendar.svg',
  'img/pwa/icon-metro-calendar-big.svg',
  'img/pwa/icon-metro-printer.svg',
  'img/pwa/icon-settings.svg',
  'img/pwa/icon-user-nurse.svg',
  'img/pwa/i-icon.svg',
  'img/pwa/instagram.svg',
  'img/pwa/left-arrow.svg',
  'img/pwa/left-arrow-big.svg',
  'img/pwa/left-arrow-big-black.svg',
  'img/pwa/left-arrow-circle.svg',
  'img/pwa/likess.svg',
  'img/pwa/linkedin.svg',
  'img/pwa/lock-icon.svg',
  'img/pwa/logo.png',
  'img/pwa/logo.svg',
  'img/pwa/maledoc.svg',
  'img/pwa/man-icon.svg',
  'img/pwa/map-doctor.svg',
  'img/pwa/mic-icon.svg',
  'img/pwa/mute.svg',
  'img/pwa/patient.svg',
  'img/pwa/pause-icon.svg',
  'img/pwa/paypal.svg',
  'img/pwa/phone-icon.svg',
  'img/pwa/placeholder-small.svg',
  'img/pwa/price-check.svg',
  'img/pwa/purse.svg',
  'img/pwa/register-top-img.png',
  'img/pwa/right-arrow.svg',
  'img/pwa/right-arrow-circle.svg',
  'img/pwa/send.svg',
  'img/pwa/smartphone.svg',
  'img/pwa/smile.svg',
  'img/pwa/specker-icon.svg',
  'img/pwa/star.svg',
  'img/pwa/stethoscope.svg',
  'img/pwa/telephone.svg',
  'img/pwa/today-icon.svg',
  'img/pwa/twitter.svg',
  'img/pwa/user.jpg',
  'img/pwa/user-icon.svg',
  'img/pwa/video-call.png',
  'img/pwa/video-call.svg',
  'img/pwa/video-icon.svg',
  'img/pwa/patients/patient1.jpg',
  'img/pwa/patients/patient2.jpg',
  'img/pwa/patients/patient3.jpg',
  'img/pwa/patients/patient4.jpg',
  'img/pwa/patients/patient5.jpg',
  'img/pwa/patients/patient6.jpg',
  'img/pwa/patients/patient7.jpg',
  'img/pwa/patients/patient8.jpg',
  'img/pwa/patients/patient10.jpg',
  'img/pwa/patients/patient15.jpg',
  'img/pwa/features/feature-01.jpg',
  'img/pwa/features/feature-02.jpg',
  'img/pwa/features/feature-03.jpg',
  'img/pwa/features/feature-04.jpg',
  'js/pwa/jquery-3.5.1.min.js',
  'js/pwa/bootstrap.min.js',
  'js/pwa/bootstrap-datetimepicker.min.js',
  'js/pwa/Chart.bundle.js',
  'js/pwa/install.js',
  'js/pwa/jquery.datepicker2.js',
  'js/pwa/moment.min.js',
  'js/pwa/popper.min.js',
  'script.js',
  'plugins/swiper/js/swiper.min.js',
  'plugins/fancybox/jquery.fancybox.min.js',
  'fonts/MaterialIcons-Regular.woff',
  'fonts/MaterialIcons-Regular.woff2',
  'fonts/poppins-regular-webfont.woff2',
  'fonts/poppins-medium-webfont.woff2',
  'fonts/poppins-regular-webfont.woff',
  'fonts/poppins-medium-webfont.woff',
  'plugins/fontawesome/webfonts/fa-solid-900.woff2',
  'plugins/fontawesome/webfonts/fa-regular-400.woff2',
  'plugins/fontawesome/webfonts/fa-solid-900.woff',
  'plugins/fontawesome/webfonts/fa-regular-400.woff',
  'plugins/fontawesome/webfonts/fa-solid-900.ttf',
  'plugins/fontawesome/webfonts/fa-regular-400.ttf',
];

self.addEventListener('install', (evt) => {
  console.log('[ServiceWorker] Install');
  // Precache static resources here.
  evt.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[ServiceWorker] Pre-caching offline page');
      return cache.addAll(FILES_TO_CACHE);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (evt) => {
  console.log('[ServiceWorker] Activate');
  // Remove previous cached data from disk.
  evt.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(keyList.map((key) => {
        if (key !== CACHE_NAME && key !== DATA_CACHE_NAME) {
          console.log('[ServiceWorker] Removing old cache', key);
          return caches.delete(key);
        }
      }));
    })
);
  self.clients.claim();
});

self.addEventListener('fetch', (evt) => {
  console.log('[ServiceWorker] Fetch', evt.request.url);
  // Add fetch event handler here.
  if (evt.request.url.includes('forecast/')) {
  console.log('[Service Worker] Fetch (data)', evt.request.url);
  evt.respondWith(
      caches.open(DATA_CACHE_NAME).then((cache) => {
        return fetch(evt.request)
            .then((response) => {
              // If the response was good, clone it and store it in the cache.
              if (response.status === 200) {
                cache.put(evt.request.url, response.clone());
              }
              return response;
            }).catch((err) => {
              // Network request failed, try to get it from the cache.
              return cache.match(evt.request);
            });
      }));
  return;
}
evt.respondWith(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.match(evt.request)
          .then((response) => {
            return response || fetch(evt.request);
          });
    })
);
});