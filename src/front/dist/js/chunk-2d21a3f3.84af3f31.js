(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d21a3f3"],{bb63:function(t,e,r){"use strict";r.r(e);var o=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"authors"},[r("v-container",{staticClass:"pa-0",attrs:{"grid-list-lg":""}},[r("v-layout",{attrs:{row:"",wrap:""}},t._l(t.favoritesAuthors,(function(e){return r("v-flex",{key:e.id,attrs:{xs6:"",sm3:"",md4:""}},[r("UserItem",{attrs:{fav:"",author:e},on:{deleteFavorites:t.deleteFavorites}})],1)})),1)],1)],1)},s=[],i=(r("8e6e"),r("ac6a"),r("456d"),r("bd86")),n=r("2f62"),a=r("04ce");function c(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(t);e&&(o=o.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),r.push.apply(r,o)}return r}function u(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?c(r,!0).forEach((function(e){Object(i["a"])(t,e,r[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):c(r).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))}))}return t}var l={name:"Authors",computed:u({},Object(n["d"])("auth",["auth"]),{},Object(n["d"])("profile",["favoritesAuthors"])),components:{UserItem:a["a"]},methods:u({},Object(n["b"])("profile",["getFavoritesDiscussionAuthors","toggleDiscusionAuthorFav"]),{deleteFavorites:function(t){var e=this;this.toggleDiscusionAuthorFav(t).then((function(r){e.$emit("removeAuthor",t),e.$store.commit("profile/removeFavoritesDiscussionAuthors",r.id)}))}}),created:function(){0==this.favoritesAuthors.length&&this.getFavoritesDiscussionAuthors(1)}},f=l,h=r("2877"),p=Object(h["a"])(f,o,s,!1,null,null,null);e["default"]=p.exports}}]);
//# sourceMappingURL=chunk-2d21a3f3.84af3f31.js.map