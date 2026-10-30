(function(){const t=document.createElement("link").relList;if(t&&t.supports&&t.supports("modulepreload"))return;for(const a of document.querySelectorAll('link[rel="modulepreload"]'))i(a);new MutationObserver(a=>{for(const s of a)if(s.type==="childList")for(const r of s.addedNodes)r.tagName==="LINK"&&r.rel==="modulepreload"&&i(r)}).observe(document,{childList:!0,subtree:!0});function n(a){const s={};return a.integrity&&(s.integrity=a.integrity),a.referrerPolicy&&(s.referrerPolicy=a.referrerPolicy),a.crossOrigin==="use-credentials"?s.credentials="include":a.crossOrigin==="anonymous"?s.credentials="omit":s.credentials="same-origin",s}function i(a){if(a.ep)return;a.ep=!0;const s=n(a);fetch(a.href,s)}})();var G0={exports:{}},Uc={};/**
 * @license React
 * react-jsx-runtime.production.js
 *
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */var kx=Symbol.for("react.transitional.element"),Yx=Symbol.for("react.fragment");function V0(e,t,n){var i=null;if(n!==void 0&&(i=""+n),t.key!==void 0&&(i=""+t.key),"key"in t){n={};for(var a in t)a!=="key"&&(n[a]=t[a])}else n=t;return t=n.ref,{$$typeof:kx,type:e,key:i,ref:t!==void 0?t:null,props:n}}Uc.Fragment=Yx;Uc.jsx=V0;Uc.jsxs=V0;G0.exports=Uc;var Kt=G0.exports,X0={exports:{}},Ct={};/**
 * @license React
 * react.production.js
 *
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */var Mp=Symbol.for("react.transitional.element"),qx=Symbol.for("react.portal"),Wx=Symbol.for("react.fragment"),jx=Symbol.for("react.strict_mode"),Zx=Symbol.for("react.profiler"),Kx=Symbol.for("react.consumer"),Qx=Symbol.for("react.context"),Jx=Symbol.for("react.forward_ref"),$x=Symbol.for("react.suspense"),tM=Symbol.for("react.memo"),k0=Symbol.for("react.lazy"),eM=Symbol.for("react.activity"),nM=Symbol.for("react.view_transition"),Km=Symbol.iterator;function iM(e){return e===null||typeof e!="object"?null:(e=Km&&e[Km]||e["@@iterator"],typeof e=="function"?e:null)}var Y0={isMounted:function(){return!1},enqueueForceUpdate:function(){},enqueueReplaceState:function(){},enqueueSetState:function(){}},q0=Object.assign,W0={};function no(e,t,n){this.props=e,this.context=t,this.refs=W0,this.updater=n||Y0}no.prototype.isReactComponent={};no.prototype.setState=function(e,t){if(typeof e!="object"&&typeof e!="function"&&e!=null)throw Error("takes an object of state variables to update or a function which returns an object of state variables.");this.updater.enqueueSetState(this,e,t,"setState")};no.prototype.forceUpdate=function(e){this.updater.enqueueForceUpdate(this,e,"forceUpdate")};function j0(){}j0.prototype=no.prototype;function Ep(e,t,n){this.props=e,this.context=t,this.refs=W0,this.updater=n||Y0}var Tp=Ep.prototype=new j0;Tp.constructor=Ep;q0(Tp,no.prototype);Tp.isPureReactComponent=!0;var Qm=Array.isArray;function Eh(){}var ge={H:null,A:null,T:null,S:null},Z0=Object.prototype.hasOwnProperty;function bp(e,t,n){var i=n.ref;return{$$typeof:Mp,type:e,key:t,ref:i!==void 0?i:null,props:n}}function aM(e,t){return bp(e.type,t,e.props)}function Ap(e){return typeof e=="object"&&e!==null&&e.$$typeof===Mp}function sM(e){var t={"=":"=0",":":"=2"};return"$"+e.replace(/[=:]/g,function(n){return t[n]})}var Jm=/\/+/g;function uf(e,t){return typeof e=="object"&&e!==null&&e.key!=null?sM(""+e.key):t.toString(36)}function rM(e){switch(e.status){case"fulfilled":return e.value;case"rejected":throw e.reason;default:switch(typeof e.status=="string"?e.then(Eh,Eh):(e.status="pending",e.then(function(t){e.status==="pending"&&(e.status="fulfilled",e.value=t)},function(t){e.status==="pending"&&(e.status="rejected",e.reason=t)})),e.status){case"fulfilled":return e.value;case"rejected":throw e.reason}}throw e}function sr(e,t,n,i,a){var s=typeof e;(s==="undefined"||s==="boolean")&&(e=null);var r=!1;if(e===null)r=!0;else switch(s){case"bigint":case"string":case"number":r=!0;break;case"object":switch(e.$$typeof){case Mp:case qx:r=!0;break;case k0:return r=e._init,sr(r(e._payload),t,n,i,a)}}if(r)return a=a(e),r=i===""?"."+uf(e,0):i,Qm(a)?(n="",r!=null&&(n=r.replace(Jm,"$&/")+"/"),sr(a,t,n,"",function(u){return u})):a!=null&&(Ap(a)&&(a=aM(a,n+(a.key==null||e&&e.key===a.key?"":(""+a.key).replace(Jm,"$&/")+"/")+r)),t.push(a)),1;r=0;var o=i===""?".":i+":";if(Qm(e))for(var l=0;l<e.length;l++)i=e[l],s=o+uf(i,l),r+=sr(i,t,n,s,a);else if(l=iM(e),typeof l=="function")for(e=l.call(e),l=0;!(i=e.next()).done;)i=i.value,s=o+uf(i,l++),r+=sr(i,t,n,s,a);else if(s==="object"){if(typeof e.then=="function")return sr(rM(e),t,n,i,a);throw t=String(e),Error("Objects are not valid as a React child (found: "+(t==="[object Object]"?"object with keys {"+Object.keys(e).join(", ")+"}":t)+"). If you meant to render a collection of children, use an array instead.")}return r}function Ul(e,t,n){if(e==null)return e;var i=[],a=0;return sr(e,i,"","",function(s){return t.call(n,s,a++)}),i}function oM(e){if(e._status===-1){var t=e._result,n=t();n.then(function(i){(e._status===0||e._status===-1)&&(e._status=1,e._result=i,n.status===void 0&&(n.status="fulfilled",n.value=i))},function(i){(e._status===0||e._status===-1)&&(e._status=2,e._result=i,n.status===void 0&&(n.status="rejected",n.reason=i))}),e._status===-1&&(e._status=0,e._result=n)}if(e._status===1)return e._result.default;throw e._result}var $m=typeof reportError=="function"?reportError:function(e){if(typeof window=="object"&&typeof window.ErrorEvent=="function"){var t=new window.ErrorEvent("error",{bubbles:!0,cancelable:!0,message:typeof e=="object"&&e!==null&&typeof e.message=="string"?String(e.message):String(e),error:e});if(!window.dispatchEvent(t))return}else if(typeof process=="object"&&typeof process.emit=="function"){process.emit("uncaughtException",e);return}console.error(e)};function K0(e){var t=ge.T,n={};n.types=t!==null?t.types:null,ge.T=n;try{var i=e(),a=ge.S;a!==null&&a(n,i),typeof i=="object"&&i!==null&&typeof i.then=="function"&&i.then(Eh,$m)}catch(s){$m(s)}finally{t!==null&&n.types!==null&&(t.types=n.types),ge.T=t}}function Q0(e){var t=ge.T;if(t!==null){var n=t.types;n===null?t.types=[e]:n.indexOf(e)===-1&&n.push(e)}else K0(Q0.bind(null,e))}var lM={map:Ul,forEach:function(e,t,n){Ul(e,function(){t.apply(this,arguments)},n)},count:function(e){var t=0;return Ul(e,function(){t++}),t},toArray:function(e){return Ul(e,function(t){return t})||[]},only:function(e){if(!Ap(e))throw Error("React.Children.only expected to receive a single React element child.");return e}};Ct.Activity=eM;Ct.Children=lM;Ct.Component=no;Ct.Fragment=Wx;Ct.Profiler=Zx;Ct.PureComponent=Ep;Ct.StrictMode=jx;Ct.Suspense=$x;Ct.ViewTransition=nM;Ct.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE=ge;Ct.__COMPILER_RUNTIME={__proto__:null,c:function(e){return ge.H.useMemoCache(e)}};Ct.addTransitionType=Q0;Ct.cache=function(e){return function(){return e.apply(null,arguments)}};Ct.cacheSignal=function(){return null};Ct.cloneElement=function(e,t,n){if(e==null)throw Error("The argument must be a React element, but you passed "+e+".");var i=q0({},e.props),a=e.key;if(t!=null)for(s in t.key!==void 0&&(a=""+t.key),t)!Z0.call(t,s)||s==="key"||s==="__self"||s==="__source"||s==="ref"&&t.ref===void 0||(i[s]=t[s]);var s=arguments.length-2;if(s===1)i.children=n;else if(1<s){for(var r=Array(s),o=0;o<s;o++)r[o]=arguments[o+2];i.children=r}return bp(e.type,a,i)};Ct.createContext=function(e){return e={$$typeof:Qx,_currentValue:e,_currentValue2:e,_threadCount:0,Provider:null,Consumer:null},e.Provider=e,e.Consumer={$$typeof:Kx,_context:e},e};Ct.createElement=function(e,t,n){var i,a={},s=null;if(t!=null)for(i in t.key!==void 0&&(s=""+t.key),t)Z0.call(t,i)&&i!=="key"&&i!=="__self"&&i!=="__source"&&(a[i]=t[i]);var r=arguments.length-2;if(r===1)a.children=n;else if(1<r){for(var o=Array(r),l=0;l<r;l++)o[l]=arguments[l+2];a.children=o}if(e&&e.defaultProps)for(i in r=e.defaultProps,r)a[i]===void 0&&(a[i]=r[i]);return bp(e,s,a)};Ct.createRef=function(){return{current:null}};Ct.forwardRef=function(e){return{$$typeof:Jx,render:e}};Ct.isValidElement=Ap;Ct.lazy=function(e){return{$$typeof:k0,_payload:{_status:-1,_result:e},_init:oM}};Ct.memo=function(e,t){return{$$typeof:tM,type:e,compare:t===void 0?null:t}};Ct.startTransition=K0;Ct.unstable_useCacheRefresh=function(){return ge.H.useCacheRefresh()};Ct.use=function(e){return ge.H.use(e)};Ct.useActionState=function(e,t,n){return ge.H.useActionState(e,t,n)};Ct.useCallback=function(e,t){return ge.H.useCallback(e,t)};Ct.useContext=function(e){return ge.H.useContext(e)};Ct.useDebugValue=function(){};Ct.useDeferredValue=function(e,t){return ge.H.useDeferredValue(e,t)};Ct.useEffect=function(e,t){return ge.H.useEffect(e,t)};Ct.useEffectEvent=function(e){return ge.H.useEffectEvent(e)};Ct.useId=function(){return ge.H.useId()};Ct.useImperativeHandle=function(e,t,n){return ge.H.useImperativeHandle(e,t,n)};Ct.useInsertionEffect=function(e,t){return ge.H.useInsertionEffect(e,t)};Ct.useLayoutEffect=function(e,t){return ge.H.useLayoutEffect(e,t)};Ct.useMemo=function(e,t){return ge.H.useMemo(e,t)};Ct.useOptimistic=function(e,t){return ge.H.useOptimistic(e,t)};Ct.useReducer=function(e,t,n){return ge.H.useReducer(e,t,n)};Ct.useRef=function(e){return ge.H.useRef(e)};Ct.useState=function(e){return ge.H.useState(e)};Ct.useSyncExternalStore=function(e,t,n){return ge.H.useSyncExternalStore(e,t,n)};Ct.useTransition=function(){return ge.H.useTransition()};Ct.version="19.3.1";X0.exports=Ct;var Pn=X0.exports,J0={exports:{}},Nc={},$0={exports:{}},tv={};/**
 * @license React
 * scheduler.production.js
 *
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */(function(e){function t(D,V){var z=D.length;D.push(V);t:for(;0<z;){var tt=z-1>>>1,it=D[tt];if(0<a(it,V))D[tt]=V,D[z]=it,z=tt;else break t}}function n(D){return D.length===0?null:D[0]}function i(D){if(D.length===0)return null;var V=D[0],z=D.pop();if(z!==V){D[0]=z;t:for(var tt=0,it=D.length,ht=it>>>1;tt<ht;){var Ft=2*(tt+1)-1,kt=D[Ft],k=Ft+1,$=D[k];if(0>a(kt,z))k<it&&0>a($,kt)?(D[tt]=$,D[k]=z,tt=k):(D[tt]=kt,D[Ft]=z,tt=Ft);else if(k<it&&0>a($,z))D[tt]=$,D[k]=z,tt=k;else break t}}return V}function a(D,V){var z=D.sortIndex-V.sortIndex;return z!==0?z:D.id-V.id}if(e.unstable_now=void 0,typeof performance=="object"&&typeof performance.now=="function"){var s=performance;e.unstable_now=function(){return s.now()}}else{var r=Date,o=r.now();e.unstable_now=function(){return r.now()-o}}var l=[],u=[],h=1,p=null,f=3,d=!1,v=!1,y=!1,m=!1,c=typeof setTimeout=="function"?setTimeout:null,_=typeof clearTimeout=="function"?clearTimeout:null,g=typeof setImmediate<"u"?setImmediate:null;function x(D){for(var V=n(u);V!==null;){if(V.callback===null)i(u);else if(V.startTime<=D)i(u),V.sortIndex=V.expirationTime,t(l,V);else break;V=n(u)}}function C(D){if(y=!1,x(D),!v)if(n(l)!==null)v=!0,R||(R=!0,F());else{var V=n(u);V!==null&&K(C,V.startTime-D)}}var R=!1,b=-1,w=5,W=-1;function S(){return m?!0:!(e.unstable_now()-W<w)}function T(){if(m=!1,R){var D=e.unstable_now();W=D;var V=!0;try{t:{v=!1,y&&(y=!1,_(b),b=-1),d=!0;var z=f;try{e:{for(x(D),p=n(l);p!==null&&!(p.expirationTime>D&&S());){var tt=p.callback;if(typeof tt=="function"){p.callback=null,f=p.priorityLevel;var it=tt(p.expirationTime<=D);if(D=e.unstable_now(),typeof it=="function"){p.callback=it,x(D),V=!0;break e}p===n(l)&&i(l),x(D)}else i(l);p=n(l)}if(p!==null)V=!0;else{var ht=n(u);ht!==null&&K(C,ht.startTime-D),V=!1}}break t}finally{p=null,f=z,d=!1}V=void 0}}finally{V?F():R=!1}}}var F;if(typeof g=="function")F=function(){g(T)};else if(typeof MessageChannel<"u"){var G=new MessageChannel,Y=G.port2;G.port1.onmessage=T,F=function(){Y.postMessage(null)}}else F=function(){c(T,0)};function K(D,V){b=c(function(){D(e.unstable_now())},V)}e.unstable_IdlePriority=5,e.unstable_ImmediatePriority=1,e.unstable_LowPriority=4,e.unstable_NormalPriority=3,e.unstable_Profiling=null,e.unstable_UserBlockingPriority=2,e.unstable_cancelCallback=function(D){D.callback=null},e.unstable_forceFrameRate=function(D){0>D||125<D?console.error("forceFrameRate takes a positive int between 0 and 125, forcing frame rates higher than 125 fps is not supported"):w=0<D?Math.floor(1e3/D):5},e.unstable_getCurrentPriorityLevel=function(){return f},e.unstable_next=function(D){switch(f){case 1:case 2:case 3:var V=3;break;default:V=f}var z=f;f=V;try{return D()}finally{f=z}},e.unstable_requestPaint=function(){m=!0},e.unstable_runWithPriority=function(D,V){switch(D){case 1:case 2:case 3:case 4:case 5:break;default:D=3}var z=f;f=D;try{return V()}finally{f=z}},e.unstable_scheduleCallback=function(D,V,z){var tt=e.unstable_now();switch(typeof z=="object"&&z!==null?(z=z.delay,z=typeof z=="number"&&0<z?tt+z:tt):z=tt,D){case 1:var it=-1;break;case 2:it=250;break;case 5:it=1073741823;break;case 4:it=1e4;break;default:it=5e3}return it=z+it,D={id:h++,callback:V,priorityLevel:D,startTime:z,expirationTime:it,sortIndex:-1},z>tt?(D.sortIndex=z,t(u,D),n(l)===null&&D===n(u)&&(y?(_(b),b=-1):y=!0,K(C,z-tt))):(D.sortIndex=it,t(l,D),v||d||(v=!0,R||(R=!0,F()))),D},e.unstable_shouldYield=S,e.unstable_wrapCallback=function(D){var V=f;return function(){var z=f;f=V;try{return D.apply(this,arguments)}finally{f=z}}}})(tv);$0.exports=tv;var uM=$0.exports,ev={exports:{}},on={};/**
 * @license React
 * react-dom.production.js
 *
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */var cM=Pn;function nv(e){var t="https://react.dev/errors/"+e;if(1<arguments.length){t+="?args[]="+encodeURIComponent(arguments[1]);for(var n=2;n<arguments.length;n++)t+="&args[]="+encodeURIComponent(arguments[n])}return"Minified React error #"+e+"; visit "+t+" for the full message or use the non-minified dev environment for full errors and additional helpful warnings."}function ca(){}var dn={d:{f:ca,r:function(){throw Error(nv(522))},D:ca,C:ca,L:ca,m:ca,X:ca,S:ca,M:ca},p:0,findDOMNode:null},fM=Symbol.for("react.portal"),hM=Symbol.for("react.recoverable"),t_=Symbol.for("react.optimistic_key");function dM(e,t,n){var i=3<arguments.length&&arguments[3]!==void 0?arguments[3]:null;return{$$typeof:fM,key:i==null?null:i===t_?t_:""+i,children:e,containerInfo:t,implementation:n}}var Po=cM.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE;function Lc(e,t){if(e==="font")return"";if(typeof t=="string")return t==="use-credentials"?t:""}on.__DOM_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE=dn;on.browser=function(e){return{$$typeof:hM,_reason:e}};on.createPortal=function(e,t){var n=2<arguments.length&&arguments[2]!==void 0?arguments[2]:null;if(!t||t.nodeType!==1&&t.nodeType!==9&&t.nodeType!==11)throw Error(nv(299));return dM(e,t,null,n)};on.flushSync=function(e){var t=Po.T,n=dn.p;try{if(Po.T=null,dn.p=2,e)return e()}finally{Po.T=t,dn.p=n,dn.d.f()}};on.preconnect=function(e,t){typeof e=="string"&&(t?(t=t.crossOrigin,t=typeof t=="string"?t==="use-credentials"?t:"":void 0):t=null,dn.d.C(e,t))};on.prefetchDNS=function(e){typeof e=="string"&&dn.d.D(e)};on.preinit=function(e,t){if(typeof e=="string"&&t&&typeof t.as=="string"){var n=t.as,i=Lc(n,t.crossOrigin),a=typeof t.integrity=="string"?t.integrity:void 0,s=typeof t.fetchPriority=="string"?t.fetchPriority:void 0;n==="style"?dn.d.S(e,typeof t.precedence=="string"?t.precedence:void 0,{crossOrigin:i,integrity:a,fetchPriority:s}):n==="script"&&dn.d.X(e,{crossOrigin:i,integrity:a,fetchPriority:s,nonce:typeof t.nonce=="string"?t.nonce:void 0})}};on.preinitModule=function(e,t){if(typeof e=="string")if(typeof t=="object"&&t!==null){if(t.as==null||t.as==="script"){var n=Lc(t.as,t.crossOrigin);dn.d.M(e,{crossOrigin:n,integrity:typeof t.integrity=="string"?t.integrity:void 0,nonce:typeof t.nonce=="string"?t.nonce:void 0,fetchPriority:typeof t.fetchPriority=="string"?t.fetchPriority:void 0})}}else t==null&&dn.d.M(e)};on.preload=function(e,t){if(typeof e=="string"&&typeof t=="object"&&t!==null&&typeof t.as=="string"){var n=t.as,i=Lc(n,t.crossOrigin);dn.d.L(e,n,{crossOrigin:i,integrity:typeof t.integrity=="string"?t.integrity:void 0,nonce:typeof t.nonce=="string"?t.nonce:void 0,type:typeof t.type=="string"?t.type:void 0,fetchPriority:typeof t.fetchPriority=="string"?t.fetchPriority:void 0,referrerPolicy:typeof t.referrerPolicy=="string"?t.referrerPolicy:void 0,imageSrcSet:typeof t.imageSrcSet=="string"?t.imageSrcSet:void 0,imageSizes:typeof t.imageSizes=="string"?t.imageSizes:void 0,media:typeof t.media=="string"?t.media:void 0})}};on.preloadModule=function(e,t){if(typeof e=="string")if(t){var n=Lc(t.as,t.crossOrigin);dn.d.m(e,{as:typeof t.as=="string"&&t.as!=="script"?t.as:void 0,crossOrigin:n,integrity:typeof t.integrity=="string"?t.integrity:void 0,nonce:typeof t.nonce=="string"?t.nonce:void 0,fetchPriority:typeof t.fetchPriority=="string"?t.fetchPriority:void 0})}else dn.d.m(e)};on.requestFormReset=function(e){dn.d.r(e)};on.unstable_batchedUpdates=function(e,t){return e(t)};on.useFormState=function(e,t,n){return Po.H.useFormState(e,t,n)};on.useFormStatus=function(){return Po.H.useHostTransitionStatus()};on.version="19.3.1";function iv(){if(!(typeof __REACT_DEVTOOLS_GLOBAL_HOOK__>"u"||typeof __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE!="function"))try{__REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE(iv)}catch(e){console.error(e)}}iv(),ev.exports=on;var pM=ev.exports;/**
 * @license React
 * react-dom-client.production.js
 *
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */var Fe=uM,av=Pn,mM=pM;function q(e){var t="https://react.dev/errors/"+e;if(1<arguments.length){t+="?args[]="+encodeURIComponent(arguments[1]);for(var n=2;n<arguments.length;n++)t+="&args[]="+encodeURIComponent(arguments[n])}return"Minified React error #"+e+"; visit "+t+" for the full message or use the non-minified dev environment for full errors and additional helpful warnings."}function sv(e){return!(!e||e.nodeType!==1&&e.nodeType!==9&&e.nodeType!==11)}function hl(e){for(var t=e,n=t;n&&!n.alternate;)t=n,t.flags&4098&&(e=t.return),n=t.return;for(;t.return;)t=t.return;return t.tag===3?e:null}function rv(e){if(e.tag===13){var t=e.memoizedState;if(t===null&&(e=e.alternate,e!==null&&(t=e.memoizedState)),t!==null)return t.dehydrated}return null}function ov(e){if(e.tag===31){var t=e.memoizedState;if(t===null&&(e=e.alternate,e!==null&&(t=e.memoizedState)),t!==null)return t.dehydrated}return null}function e_(e){if(hl(e)!==e)throw Error(q(188))}function _M(e){var t=e.alternate;if(!t){if(t=hl(e),t===null)throw Error(q(188));return t!==e?null:e}for(var n=e,i=t;;){var a=n.return;if(a===null)break;var s=a.alternate;if(s===null){if(i=a.return,i!==null){n=i;continue}break}if(a.child===s.child){for(s=a.child;s;){if(s===n)return e_(a),e;if(s===i)return e_(a),t;s=s.sibling}throw Error(q(188))}if(n.return!==i.return)n=a,i=s;else{for(var r=!1,o=a.child;o;){if(o===n){r=!0,n=a,i=s;break}if(o===i){r=!0,i=a,n=s;break}o=o.sibling}if(!r){for(o=s.child;o;){if(o===n){r=!0,n=s,i=a;break}if(o===i){r=!0,i=s,n=a;break}o=o.sibling}if(!r)throw Error(q(189))}}if(n.alternate!==i)throw Error(q(190))}if(n.tag!==3)throw Error(q(188));return n.stateNode.current===n?e:t}function lv(e){var t=e.tag;if(t===5||t===26||t===27||t===6)return e;for(e=e.child;e!==null;){if(t=lv(e),t!==null)return t;e=e.sibling}return null}function Rn(e,t,n,i,a,s){for(;e!==null;){if((e.tag===5||e.tag===27||e.tag===6)&&n(e,i,a,s)||(e.tag!==22||e.memoizedState===null)&&(t||e.tag!==5&&e.tag!==27)&&Rn(e.child,t,n,i,a,s))return!0;e=e.sibling}return!1}function Ps(e){for(e=e.return;e!==null;){if(e.tag===3||e.tag===5||e.tag===27)return e;e=e.return}return null}function n_(e){var t=!1;for(e=e.return;e!==null&&(e.tag===4&&(t=!0),!(e.tag===3||e.tag===5||e.tag===27));)e=e.return;return t}function uv(e){var t=[null,null],n=Ps(e);return n===null||cv(t,e,n.child,{foundSelf:!1}),t}function cv(e,t,n,i){for(;n!==null;){if(n===t)i.foundSelf=!0;else if(n.tag===5||n.tag===27||n.tag===6){if(i.foundSelf)return e[1]=n,!0;e[0]=n}else if((n.tag!==22||n.memoizedState===null)&&cv(e,t,n.child,i))return!0;n=n.sibling}return!1}function Be(e){switch(e.tag){case 5:case 27:case 6:return e.stateNode;case 3:return e.stateNode.containerInfo;default:throw Error(q(559))}}var ur=null,Th=null;function gM(e,t,n){return e===n?!0:e===t?(ur=e,!0):!1}function vM(e,t,n){return e===n?(Th=e,!1):e===t?(Th!==null&&(ur=e),!0):!1}function i_(e){if(e===null)return null;do e=e===null?null:e.return;while(e&&e.tag!==5&&e.tag!==27&&e.tag!==3);return e||null}function bh(e,t,n){for(var i=0,a=e;a;a=n(a))i++;a=0;for(var s=t;s;s=n(s))a++;for(;0<i-a;)e=n(e),i--;for(;0<a-i;)t=n(t),a--;for(;i--;){if(e===t||t!==null&&e===t.alternate)return e;e=n(e),t=n(t)}return null}var de=Object.assign,SM=Symbol.for("react.element"),Nl=Symbol.for("react.transitional.element"),Ro=Symbol.for("react.portal"),cr=Symbol.for("react.fragment"),fv=Symbol.for("react.strict_mode"),Ah=Symbol.for("react.profiler"),hv=Symbol.for("react.consumer"),Ci=Symbol.for("react.context"),Rp=Symbol.for("react.forward_ref"),Rh=Symbol.for("react.suspense"),Ch=Symbol.for("react.suspense_list"),Cp=Symbol.for("react.memo"),ya=Symbol.for("react.lazy"),wh=Symbol.for("react.activity"),yM=Symbol.for("react.legacy_hidden"),xM=Symbol.for("react.memo_cache_sentinel"),Dh=Symbol.for("react.view_transition"),MM=Symbol.for("react.recoverable"),a_=Symbol.iterator;function ho(e){return e===null||typeof e!="object"?null:(e=a_&&e[a_]||e["@@iterator"],typeof e=="function"?e:null)}var EM=Symbol.for("react.client.reference");function Uh(e){if(e==null)return null;if(typeof e=="function")return e.$$typeof===EM?null:e.displayName||e.name||null;if(typeof e=="string")return e;switch(e){case cr:return"Fragment";case Ah:return"Profiler";case fv:return"StrictMode";case Rh:return"Suspense";case Ch:return"SuspenseList";case wh:return"Activity";case Dh:return"ViewTransition"}if(typeof e=="object")switch(e.$$typeof){case Ro:return"Portal";case Ci:return e.displayName||"Context";case hv:return(e._context.displayName||"Context")+".Consumer";case Rp:var t=e.render;return e=e.displayName,e||(e=t.displayName||t.name||"",e=e!==""?"ForwardRef("+e+")":"ForwardRef"),e;case Cp:return t=e.displayName||null,t!==null?t:Uh(e.type)||"Memo";case ya:t=e._payload,e=e._init;try{return Uh(e(t))}catch{}}return null}var Co=Array.isArray,xt=av.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE,te=mM.__DOM_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE,vs={pending:!1,data:null,method:null,action:null},Nh=[],fr=-1;function Pi(e){return{current:e}}function Je(e){0>fr||(e.current=Nh[fr],Nh[fr]=null,fr--)}function ve(e,t){fr++,Nh[fr]=e.current,e.current=t}var Ni=Pi(null),Zo=Pi(null),Ua=Pi(null),Zu=Pi(null);function Ku(e,t){switch(ve(Ua,t),ve(Zo,e),ve(Ni,null),t.nodeType){case 9:case 11:e=(e=t.documentElement)&&(e=e.namespaceURI)?gg(e):0;break;default:if(e=t.tagName,t=t.namespaceURI)t=gg(t),e=Oy(t,e);else switch(e){case"svg":e=1;break;case"math":e=2;break;default:e=0}}Je(Ni),ve(Ni,e)}function Ir(){Je(Ni),Je(Zo),Je(Ua)}function Lh(e){var t=e.memoizedState;t!==null&&(Wr._currentValue=t.memoizedState,ve(Zu,e)),t=Ni.current;var n=Oy(t,e.type);t!==n&&(ve(Zo,e),ve(Ni,n))}function Qu(e){Zo.current===e&&(Je(Ni),Je(Zo)),Zu.current===e&&(Je(Zu),Wr._currentValue=vs)}var cf,s_;function va(e){if(cf===void 0)try{throw Error()}catch(n){var t=n.stack.trim().match(/\n( *(at )?)/);cf=t&&t[1]||"",s_=-1<n.stack.indexOf(`
    at`)?" (<anonymous>)":-1<n.stack.indexOf("@")?"@unknown:0:0":""}return`
`+cf+e+s_}var ff=!1;function hf(e,t){if(!e||ff)return"";ff=!0;var n=Error.prepareStackTrace;Error.prepareStackTrace=void 0;try{var i={DetermineComponentFrameRoot:function(){try{if(t){var p=function(){throw Error()};if(Object.defineProperty(p.prototype,"props",{set:function(){throw Error()}}),typeof Reflect=="object"&&Reflect.construct){try{Reflect.construct(p,[])}catch(v){var f=v}Reflect.construct(e,[],p)}else{try{p.call()}catch(v){f=v}p=!1;try{var d=Object.getOwnPropertyDescriptor(e.prototype,"props");Object.defineProperty(e.prototype,"props",{configurable:!0,set:function(){throw Error()}}),p=!0,new e}finally{p&&(d!==void 0?Object.defineProperty(e.prototype,"props",d):delete e.prototype.props)}}}else{try{throw Error()}catch(v){f=v}(p=e())&&typeof p.catch=="function"&&p.catch(function(){})}}catch(v){if(v&&f&&typeof v.stack=="string")return[v.stack,f.stack]}return[null,null]}};i.DetermineComponentFrameRoot.displayName="DetermineComponentFrameRoot";var a=Object.getOwnPropertyDescriptor(i.DetermineComponentFrameRoot,"name");a&&a.configurable&&Object.defineProperty(i.DetermineComponentFrameRoot,"name",{value:"DetermineComponentFrameRoot"});var s=i.DetermineComponentFrameRoot(),r=s[0],o=s[1];if(r&&o){var l=r.split(`
`),u=o.split(`
`);for(a=i=0;i<l.length&&!l[i].includes("DetermineComponentFrameRoot");)i++;for(;a<u.length&&!u[a].includes("DetermineComponentFrameRoot");)a++;if(i===l.length||a===u.length)for(i=l.length-1,a=u.length-1;1<=i&&0<=a&&l[i]!==u[a];)a--;for(;1<=i&&0<=a;i--,a--)if(l[i]!==u[a]){if(i!==1||a!==1)do if(i--,a--,0>a||l[i]!==u[a]){var h=`
`+l[i].replace(" at new "," at ");return e.displayName&&h.includes("<anonymous>")&&(h=h.replace("<anonymous>",e.displayName)),h}while(1<=i&&0<=a);break}}}finally{ff=!1,Error.prepareStackTrace=n}return(n=e?e.displayName||e.name:"")?va(n):""}function TM(e,t){switch(e.tag){case 26:case 27:case 5:return va(e.type);case 16:return va("Lazy");case 13:return e.child!==t&&t!==null?va("Suspense Fallback"):va("Suspense");case 19:return va("SuspenseList");case 0:case 15:return hf(e.type,!1);case 11:return hf(e.type.render,!1);case 1:return hf(e.type,!0);case 31:return va("Activity");case 30:return va("ViewTransition");default:return""}}function r_(e){try{var t="",n=null;do t+=TM(e,n),n=e,e=e.return;while(e);return t}catch(i){return`
Error generating stack: `+i.message+`
`+i.stack}}var Oh=Object.prototype.hasOwnProperty,wp=Fe.unstable_scheduleCallback,df=Fe.unstable_cancelCallback,bM=Fe.unstable_shouldYield,AM=Fe.unstable_requestPaint,Gn=Fe.unstable_now,RM=Fe.unstable_getCurrentPriorityLevel,dv=Fe.unstable_ImmediatePriority,pv=Fe.unstable_UserBlockingPriority,Ju=Fe.unstable_NormalPriority,CM=Fe.unstable_LowPriority,mv=Fe.unstable_IdlePriority,wM=Fe.log,DM=Fe.unstable_setDisableYieldValue,dl=null,Vn=null;function ba(e){if(typeof wM=="function"&&DM(e),Vn&&typeof Vn.setStrictMode=="function")try{Vn.setStrictMode(dl,e)}catch{}}var Xn=Math.clz32?Math.clz32:LM,UM=Math.log,NM=Math.LN2;function LM(e){return e>>>=0,e===0?32:31-(UM(e)/NM|0)|0}var Ll=256,Ol=262144,Pl=4194304;function ls(e){var t=e&42;if(t!==0)return t;switch(e&-e){case 1:return 1;case 2:return 2;case 4:return 4;case 8:return 8;case 16:return 16;case 32:return 32;case 64:return 64;case 128:return 128;case 256:case 512:case 1024:case 2048:case 4096:case 8192:case 16384:case 32768:case 65536:case 131072:return e&-e;case 262144:case 524288:case 1048576:case 2097152:return e&3932160;case 4194304:case 8388608:case 16777216:case 33554432:return e&62914560;case 67108864:return 67108864;case 134217728:return 134217728;case 268435456:return 268435456;case 536870912:return 536870912;case 1073741824:return 0;default:return e}}function Oc(e,t,n){var i=e.pendingLanes;if(i===0)return 0;var a=0,s=e.suspendedLanes,r=e.pingedLanes;e=e.warmLanes;var o=i&134217727;return o!==0?(i=o&~s,i!==0?a=ls(i):(r&=o,r!==0?a=ls(r):n||(n=o&~e,n!==0&&(a=ls(n))))):(o=i&~s,o!==0?a=ls(o):r!==0?a=ls(r):n||(n=i&~e,n!==0&&(a=ls(n)))),a===0?0:t!==0&&t!==a&&!(t&s)&&(s=a&-a,n=t&-t,s>=n||s===32&&(n&4194048)!==0)?t:a}function pl(e,t){return(e.pendingLanes&~(e.suspendedLanes&~e.pingedLanes)&t)===0}function _v(e,t){t&8&&(t|=t&32);var n=e.entangledLanes;if(n!==0)for(e=e.entanglements,n&=t;0<n;){var i=31-Xn(n),a=1<<i;t|=e[i],n&=~a}return t}function OM(e,t){switch(e){case 1:case 2:case 4:case 8:case 64:return t+250;case 16:case 32:case 128:case 256:case 512:case 1024:case 2048:case 4096:case 8192:case 16384:case 32768:case 65536:case 131072:case 262144:case 524288:case 1048576:case 2097152:return t+5e3;case 4194304:case 8388608:case 16777216:case 33554432:return-1;case 67108864:case 134217728:case 268435456:case 536870912:case 1073741824:return-1;default:return-1}}function gv(){var e=Pl;return Pl<<=1,!(Pl&62914560)&&(Pl=4194304),e}function pf(e){for(var t=[],n=0;31>n;n++)t.push(e);return t}function ml(e,t){e.pendingLanes|=t,t!==268435456&&(e.suspendedLanes=0,e.pingedLanes=0,e.warmLanes=0)}function PM(e,t,n,i,a,s){var r=e.pendingLanes;e.pendingLanes=n,e.suspendedLanes=0,e.pingedLanes=0,e.warmLanes=0,e.expiredLanes&=n,e.entangledLanes&=n,e.errorRecoveryDisabledLanes&=n,e.shellSuspendCounter=0;var o=e.entanglements,l=e.expirationTimes,u=e.hiddenUpdates;for(n=r&~n;0<n;){var h=31-Xn(n),p=1<<h;o[h]=0,l[h]=-1;var f=u[h];if(f!==null)for(u[h]=null,h=0;h<f.length;h++){var d=f[h];d!==null&&(d.lane&=-536870913)}n&=~p}i!==0&&vv(e,i,0),s!==0&&a===0&&e.tag!==0&&(e.suspendedLanes|=s&~(r&~t))}function vv(e,t,n){e.pendingLanes|=t,e.suspendedLanes&=~t;var i=31-Xn(t);e.entangledLanes|=t,e.entanglements[i]=e.entanglements[i]|1073741824|n&261930}function Sv(e,t){var n=e.entangledLanes|=t;for(e=e.entanglements;n;){var i=31-Xn(n),a=1<<i;a&t|e[i]&t&&(e[i]|=t),n&=~a}}function yv(e,t){var n=t&-t;return n=n&42?1:Dp(n),n&(e.suspendedLanes|t)?0:n}function Dp(e){switch(e){case 2:e=1;break;case 8:e=4;break;case 32:e=16;break;case 256:case 512:case 1024:case 2048:case 4096:case 8192:case 16384:case 32768:case 65536:case 131072:case 262144:case 524288:case 1048576:case 2097152:case 4194304:case 8388608:case 16777216:case 33554432:e=128;break;case 268435456:e=134217728;break;default:e=0}return e}function Up(e){return e&=-e,2<e?8<e?e&134217727?32:268435456:8:2}function xv(){var e=te.p;return e!==0?e:(e=window.event,e===void 0?32:ex(e.type))}function o_(e,t){var n=te.p;try{return te.p=e,t()}finally{te.p=n}}var ra=Math.random().toString(36).slice(2),Ke="__reactFiber$"+ra,Cn="__reactProps$"+ra,io="__reactContainer$"+ra,l_="__reactEvents$"+ra,zM="__reactListeners$"+ra,IM="__reactHandles$"+ra,u_="__reactResources$"+ra,_l="__reactMarker$"+ra,$u="__reactLoad$"+ra;function Pc(e){delete e[Ke],delete e[Cn],delete e[zM],delete e[IM]}function ps(e){var t;if(t=e[Ke])return t;for(var n=e.parentNode;n;){if(t=n[io]||n[Ke]){if(n=t.alternate,t.child!==null||n!==null&&n.child!==null)for(e=bg(e);e!==null;){if(n=e[Ke])return n;e=bg(e)}return t}e=n,n=e.parentNode}return null}function ao(e){if(e=e[Ke]||e[io]){var t=e.tag;if(t===5||t===6||t===13||t===31||t===26||t===27||t===3)return e}return null}function wo(e){var t=e.tag;if(t===5||t===26||t===27||t===6)return e.stateNode;throw Error(q(33))}function Er(e){var t=e[u_];return t||(t=e[u_]={hoistableStyles:new Map,hoistableScripts:new Map}),t}function Ye(e){e[_l]=!0}function Mv(e){e[$u]=void 0}var Ev=new Set,Tv={};function zs(e,t){Br(e,t),Br(e+"Capture",t)}function Br(e,t){for(Tv[e]=t,e=0;e<t.length;e++)Ev.add(t[e])}var BM=RegExp("^[:A-Z_a-z\\u00C0-\\u00D6\\u00D8-\\u00F6\\u00F8-\\u02FF\\u0370-\\u037D\\u037F-\\u1FFF\\u200C-\\u200D\\u2070-\\u218F\\u2C00-\\u2FEF\\u3001-\\uD7FF\\uF900-\\uFDCF\\uFDF0-\\uFFFD][:A-Z_a-z\\u00C0-\\u00D6\\u00D8-\\u00F6\\u00F8-\\u02FF\\u0370-\\u037D\\u037F-\\u1FFF\\u200C-\\u200D\\u2070-\\u218F\\u2C00-\\u2FEF\\u3001-\\uD7FF\\uF900-\\uFDCF\\uFDF0-\\uFFFD\\-.0-9\\u00B7\\u0300-\\u036F\\u203F-\\u2040]*$"),c_={},f_={};function FM(e){return Oh.call(f_,e)?!0:Oh.call(c_,e)?!1:BM.test(e)?f_[e]=!0:(c_[e]=!0,!1)}var Qt=!1;function h_(){var e=Qt;return Qt=!1,e}function Mu(e,t,n){if(FM(t))if(n===null)e.removeAttribute(t);else{switch(typeof n){case"undefined":case"function":case"symbol":e.removeAttribute(t);return;case"boolean":var i=t.toLowerCase().slice(0,5);if(i!=="data-"&&i!=="aria-"){e.removeAttribute(t);return}}e.setAttribute(t,n)}}function zl(e,t,n){if(n===null)e.removeAttribute(t);else{switch(typeof n){case"undefined":case"function":case"symbol":case"boolean":e.removeAttribute(t);return}e.setAttribute(t,n)}}function Bi(e,t,n,i){if(i===null)e.removeAttribute(n);else{switch(typeof i){case"undefined":case"function":case"symbol":case"boolean":e.removeAttribute(n);return}e.setAttributeNS(t,n,i)}}function In(e){switch(typeof e){case"bigint":case"boolean":case"number":case"string":case"undefined":return e;case"object":return e;default:return""}}function bv(e){var t=e.type;return(e=e.nodeName)&&e.toLowerCase()==="input"&&(t==="checkbox"||t==="radio")}function HM(e,t,n){var i=Object.getOwnPropertyDescriptor(e.constructor.prototype,t);if(!e.hasOwnProperty(t)&&typeof i<"u"&&typeof i.get=="function"&&typeof i.set=="function"){var a=i.get,s=i.set;return Object.defineProperty(e,t,{configurable:!0,get:function(){return a.call(this)},set:function(r){n=""+r,s.call(this,r)}}),Object.defineProperty(e,t,{enumerable:i.enumerable}),{getValue:function(){return n},setValue:function(r){n=""+r},stopTracking:function(){e._valueTracker=null,delete e[t]}}}}function Ph(e){if(!e._valueTracker){var t=bv(e)?"checked":"value";e._valueTracker=HM(e,t,""+e[t])}}function Av(e){if(!e)return!1;var t=e._valueTracker;if(!t)return!0;var n=t.getValue(),i="";return e&&(i=bv(e)?e.checked?"true":"false":e.value),e=i,e!==n?(t.setValue(e),!0):!1}var GM=/[\n"\\]/g;function ti(e){return e.replace(GM,function(t){return"\\"+t.charCodeAt(0).toString(16)+" "})}function zh(e,t,n,i,a,s,r,o){e.name="",r!=null&&typeof r!="function"&&typeof r!="symbol"&&typeof r!="boolean"?e.type=r:e.removeAttribute("type"),t!=null?r==="number"?(t===0&&e.value===""||e.value!=t)&&(e.value=""+In(t)):e.value!==""+In(t)&&(e.value=""+In(t)):r!=="submit"&&r!=="reset"||e.removeAttribute("value"),t!=null?r==="number"&&e.value==t?mf(e,In(e.value)):mf(e,In(t)):n!=null?mf(e,In(n)):i!=null&&e.removeAttribute("value"),a==null&&s!=null&&(e.defaultChecked=!!s),a!=null&&(e.checked=a&&typeof a!="function"&&typeof a!="symbol"),o!=null&&typeof o!="function"&&typeof o!="symbol"&&typeof o!="boolean"?e.name=""+In(o):e.removeAttribute("name")}function Rv(e,t,n,i,a,s,r,o){if(s!=null&&typeof s!="function"&&typeof s!="symbol"&&typeof s!="boolean"&&(e.type=s),t!=null||n!=null){if(!(s!=="submit"&&s!=="reset"||t!=null)){Ph(e);return}n=n!=null?""+In(n):"",t=t!=null?""+In(t):n,o||t===e.value||(e.value=t),e.defaultValue=t}i=i??a,i=typeof i!="function"&&typeof i!="symbol"&&!!i,e.checked=o?e.checked:!!i,e.defaultChecked=!!i,r!=null&&typeof r!="function"&&typeof r!="symbol"&&typeof r!="boolean"&&(e.name=r),Ph(e)}function mf(e,t){e.defaultValue!==""+t&&(e.defaultValue=""+t)}function Tr(e,t,n,i){if(e=e.options,t){t={};for(var a=0;a<n.length;a++)t["$"+n[a]]=!0;for(n=0;n<e.length;n++)a=t.hasOwnProperty("$"+e[n].value),e[n].selected!==a&&(e[n].selected=a),a&&i&&(e[n].defaultSelected=!0)}else{for(n=""+In(n),t=null,a=0;a<e.length;a++){if(e[a].value===n){e[a].selected=!0,i&&(e[a].defaultSelected=!0);return}t!==null||e[a].disabled||(t=e[a])}t!==null&&(t.selected=!0)}}function Cv(e,t,n){if(t!=null&&(t=""+In(t),t!==e.value&&(e.value=t),n==null)){e.defaultValue!==t&&(e.defaultValue=t);return}e.defaultValue=n!=null?""+In(n):""}function wv(e,t,n,i){if(t==null){if(i!=null){if(n!=null)throw Error(q(92));if(Co(i)){if(1<i.length)throw Error(q(93));i=i[0]}n=i}n==null&&(n=""),t=n}n=In(t),e.defaultValue=n,i=e.textContent,i===n&&i!==""&&i!==null&&(e.value=i),Ph(e)}function Fr(e,t){if(t){var n=e.firstChild;if(n&&n===e.lastChild&&n.nodeType===3){n.nodeValue=t;return}}e.textContent=t}var VM=new Set("animationIterationCount aspectRatio borderImageOutset borderImageSlice borderImageWidth boxFlex boxFlexGroup boxOrdinalGroup columnCount columns flex flexGrow flexPositive flexShrink flexNegative flexOrder gridArea gridRow gridRowEnd gridRowSpan gridRowStart gridColumn gridColumnEnd gridColumnSpan gridColumnStart fontWeight lineClamp lineHeight opacity order orphans scale tabSize widows zIndex zoom fillOpacity floodOpacity stopOpacity strokeDasharray strokeDashoffset strokeMiterlimit strokeOpacity strokeWidth MozAnimationIterationCount MozBoxFlex MozBoxFlexGroup MozLineClamp msAnimationIterationCount msFlex msZoom msFlexGrow msFlexNegative msFlexOrder msFlexPositive msFlexShrink msGridColumn msGridColumnSpan msGridRow msGridRowSpan WebkitAnimationIterationCount WebkitBoxFlex WebKitBoxFlexGroup WebkitBoxOrdinalGroup WebkitColumnCount WebkitColumns WebkitFlex WebkitFlexGrow WebkitFlexPositive WebkitFlexShrink WebkitLineClamp".split(" "));function d_(e,t,n){var i=t.indexOf("--")===0;n==null||typeof n=="boolean"||n===""?i?e.setProperty(t,""):t==="float"?e.cssFloat="":e[t]="":i?e.setProperty(t,n):typeof n!="number"||n===0||VM.has(t)?t==="float"?e.cssFloat=n:e[t]=(""+n).trim():e[t]=n+"px"}function Dv(e,t,n){if(t!=null&&typeof t!="object")throw Error(q(62));if(e=e.style,n!=null){for(var i in n)!n.hasOwnProperty(i)||t!=null&&t.hasOwnProperty(i)||(i.indexOf("--")===0?e.setProperty(i,""):i==="float"?e.cssFloat="":e[i]="",Qt=!0);for(var a in t)i=t[a],t.hasOwnProperty(a)&&n[a]!==i&&(d_(e,a,i),Qt=!0)}else for(var s in t)t.hasOwnProperty(s)&&d_(e,s,t[s])}function Np(e){if(e.indexOf("-")===-1)return!1;switch(e){case"annotation-xml":case"color-profile":case"font-face":case"font-face-src":case"font-face-uri":case"font-face-format":case"font-face-name":case"missing-glyph":return!1;default:return!0}}var XM=new Map([["acceptCharset","accept-charset"],["htmlFor","for"],["httpEquiv","http-equiv"],["crossOrigin","crossorigin"],["accentHeight","accent-height"],["alignmentBaseline","alignment-baseline"],["arabicForm","arabic-form"],["baselineShift","baseline-shift"],["capHeight","cap-height"],["clipPath","clip-path"],["clipRule","clip-rule"],["colorInterpolation","color-interpolation"],["colorInterpolationFilters","color-interpolation-filters"],["colorProfile","color-profile"],["colorRendering","color-rendering"],["dominantBaseline","dominant-baseline"],["enableBackground","enable-background"],["fillOpacity","fill-opacity"],["fillRule","fill-rule"],["floodColor","flood-color"],["floodOpacity","flood-opacity"],["fontFamily","font-family"],["fontSize","font-size"],["fontSizeAdjust","font-size-adjust"],["fontStretch","font-stretch"],["fontStyle","font-style"],["fontVariant","font-variant"],["fontWeight","font-weight"],["glyphName","glyph-name"],["glyphOrientationHorizontal","glyph-orientation-horizontal"],["glyphOrientationVertical","glyph-orientation-vertical"],["horizAdvX","horiz-adv-x"],["horizOriginX","horiz-origin-x"],["imageRendering","image-rendering"],["letterSpacing","letter-spacing"],["lightingColor","lighting-color"],["markerEnd","marker-end"],["markerMid","marker-mid"],["markerStart","marker-start"],["maskType","mask-type"],["overlinePosition","overline-position"],["overlineThickness","overline-thickness"],["paintOrder","paint-order"],["panose-1","panose-1"],["pointerEvents","pointer-events"],["renderingIntent","rendering-intent"],["shapeRendering","shape-rendering"],["stopColor","stop-color"],["stopOpacity","stop-opacity"],["strikethroughPosition","strikethrough-position"],["strikethroughThickness","strikethrough-thickness"],["strokeDasharray","stroke-dasharray"],["strokeDashoffset","stroke-dashoffset"],["strokeLinecap","stroke-linecap"],["strokeLinejoin","stroke-linejoin"],["strokeMiterlimit","stroke-miterlimit"],["strokeOpacity","stroke-opacity"],["strokeWidth","stroke-width"],["textAnchor","text-anchor"],["textDecoration","text-decoration"],["textRendering","text-rendering"],["transformOrigin","transform-origin"],["underlinePosition","underline-position"],["underlineThickness","underline-thickness"],["unicodeBidi","unicode-bidi"],["unicodeRange","unicode-range"],["unitsPerEm","units-per-em"],["vAlphabetic","v-alphabetic"],["vHanging","v-hanging"],["vIdeographic","v-ideographic"],["vMathematical","v-mathematical"],["vectorEffect","vector-effect"],["vertAdvY","vert-adv-y"],["vertOriginX","vert-origin-x"],["vertOriginY","vert-origin-y"],["wordSpacing","word-spacing"],["writingMode","writing-mode"],["xmlnsXlink","xmlns:xlink"],["xHeight","x-height"]]),kM=/^[\u0000-\u001F ]*j[\r\n\t]*a[\r\n\t]*v[\r\n\t]*a[\r\n\t]*s[\r\n\t]*c[\r\n\t]*r[\r\n\t]*i[\r\n\t]*p[\r\n\t]*t[\r\n\t]*:/i;function Eu(e){return kM.test(""+e)?"javascript:throw new Error('React has blocked a javascript: URL as a security precaution.')":e}function wi(){}var Ih=null;function Lp(e){return e=e.target||e.srcElement||window,e.correspondingUseElement&&(e=e.correspondingUseElement),e.nodeType===3?e.parentNode:e}var hr=null,br=null;function p_(e){var t=ao(e);if(t&&(e=t.stateNode)){var n=e[Cn]||null;t:switch(e=t.stateNode,t.type){case"input":if(zh(e,n.value,n.defaultValue,n.defaultValue,n.checked,n.defaultChecked,n.type,n.name),t=n.name,n.type==="radio"&&t!=null){for(n=e;n.parentNode;)n=n.parentNode;for(n=n.querySelectorAll('input[name="'+ti(""+t)+'"][type="radio"]'),t=0;t<n.length;t++){var i=n[t];if(i!==e&&i.form===e.form){var a=i[Cn]||null;if(!a)throw Error(q(90));zh(i,a.value,a.defaultValue,a.defaultValue,a.checked,a.defaultChecked,a.type,a.name)}}for(t=0;t<n.length;t++)i=n[t],i.form===e.form&&Av(i)}break t;case"textarea":Cv(e,n.value,n.defaultValue);break t;case"select":t=n.value,t!=null&&Tr(e,!!n.multiple,t,!1)}}}var _f=!1;function Uv(e,t,n){if(_f)return e(t,n);_f=!0;try{var i=e(t);return i}finally{if(_f=!1,(hr!==null||br!==null)&&(Zc(),hr&&(t=hr,e=br,br=hr=null,p_(t),e)))for(t=0;t<e.length;t++)p_(e[t])}}function Ko(e,t){var n=e.stateNode;if(n===null)return null;var i=n[Cn]||null;if(i===null)return null;n=i[t];t:switch(t){case"onClick":case"onClickCapture":case"onDoubleClick":case"onDoubleClickCapture":case"onMouseDown":case"onMouseDownCapture":case"onMouseMove":case"onMouseMoveCapture":case"onMouseUp":case"onMouseUpCapture":case"onMouseEnter":(i=!i.disabled)||(e=e.type,i=!(e==="button"||e==="input"||e==="select"||e==="textarea")),e=!i;break t;default:e=!1}if(e)return null;if(n&&typeof n!="function")throw Error(q(231,t,typeof n));return n}var Ji=!(typeof window>"u"||typeof window.document>"u"||typeof window.document.createElement>"u"),Bh=!1;if(Ji)try{var po={};Object.defineProperty(po,"passive",{get:function(){Bh=!0}}),window.addEventListener("test",po,po),window.removeEventListener("test",po,po)}catch{Bh=!1}var Aa=null,Op=null,Tu=null;function Nv(){if(Tu)return Tu;var e,t=Op,n=t.length,i,a="value"in Aa?Aa.value:Aa.textContent,s=a.length;for(e=0;e<n&&t[e]===a[e];e++);var r=n-e;for(i=1;i<=r&&t[n-i]===a[s-i];i++);return Tu=a.slice(e,1<i?1-i:void 0)}function bu(e){var t=e.keyCode;return"charCode"in e?(e=e.charCode,e===0&&t===13&&(e=13)):e=t,e===10&&(e=13),32<=e||e===13?e:0}function Il(){return!0}function m_(){return!1}function pn(e){function t(n,i,a,s,r){this._reactName=n,this._targetInst=a,this.type=i,this.nativeEvent=s,this.target=r,this.currentTarget=null;for(var o in e)e.hasOwnProperty(o)&&(n=e[o],this[o]=n?n(s):s[o]);return this.isDefaultPrevented=(s.defaultPrevented!=null?s.defaultPrevented:s.returnValue===!1)?Il:m_,this.isPropagationStopped=m_,this}return de(t.prototype,{preventDefault:function(){this.defaultPrevented=!0;var n=this.nativeEvent;n&&(n.preventDefault?n.preventDefault():typeof n.returnValue!="unknown"&&(n.returnValue=!1),this.isDefaultPrevented=Il)},stopPropagation:function(){var n=this.nativeEvent;n&&(n.stopPropagation?n.stopPropagation():typeof n.cancelBubble!="unknown"&&(n.cancelBubble=!0),this.isPropagationStopped=Il)},persist:function(){},isPersistent:Il}),t}var Ka={eventPhase:0,bubbles:0,cancelable:0,timeStamp:function(e){return e.timeStamp||Date.now()},defaultPrevented:0,isTrusted:0},zc=pn(Ka),gl=de({},Ka,{view:0,detail:0}),YM=pn(gl),gf,vf,mo,Ic=de({},gl,{screenX:0,screenY:0,clientX:0,clientY:0,pageX:0,pageY:0,ctrlKey:0,shiftKey:0,altKey:0,metaKey:0,getModifierState:Pp,button:0,buttons:0,relatedTarget:function(e){return e.relatedTarget===void 0?e.fromElement===e.srcElement?e.toElement:e.fromElement:e.relatedTarget},movementX:function(e){return"movementX"in e?e.movementX:(e!==mo&&(mo&&e.type==="mousemove"?(gf=e.screenX-mo.screenX,vf=e.screenY-mo.screenY):vf=gf=0,mo=e),gf)},movementY:function(e){return"movementY"in e?e.movementY:vf}}),__=pn(Ic),qM=de({},Ic,{dataTransfer:0}),WM=pn(qM),jM=de({},gl,{relatedTarget:0}),Sf=pn(jM),ZM=de({},Ka,{animationName:0,elapsedTime:0,pseudoElement:0}),KM=pn(ZM),QM=de({},Ka,{clipboardData:function(e){return"clipboardData"in e?e.clipboardData:window.clipboardData}}),JM=pn(QM),$M=de({},Ka,{data:0}),g_=pn($M),tE={Esc:"Escape",Spacebar:" ",Left:"ArrowLeft",Up:"ArrowUp",Right:"ArrowRight",Down:"ArrowDown",Del:"Delete",Win:"OS",Menu:"ContextMenu",Apps:"ContextMenu",Scroll:"ScrollLock",MozPrintableKey:"Unidentified"},eE={8:"Backspace",9:"Tab",12:"Clear",13:"Enter",16:"Shift",17:"Control",18:"Alt",19:"Pause",20:"CapsLock",27:"Escape",32:" ",33:"PageUp",34:"PageDown",35:"End",36:"Home",37:"ArrowLeft",38:"ArrowUp",39:"ArrowRight",40:"ArrowDown",45:"Insert",46:"Delete",112:"F1",113:"F2",114:"F3",115:"F4",116:"F5",117:"F6",118:"F7",119:"F8",120:"F9",121:"F10",122:"F11",123:"F12",144:"NumLock",145:"ScrollLock",224:"Meta"},nE={Alt:"altKey",Control:"ctrlKey",Meta:"metaKey",Shift:"shiftKey"};function iE(e){var t=this.nativeEvent;return t.getModifierState?t.getModifierState(e):(e=nE[e])?!!t[e]:!1}function Pp(){return iE}var aE=de({},gl,{key:function(e){if(e.key){var t=tE[e.key]||e.key;if(t!=="Unidentified")return t}return e.type==="keypress"?(e=bu(e),e===13?"Enter":String.fromCharCode(e)):e.type==="keydown"||e.type==="keyup"?eE[e.keyCode]||"Unidentified":""},code:0,location:0,ctrlKey:0,shiftKey:0,altKey:0,metaKey:0,repeat:0,locale:0,getModifierState:Pp,charCode:function(e){return e.type==="keypress"?bu(e):0},keyCode:function(e){return e.type==="keydown"||e.type==="keyup"?e.keyCode:0},which:function(e){return e.type==="keypress"?bu(e):e.type==="keydown"||e.type==="keyup"?e.keyCode:0}}),sE=pn(aE),rE=de({},Ic,{pointerId:0,width:0,height:0,pressure:0,tangentialPressure:0,tiltX:0,tiltY:0,twist:0,pointerType:0,isPrimary:0}),v_=pn(rE),oE=de({},Ka,{submitter:0}),lE=pn(oE),uE=de({},gl,{touches:0,targetTouches:0,changedTouches:0,altKey:0,metaKey:0,ctrlKey:0,shiftKey:0,getModifierState:Pp}),cE=pn(uE),fE=de({},Ka,{propertyName:0,elapsedTime:0,pseudoElement:0}),hE=pn(fE),dE=de({},Ic,{deltaX:function(e){return"deltaX"in e?e.deltaX:"wheelDeltaX"in e?-e.wheelDeltaX:0},deltaY:function(e){return"deltaY"in e?e.deltaY:"wheelDeltaY"in e?-e.wheelDeltaY:"wheelDelta"in e?-e.wheelDelta:0},deltaZ:0,deltaMode:0}),pE=pn(dE),mE=de({},Ka,{newState:0,oldState:0,source:0}),_E=pn(mE),gE=[9,13,27,32],zp=Ji&&"CompositionEvent"in window,zo=null;Ji&&"documentMode"in document&&(zo=document.documentMode);var vE=Ji&&"TextEvent"in window&&!zo,Lv=Ji&&(!zp||zo&&8<zo&&11>=zo),S_=" ",y_=!1;function Ov(e,t){switch(e){case"keyup":return gE.indexOf(t.keyCode)!==-1;case"keydown":return t.keyCode!==229;case"keypress":case"mousedown":case"focusout":return!0;default:return!1}}function Pv(e){return e=e.detail,typeof e=="object"&&"data"in e?e.data:null}var dr=!1;function SE(e,t){switch(e){case"compositionend":return Pv(t);case"keypress":return t.which!==32?null:(y_=!0,S_);case"textInput":return e=t.data,e===S_&&y_?null:e;default:return null}}function yE(e,t){if(dr)return e==="compositionend"||!zp&&Ov(e,t)?(e=Nv(),Tu=Op=Aa=null,dr=!1,e):null;switch(e){case"paste":return null;case"keypress":if(!(t.ctrlKey||t.altKey||t.metaKey)||t.ctrlKey&&t.altKey){if(t.char&&1<t.char.length)return t.char;if(t.which)return String.fromCharCode(t.which)}return null;case"compositionend":return Lv&&t.locale!=="ko"?null:t.data;default:return null}}var xE={color:!0,date:!0,datetime:!0,"datetime-local":!0,email:!0,month:!0,number:!0,password:!0,range:!0,search:!0,tel:!0,text:!0,time:!0,url:!0,week:!0};function x_(e){var t=e&&e.nodeName&&e.nodeName.toLowerCase();return t==="input"?!!xE[e.type]:t==="textarea"}function zv(e,t,n,i){hr?br?br.push(i):br=[i]:hr=i,t=xc(t,"onChange"),0<t.length&&(n=new zc("onChange","change",null,n,i),e.push({event:n,listeners:t}))}var Io=null,Qo=null;function ME(e){Uy(e,0)}function Bc(e){var t=wo(e);if(Av(t))return e}function M_(e,t){if(e==="change")return t}var Iv=!1;if(Ji){var yf;if(Ji){var xf="oninput"in document;if(!xf){var E_=document.createElement("div");E_.setAttribute("oninput","return;"),xf=typeof E_.oninput=="function"}yf=xf}else yf=!1;Iv=yf&&(!document.documentMode||9<document.documentMode)}function T_(){Io&&(Io.detachEvent("onpropertychange",Bv),Qo=Io=null)}function Bv(e){if(e.propertyName==="value"&&Bc(Qo)){var t=[];zv(t,Qo,e,Lp(e)),Uv(ME,t)}}function EE(e,t,n){e==="focusin"?(T_(),Io=t,Qo=n,Io.attachEvent("onpropertychange",Bv)):e==="focusout"&&T_()}function TE(e){if(e==="selectionchange"||e==="keyup"||e==="keydown")return Bc(Qo)}function bE(e,t){if(e==="click")return Bc(t)}function AE(e,t){if(e==="input"||e==="change")return Bc(t)}function RE(e,t){return e===t&&(e!==0||1/e===1/t)||e!==e&&t!==t}var Yn=typeof Object.is=="function"?Object.is:RE;function Jo(e,t){if(Yn(e,t))return!0;if(typeof e!="object"||e===null||typeof t!="object"||t===null)return!1;var n=Object.keys(e),i=Object.keys(t);if(n.length!==i.length)return!1;for(i=0;i<n.length;i++){var a=n[i];if(!Oh.call(t,a)||!Yn(e[a],t[a]))return!1}return!0}function Fh(e){if(e=e||(typeof document<"u"?document:void 0),typeof e>"u")return null;try{return e.activeElement||e.body}catch{return e.body}}function b_(e){for(;e&&e.firstChild;)e=e.firstChild;return e}function A_(e,t){var n=b_(e);e=0;for(var i;n;){if(n.nodeType===3){if(i=e+n.textContent.length,e<=t&&i>=t)return{node:n,offset:t-e};e=i}t:{for(;n;){if(n.nextSibling){n=n.nextSibling;break t}n=n.parentNode}n=void 0}n=b_(n)}}function Fv(e,t){return e&&t?e===t?!0:e&&e.nodeType===3?!1:t&&t.nodeType===3?Fv(e,t.parentNode):"contains"in e?e.contains(t):e.compareDocumentPosition?!!(e.compareDocumentPosition(t)&16):!1:!1}function Hv(e){e=e!=null&&e.ownerDocument!=null&&e.ownerDocument.defaultView!=null?e.ownerDocument.defaultView:window;for(var t=Fh(e.document);t instanceof e.HTMLIFrameElement;){try{var n=typeof t.contentWindow.location.href=="string"}catch{n=!1}if(n)e=t.contentWindow;else break;t=Fh(e.document)}return t}function Ip(e){var t=e&&e.nodeName&&e.nodeName.toLowerCase();return t&&(t==="input"&&(e.type==="text"||e.type==="search"||e.type==="tel"||e.type==="url"||e.type==="password")||t==="textarea"||e.contentEditable==="true")}var CE=Ji&&"documentMode"in document&&11>=document.documentMode,pr=null,Hh=null,Bo=null,Gh=!1;function R_(e,t,n){var i=n.window===n?n.document:n.nodeType===9?n:n.ownerDocument;Gh||pr==null||pr!==Fh(i)||(i=pr,"selectionStart"in i&&Ip(i)?i={start:i.selectionStart,end:i.selectionEnd}:(i=(i.ownerDocument&&i.ownerDocument.defaultView||window).getSelection(),i={anchorNode:i.anchorNode,anchorOffset:i.anchorOffset,focusNode:i.focusNode,focusOffset:i.focusOffset}),Bo&&Jo(Bo,i)||(Bo=i,i=xc(Hh,"onSelect"),0<i.length&&(t=new zc("onSelect","select",null,t,n),e.push({event:t,listeners:i}),t.target=pr)))}function ts(e,t){var n={};return n[e.toLowerCase()]=t.toLowerCase(),n["Webkit"+e]="webkit"+t,n["Moz"+e]="moz"+t,n}var mr={animationend:ts("Animation","AnimationEnd"),animationiteration:ts("Animation","AnimationIteration"),animationstart:ts("Animation","AnimationStart"),transitionrun:ts("Transition","TransitionRun"),transitionstart:ts("Transition","TransitionStart"),transitioncancel:ts("Transition","TransitionCancel"),transitionend:ts("Transition","TransitionEnd")},Mf={},Gv={};Ji&&(Gv=document.createElement("div").style,"AnimationEvent"in window||(delete mr.animationend.animation,delete mr.animationiteration.animation,delete mr.animationstart.animation),"TransitionEvent"in window||delete mr.transitionend.transition);function Is(e){if(Mf[e])return Mf[e];if(!mr[e])return e;var t=mr[e],n;for(n in t)if(t.hasOwnProperty(n)&&n in Gv)return Mf[e]=t[n];return e}var Vv=Is("animationend"),Xv=Is("animationiteration"),kv=Is("animationstart"),wE=Is("transitionrun"),DE=Is("transitionstart"),UE=Is("transitioncancel"),Yv=Is("transitionend"),qv=new Map,Vh="abort auxClick beforeToggle cancel canPlay canPlayThrough click close contextMenu copy cut drag dragEnd dragEnter dragExit dragLeave dragOver dragStart drop durationChange emptied encrypted ended error fullscreenChange fullscreenError gotPointerCapture input invalid keyDown keyPress keyUp load loadedData loadedMetadata loadStart lostPointerCapture mouseDown mouseMove mouseOut mouseOver mouseUp paste pause play playing pointerCancel pointerDown pointerMove pointerOut pointerOver pointerUp progress rateChange reset resize seeked seeking stalled submit suspend timeUpdate touchCancel touchEnd touchStart volumeChange scroll toggle touchMove waiting wheel".split(" ");Vh.push("scrollEnd");function yi(e,t){qv.set(e,t),zs(t,[e])}var NE=0;function $i(e,t){if(e.name!=null&&e.name!=="auto")return e.name;if(t.autoName!==null)return t.autoName;e=Si.identifierPrefix;var n=NE++;return e="_"+e+"t_"+n.toString(32)+"_",t.autoName=e}function C_(e){if(e==null||typeof e=="string")return e;var t=null,n=Nr;if(n!==null)for(var i=0;i<n.length;i++){var a=e[n[i]];if(a!=null){if(a==="none")return"none";t=t==null?a:t+(" "+a)}}return t??e.default}function oa(e,t){return e=C_(e),t=C_(t),t==null?e==="auto"?null:e:t==="auto"?null:t}var tc=typeof reportError=="function"?reportError:function(e){if(typeof window=="object"&&typeof window.ErrorEvent=="function"){var t=new window.ErrorEvent("error",{bubbles:!0,cancelable:!0,message:typeof e=="object"&&e!==null&&typeof e.message=="string"?String(e.message):String(e),error:e});if(!window.dispatchEvent(t))return}else if(typeof process=="object"&&typeof process.emit=="function"){process.emit("uncaughtException",e);return}console.error(e)},Kn=[],_r=0,Bp=0;function Fc(){for(var e=_r,t=Bp=_r=0;t<e;){var n=Kn[t];Kn[t++]=null;var i=Kn[t];Kn[t++]=null;var a=Kn[t];Kn[t++]=null;var s=Kn[t];if(Kn[t++]=null,i!==null&&a!==null){var r=i.pending;r===null?a.next=a:(a.next=r.next,r.next=a),i.pending=a}s!==0&&Wv(n,a,s)}}function Hc(e,t,n,i){Kn[_r++]=e,Kn[_r++]=t,Kn[_r++]=n,Kn[_r++]=i,Bp|=i,e.lanes|=i,e=e.alternate,e!==null&&(e.lanes|=i)}function Fp(e,t,n,i){return Hc(e,t,n,i),ec(e)}function Bs(e,t){return Hc(e,null,null,t),ec(e)}function Wv(e,t,n){e.lanes|=n;var i=e.alternate;i!==null&&(i.lanes|=n);for(var a=!1,s=e.return;s!==null;)s.childLanes|=n,i=s.alternate,i!==null&&(i.childLanes|=n),s.tag===22&&(e=s.stateNode,e===null||e._visibility&1||(a=!0)),e=s,s=s.return;return e.tag===3?(s=e.stateNode,a&&t!==null&&(a=31-Xn(n),e=s.hiddenUpdates,i=e[a],i===null?e[a]=[t]:i.push(t),t.lane=n|536870912),s):null}function ec(e){if(50<jo)throw jo=0,Pu=null,Error(q(185));for(var t=e.return;t!==null;)e=t,t=e.return;return e.tag===3?e.stateNode:null}var gr={};function LE(e,t,n,i){this.tag=e,this.key=n,this.sibling=this.child=this.return=this.stateNode=this.type=this.elementType=null,this.index=0,this.refCleanup=this.ref=null,this.pendingProps=t,this.dependencies=this.memoizedState=this.updateQueue=this.memoizedProps=null,this.mode=i,this.subtreeFlags=this.flags=0,this.deletions=null,this.childLanes=this.lanes=0,this.alternate=null}function Mn(e,t,n,i){return new LE(e,t,n,i)}function Hp(e){return e=e.prototype,!(!e||!e.isReactComponent)}function Ki(e,t){var n=e.alternate;return n===null?(n=Mn(e.tag,t,e.key,e.mode),n.elementType=e.elementType,n.type=e.type,n.stateNode=e.stateNode,n.alternate=e,e.alternate=n):(n.pendingProps=t,n.type=e.type,n.flags=0,n.subtreeFlags=0,n.deletions=null),n.flags=e.flags&1206910976,n.childLanes=e.childLanes,n.lanes=e.lanes,n.child=e.child,n.memoizedProps=e.memoizedProps,n.memoizedState=e.memoizedState,n.updateQueue=e.updateQueue,t=e.dependencies,n.dependencies=t===null?null:{lanes:t.lanes,firstContext:t.firstContext},n.sibling=e.sibling,n.index=e.index,n.ref=e.ref,n.refCleanup=e.refCleanup,n}function jv(e,t){e.flags&=1206910978;var n=e.alternate;return n===null?(e.childLanes=0,e.lanes=t,e.child=null,e.subtreeFlags=0,e.memoizedProps=null,e.memoizedState=null,e.updateQueue=null,e.dependencies=null,e.stateNode=null):(e.childLanes=n.childLanes,e.lanes=n.lanes,e.child=n.child,e.subtreeFlags=0,e.deletions=null,e.memoizedProps=n.memoizedProps,e.memoizedState=n.memoizedState,e.updateQueue=n.updateQueue,e.type=n.type,t=n.dependencies,e.dependencies=t===null?null:{lanes:t.lanes,firstContext:t.firstContext}),e}function Au(e,t,n,i,a,s){var r=0;if(i=e,typeof i=="function")Hp(i)&&(r=1);else if(typeof i=="string")r=ob(e,n,Ni.current)?26:e==="html"||e==="head"||e==="body"?27:5;else t:switch(i){case wh:return e=Mn(31,n,t,a),e.elementType=wh,e.lanes=s,e;case cr:return Ss(n.children,a,s,t);case fv:r=8,a|=24;break;case Ah:return e=Mn(12,n,t,a|2),e.elementType=Ah,e.lanes=s,e;case Rh:return e=Mn(13,n,t,a),e.elementType=Rh,e.lanes=s,e;case Ch:return e=Mn(19,n,t,a),e.elementType=Ch,e.lanes=s,e;case yM:case Dh:return e=a|32,e=Mn(30,n,t,e),e.elementType=Dh,e.lanes=s,e.stateNode={autoName:null,paired:null,clones:null,ref:null},e;default:if(typeof i=="object"&&i!==null)switch(i.$$typeof){case Ci:r=10;break t;case hv:r=9;break t;case Rp:r=11;break t;case Cp:r=14;break t;case ya:r=16,i=null;break t}r=29,n=Error(q(130,e===null?"null":typeof e,"")),i=null}return t=Mn(r,n,t,a),t.elementType=e,t.type=i,t.lanes=s,t}function Ss(e,t,n,i){return e=Mn(7,e,i,t),e.lanes=n,e}function Ef(e,t,n){return e=Mn(6,e,null,t),e.lanes=n,e}function Zv(e){var t=Mn(18,null,null,0);return t.stateNode=e,t}function Tf(e,t,n){return t=Mn(4,e.children!==null?e.children:[],e.key,t),t.lanes=n,t.stateNode={containerInfo:e.containerInfo,pendingChildren:null,implementation:e.implementation},t}var w_=new WeakMap;function ei(e,t){if(typeof e=="object"&&e!==null){var n=w_.get(e);return n!==void 0?n:(t={value:e,source:t,stack:r_(t)},w_.set(e,t),t)}return{value:e,source:t,stack:r_(t)}}var vr=[],Sr=0,nc=null,$o=0,Qn=[],Jn=0,Xa=null,Di=1,Ui="";function qi(e,t){vr[Sr++]=$o,vr[Sr++]=nc,nc=e,$o=t}function Kv(e,t,n){Qn[Jn++]=Di,Qn[Jn++]=Ui,Qn[Jn++]=Xa,Xa=e;var i=Di;e=Ui;var a=32-Xn(i)-1;i&=~(1<<a),n+=1;var s=32-Xn(t)+a;if(30<s){var r=a-a%5;s=(i&(1<<r)-1).toString(32),i>>=r,a-=r,Di=1<<32-Xn(t)+a|n<<a|i,Ui=s+e}else Di=1<<s|n<<a|i,Ui=e}function Gc(e){e.return!==null&&(qi(e,1),Kv(e,1,0))}function Gp(e){for(;e===nc;)nc=vr[--Sr],vr[Sr]=null,$o=vr[--Sr],vr[Sr]=null;for(;e===Xa;)Xa=Qn[--Jn],Qn[Jn]=null,Ui=Qn[--Jn],Qn[Jn]=null,Di=Qn[--Jn],Qn[Jn]=null}function Qv(e,t){Qn[Jn++]=Di,Qn[Jn++]=Ui,Qn[Jn++]=Xa,Di=t.id,Ui=t.overflow,Xa=e}var qe=null,_e=null,zt=!1,Na=null,ni=!1,Xh=Error(q(519));function ka(e){var t=Error(q(418,1<arguments.length&&arguments[1]!==void 0&&arguments[1]?"text":"HTML",""));throw tl(ei(t,e)),Xh}function D_(e){var t=e.stateNode,n=e.type,i=e.memoizedProps;switch(t[Ke]=e,t[Cn]=i,n){case"dialog":It("cancel",t),It("close",t);break;case"iframe":case"object":case"embed":It("load",t);break;case"video":case"audio":for(n=0;n<al.length;n++)It(al[n],t);break;case"source":It("error",t);break;case"img":case"image":case"link":It("error",t),It("load",t);break;case"details":It("toggle",t);break;case"input":It("invalid",t),Rv(t,i.value,i.defaultValue,i.checked,i.defaultChecked,i.type,i.name,!0);break;case"select":It("invalid",t);break;case"textarea":It("invalid",t),wv(t,i.value,i.defaultValue,i.children)}n=i.children,typeof n!="string"&&typeof n!="number"&&typeof n!="bigint"||t.textContent===""+n||i.suppressHydrationWarning===!0||Ly(t.textContent,n)?(i.popover!=null&&(It("beforetoggle",t),It("toggle",t)),i.onScroll!=null&&It("scroll",t),i.onScrollEnd!=null&&It("scrollend",t),i.onClick!=null&&(t.onclick=wi),t=!0):t=!1,t||ka(e,!0)}function ic(e){for(qe=e.return;qe;)switch(qe.tag){case 5:case 31:case 13:ni=!1;return;case 27:case 3:ni=!0;return;default:qe=qe.return}}function Vs(e){if(e!==qe)return!1;if(!zt)return ic(e),zt=!0,!1;var t=e.tag,n;if((n=t!==3&&t!==27)&&((n=t===5)&&(n=e.type,n=!(n!=="form"&&n!=="button")||Rd(e.type,e.memoizedProps)),n=!n),n&&_e&&ka(e),ic(e),t===13){if(e=e.memoizedState,e=e!==null?e.dehydrated:null,!e)throw Error(q(317));_e=Tg(e)}else if(t===31){if(e=e.memoizedState,e=e!==null?e.dehydrated:null,!e)throw Error(q(317));_e=Tg(e)}else t===27?(t=_e,Qa(e.type)?(e=Ud,Ud=null,_e=e):_e=t):_e=qe?ai(e.stateNode.nextSibling):null;return!0}function Es(){_e=qe=null,zt=!1}function bf(){var e=Na;return e!==null&&(yn===null?yn=e:yn.push.apply(yn,e),Na=null),e}function tl(e){Na===null?Na=[e]:Na.push(e)}var kh=Pi(null),Fs=null,Wi=null;function Ra(e,t,n){ve(kh,t._currentValue),t._currentValue=n}function Qi(e){e._currentValue=kh.current,Je(kh)}function Ru(e,t,n){for(;e!==null;){var i=e.alternate;if((e.childLanes&t)!==t?(e.childLanes|=t,i!==null&&(i.childLanes|=t)):i!==null&&(i.childLanes&t)!==t&&(i.childLanes|=t),e===n)break;e=e.return}}function Yh(e,t,n,i){var a=e.child;for(a!==null&&(a.return=e);a!==null;){var s=a.dependencies;if(s!==null){var r=a.child;s=s.firstContext;t:for(;s!==null;){var o=s;s=a;for(var l=0;l<t.length;l++)if(o.context===t[l]){s.lanes|=n,o=s.alternate,o!==null&&(o.lanes|=n),Ru(s.return,n,e),i||(r=null);break t}s=o.next}}else if(a.tag===18){if(r=a.return,r===null)throw Error(q(341));r.lanes|=n,s=r.alternate,s!==null&&(s.lanes|=n),Ru(r,n,e),r=null}else a.tag===13&&a.memoizedState!==null&&a.memoizedState.dehydrated===null?(a.lanes|=n,r=a.alternate,r!==null&&(r.lanes|=n),Ru(a.return,n,e),r=a.child,r=r!==null?r.sibling:null):r=a.child;if(r!==null)r.return=a;else for(r=a;r!==null;){if(r===e){r=null;break}if(a=r.sibling,a!==null){a.return=r.return,r=a;break}r=r.return}a=r}}function Ts(e,t,n,i){e=null;for(var a=t,s=!1;a!==null;){if(!s){if(a.flags&524288)s=!0;else if(a.flags&262144)break}if(a.tag===10){var r=a.alternate;if(r===null)throw Error(q(387));if(r=r.memoizedProps,r!==null){var o=a.type;Yn(a.pendingProps.value,r.value)||(e!==null?e.push(o):e=[o])}}else if(a===Zu.current){if(r=a.alternate,r===null)throw Error(q(387));r.memoizedState.memoizedState!==a.memoizedState.memoizedState&&(e!==null?e.push(Wr):e=[Wr])}a=a.return}return e!==null&&Yh(t,e,n,i),t.flags|=262144,e!==null}function ac(e){for(e=e.firstContext;e!==null;){if(!Yn(e.context._currentValue,e.memoizedValue))return!0;e=e.next}return!1}function bs(e){Fs=e,Wi=null,e=e.dependencies,e!==null&&(e.firstContext=null)}function Qe(e){return Jv(Fs,e)}function Bl(e,t){return Fs===null&&bs(e),Jv(e,t)}function Jv(e,t){var n=t._currentValue;if(t={context:t,memoizedValue:n,next:null},Wi===null){if(e===null)throw Error(q(308));Wi=t,e.dependencies={lanes:0,firstContext:t},e.flags|=524288}else Wi=Wi.next=t;return n}var OE=typeof AbortController<"u"?AbortController:function(){var e=[],t=this.signal={aborted:!1,addEventListener:function(n,i){e.push(i)}};this.abort=function(){t.aborted=!0,e.forEach(function(n){return n()})}},PE=Fe.unstable_scheduleCallback,zE=Fe.unstable_NormalPriority,Oe={$$typeof:Ci,Consumer:null,Provider:null,_currentValue:null,_currentValue2:null,_threadCount:0};function Vp(){return{controller:new OE,data:new Map,refCount:0}}function vl(e){e.refCount--,e.refCount===0&&PE(zE,function(){e.controller.abort()})}function U_(e,t){if(e.pendingLanes&4194048){var n=e.transitionTypes;for(n===null&&(n=e.transitionTypes=[]),e=0;e<t.length;e++){var i=t[e];n.indexOf(i)===-1&&n.push(i)}}}var Do=null;function IE(e){var t=e.transitionTypes;return e.transitionTypes=null,t}var Fo=null,qh=0,As=0,Ar=null;function BE(e,t){if(Fo===null){var n=Fo=[];qh=0,As=_m(),Ar={status:"pending",value:void 0,then:function(i){n.push(i)}}}return qh++,t.then(N_,N_),t}function N_(){if(--qh===0&&(Do=null,Fo!==null)){Ar!==null&&(Ar.status="fulfilled");var e=Fo;Fo=null,As=0,Ar=null;for(var t=0;t<e.length;t++)(0,e[t])()}}function FE(e,t){var n=[],i={status:"pending",value:null,reason:null,then:function(a){n.push(a)}};return e.then(function(){i.status="fulfilled",i.value=t;for(var a=0;a<n.length;a++)(0,n[a])(t)},function(a){for(i.status="rejected",i.reason=a,a=0;a<n.length;a++)(0,n[a])(void 0)}),i}var L_=xt.S;xt.S=function(e,t){if(_y=Gn(),typeof t=="object"&&t!==null&&typeof t.then=="function"&&BE(e,t),Do!==null)for(var n=kr;n!==null;)U_(n,Do),n=n.next;if(n=e.types,n!==null){for(var i=kr;i!==null;)U_(i,n),i=i.next;if(As!==0){i=Do,i===null&&(i=Do=[]);for(var a=0;a<n.length;a++){var s=n[a];i.indexOf(s)===-1&&i.push(s)}}}L_!==null&&L_(e,t)};var ys=Pi(null);function Xp(){var e=ys.current;return e!==null?e:he.pooledCache}function Cu(e,t){t===null?ve(ys,ys.current):ve(ys,t.pool)}function $v(){var e=Xp();return e===null?null:{parent:Oe._currentValue,pool:e}}var so=Error(q(460)),kp=Error(q(474)),Vc=Error(q(542)),sc={then:function(){}};function O_(e){return e=e.status,e==="fulfilled"||e==="rejected"}function tS(e,t,n){switch(n=e[n],n===void 0?e.push(t):n!==t&&(t.then(wi,wi),t=n),t.status){case"fulfilled":return t.value;case"rejected":throw e=t.reason,z_(e),e===void 0&&!("reason"in t)?Error(q(600)):e;default:if(typeof t.status=="string")t.then(wi,wi);else{if(e=he,e!==null&&100<e.shellSuspendCounter)throw Error(q(482));e=t,e.status="pending",e.then(function(i){if(t.status==="pending"){var a=t;a.status="fulfilled",a.value=i}},function(i){if(t.status==="pending"){var a=t;a.status="rejected",a.reason=i}})}switch(t.status){case"fulfilled":return t.value;case"rejected":throw e=t.reason,z_(e),e}throw xs=t,so}}function us(e){try{var t=e._init;return t(e._payload)}catch(n){throw n!==null&&typeof n=="object"&&typeof n.then=="function"?(xs=n,so):n}}var xs=null;function P_(){if(xs===null)throw Error(q(459));var e=xs;return xs=null,e}function z_(e){if(e===so||e===Vc)throw Error(q(483))}var Rr=null,el=0;function Fl(e){var t=el;return el+=1,Rr===null&&(Rr=[]),tS(Rr,e,t)}function fa(e,t){t=t.props.ref,e.ref=t!==void 0?t:null}function Hl(e,t){throw t.$$typeof===SM?Error(q(525)):(e=Object.prototype.toString.call(t),Error(q(31,e==="[object Object]"?"object with keys {"+Object.keys(t).join(", ")+"}":e)))}function eS(e){function t(c,_){if(e){var g=c.deletions;g===null?(c.deletions=[_],c.flags|=16):g.push(_)}}function n(c,_){if(!e)return null;for(;_!==null;)t(c,_),_=_.sibling;return null}function i(c){for(var _=new Map;c!==null;)c.key===null?_.set(c.index,c):_.set(c.key,c),c=c.sibling;return _}function a(c,_){return c=Ki(c,_),c.index=0,c.sibling=null,c}function s(c,_,g){return c.index=g,e?(g=c.alternate,g!==null?(g=g.index,g<_?(c.flags|=2,_):g):(c.flags|=134217730,_)):(c.flags|=1048576,_)}function r(c){return e&&c.alternate===null&&(c.flags|=134217730),c}function o(c,_,g,x){return _===null||_.tag!==6?(_=Ef(g,c.mode,x),_.return=c,_):(_=a(_,g),_.return=c,_)}function l(c,_,g,x){var C=g.type;return C===cr?(c=h(c,_,g.props.children,x,g.key),fa(c,g),c):_!==null&&(_.elementType===C||typeof C=="object"&&C!==null&&C.$$typeof===ya&&us(C)===_.type)?(_=a(_,g.props),fa(_,g),_.return=c,_):(_=Au(g.type,g.key,g.props,null,c.mode,x),fa(_,g),_.return=c,_)}function u(c,_,g,x){return _===null||_.tag!==4||_.stateNode.containerInfo!==g.containerInfo||_.stateNode.implementation!==g.implementation?(_=Tf(g,c.mode,x),_.return=c,_):(_=a(_,g.children||[]),_.return=c,_)}function h(c,_,g,x,C){return _===null||_.tag!==7?(_=Ss(g,c.mode,x,C),_.return=c,_):(_=a(_,g),_.return=c,_)}function p(c,_,g){if(typeof _=="string"&&_!==""||typeof _=="number"||typeof _=="bigint")return _=Ef(""+_,c.mode,g),_.return=c,_;if(typeof _=="object"&&_!==null){switch(_.$$typeof){case Nl:return g=Au(_.type,_.key,_.props,null,c.mode,g),fa(g,_),g.return=c,g;case Ro:return _=Tf(_,c.mode,g),_.return=c,_;case ya:return _=us(_),p(c,_,g)}if(Co(_)||ho(_))return _=Ss(_,c.mode,g,null),_.return=c,_;if(typeof _.then=="function")return p(c,Fl(_),g);if(_.$$typeof===Ci)return p(c,Bl(c,_),g);Hl(c,_)}return null}function f(c,_,g,x){var C=_!==null?_.key:null;if(typeof g=="string"&&g!==""||typeof g=="number"||typeof g=="bigint")return C!==null?null:o(c,_,""+g,x);if(typeof g=="object"&&g!==null){switch(g.$$typeof){case Nl:return g.key===C?l(c,_,g,x):null;case Ro:return g.key===C?u(c,_,g,x):null;case ya:return g=us(g),f(c,_,g,x)}if(Co(g)||ho(g))return C!==null?null:h(c,_,g,x,null);if(typeof g.then=="function")return f(c,_,Fl(g),x);if(g.$$typeof===Ci)return f(c,_,Bl(c,g),x);Hl(c,g)}return null}function d(c,_,g,x,C){if(typeof x=="string"&&x!==""||typeof x=="number"||typeof x=="bigint")return c=c.get(g)||null,o(_,c,""+x,C);if(typeof x=="object"&&x!==null){switch(x.$$typeof){case Nl:return c=c.get(x.key===null?g:x.key)||null,l(_,c,x,C);case Ro:return c=c.get(x.key===null?g:x.key)||null,u(_,c,x,C);case ya:return x=us(x),d(c,_,g,x,C)}if(Co(x)||ho(x))return c=c.get(g)||null,h(_,c,x,C,null);if(typeof x.then=="function")return d(c,_,g,Fl(x),C);if(x.$$typeof===Ci)return d(c,_,g,Bl(_,x),C);Hl(_,x)}return null}function v(c,_,g,x){for(var C=null,R=null,b=_,w=_=0,W=null;b!==null&&w<g.length;w++){b.index>w?(W=b,b=null):W=b.sibling;var S=f(c,b,g[w],x);if(S===null){b===null&&(b=W);break}e&&b&&S.alternate===null&&t(c,b),_=s(S,_,w),R===null?C=S:R.sibling=S,R=S,b=W}if(w===g.length)return n(c,b),zt&&qi(c,w),C;if(b===null){for(;w<g.length;w++)b=p(c,g[w],x),b!==null&&(_=s(b,_,w),R===null?C=b:R.sibling=b,R=b);return zt&&qi(c,w),C}for(b=i(b);w<g.length;w++)W=d(b,c,w,g[w],x),W!==null&&(e&&(S=W.alternate,S!==null&&b.delete(S.key===null?w:S.key)),_=s(W,_,w),R===null?C=W:R.sibling=W,R=W);return e&&b.forEach(function(T){return t(c,T)}),zt&&qi(c,w),C}function y(c,_,g,x){if(g==null)throw Error(q(151));for(var C=null,R=null,b=_,w=_=0,W=null,S=g.next();b!==null&&!S.done;w++,S=g.next()){b.index>w?(W=b,b=null):W=b.sibling;var T=f(c,b,S.value,x);if(T===null){b===null&&(b=W);break}e&&b&&T.alternate===null&&t(c,b),_=s(T,_,w),R===null?C=T:R.sibling=T,R=T,b=W}if(S.done)return n(c,b),zt&&qi(c,w),C;if(b===null){for(;!S.done;w++,S=g.next())S=p(c,S.value,x),S!==null&&(_=s(S,_,w),R===null?C=S:R.sibling=S,R=S);return zt&&qi(c,w),C}for(b=i(b);!S.done;w++,S=g.next())S=d(b,c,w,S.value,x),S!==null&&(e&&(W=S.alternate,W!==null&&b.delete(W.key===null?w:W.key)),_=s(S,_,w),R===null?C=S:R.sibling=S,R=S);return e&&b.forEach(function(F){return t(c,F)}),zt&&qi(c,w),C}function m(c,_,g,x){if(typeof g=="object"&&g!==null&&g.type===cr&&g.key===null&&g.props.ref===void 0&&(g=g.props.children),typeof g=="object"&&g!==null){switch(g.$$typeof){case Nl:t:{for(var C=g.key;_!==null;){if(_.key===C){if(C=g.type,C===cr){if(_.tag===7){n(c,_.sibling),x=a(_,g.props.children),fa(x,g),x.return=c,c=x;break t}}else if(_.elementType===C||typeof C=="object"&&C!==null&&C.$$typeof===ya&&us(C)===_.type){n(c,_.sibling),x=a(_,g.props),fa(x,g),x.return=c,c=x;break t}n(c,_);break}else t(c,_);_=_.sibling}g.type===cr?(x=Ss(g.props.children,c.mode,x,g.key),fa(x,g),x.return=c,c=x):(x=Au(g.type,g.key,g.props,null,c.mode,x),fa(x,g),x.return=c,c=x)}return r(c);case Ro:t:{for(C=g.key;_!==null;){if(_.key===C)if(_.tag===4&&_.stateNode.containerInfo===g.containerInfo&&_.stateNode.implementation===g.implementation){n(c,_.sibling),x=a(_,g.children||[]),x.return=c,c=x;break t}else{n(c,_);break}else t(c,_);_=_.sibling}x=Tf(g,c.mode,x),x.return=c,c=x}return r(c);case ya:return g=us(g),m(c,_,g,x)}if(Co(g))return v(c,_,g,x);if(ho(g)){if(C=ho(g),typeof C!="function")throw Error(q(150));return g=C.call(g),y(c,_,g,x)}if(typeof g.then=="function")return m(c,_,Fl(g),x);if(g.$$typeof===Ci)return m(c,_,Bl(c,g),x);Hl(c,g)}return typeof g=="string"&&g!==""||typeof g=="number"||typeof g=="bigint"?(g=""+g,_!==null&&_.tag===6?(n(c,_.sibling),x=a(_,g),x.return=c,c=x):(n(c,_),x=Ef(g,c.mode,x),x.return=c,c=x),r(c)):n(c,_)}return function(c,_,g,x){try{el=0;var C=m(c,_,g,x);return Rr=null,C}catch(b){if(b===so||b===Vc)throw b;var R=Mn(29,b,null,c.mode);return R.lanes=x,R.return=c,R}finally{}}}var Rs=eS(!0),nS=eS(!1),xa=!1;function Yp(e){e.updateQueue={baseState:e.memoizedState,firstBaseUpdate:null,lastBaseUpdate:null,shared:{pending:null,lanes:0,hiddenCallbacks:null},callbacks:null}}function Wh(e,t){e=e.updateQueue,t.updateQueue===e&&(t.updateQueue={baseState:e.baseState,firstBaseUpdate:e.firstBaseUpdate,lastBaseUpdate:e.lastBaseUpdate,shared:e.shared,callbacks:null})}function La(e){return{lane:e,tag:0,payload:null,callback:null,next:null}}function Oa(e,t,n){var i=e.updateQueue;if(i===null)return null;if(i=i.shared,$t&2){var a=i.pending;return a===null?t.next=t:(t.next=a.next,a.next=t),i.pending=t,t=ec(e),Wv(e,null,n),t}return Hc(e,i,t,n),ec(e)}function Ho(e,t,n){if(t=t.updateQueue,t!==null&&(t=t.shared,(n&4194048)!==0)){var i=t.lanes;i&=e.pendingLanes,n|=i,t.lanes=n,Sv(e,n)}}function Af(e,t){var n=e.updateQueue,i=e.alternate;if(i!==null&&(i=i.updateQueue,n===i)){var a=null,s=null;if(n=n.firstBaseUpdate,n!==null){do{var r={lane:n.lane,tag:n.tag,payload:n.payload,callback:null,next:null};s===null?a=s=r:s=s.next=r,n=n.next}while(n!==null);s===null?a=s=t:s=s.next=t}else a=s=t;n={baseState:i.baseState,firstBaseUpdate:a,lastBaseUpdate:s,shared:i.shared,callbacks:i.callbacks},e.updateQueue=n;return}e=n.lastBaseUpdate,e===null?n.firstBaseUpdate=t:e.next=t,n.lastBaseUpdate=t}var jh=!1;function Go(){if(jh){var e=Ar;if(e!==null)throw e}}function Vo(e,t,n,i){jh=!1;var a=e.updateQueue;xa=!1;var s=a.firstBaseUpdate,r=a.lastBaseUpdate,o=a.shared.pending;if(o!==null){a.shared.pending=null;var l=o,u=l.next;l.next=null,r===null?s=u:r.next=u,r=l;var h=e.alternate;h!==null&&(h=h.updateQueue,o=h.lastBaseUpdate,o!==r&&(o===null?h.firstBaseUpdate=u:o.next=u,h.lastBaseUpdate=l))}if(s!==null){var p=a.baseState;r=0,h=u=l=null,o=s;do{var f=o.lane&-536870913,d=f!==o.lane;if(d?(Gt&f)===f:(i&f)===f){f!==0&&f===As&&(jh=!0),h!==null&&(h=h.next={lane:0,tag:o.tag,payload:o.payload,callback:null,next:null});t:{var v=e,y=o;f=t;var m=n;switch(y.tag){case 1:if(v=y.payload,typeof v=="function"){p=v.call(m,p,f);break t}p=v;break t;case 3:v.flags=v.flags&-65537|128;case 0:if(v=y.payload,f=typeof v=="function"?v.call(m,p,f):v,f==null)break t;p=de({},p,f);break t;case 2:xa=!0}}f=o.callback,f!==null&&(e.flags|=64,d&&(e.flags|=8192),d=a.callbacks,d===null?a.callbacks=[f]:d.push(f))}else d={lane:f,tag:o.tag,payload:o.payload,callback:o.callback,next:null},h===null?(u=h=d,l=p):h=h.next=d,r|=f;if(o=o.next,o===null){if(o=a.shared.pending,o===null)break;d=o,o=d.next,d.next=null,a.lastBaseUpdate=d,a.shared.pending=null}}while(!0);h===null&&(l=p),a.baseState=l,a.firstBaseUpdate=u,a.lastBaseUpdate=h,s===null&&(a.shared.lanes=0),Wa|=r,e.lanes=r,e.memoizedState=p}}function iS(e,t){if(typeof e!="function")throw Error(q(191,e));e.call(t)}function aS(e,t){var n=e.callbacks;if(n!==null)for(e.callbacks=null,e=0;e<n.length;e++)iS(n[e],t)}var Ya=Pi(null),rc=Pi(0);function I_(e,t){e=ia,ve(rc,e),ve(Ya,t),ia=e|t.baseLanes}function Zh(){ve(rc,ia),ve(Ya,Ya.current)}function qp(){ia=rc.current,Je(Ya),Je(rc)}var nn=Pi(null),rn=null;function Pa(e){var t=e.alternate;ve($e,$e.current&1),ve(nn,e),rn===null&&(t===null||Ya.current!==null||t.memoizedState!==null)&&(rn=e)}function Kh(e){ve($e,$e.current),ve(nn,e),rn===null&&(rn=e)}function sS(e){e.tag===22?(ve($e,$e.current),ve(nn,e),rn===null&&(rn=e)):za()}function za(){ve($e,$e.current),ve(nn,nn.current)}function Bn(e){Je(nn),rn===e&&(rn=null),Je($e)}var $e=Pi(0);function nl(e,t){ve(nn,nn.current),ve($e,t)}function Wp(e){Je($e),Je(nn),rn===e&&(rn=null)}function oc(e){for(var t=e;t!==null;){if(t.tag===13){var n=t.memoizedState;if(n!==null&&(n=n.dehydrated,n===null||Dd(n)||ym(n)))return t}else if(t.tag===19&&t.memoizedProps.revealOrder!=="independent"){if(t.flags&128)return t}else if(t.child!==null){t.child.return=t,t=t.child;continue}if(t===e)break;for(;t.sibling===null;){if(t.return===null||t.return===e)return null;t=t.return}t.sibling.return=t.return,t=t.sibling}return null}var ta=0,Nt=null,ce=null,Le=null,lc=!1,Cr=!1,Cs=!1,uc=0,il=0,wr=null,HE=0;function Ae(){throw Error(q(321))}function jp(e,t){if(t===null)return!1;for(var n=0;n<t.length&&n<e.length;n++)if(!Yn(e[n],t[n]))return!1;return!0}function Zp(e,t,n,i,a,s){return ta=s,Nt=t,t.memoizedState=null,t.updateQueue=null,t.lanes=0,xt.H=e===null||e.memoizedState===null?zS:IS,Cs=!1,s=n(i,a),Cs=!1,Cr&&(s=oS(t,n,i,a)),rS(e),s}function rS(e){xt.H=cc;var t=ce!==null&&ce.next!==null;if(ta=0,Le=ce=Nt=null,lc=!1,il=0,wr=null,t)throw Error(q(300));e===null||Pe||(e=e.dependencies,e!==null&&ac(e)&&(Pe=!0))}function oS(e,t,n,i){Nt=e;var a=0;do{if(Cr&&(wr=null),il=0,Cr=!1,25<=a)throw Error(q(301));if(a+=1,Le=ce=null,e.updateQueue!=null){var s=e.updateQueue;s.lastEffect=null,s.events=null,s.stores=null,s.memoCache!=null&&(s.memoCache.index=0)}xt.H=jE,s=t(n,i)}while(Cr);return s}function GE(){var e=xt.H,t=e.useState()[0];return t=typeof t.then=="function"?Sl(t):t,e=e.useState()[0],(ce!==null?ce.memoizedState:null)!==e&&(Nt.flags|=1024),t}function Kp(){var e=uc!==0;return uc=0,e}function Qp(e,t,n){t.updateQueue=e.updateQueue,t.flags&=-2053,e.lanes&=~n}function Jp(e){if(lc){for(e=e.memoizedState;e!==null;){var t=e.queue;t!==null&&(t.pending=null),e=e.next}lc=!1}ta=0,Le=ce=Nt=null,Cr=!1,il=uc=0,wr=null}function fn(){var e={memoizedState:null,baseState:null,baseQueue:null,queue:null,next:null};return Le===null?Nt.memoizedState=Le=e:Le=Le.next=e,Le}function De(){if(ce===null){var e=Nt.alternate;e=e!==null?e.memoizedState:null}else e=ce.next;var t=Le===null?Nt.memoizedState:Le.next;if(t!==null)Le=t,ce=e;else{if(e===null)throw Nt.alternate===null?Error(q(467)):Error(q(310));ce=e,e={memoizedState:ce.memoizedState,baseState:ce.baseState,baseQueue:ce.baseQueue,queue:ce.queue,next:null},Le===null?Nt.memoizedState=Le=e:Le=Le.next=e}return Le}function Xc(){return{lastEffect:null,events:null,stores:null,memoCache:null}}function Sl(e){var t=il;return il+=1,wr===null&&(wr=[]),e=tS(wr,e,t),t=Nt,(Le===null?t.memoizedState:Le.next)===null&&(t=t.alternate,xt.H=t===null||t.memoizedState===null?zS:IS),e}function kc(e){if(e!==null&&typeof e=="object"){if(typeof e.then=="function")return Sl(e);if(e.$$typeof===MM)return;if(e.$$typeof===Ci)return Qe(e)}throw Error(q(438,String(e)))}function $p(e){var t=null,n=Nt.updateQueue;if(n!==null&&(t=n.memoCache),t==null){var i=Nt.alternate;i!==null&&(i=i.updateQueue,i!==null&&(i=i.memoCache,i!=null&&(t={data:i.data.map(function(a){return a.slice()}),index:0})))}if(t==null&&(t={data:[],index:0}),n===null&&(n=Xc(),Nt.updateQueue=n),n.memoCache=t,n=t.data[t.index],n===void 0)for(n=t.data[t.index]=Array(e),i=0;i<e;i++)n[i]=xM;return t.index++,n}function ea(e,t){return typeof t=="function"?t(e):t}function wu(e){var t=De();return tm(t,ce,e)}function tm(e,t,n){var i=e.queue;if(i===null)throw Error(q(311));i.lastRenderedReducer=n;var a=e.baseQueue,s=i.pending;if(s!==null){if(a!==null){var r=a.next;a.next=s.next,s.next=r}t.baseQueue=a=s,i.pending=null}if(s=e.baseState,a===null)e.memoizedState=s;else{t=a.next;var o=r=null,l=null,u=t,h=!1;do{var p=u.lane&-536870913;if(p!==u.lane?(Gt&p)===p:(ta&p)===p){var f=u.revertLane;if(f===0)l!==null&&(l=l.next={lane:0,revertLane:0,gesture:null,action:u.action,hasEagerState:u.hasEagerState,eagerState:u.eagerState,next:null}),p===As&&(h=!0);else if((ta&f)===f){u=u.next,f===As&&(h=!0);continue}else p={lane:0,revertLane:u.revertLane,gesture:null,action:u.action,hasEagerState:u.hasEagerState,eagerState:u.eagerState,next:null},l===null?(o=l=p,r=s):l=l.next=p,Nt.lanes|=f,Wa|=f;p=u.action,Cs&&n(s,p),s=u.hasEagerState?u.eagerState:n(s,p)}else f={lane:p,revertLane:u.revertLane,gesture:u.gesture,action:u.action,hasEagerState:u.hasEagerState,eagerState:u.eagerState,next:null},l===null?(o=l=f,r=s):l=l.next=f,Nt.lanes|=p,Wa|=p;u=u.next}while(u!==null&&u!==t);if(l===null?r=s:l.next=o,!Yn(s,e.memoizedState)&&(Pe=!0,h&&(n=Ar,n!==null)))throw n;e.memoizedState=s,e.baseState=r,e.baseQueue=l,i.lastRenderedState=s}return a===null&&(i.lanes=0),[e.memoizedState,i.dispatch]}function Rf(e){var t=De(),n=t.queue;if(n===null)throw Error(q(311));n.lastRenderedReducer=e;var i=n.dispatch,a=n.pending,s=t.memoizedState;if(a!==null){n.pending=null;var r=a=a.next;do s=e(s,r.action),r=r.next;while(r!==a);Yn(s,t.memoizedState)||(Pe=!0),t.memoizedState=s,t.baseQueue===null&&(t.baseState=s),n.lastRenderedState=s}return[s,i]}function lS(e,t,n){var i=Nt,a=De(),s=zt;if(s){if(n===void 0)throw Error(q(407));n=n()}else n=t();var r=!Yn((ce||a).memoizedState,n);if(r&&(a.memoizedState=n,Pe=!0),a=a.queue,em(fS.bind(null,i,a,e),[e]),e=a.getSnapshot!==t||r||Le!==null&&(Le.memoizedState.tag&1)!==0,Hr(e?9:8,{destroy:void 0},cS.bind(null,i,a,n,t),null),e){if(i.flags|=2048,he===null)throw Error(q(349));s||ta&127||uS(i,t,n)}return n}function uS(e,t,n){e.flags|=16384,e={getSnapshot:t,value:n},t=Nt.updateQueue,t===null?(t=Xc(),Nt.updateQueue=t,t.stores=[e]):(n=t.stores,n===null?t.stores=[e]:n.push(e))}function cS(e,t,n,i){t.value=n,t.getSnapshot=i,hS(t)&&dS(e)}function fS(e,t,n){return n(function(){hS(t)&&dS(e)})}function hS(e){var t=e.getSnapshot;e=e.value;try{var n=t();return!Yn(e,n)}catch{return!0}}function dS(e){var t=Bs(e,2);t!==null&&Tn(t,e,2)}function Qh(e){var t=fn();if(typeof e=="function"){var n=e;if(e=n(),Cs){ba(!0);try{n()}finally{ba(!1)}}}return t.memoizedState=t.baseState=e,t.queue={pending:null,lanes:0,dispatch:null,lastRenderedReducer:ea,lastRenderedState:e},t}function pS(e,t,n,i){return e.baseState=n,tm(e,ce,typeof i=="function"?i:ea)}function VE(e,t,n,i,a){if(qc(e))throw Error(q(485));if(e=t.action,e!==null){var s={payload:a,action:e,next:null,isTransition:!0,status:"pending",value:null,reason:null,listeners:[],then:function(r){s.listeners.push(r)}};xt.T!==null?n(!0):s.isTransition=!1,i(s),n=t.pending,n===null?(s.next=t.pending=s,mS(t,s)):(s.next=n.next,t.pending=n.next=s)}}function mS(e,t){var n=t.action,i=t.payload,a=e.state;if(t.isTransition){var s=xt.T,r={};r.types=s!==null?s.types:null,xt.T=r;try{var o=n(a,i),l=xt.S;l!==null&&l(r,o),B_(e,t,o)}catch(u){Jh(e,t,u)}finally{s!==null&&r.types!==null&&(s.types=r.types),xt.T=s}}else try{s=n(a,i),B_(e,t,s)}catch(u){Jh(e,t,u)}}function B_(e,t,n){n!==null&&typeof n=="object"&&typeof n.then=="function"?n.then(function(i){F_(e,t,i)},function(i){return Jh(e,t,i)}):F_(e,t,n)}function F_(e,t,n){t.status="fulfilled",t.value=n,_S(t),e.state=n,t=e.pending,t!==null&&(n=t.next,n===t?e.pending=null:(n=n.next,t.next=n,mS(e,n)))}function Jh(e,t,n){var i=e.pending;if(e.pending=null,i!==null){i=i.next;do t.status="rejected",t.reason=n,_S(t),t=t.next;while(t!==i)}e.action=null}function _S(e){e=e.listeners;for(var t=0;t<e.length;t++)(0,e[t])()}function gS(e,t){return t}function H_(e,t){if(zt){var n=he.formState;if(n!==null){t:{var i=Nt;if(zt){if(_e){e:{for(var a=_e,s=ni;a.nodeType!==8;){if(!s){a=null;break e}if(a=ai(a.nextSibling),a===null){a=null;break e}}s=a.data,a=s==="F!"||s==="F"?a:null}if(a){_e=ai(a.nextSibling),i=a.data==="F!";break t}}ka(i)}i=!1}i&&(t=n[0])}}return n=fn(),n.memoizedState=n.baseState=t,i={pending:null,lanes:0,dispatch:null,lastRenderedReducer:gS,lastRenderedState:t},n.queue=i,n=LS.bind(null,Nt,i),i.dispatch=n,i=Qh(!1),s=sm.bind(null,Nt,!1,i.queue),i=fn(),a={state:t,dispatch:null,action:e,pending:null},i.queue=a,n=VE.bind(null,Nt,a,s,n),a.dispatch=n,i.memoizedState=e,[t,n,!1]}function G_(e){var t=De();return vS(t,ce,e)}function vS(e,t,n){if(t=tm(e,t,gS)[0],e=wu(ea)[0],typeof t=="object"&&t!==null&&typeof t.then=="function")try{var i=Sl(t)}catch(r){throw r===so?Vc:r}else i=t;t=De();var a=t.queue,s=a.dispatch;return n!==t.memoizedState&&(Nt.flags|=2048,Hr(9,{destroy:void 0},XE.bind(null,a,n),null)),[i,s,e]}function XE(e,t){e.action=t}function V_(e){var t=De(),n=ce;if(n!==null)return vS(t,n,e);De(),t=t.memoizedState,n=De();var i=n.queue.dispatch;return n.memoizedState=e,[t,i,!1]}function Hr(e,t,n,i){return e={tag:e,create:n,deps:i,inst:t,next:null},t=Nt.updateQueue,t===null&&(t=Xc(),Nt.updateQueue=t),n=t.lastEffect,n===null?t.lastEffect=e.next=e:(i=n.next,n.next=e,e.next=i,t.lastEffect=e),e}function SS(){return De().memoizedState}function Du(e,t,n,i){var a=fn();Nt.flags|=e,a.memoizedState=Hr(1|t,{destroy:void 0},n,i===void 0?null:i)}function Yc(e,t,n,i){var a=De();i=i===void 0?null:i;var s=a.memoizedState.inst;ce!==null&&i!==null&&jp(i,ce.memoizedState.deps)?a.memoizedState=Hr(t,s,n,i):(Nt.flags|=e,a.memoizedState=Hr(1|t,s,n,i))}function X_(e,t){Du(8390656,8,e,t)}function em(e,t){Yc(2048,8,e,t)}function kE(e){Nt.flags|=4;var t=Nt.updateQueue;if(t===null)t=Xc(),Nt.updateQueue=t,t.events=[e];else{var n=t.events;n===null?t.events=[e]:n.push(e)}}function yS(e){var t=De().memoizedState;return kE({ref:t,nextImpl:e}),function(){if($t&2)throw Error(q(440));return t.impl.apply(void 0,arguments)}}function xS(e,t){return Yc(4,2,e,t)}function MS(e,t){return Yc(4,4,e,t)}function ES(e,t){if(typeof t=="function"){e=e();var n=t(e);return function(){typeof n=="function"?n():t(null)}}if(t!=null)return e=e(),t.current=e,function(){t.current=null}}function TS(e,t,n){n=n!=null?n.concat([e]):null,Yc(4,4,ES.bind(null,t,e),n)}function nm(){}function bS(e,t){var n=De();t=t===void 0?null:t;var i=n.memoizedState;return t!==null&&jp(t,i[1])?i[0]:(n.memoizedState=[e,t],e)}function AS(e,t){var n=De();t=t===void 0?null:t;var i=n.memoizedState;if(t!==null&&jp(t,i[1]))return i[0];if(i=e(),Cs){ba(!0);try{e()}finally{ba(!1)}}return n.memoizedState=[i,t],i}function im(e,t,n){return n===void 0||ta&1073741824&&!(Gt&261930)?e.memoizedState=t:(e.memoizedState=n,e=vy(),Nt.lanes|=e,Wa|=e,n)}function RS(e,t,n,i){return Yn(n,t)?n:Ya.current!==null?(e=im(e,n,i),Yn(e,t)||(Pe=!0),e):!(ta&106)||ta&1073741824&&!(Gt&261930)?(Pe=!0,e.memoizedState=n):(e=vy(),Nt.lanes|=e,Wa|=e,t)}function CS(e,t,n,i,a){var s=te.p;te.p=s!==0&&8>s?s:8;var r=xt.T,o={};o.types=r!==null?r.types:null,xt.T=o,sm(e,!1,t,n);try{var l=a(),u=xt.S;if(u!==null&&u(o,l),l!==null&&typeof l=="object"&&typeof l.then=="function"){var h=FE(l,i);Xo(e,t,h,kn(e))}else Xo(e,t,i,kn(e))}catch(p){Xo(e,t,{then:function(){},status:"rejected",reason:p},kn())}finally{te.p=s,r!==null&&o.types!==null&&(r.types=o.types),xt.T=r}}function YE(){}function $h(e,t,n,i){if(e.tag!==5)throw Error(q(476));var a=wS(e).queue;CS(e,a,t,vs,n===null?YE:function(){return DS(e),n(i)})}function wS(e){var t=e.memoizedState;if(t!==null)return t;t={memoizedState:vs,baseState:vs,baseQueue:null,queue:{pending:null,lanes:0,dispatch:null,lastRenderedReducer:ea,lastRenderedState:vs},next:null};var n={};return t.next={memoizedState:n,baseState:n,baseQueue:null,queue:{pending:null,lanes:0,dispatch:null,lastRenderedReducer:ea,lastRenderedState:n},next:null},e.memoizedState=t,e=e.alternate,e!==null&&(e.memoizedState=t),t}function DS(e){var t=wS(e);t.next===null&&(t=e.alternate.memoizedState),Xo(e,t.next.queue,{},kn())}function am(){return Qe(Wr)}function US(){return De().memoizedState}function NS(){return De().memoizedState}function qE(e){for(var t=e.return;t!==null;){switch(t.tag){case 24:case 3:var n=kn();e=La(n);var i=Oa(t,e,n);i!==null&&(Tn(i,t,n),Ho(i,t,n)),t={cache:Vp()},e.payload=t;return}t=t.return}}function WE(e,t,n){var i=kn();n={lane:i,revertLane:0,gesture:null,action:n,hasEagerState:!1,eagerState:null,next:null},qc(e)?OS(t,n):(n=Fp(e,t,n,i),n!==null&&(Tn(n,e,i),PS(n,t,i)))}function LS(e,t,n){var i=kn();Xo(e,t,n,i)}function Xo(e,t,n,i){var a={lane:i,revertLane:0,gesture:null,action:n,hasEagerState:!1,eagerState:null,next:null};if(qc(e))OS(t,a);else{var s=e.alternate;if(e.lanes===0&&(s===null||s.lanes===0)&&(s=t.lastRenderedReducer,s!==null))try{var r=t.lastRenderedState,o=s(r,n);if(a.hasEagerState=!0,a.eagerState=o,Yn(o,r))return Hc(e,t,a,0),he===null&&Fc(),!1}catch{}finally{}if(n=Fp(e,t,a,i),n!==null)return Tn(n,e,i),PS(n,t,i),!0}return!1}function sm(e,t,n,i){if(i={lane:2,revertLane:_m(),gesture:null,action:i,hasEagerState:!1,eagerState:null,next:null},qc(e)){if(t)throw Error(q(479))}else t=Fp(e,n,i,2),t!==null&&Tn(t,e,2)}function qc(e){var t=e.alternate;return e===Nt||t!==null&&t===Nt}function OS(e,t){Cr=lc=!0;var n=e.pending;n===null?t.next=t:(t.next=n.next,n.next=t),e.pending=t}function PS(e,t,n){if(n&4194048){var i=t.lanes;i&=e.pendingLanes,n|=i,t.lanes=n,Sv(e,n)}}var cc={readContext:Qe,use:kc,useCallback:Ae,useContext:Ae,useEffect:Ae,useImperativeHandle:Ae,useLayoutEffect:Ae,useInsertionEffect:Ae,useMemo:Ae,useReducer:Ae,useRef:Ae,useState:Ae,useDebugValue:Ae,useDeferredValue:Ae,useTransition:Ae,useSyncExternalStore:Ae,useId:Ae,useHostTransitionStatus:Ae,useFormState:Ae,useActionState:Ae,useOptimistic:Ae,useMemoCache:Ae,useCacheRefresh:Ae,useEffectEvent:Ae},zS={readContext:Qe,use:kc,useCallback:function(e,t){return fn().memoizedState=[e,t===void 0?null:t],e},useContext:Qe,useEffect:X_,useImperativeHandle:function(e,t,n){n=n!=null?n.concat([e]):null,Du(4194308,4,ES.bind(null,t,e),n)},useLayoutEffect:function(e,t){return Du(4194308,4,e,t)},useInsertionEffect:function(e,t){Du(4,2,e,t)},useMemo:function(e,t){var n=fn();t=t===void 0?null:t;var i=e();if(Cs){ba(!0);try{e()}finally{ba(!1)}}return n.memoizedState=[i,t],i},useReducer:function(e,t,n){var i=fn();if(n!==void 0){var a=n(t);if(Cs){ba(!0);try{n(t)}finally{ba(!1)}}}else a=t;return i.memoizedState=i.baseState=a,e={pending:null,lanes:0,dispatch:null,lastRenderedReducer:e,lastRenderedState:a},i.queue=e,e=e.dispatch=WE.bind(null,Nt,e),[i.memoizedState,e]},useRef:function(e){var t=fn();return e={current:e},t.memoizedState=e},useState:function(e){e=Qh(e);var t=e.queue,n=LS.bind(null,Nt,t);return t.dispatch=n,[e.memoizedState,n]},useDebugValue:nm,useDeferredValue:function(e,t){var n=fn();return im(n,e,t)},useTransition:function(){var e=Qh(!1);return e=CS.bind(null,Nt,e.queue,!0,!1),fn().memoizedState=e,[!1,e]},useSyncExternalStore:function(e,t,n){var i=Nt,a=fn();if(zt){if(n===void 0)throw Error(q(407));n=n()}else{if(n=t(),he===null)throw Error(q(349));Gt&127||uS(i,t,n)}a.memoizedState=n;var s={value:n,getSnapshot:t};return a.queue=s,X_(fS.bind(null,i,s,e),[e]),i.flags|=2048,Hr(9,{destroy:void 0},cS.bind(null,i,s,n,t),null),n},useId:function(){var e=fn(),t=he.identifierPrefix;if(zt){var n=Ui,i=Di;n=(i&~(1<<32-Xn(i)-1)).toString(32)+n,t="_"+t+"R_"+n,n=uc++,0<n&&(t+="H"+n.toString(32)),t+="_"}else n=HE++,t="_"+t+"r_"+n.toString(32)+"_";return e.memoizedState=t},useHostTransitionStatus:am,useFormState:H_,useActionState:H_,useOptimistic:function(e){var t=fn();t.memoizedState=t.baseState=e;var n={pending:null,lanes:0,dispatch:null,lastRenderedReducer:null,lastRenderedState:null};return t.queue=n,t=sm.bind(null,Nt,!0,n),n.dispatch=t,[e,t]},useMemoCache:$p,useCacheRefresh:function(){return fn().memoizedState=qE.bind(null,Nt)},useEffectEvent:function(e){var t=fn(),n={impl:e};return t.memoizedState=n,function(){if($t&2)throw Error(q(440));return n.impl.apply(void 0,arguments)}}},IS={readContext:Qe,use:kc,useCallback:bS,useContext:Qe,useEffect:em,useImperativeHandle:TS,useInsertionEffect:xS,useLayoutEffect:MS,useMemo:AS,useReducer:wu,useRef:SS,useState:function(){return wu(ea)},useDebugValue:nm,useDeferredValue:function(e,t){var n=De();return RS(n,ce.memoizedState,e,t)},useTransition:function(){var e=wu(ea)[0],t=De().memoizedState;return[typeof e=="boolean"?e:Sl(e),t]},useSyncExternalStore:lS,useId:US,useHostTransitionStatus:am,useFormState:G_,useActionState:G_,useOptimistic:function(e,t){var n=De();return pS(n,ce,e,t)},useMemoCache:$p,useCacheRefresh:NS,useEffectEvent:yS},jE={readContext:Qe,use:kc,useCallback:bS,useContext:Qe,useEffect:em,useImperativeHandle:TS,useInsertionEffect:xS,useLayoutEffect:MS,useMemo:AS,useReducer:Rf,useRef:SS,useState:function(){return Rf(ea)},useDebugValue:nm,useDeferredValue:function(e,t){var n=De();return ce===null?im(n,e,t):RS(n,ce.memoizedState,e,t)},useTransition:function(){var e=Rf(ea)[0],t=De().memoizedState;return[typeof e=="boolean"?e:Sl(e),t]},useSyncExternalStore:lS,useId:US,useHostTransitionStatus:am,useFormState:V_,useActionState:V_,useOptimistic:function(e,t){var n=De();return ce!==null?pS(n,ce,e,t):(n.baseState=e,[e,n.queue.dispatch])},useMemoCache:$p,useCacheRefresh:NS,useEffectEvent:yS};function Cf(e,t,n,i){t=e.memoizedState,n=n(i,t),n=n==null?t:de({},t,n),e.memoizedState=n,e.lanes===0&&(e.updateQueue.baseState=n)}var td={enqueueSetState:function(e,t,n){e=e._reactInternals;var i=kn(),a=La(i);a.payload=t,n!=null&&(a.callback=n),t=Oa(e,a,i),t!==null&&(Tn(t,e,i),Ho(t,e,i))},enqueueReplaceState:function(e,t,n){e=e._reactInternals;var i=kn(),a=La(i);a.tag=1,a.payload=t,n!=null&&(a.callback=n),t=Oa(e,a,i),t!==null&&(Tn(t,e,i),Ho(t,e,i))},enqueueForceUpdate:function(e,t){e=e._reactInternals;var n=kn(),i=La(n);i.tag=2,t!=null&&(i.callback=t),t=Oa(e,i,n),t!==null&&(Tn(t,e,n),Ho(t,e,n))}};function k_(e,t,n,i,a,s,r){return e=e.stateNode,typeof e.shouldComponentUpdate=="function"?e.shouldComponentUpdate(i,s,r):t.prototype&&t.prototype.isPureReactComponent?!Jo(n,i)||!Jo(a,s):!0}function Y_(e,t,n,i){e=t.state,typeof t.componentWillReceiveProps=="function"&&t.componentWillReceiveProps(n,i),typeof t.UNSAFE_componentWillReceiveProps=="function"&&t.UNSAFE_componentWillReceiveProps(n,i),t.state!==e&&td.enqueueReplaceState(t,t.state,null)}function ws(e,t){var n=t;if("ref"in t){n={};for(var i in t)i!=="ref"&&(n[i]=t[i])}if(e=e.defaultProps){n===t&&(n=de({},n));for(var a in e)n[a]===void 0&&(n[a]=e[a])}return n}function BS(e){tc(e)}function FS(e){console.error(e)}function HS(e){tc(e)}function fc(e,t){try{var n=e.onUncaughtError;n(t.value,{componentStack:t.stack})}catch(i){setTimeout(function(){throw i})}}function q_(e,t,n){try{var i=e.onCaughtError;i(n.value,{componentStack:n.stack,errorBoundary:t.tag===1?t.stateNode:null})}catch(a){setTimeout(function(){throw a})}}function ed(e,t,n){return n=La(n),n.tag=3,n.payload={element:null},n.callback=function(){fc(e,t)},n}function GS(e){return e=La(e),e.tag=3,e}function VS(e,t,n,i){var a=n.type.getDerivedStateFromError;if(typeof a=="function"){var s=i.value;e.payload=function(){return a(s)},e.callback=function(){q_(t,n,i)}}var r=n.stateNode;r!==null&&typeof r.componentDidCatch=="function"&&(e.callback=function(){q_(t,n,i),typeof a!="function"&&(Ia===null?Ia=new Set([this]):Ia.add(this));var o=i.stack;this.componentDidCatch(i.value,{componentStack:o!==null?o:""})})}function ZE(e,t,n,i,a){if(n.flags|=32768,i!==null&&typeof i=="object"&&typeof i.then=="function"){if(t=n.alternate,t!==null&&Ts(t,n,a,!0),n=nn.current,n!==null){switch(n.tag){case 31:case 13:case 19:return rn===null?Sc():n.alternate===null&&Re===0&&(Re=3),n.flags&=-257,n.flags|=65536,n.lanes=a,i===sc?n.flags|=16384:(t=n.updateQueue,t===null?n.updateQueue=new Set([i]):t.add(i),Pf(e,i,a)),!1;case 22:return n.flags|=65536,i===sc?n.flags|=16384:(t=n.updateQueue,t===null?(t={transitions:null,markerInstances:null,retryQueue:new Set([i])},n.updateQueue=t):(n=t.retryQueue,n===null?t.retryQueue=new Set([i]):n.add(i)),Pf(e,i,a)),!1}throw Error(q(435,n.tag))}return Pf(e,i,a),Sc(),!1}if(zt)return t=nn.current,t!==null?(!(t.flags&65536)&&(t.flags|=256),t.flags|=65536,t.lanes=a,i!==Xh&&(e=Error(q(422),{cause:i}),tl(ei(e,n)))):(i!==Xh&&(t=Error(q(423),{cause:i}),tl(ei(t,n))),e=e.current.alternate,e.flags|=65536,a&=-a,e.lanes|=a,i=ei(i,n),a=ed(e.stateNode,i,a),Af(e,a),Re!==4&&(Re=2)),!1;var s=Error(q(520),{cause:i});if(s=ei(s,n),Wo===null?Wo=[s]:Wo.push(s),Re!==4&&(Re=2),t===null)return!0;i=ei(i,n),n=t;do{switch(n.tag){case 3:return n.flags|=65536,e=a&-a,n.lanes|=e,e=ed(n.stateNode,i,e),Af(n,e),!1;case 1:if(t=n.type,s=n.stateNode,!(n.flags&128)&&(typeof t.getDerivedStateFromError=="function"||s!==null&&typeof s.componentDidCatch=="function"&&(Ia===null||!Ia.has(s))))return n.flags|=65536,a&=-a,n.lanes|=a,a=GS(a),VS(a,e,n,i),Af(n,a),!1;break;case 22:if(n.memoizedState!==null)return n.flags|=65536,!1}n=n.return}while(n!==null);return!1}var rm=Error(q(461)),Pe=!1;function Ie(e,t,n,i){t.child=e===null?nS(t,null,n,i):Rs(t,e.child,n,i)}function W_(e,t,n,i,a){n=n.render;var s=t.ref;if("ref"in i){var r={};for(var o in i)o!=="ref"&&(r[o]=i[o])}else r=i;return bs(t),i=Zp(e,t,n,r,s,a),o=Kp(),e!==null&&!Pe?(Qp(e,t,a),na(e,t,a)):(zt&&o&&Gc(t),t.flags|=1,Ie(e,t,i,a),t.child)}function j_(e,t,n,i,a){if(e===null){var s=n.type;return typeof s=="function"&&!Hp(s)&&s.defaultProps===void 0&&n.compare===null?(t.tag=15,t.type=s,XS(e,t,s,i,a)):(e=Au(n.type,null,i,t,t.mode,a),e.ref=t.ref,e.return=t,t.child=e)}if(s=e.child,!lm(e,a)){var r=s.memoizedProps;if(n=n.compare,n=n!==null?n:Jo,n(r,i)&&e.ref===t.ref)return na(e,t,a)}return t.flags|=1,e=Ki(s,i),e.ref=t.ref,e.return=t,t.child=e}function XS(e,t,n,i,a){if(e!==null){var s=e.memoizedProps;if(Jo(s,i)&&e.ref===t.ref)if(Pe=!1,t.pendingProps=i=s,lm(e,a))e.flags&131072&&(Pe=!0);else return t.lanes=e.lanes,na(e,t,a)}return nd(e,t,n,i,a)}function kS(e,t,n,i){var a=i.children,s=e!==null?e.memoizedState:null;if(e===null&&t.stateNode===null&&(t.stateNode={_visibility:1,_pendingMarkers:null,_retryCache:null,_transitions:null}),i.mode==="hidden"){if(t.flags&128){if(s=s!==null?s.baseLanes|n:n,e!==null){for(i=t.child=e.child,a=0;i!==null;)a=a|i.lanes|i.childLanes,i=i.sibling;i=a&~s}else i=0,t.child=null;return Z_(e,t,s,n,i)}if(n&536870912)t.memoizedState={baseLanes:0,cachePool:null},e!==null&&Cu(t,s!==null?s.cachePool:null),s!==null?I_(t,s):Zh(),sS(t);else return i=t.lanes=536870912,Z_(e,t,s!==null?s.baseLanes|n:n,n,i)}else s!==null?(Cu(t,s.cachePool),I_(t,s),za(),t.memoizedState=null):(e!==null&&Cu(t,null),Zh(),za());return Ie(e,t,a,n),t.child}function ko(e,t){return e!==null&&e.tag===22||t.stateNode!==null||(t.stateNode={_visibility:1,_pendingMarkers:null,_retryCache:null,_transitions:null}),t.sibling}function Z_(e,t,n,i,a){var s=Xp();return s=s===null?null:{parent:Oe._currentValue,pool:s},t.memoizedState={baseLanes:n,cachePool:s},e!==null&&Cu(t,null),Zh(),sS(t),e!==null&&Ts(e,t,i,!0),t.childLanes=a,null}function Uu(e,t){return t=Wc({mode:t.mode,children:t.children},e.mode),t.ref=e.ref,e.child=t,t.return=e,t}function K_(e,t,n){return Rs(t,e.child,null,n),e=Uu(t,t.pendingProps),e.flags|=2,Bn(t),t.memoizedState=null,e}function KE(e,t,n){var i=t.pendingProps,a=(t.flags&128)!==0;if(t.flags&=-129,e===null){if(zt){if(i.mode==="hidden")return e=Uu(t,i),t.lanes=536870912,e.memoizedState={baseLanes:0,cachePool:null},ko(null,e);if(Kh(t),(e=_e)?(e=Xy(e,ni),e=e!==null&&e.data==="&"?e:null,e!==null&&(t.memoizedState={dehydrated:e,treeContext:Xa!==null?{id:Di,overflow:Ui}:null,retryLane:536870912,hydrationErrors:null},n=Zv(e),n.return=t,t.child=n,qe=t,_e=null)):e=null,e===null)throw ka(t);return t.lanes=536870912,null}return Uu(t,i)}var s=e.memoizedState;if(s!==null){var r=s.dehydrated;if(Kh(t),a)if(t.flags&256)t.flags&=-257,t=K_(e,t,n);else if(t.memoizedState!==null)t.child=e.child,t.flags|=128,t=null;else throw Error(q(558));else if(Pe||Ts(e,t,n,!1),a=(n&e.childLanes)!==0,Pe||a){if(Ya.current===null){if(i=he,i!==null&&(r=yv(i,n),r!==0&&r!==s.retryLane))throw s.retryLane=r,Bs(e,r),Tn(i,e,r),rm;Sc()}t=K_(e,t,n)}else e=s.treeContext,_e=ai(r.nextSibling),qe=t,zt=!0,Na=null,ni=!1,e!==null&&Qv(t,e),t=Uu(t,i),t.flags|=134221824;return t}return e=Ki(e.child,{mode:i.mode,children:i.children}),e.ref=t.ref,t.child=e,e.return=t,e}function rr(e,t){var n=t.ref;if(n===null)e!==null&&e.ref!==null&&(t.flags|=4194816);else{if(typeof n!="function"&&typeof n!="object")throw Error(q(284));(e===null||e.ref!==n)&&(t.flags|=4194816)}}function nd(e,t,n,i,a){return bs(t),n=Zp(e,t,n,i,void 0,a),i=Kp(),e!==null&&!Pe?(Qp(e,t,a),na(e,t,a)):(zt&&i&&Gc(t),t.flags|=1,Ie(e,t,n,a),t.child)}function Q_(e,t,n,i,a,s){return bs(t),t.updateQueue=null,n=oS(t,i,n,a),rS(e),i=Kp(),e!==null&&!Pe?(Qp(e,t,s),na(e,t,s)):(zt&&i&&Gc(t),t.flags|=1,Ie(e,t,n,s),t.child)}function J_(e,t,n,i,a){if(bs(t),t.stateNode===null){var s=gr,r=n.contextType;typeof r=="object"&&r!==null&&(s=Qe(r)),s=new n(i,s),t.memoizedState=s.state!==null&&s.state!==void 0?s.state:null,s.updater=td,t.stateNode=s,s._reactInternals=t,s=t.stateNode,s.props=i,s.state=t.memoizedState,s.refs={},Yp(t),r=n.contextType,s.context=typeof r=="object"&&r!==null?Qe(r):gr,s.state=t.memoizedState,r=n.getDerivedStateFromProps,typeof r=="function"&&(Cf(t,n,r,i),s.state=t.memoizedState),typeof n.getDerivedStateFromProps=="function"||typeof s.getSnapshotBeforeUpdate=="function"||typeof s.UNSAFE_componentWillMount!="function"&&typeof s.componentWillMount!="function"||(r=s.state,typeof s.componentWillMount=="function"&&s.componentWillMount(),typeof s.UNSAFE_componentWillMount=="function"&&s.UNSAFE_componentWillMount(),r!==s.state&&td.enqueueReplaceState(s,s.state,null),Vo(t,i,s,a),Go(),s.state=t.memoizedState),typeof s.componentDidMount=="function"&&(t.flags|=4194308),i=!0}else if(e===null){s=t.stateNode;var o=t.memoizedProps,l=ws(n,o);s.props=l;var u=s.context,h=n.contextType;r=gr,typeof h=="object"&&h!==null&&(r=Qe(h));var p=n.getDerivedStateFromProps;h=typeof p=="function"||typeof s.getSnapshotBeforeUpdate=="function",o=t.pendingProps!==o,h||typeof s.UNSAFE_componentWillReceiveProps!="function"&&typeof s.componentWillReceiveProps!="function"||(o||u!==r)&&Y_(t,s,i,r),xa=!1;var f=t.memoizedState;s.state=f,Vo(t,i,s,a),Go(),u=t.memoizedState,o||f!==u||xa?(typeof p=="function"&&(Cf(t,n,p,i),u=t.memoizedState),(l=xa||k_(t,n,l,i,f,u,r))?(h||typeof s.UNSAFE_componentWillMount!="function"&&typeof s.componentWillMount!="function"||(typeof s.componentWillMount=="function"&&s.componentWillMount(),typeof s.UNSAFE_componentWillMount=="function"&&s.UNSAFE_componentWillMount()),typeof s.componentDidMount=="function"&&(t.flags|=4194308)):(typeof s.componentDidMount=="function"&&(t.flags|=4194308),t.memoizedProps=i,t.memoizedState=u),s.props=i,s.state=u,s.context=r,i=l):(typeof s.componentDidMount=="function"&&(t.flags|=4194308),i=!1)}else{s=t.stateNode,Wh(e,t),r=t.memoizedProps,h=ws(n,r),s.props=h,p=t.pendingProps,f=s.context,u=n.contextType,l=gr,typeof u=="object"&&u!==null&&(l=Qe(u)),o=n.getDerivedStateFromProps,(u=typeof o=="function"||typeof s.getSnapshotBeforeUpdate=="function")||typeof s.UNSAFE_componentWillReceiveProps!="function"&&typeof s.componentWillReceiveProps!="function"||(r!==p||f!==l)&&Y_(t,s,i,l),xa=!1,f=t.memoizedState,s.state=f,Vo(t,i,s,a),Go();var d=t.memoizedState;r!==p||f!==d||xa||e!==null&&e.dependencies!==null&&ac(e.dependencies)?(typeof o=="function"&&(Cf(t,n,o,i),d=t.memoizedState),(h=xa||k_(t,n,h,i,f,d,l)||e!==null&&e.dependencies!==null&&ac(e.dependencies))?(u||typeof s.UNSAFE_componentWillUpdate!="function"&&typeof s.componentWillUpdate!="function"||(typeof s.componentWillUpdate=="function"&&s.componentWillUpdate(i,d,l),typeof s.UNSAFE_componentWillUpdate=="function"&&s.UNSAFE_componentWillUpdate(i,d,l)),typeof s.componentDidUpdate=="function"&&(t.flags|=4),typeof s.getSnapshotBeforeUpdate=="function"&&(t.flags|=1024)):(typeof s.componentDidUpdate!="function"||r===e.memoizedProps&&f===e.memoizedState||(t.flags|=4),typeof s.getSnapshotBeforeUpdate!="function"||r===e.memoizedProps&&f===e.memoizedState||(t.flags|=1024),t.memoizedProps=i,t.memoizedState=d),s.props=i,s.state=d,s.context=l,i=h):(typeof s.componentDidUpdate!="function"||r===e.memoizedProps&&f===e.memoizedState||(t.flags|=4),typeof s.getSnapshotBeforeUpdate!="function"||r===e.memoizedProps&&f===e.memoizedState||(t.flags|=1024),i=!1)}return s=i,rr(e,t),i=(t.flags&128)!==0,s||i?(s=t.stateNode,n=i&&typeof n.getDerivedStateFromError!="function"?null:s.render(),t.flags|=1,e!==null&&i?(t.child=Rs(t,e.child,null,a),t.child=Rs(t,null,n,a)):Ie(e,t,n,a),t.memoizedState=s.state,e=t.child):e=na(e,t,a),e}function $_(e,t,n,i){return Es(),t.flags|=256,Ie(e,t,n,i),t.child}var id={dehydrated:null,treeContext:null,retryLane:0,hydrationErrors:null};function ad(e){return{baseLanes:e,cachePool:$v()}}function sd(e,t,n){return e=e!==null?e.childLanes&~n:0,t&&(e|=Hn),e}function YS(e,t,n){var i=t.pendingProps,a=!1,s=(t.flags&128)!==0,r;if((r=s)||(r=e!==null&&e.memoizedState===null?!1:($e.current&2)!==0),r&&(a=!0,t.flags&=-129),r=(t.flags&32)!==0,t.flags&=-33,e===null){if(zt){if(a?Pa(t):za(),(e=_e)?(e=Xy(e,ni),e=e!==null&&e.data!=="&"?e:null,e!==null&&(t.memoizedState={dehydrated:e,treeContext:Xa!==null?{id:Di,overflow:Ui}:null,retryLane:536870912,hydrationErrors:null},n=Zv(e),n.return=t,t.child=n,qe=t,_e=null)):e=null,e===null)throw ka(t);return ym(e)?t.lanes=32:t.lanes=536870912,null}return s=i.children,i=i.fallback,a?(za(),a=t.mode,s=Wc({mode:"hidden",children:s},a),i=Ss(i,a,n,null),s.return=t,i.return=t,s.sibling=i,t.child=s,i=t.child,i.memoizedState=ad(n),i.childLanes=sd(e,r,n),t.memoizedState=id,ko(null,i)):(Pa(t),om(t,s))}var o=e.memoizedState;if(o!==null){var l=o.dehydrated;if(l!==null)return QE(e,t,s,r,i,l,o,n)}return a?(za(),a=i.fallback,s=t.mode,o=e.child,l=o.sibling,i=Ki(o,{mode:"hidden",children:i.children}),i.subtreeFlags=o.subtreeFlags&1206910976,l!==null?a=Ki(l,a):(a=Ss(a,s,n,null),a.flags|=2),a.return=t,i.return=t,i.sibling=a,t.child=i,ko(null,i),i=t.child,a=e.child.memoizedState,a===null?a=ad(n):(s=a.cachePool,s!==null?(o=Oe._currentValue,s=s.parent!==o?{parent:o,pool:o}:s):s=$v(),a={baseLanes:a.baseLanes|n,cachePool:s}),i.memoizedState=a,i.childLanes=sd(e,r,n),t.memoizedState=id,ko(e.child,i)):(Pa(t),n=e.child,e=n.sibling,n=Ki(n,{mode:"visible",children:i.children}),n.return=t,n.sibling=null,e!==null&&(r=t.deletions,r===null?(t.deletions=[e],t.flags|=16):r.push(e)),t.child=n,t.memoizedState=null,n)}function om(e,t){return t=Wc({mode:"visible",children:t},e.mode),t.return=e,e.child=t}function Wc(e,t){return e=Mn(22,e,null,t),e.lanes=0,e}function Gl(e,t,n){return Rs(t,e.child,null,n),e=om(t,t.pendingProps.children),e.flags|=2,t.memoizedState=null,e}function QE(e,t,n,i,a,s,r,o){if(n)return t.flags&256?(Pa(t),t.flags&=-257,Gl(e,t,o)):t.memoizedState!==null?(za(),t.child=e.child,t.flags|=128,null):(za(),s=a.fallback,r=t.mode,a=Wc({mode:"visible",children:a.children},r),s=Ss(s,r,o,null),s.flags|=2,a.return=t,s.return=t,a.sibling=s,t.child=a,Rs(t,e.child,null,o),a=t.child,a.memoizedState=ad(o),a.childLanes=sd(e,i,o),t.memoizedState=id,ko(null,a));if(Pa(t),ym(s)){if(i=s.nextSibling&&s.nextSibling.dataset,i)var l=i.dgst;return i=l,i!==""&&(a=Error(q(419)),a.stack="",a.digest=i,tl({value:a,source:null,stack:null})),Gl(e,t,o)}if(Pe||Ts(e,t,o,!1),i=(o&e.childLanes)!==0,Pe||i){if(Ya.current!==null)return Gl(e,t,o);if(i=he,i!==null&&(a=yv(i,o),a!==0&&a!==r.retryLane))throw r.retryLane=a,Bs(e,a),Tn(i,e,a),rm;return Dd(s)||Sc(),Gl(e,t,o)}return Dd(s)?(t.flags|=192,t.child=e.child,null):(e=r.treeContext,_e=ai(s.nextSibling),qe=t,zt=!0,Na=null,ni=!1,e!==null&&Qv(t,e),t=om(t,a.children),t.flags|=134221824,t)}function tg(e,t,n){e.lanes|=t;var i=e.alternate;i!==null&&(i.lanes|=t),Ru(e.return,t,n)}function eg(e){for(var t=null;e!==null;){var n=e.alternate;n!==null&&oc(n)===null&&(t=e),e=e.sibling}return t}function Vl(e,t,n,i,a,s){var r=e.memoizedState;r===null?e.memoizedState={isBackwards:t,rendering:null,renderingStartTime:0,last:i,tail:n,tailMode:a,treeForkCount:s}:(r.isBackwards=t,r.rendering=null,r.renderingStartTime=0,r.last=i,r.tail=n,r.tailMode=a,r.treeForkCount=s)}function wf(e){var t=e.child;for(e.child=null;t!==null;){var n=t.sibling;t.sibling=e.child,e.child=t,t=n}}function rd(e,t,n){var i=t.pendingProps,a=i.revealOrder,s=i.tail;i=i.children;var r=$e.current;if(t.flags&128)return nl(t,r),null;var o=(r&2)!==0;if(o?(r=r&1|2,t.flags|=128):r&=1,nl(t,r),a==="backwards"&&e!==null?(wf(e),Ie(e,t,i,n),wf(e)):Ie(e,t,i,n),i=zt?$o:0,!o&&e!==null&&e.flags&128)t:for(e=t.child;e!==null;){if(e.tag===13)e.memoizedState!==null&&tg(e,n,t);else if(e.tag===19)tg(e,n,t);else if(e.child!==null){e.child.return=e,e=e.child;continue}if(e===t)break t;for(;e.sibling===null;){if(e.return===null||e.return===t)break t;e=e.return}e.sibling.return=e.return,e=e.sibling}switch(a){case"backwards":n=eg(t.child),n===null?(a=t.child,t.child=null):(a=n.sibling,n.sibling=null,wf(t)),Vl(t,!0,a,null,s,i);break;case"unstable_legacy-backwards":for(n=null,a=t.child,t.child=null;a!==null;){if(e=a.alternate,e!==null&&oc(e)===null){t.child=a;break}e=a.sibling,a.sibling=n,n=a,a=e}Vl(t,!0,n,null,s,i);break;case"together":Vl(t,!1,null,null,void 0,i);break;case"independent":t.memoizedState=null;break;default:n=eg(t.child),n===null?(a=t.child,t.child=null):(a=n.sibling,n.sibling=null),Vl(t,!1,a,n,s,i)}return t.child}function ng(e,t,n){var i=t.pendingProps;return Ra(t,t.type,i.value),Ie(e,t,i.children,n),t.child}function na(e,t,n){if(e!==null&&(t.dependencies=e.dependencies),Wa|=t.lanes,!(n&t.childLanes))if(e!==null){if(Ts(e,t,n,!1),(n&t.childLanes)===0)return null}else return null;if(e!==null&&t.child!==e.child)throw Error(q(153));if(t.child!==null){for(e=t.child,n=Ki(e,e.pendingProps),t.child=n,n.return=t;e.sibling!==null;)e=e.sibling,n=n.sibling=Ki(e,e.pendingProps),n.return=t;n.sibling=null}return t.child}function lm(e,t){return e.lanes&t?!0:(e=e.dependencies,!!(e!==null&&ac(e)))}function JE(e,t,n){switch(t.tag){case 3:Ku(t,t.stateNode.containerInfo),Ra(t,Oe,e.memoizedState.cache),Es();break;case 27:case 5:Lh(t);break;case 4:Ku(t,t.stateNode.containerInfo);break;case 10:Ra(t,t.type,t.memoizedProps.value);break;case 31:if(t.memoizedState!==null)return t.flags|=128,Kh(t),null;break;case 13:var i=t.memoizedState;if(i!==null){if(i.dehydrated!==null)return Pa(t),t.flags|=128,null;i=Ts(e,t,n,!1);var a=t.child.childLanes;return i||n&a?YS(e,t,n):(Pa(t),e=na(e,t,n),e!==null?e.sibling:null)}Pa(t);break;case 19:if(t.flags&128)return rd(e,t,n);if(a=(e.flags&128)!==0,i=(n&t.childLanes)!==0,i||(Ts(e,t,n,!1),i=(n&t.childLanes)!==0),a){if(i)return rd(e,t,n);t.flags|=128}if(a=t.memoizedState,a!==null&&(a.rendering=null,a.tail=null,a.lastEffect=null),nl(t,$e.current),i)break;return null;case 22:return t.lanes=0,kS(e,t,n,t.pendingProps);case 24:Ra(t,Oe,e.memoizedState.cache)}return na(e,t,n)}function qS(e,t,n){if(e!==null)if(e.memoizedProps!==t.pendingProps)Pe=!0;else{if(!lm(e,n)&&!(t.flags&128))return Pe=!1,JE(e,t,n);Pe=!!(e.flags&131072)}else Pe=!1,zt&&t.flags&1048576&&Kv(t,$o,t.index);switch(t.lanes=0,t.tag){case 16:t:{var i=t.pendingProps;if(e=us(t.elementType),t.type=e,typeof e=="function")Hp(e)?(i=ws(e,i),t.tag=1,t=J_(null,t,e,i,n)):(t.tag=0,t=nd(null,t,e,i,n));else{if(e!=null){var a=e.$$typeof;if(a===Rp){t.tag=11,t=W_(null,t,e,i,n);break t}else if(a===Cp){t.tag=14,t=j_(null,t,e,i,n);break t}else if(a===Ci){t.tag=10,t.type=e,t=ng(null,t,n);break t}}throw t=Uh(e)||e,Error(q(306,t,""))}}return t;case 0:return nd(e,t,t.type,t.pendingProps,n);case 1:return i=t.type,a=ws(i,t.pendingProps),J_(e,t,i,a,n);case 3:t:{if(Ku(t,t.stateNode.containerInfo),e===null)throw Error(q(387));i=t.pendingProps;var s=t.memoizedState;a=s.element,Wh(e,t),Vo(t,i,null,n);var r=t.memoizedState;if(i=r.cache,Ra(t,Oe,i),i!==s.cache&&Yh(t,[Oe],n,!0),Go(),i=r.element,s.isDehydrated)if(s={element:i,isDehydrated:!1,cache:r.cache},t.updateQueue.baseState=s,t.memoizedState=s,t.flags&256){t=$_(e,t,i,n);break t}else if(i!==a){a=ei(Error(q(424)),t),tl(a),t=$_(e,t,i,n);break t}else{switch(e=t.stateNode.containerInfo,e.nodeType){case 9:e=e.body;break;default:e=e.nodeName==="HTML"?e.ownerDocument.body:e}for(_e=ai(e.firstChild),qe=t,zt=!0,Na=null,ni=!0,n=nS(t,null,i,n),t.child=n;n;)n.flags=n.flags&-3|134221824,n=n.sibling}else{if(Es(),i===a){t=na(e,t,n);break t}Ie(e,t,i,n)}t=t.child}return t;case 26:return rr(e,t),e===null?(n=Rg(t.type,null,t.pendingProps,null))?t.memoizedState=n:zt||(t.stateNode=Py(t.type,t.pendingProps,Ua.current,t)):t.memoizedState=Rg(t.type,e.memoizedProps,t.pendingProps,e.memoizedState),null;case 27:return Lh(t),e===null&&zt&&(i=t.stateNode=ky(t.type,t.pendingProps,Ua.current),qe=t,ni=!0,a=_e,Qa(t.type)?(Ud=a,_e=ai(i.firstChild)):_e=a),Ie(e,t,t.pendingProps.children,n),rr(e,t),e===null&&(t.flags|=4194304),t.child;case 5:return e===null&&zt&&((a=i=_e)&&(i=qT(i,t.type,t.pendingProps,ni),i!==null?(t.stateNode=i,qe=t,_e=ai(i.firstChild),ni=!1,a=!0):a=!1),a||ka(t)),Lh(t),a=t.type,s=t.pendingProps,r=e!==null?e.memoizedProps:null,i=s.children,Rd(a,s)?i=null:r!==null&&Rd(a,r)&&(t.flags|=32),t.memoizedState!==null&&(a=Zp(e,t,GE,null,null,n),Wr._currentValue=a),rr(e,t),Ie(e,t,i,n),t.child;case 6:return e===null&&zt&&((e=n=_e)&&(n=WT(n,t.pendingProps,ni),n!==null?(t.stateNode=n,qe=t,_e=null,e=!0):e=!1),e||ka(t)),null;case 13:return YS(e,t,n);case 4:return Ku(t,t.stateNode.containerInfo),i=t.pendingProps,e===null?t.child=Rs(t,null,i,n):Ie(e,t,i,n),t.child;case 11:return W_(e,t,t.type,t.pendingProps,n);case 7:return i=t.pendingProps,rr(e,t),Ie(e,t,i,n),t.child;case 8:return Ie(e,t,t.pendingProps.children,n),t.child;case 12:return Ie(e,t,t.pendingProps.children,n),t.child;case 10:return ng(e,t,n);case 9:return a=t.type._context,i=t.pendingProps.children,bs(t),a=Qe(a),i=i(a),t.flags|=1,Ie(e,t,i,n),t.child;case 14:return j_(e,t,t.type,t.pendingProps,n);case 15:return XS(e,t,t.type,t.pendingProps,n);case 19:return rd(e,t,n);case 31:return KE(e,t,n);case 22:return kS(e,t,n,t.pendingProps);case 24:return bs(t),i=Qe(Oe),e===null?(a=Xp(),a===null&&(a=he,s=Vp(),a.pooledCache=s,s.refCount++,s!==null&&(a.pooledCacheLanes|=n),a=s),t.memoizedState={parent:i,cache:a},Yp(t),Ra(t,Oe,a)):(e.lanes&n&&(Wh(e,t),Vo(t,null,null,n),Go()),a=e.memoizedState,s=t.memoizedState,a.parent!==i?(a={parent:i,cache:i},t.memoizedState=a,t.lanes===0&&(t.memoizedState=t.updateQueue.baseState=a),Ra(t,Oe,i)):(i=s.cache,Ra(t,Oe,i),i!==a.cache&&Yh(t,[Oe],n,!0))),Ie(e,t,t.pendingProps.children,n),t.child;case 30:return t.stateNode===null&&(t.stateNode={autoName:null,paired:null,clones:null,ref:null}),i=t.pendingProps,i.name!=null&&i.name!=="auto"?t.flags|=e===null?18882560:18874368:zt&&Gc(t),e!==null&&e.memoizedProps.name!==i.name?t.flags|=4194816:rr(e,t),Ie(e,t,i.children,n),t.child;case 29:throw t.pendingProps}throw Error(q(156,t.tag))}function Fi(e){e.flags|=4}function Df(e,t,n,i,a){var s;if((s=(e.mode&32)!==0)&&(s=n===null?Dg(t,i):Dg(t,i)&&(i.src!==n.src||i.srcSet!==n.srcSet)),s){if(e.flags|=16777216,(a&335544128)===a)if(e.stateNode.complete)e.flags|=8192;else if(xy())e.flags|=8192;else throw xs=sc,kp}else e.flags&=-16777217}function ig(e,t){if(t.type!=="stylesheet"||t.state.loading&4)e.flags&=-16777217;else if(e.flags|=16777216,!jy(t))if(xy())e.flags|=8192;else throw xs=sc,kp}function Xl(e,t){t!==null&&(e.flags|=4),e.flags&16384&&(t=e.tag!==22?gv():536870912,e.lanes|=t,Gr|=t)}function _o(e,t){if(!zt)switch(e.tailMode){case"visible":break;case"collapsed":for(var n=e.tail,i=null;n!==null;)n.alternate!==null&&(i=n),n=n.sibling;i===null?t||e.tail===null?e.tail=null:e.tail.sibling=null:i.sibling=null;break;default:for(t=e.tail,n=null;t!==null;)t.alternate!==null&&(n=t),t=t.sibling;n===null?e.tail=null:n.sibling=null}}function me(e){var t=e.alternate!==null&&e.alternate.child===e.child,n=0,i=0;if(t)for(var a=e.child;a!==null;)n|=a.lanes|a.childLanes,i|=a.subtreeFlags&1206910976,i|=a.flags&1206910976,a.return=e,a=a.sibling;else for(a=e.child;a!==null;)n|=a.lanes|a.childLanes,i|=a.subtreeFlags,i|=a.flags,a.return=e,a=a.sibling;return e.subtreeFlags|=i,e.childLanes=n,t}function $E(e,t,n){var i=t.pendingProps;switch(Gp(t),t.tag){case 16:case 15:case 0:case 11:case 7:case 8:case 12:case 9:case 14:return me(t),null;case 1:return me(t),null;case 3:return n=t.stateNode,i=null,e!==null&&(i=e.memoizedState.cache),t.memoizedState.cache!==i&&(t.flags|=2048),Qi(Oe),Ir(),n.pendingContext&&(n.context=n.pendingContext,n.pendingContext=null),(e===null||e.child===null)&&(Vs(t)?Fi(t):e===null||e.memoizedState.isDehydrated&&!(t.flags&256)||(t.flags|=1024,bf())),me(t),null;case 26:var a=t.type,s=t.memoizedState;return e===null?(Fi(t),s!==null?(me(t),ig(t,s)):(me(t),Df(t,a,null,i,n))):s?s!==e.memoizedState?(Fi(t),me(t),ig(t,s)):(me(t),t.flags&=-16777217):(e=e.memoizedProps,e!==i&&Fi(t),me(t),Df(t,a,e,i,n)),null;case 27:if(Qu(t),n=Ua.current,a=t.type,e!==null&&t.stateNode!=null)e.memoizedProps!==i&&Fi(t);else{if(!i){if(t.stateNode===null)throw Error(q(166));return me(t),t.subtreeFlags&=-33554433,null}e=Ni.current,Vs(t)?D_(t):(e=ky(a,i,n),t.stateNode=e,Fi(t))}return me(t),t.subtreeFlags&=-33554433,null;case 5:if(Qu(t),a=t.type,e!==null&&t.stateNode!=null)e.memoizedProps!==i&&Fi(t);else{if(!i){if(t.stateNode===null)throw Error(q(166));return me(t),t.subtreeFlags&=-33554433,null}if(s=Ni.current,Vs(t))D_(t);else{var r=rl(Ua.current);switch(s){case 1:s=r.createElementNS("http://www.w3.org/2000/svg",a);break;case 2:s=r.createElementNS("http://www.w3.org/1998/Math/MathML",a);break;default:switch(a){case"svg":s=r.createElementNS("http://www.w3.org/2000/svg",a);break;case"math":s=r.createElementNS("http://www.w3.org/1998/Math/MathML",a);break;case"script":s=r.createElement("div"),s.innerHTML="<script><\/script>",s=s.removeChild(s.firstChild);break;case"select":s=typeof i.is=="string"?r.createElement("select",{is:i.is}):r.createElement("select"),i.multiple?s.multiple=!0:i.size&&(s.size=i.size);break;default:s=typeof i.is=="string"?r.createElement(a,{is:i.is}):r.createElement(a)}}s[Ke]=t,s[Cn]=i;t:for(r=t.child;r!==null;){if(r.tag===5||r.tag===6)s.appendChild(r.stateNode);else if(r.tag!==4&&r.tag!==27&&r.child!==null){r.child.return=r,r=r.child;continue}if(r===t)break t;for(;r.sibling===null;){if(r.return===null||r.return===t)break t;r=r.return}r.sibling.return=r.return,r=r.sibling}t.stateNode=s;t:switch(tn(s,a,i),a){case"button":case"input":case"select":case"textarea":i=!!i.autoFocus;break t;case"img":i=!0;break t;default:i=!1}i&&Fi(t)}}return me(t),t.subtreeFlags&=-33554433,Df(t,t.type,e===null?null:e.memoizedProps,t.pendingProps,n),null;case 6:if(e&&t.stateNode!=null)e.memoizedProps!==i&&Fi(t);else{if(typeof i!="string"&&t.stateNode===null)throw Error(q(166));if(e=Ua.current,Vs(t)){if(e=t.stateNode,n=t.memoizedProps,i=null,a=qe,a!==null)switch(a.tag){case 27:case 5:i=a.memoizedProps}e[Ke]=t,e=!!(e.nodeValue===n||i!==null&&i.suppressHydrationWarning===!0||Ly(e.nodeValue,n)),e||ka(t,!0)}else e=rl(e).createTextNode(i),e[Ke]=t,t.stateNode=e}return me(t),null;case 31:if(n=t.memoizedState,e===null||e.memoizedState!==null){if(i=Vs(t),n!==null){if(e===null){if(!i)throw Error(q(318));if(e=t.memoizedState,e=e!==null?e.dehydrated:null,!e)throw Error(q(557));e[Ke]=t}else Es(),!(t.flags&128)&&(t.memoizedState=null),t.flags|=4;me(t),e=!1}else n=bf(),e!==null&&e.memoizedState!==null&&(e.memoizedState.hydrationErrors=n),e=!0;if(!e)return t.flags&256?(Bn(t),t):(Bn(t),null);if(t.flags&128)throw Error(q(558))}return me(t),null;case 13:if(i=t.memoizedState,e===null||e.memoizedState!==null&&e.memoizedState.dehydrated!==null){if(a=Vs(t),i!==null&&i.dehydrated!==null){if(e===null){if(!a)throw Error(q(318));if(a=t.memoizedState,a=a!==null?a.dehydrated:null,!a)throw Error(q(317));a[Ke]=t}else Es(),!(t.flags&128)&&(t.memoizedState=null),t.flags|=4;me(t),a=!1}else a=bf(),e!==null&&e.memoizedState!==null&&(e.memoizedState.hydrationErrors=a),a=!0;if(!a)return t.flags&256?(Bn(t),t):(Bn(t),null)}return Bn(t),t.flags&128?(t.lanes=n,t):(n=i!==null,e=e!==null&&e.memoizedState!==null,n&&(i=t.child,a=null,i.alternate!==null&&i.alternate.memoizedState!==null&&i.alternate.memoizedState.cachePool!==null&&(a=i.alternate.memoizedState.cachePool.pool),s=null,i.memoizedState!==null&&i.memoizedState.cachePool!==null&&(s=i.memoizedState.cachePool.pool),s!==a&&(i.flags|=2048)),n!==e&&n&&(t.child.flags|=8192),Xl(t,t.updateQueue),me(t),null);case 4:return Ir(),e===null&&gm(t.stateNode.containerInfo),t.flags|=67108864,me(t),null;case 10:return Qi(t.type),me(t),null;case 19:if(Wp(t),i=t.memoizedState,i===null)return me(t),null;if(a=(t.flags&128)!==0,s=i.rendering,s===null)if(a)_o(i,!1);else{if(Re!==0||e!==null&&e.flags&128)for(e=t.child;e!==null;){if(s=oc(e),s!==null){for(t.flags|=128,_o(i,!1),e=s.updateQueue,t.updateQueue=e,Xl(t,e),t.subtreeFlags=0,e=n,n=t.child;n!==null;)jv(n,e),n=n.sibling;return nl(t,$e.current&1|2),zt&&qi(t,i.treeForkCount),t.child}e=e.sibling}i.tail!==null&&Gn()>gc&&(t.flags|=128,a=!0,_o(i,!1),t.lanes=4194304)}else{if(!a)if(e=oc(s),e!==null){if(t.flags|=128,a=!0,e=e.updateQueue,t.updateQueue=e,Xl(t,e),_o(i,!0),i.tail===null&&i.tailMode!=="collapsed"&&i.tailMode!=="visible"&&!s.alternate&&!zt)return me(t),null}else 2*Gn()-i.renderingStartTime>gc&&n!==536870912&&(t.flags|=128,a=!0,_o(i,!1),t.lanes=4194304);i.isBackwards?(s.sibling=t.child,t.child=s):(e=i.last,e!==null?e.sibling=s:t.child=s,i.last=s)}if(i.tail!==null){e=i.tail;t:{for(n=e;n!==null;){if(n.alternate!==null){n=!1;break t}n=n.sibling}n=!0}return i.rendering=e,i.tail=e.sibling,i.renderingStartTime=Gn(),e.sibling=null,s=$e.current,s=a?s&1|2:s&1,i.tailMode==="visible"||i.tailMode==="collapsed"||!n||zt?nl(t,s):(n=s,ve(nn,t),ve($e,n),rn===null&&(rn=t)),zt&&qi(t,i.treeForkCount),e}return me(t),null;case 22:case 23:return Bn(t),qp(),i=t.memoizedState!==null,e!==null?e.memoizedState!==null!==i&&(t.flags|=8192):i&&(t.flags|=8192),i?n&536870912&&!(t.flags&128)&&(me(t),t.subtreeFlags&6&&(t.flags|=8192)):me(t),n=t.updateQueue,n!==null&&Xl(t,n.retryQueue),n=null,e!==null&&e.memoizedState!==null&&e.memoizedState.cachePool!==null&&(n=e.memoizedState.cachePool.pool),i=null,t.memoizedState!==null&&t.memoizedState.cachePool!==null&&(i=t.memoizedState.cachePool.pool),i!==n&&(t.flags|=2048),e!==null&&Je(ys),null;case 24:return n=null,e!==null&&(n=e.memoizedState.cache),t.memoizedState.cache!==n&&(t.flags|=2048),Qi(Oe),me(t),null;case 25:return null;case 30:return t.flags|=33554432,me(t),null}throw Error(q(156,t.tag))}function tT(e,t){switch(Gp(t),t.tag){case 1:return e=t.flags,e&65536?(t.flags=e&-65537|128,t):null;case 3:return Qi(Oe),Ir(),e=t.flags,e&65536&&!(e&128)?(t.flags=e&-65537|128,t):null;case 26:case 27:case 5:return Qu(t),null;case 31:if(t.memoizedState!==null){if(Bn(t),t.alternate===null)throw Error(q(340));Es()}return e=t.flags,e&65536?(t.flags=e&-65537|128,t):null;case 13:if(Bn(t),e=t.memoizedState,e!==null&&e.dehydrated!==null){if(t.alternate===null)throw Error(q(340));Es()}return e=t.flags,e&65536?(t.flags=e&-65537|128,t):null;case 19:return Wp(t),e=t.flags,e&65536?(t.flags=e&-65537|128,e=t.memoizedState,e!==null&&(e.rendering=null,e.tail=null),t.flags|=4,t):null;case 4:return Ir(),null;case 10:return Qi(t.type),null;case 22:case 23:return Bn(t),qp(),e!==null&&Je(ys),e=t.flags,e&65536?(t.flags=e&-65537|128,t):null;case 24:return Qi(Oe),null;case 25:return null;default:return null}}function WS(e,t){switch(Gp(t),t.tag){case 3:Qi(Oe),Ir();break;case 26:case 27:case 5:Qu(t);break;case 4:Ir();break;case 31:t.memoizedState!==null&&Bn(t);break;case 13:Bn(t);break;case 19:Wp(t);break;case 10:Qi(t.type);break;case 22:case 23:Bn(t),qp(),e!==null&&Je(ys);break;case 24:Qi(Oe)}}function yl(e,t){try{var n=t.updateQueue,i=n!==null?n.lastEffect:null;if(i!==null){var a=i.next;n=a;do{if((n.tag&e)===e){i=void 0;var s=n.create,r=n.inst;i=s(),r.destroy=i}n=n.next}while(n!==a)}}catch(o){le(t,t.return,o)}}function qa(e,t,n){try{var i=t.updateQueue,a=i!==null?i.lastEffect:null;if(a!==null){var s=a.next;i=s;do{if((i.tag&e)===e){var r=i.inst,o=r.destroy;if(o!==void 0){r.destroy=void 0,a=t;var l=n,u=o;try{u()}catch(h){le(a,l,h)}}}i=i.next}while(i!==s)}}catch(h){le(t,t.return,h)}}function jS(e){var t=e.updateQueue;if(t!==null){var n=e.stateNode;try{aS(t,n)}catch(i){le(e,e.return,i)}}}function ZS(e,t,n){n.props=ws(e.type,e.memoizedProps),n.state=e.memoizedState;try{n.componentWillUnmount()}catch(i){le(e,t,i)}}function bi(e,t){try{var n=e.ref;if(n!==null){switch(e.tag){case 26:case 27:case 5:var i=e.stateNode;break;case 30:var a=e.stateNode,s=$i(e.memoizedProps,a);(a.ref===null||a.ref.name!==s)&&(a.ref=By(s)),i=a.ref;break;case 7:if(e.stateNode===null){var r=new qn(e);Rn(e.child,!1,kT,r,void 0,void 0),e.stateNode=r}i=e.stateNode;break;default:i=e.stateNode}typeof n=="function"?e.refCleanup=n(i):n.current=i}}catch(o){le(e,t,o)}}function Ze(e,t){var n=e.ref,i=e.refCleanup;if(n!==null)if(typeof i=="function")try{i()}catch(a){le(e,t,a)}finally{e.refCleanup=null,e=e.alternate,e!=null&&(e.refCleanup=null)}else if(typeof n=="function")try{n(null)}catch(a){le(e,t,a)}else n.current=null}function hc(e,t){if((e.tag===5||e.tag===27||e.tag===6)&&e.alternate===null&&t!==null)for(var n=0;n<t.length;n++)Vy(e.stateNode,t[n])}function ag(e){for(var t=e.return;t!==null&&(cm(t)&&Vy(e.stateNode,t.stateNode),!um(t));)t=t.return}function Yo(e){for(var t=e.return;t!==null&&(cm(t)&&YT(e.stateNode,t.stateNode),!um(t));)t=t.return}function um(e){return e.tag===5||e.tag===3||e.tag===27}function cm(e){return e&&e.tag===7&&e.stateNode!==null}function od(e){var t=e.type,n=e.memoizedProps,i=e.stateNode;try{t:switch(t){case"button":case"input":case"select":case"textarea":n.autoFocus&&i.focus();break t;case"img":n.src?i.src=n.src:n.srcSet&&(i.srcset=n.srcSet)}}catch(a){le(e,e.return,a)}}function Uf(e,t,n){try{var i=e.stateNode;AT(i,e.type,n,t),i[Cn]=t}catch(a){le(e,e.return,a)}}function KS(e){return e.tag===5||e.tag===3||e.tag===26||e.tag===27&&Qa(e.type)||e.tag===4}function Nf(e){t:for(;;){for(;e.sibling===null;){if(e.return===null||KS(e.return))return null;e=e.return}for(e.sibling.return=e.return,e=e.sibling;e.tag!==5&&e.tag!==6&&e.tag!==18;){if(e.tag===27&&Qa(e.type)||e.flags&2||e.child===null||e.tag===4)continue t;e.child.return=e,e=e.child}if(!(e.flags&2))return e.stateNode}}function ld(e,t,n,i){var a=e.tag;if(a===5||a===6)a=e.stateNode,t?(n.nodeType===9?n.body:n.nodeName==="HTML"?n.ownerDocument.body:n).insertBefore(a,t):(t=n.nodeType===9?n.body:n.nodeName==="HTML"?n.ownerDocument.body:n,t.appendChild(a),n=n._reactRootContainer,n!=null||t.onclick!==null||(t.onclick=wi)),hc(e,i),Qt=!0;else if(a!==4&&(a===27&&(hc(e,i),i=null,Qa(e.type)&&(n=e.stateNode,t=null)),e=e.child,e!==null))for(ld(e,t,n,i),e=e.sibling;e!==null;)ld(e,t,n,i),e=e.sibling}function dc(e,t,n,i){var a=e.tag;if(a===5||a===6)a=e.stateNode,t?n.insertBefore(a,t):n.appendChild(a),hc(e,i),Qt=!0;else if(a!==4&&(a===27&&(hc(e,i),i=null,Qa(e.type)&&(n=e.stateNode)),e=e.child,e!==null))for(dc(e,t,n,i),e=e.sibling;e!==null;)dc(e,t,n,i),e=e.sibling}function QS(e){var t=e.stateNode,n=e.memoizedProps;try{for(var i=e.type,a=t.attributes;a.length;)t.removeAttributeNode(a[0]);tn(t,i,n),t[Ke]=e,t[Cn]=n}catch(s){le(e,e.return,s)}}var pc=!1,Fn=null;function sg(e){(e.tag===30||e.subtreeFlags&33554432)&&(pc=!0)}var Ri=null;function rg(){var e=Ri;return Ri=null,e}var xn=0;function ro(e,t,n,i,a){return xn=0,JS(e.child,t,n,i,a)}function JS(e,t,n,i,a){for(var s=!1;e!==null;){if(e.tag===5){var r=e.stateNode;if(i!==null){var o=Cd(r);i.push(o),o.view&&(s=!0)}else s||Cd(r).view&&(s=!0);pc=!0,zy(r,xn===0?t:t+"_"+xn,n),xn++}else(e.tag!==22||e.memoizedState===null)&&(e.tag===30&&a||JS(e.child,t,n,i,a)&&(s=!0));e=e.sibling}return s}function Oi(e,t){for(;e!==null;)e.tag===5?Iy(e.stateNode,e.memoizedProps):(e.tag!==22||e.memoizedState===null)&&(e.tag===30&&t||Oi(e.child,t)),e=e.sibling}function Nu(e){if(e.subtreeFlags&18874368)for(e=e.child;e!==null;){if((e.tag!==22||e.memoizedState===null)&&(Nu(e),e.tag===30&&(e.flags&18874368)!==0&&e.stateNode.paired)){var t=e.memoizedProps;if(t.name==null||t.name==="auto")throw Error(q(544));var n=t.name;t=oa(t.default,t.share),t!=="none"&&(ro(e,n,t,null,!1)||Oi(e.child,!1))}e=e.sibling}}function ud(e,t){if(e.tag===30){var n=e.stateNode,i=e.memoizedProps,a=$i(i,n),s=oa(i.default,n.paired?i.share:i.enter);s!=="none"?ro(e,a,s,null,!1)?(Nu(e),n.paired||t||Vr(e,i.onEnter)):Oi(e.child,!1):Nu(e)}else if(e.subtreeFlags&33554432)for(e=e.child;e!==null;)ud(e,t),e=e.sibling;else Nu(e)}function cd(e){if(Fn!==null&&Fn.size!==0){var t=Fn;if(e.subtreeFlags&18874368)for(e=e.child;e!==null;){if(e.tag!==22||e.memoizedState===null){if(e.tag===30&&e.flags&18874368){var n=e.memoizedProps,i=n.name;if(i!=null&&i!=="auto"){var a=t.get(i);if(a!==void 0){var s=oa(n.default,n.share);if(s!=="none"&&(ro(e,i,s,null,!1)?(s=e.stateNode,a.paired=s,s.paired=a,Vr(e,n.onShare)):Oi(e.child,!1)),t.delete(i),t.size===0)break}}}cd(e)}e=e.sibling}}}function fd(e){if(e.tag===30){var t=e.memoizedProps,n=$i(t,e.stateNode),i=Fn!==null?Fn.get(n):void 0,a=oa(t.default,i!==void 0?t.share:t.exit);a!=="none"&&(ro(e,n,a,null,!1)?i!==void 0?(a=e.stateNode,i.paired=a,a.paired=i,Fn.delete(n),Vr(e,t.onShare)):Vr(e,t.onExit):Oi(e.child,!1)),Fn!==null&&cd(e)}else if(e.subtreeFlags&33554432)for(e=e.child;e!==null;)fd(e),e=e.sibling;else Fn!==null&&cd(e)}function $S(e){for(e=e.child;e!==null;){if(e.tag===30){var t=e.memoizedProps,n=$i(t,e.stateNode);t=oa(t.default,t.update),e.flags&=-5,t!=="none"&&ro(e,n,t,e.memoizedState=[],!1)}else e.subtreeFlags&33554432&&$S(e);e=e.sibling}}function hd(e){if(e.subtreeFlags&18874368)for(e=e.child;e!==null;){if(e.tag!==22||e.memoizedState===null){if(e.tag===30&&e.flags&18874368){var t=e.stateNode;t.paired!==null&&(t.paired=null,Oi(e.child,!1))}hd(e)}e=e.sibling}}function Lu(e){if(e.tag===30)e.stateNode.paired=null,Oi(e.child,!1),hd(e);else if(e.subtreeFlags&33554432)for(e=e.child;e!==null;)Lu(e),e=e.sibling;else hd(e)}function ty(e){for(e=e.child;e!==null;)e.tag===30?Oi(e.child,!1):e.subtreeFlags&33554432&&ty(e),e=e.sibling}function fm(e,t,n,i,a,s,r){for(var o=!1;t!==null;){if(t.tag===5){var l=t.stateNode;if(s!==null&&xn<s.length){var u=s[xn],h=Cd(l);(u.view||h.view)&&(o=!0);var p;if(p=(e.flags&4)===0)if(h.clip)p=!0;else{p=u.rect;var f=h.rect;p=p.y!==f.y||p.x!==f.x||p.height!==f.height||p.width!==f.width}p&&(e.flags|=4),h.abs?h=!u.abs:(u=u.rect,h=h.rect,h=u.height!==h.height||u.width!==h.width),h&&(e.flags|=32)}else e.flags|=32;e.flags&4&&zy(l,xn===0?n:n+"_"+xn,a),o&&e.flags&4||(Ri===null&&(Ri=[]),Ri.push(l,xn===0?i:i+"_"+xn,t.memoizedProps)),xn++}else(t.tag!==22||t.memoizedState===null)&&(t.tag===30&&r?e.flags|=t.flags&32:fm(e,t.child,n,i,a,s,r)&&(o=!0));t=t.sibling}return o}function ey(e,t){for(e=e.child;e!==null;){if(e.tag===30){var n=e.memoizedProps,i=e.stateNode,a=$i(n,i),s=oa(n.default,n.update),r;r=e.memoizedState,e.memoizedState=null,i=e;var o=e.child;xn=0,a=fm(i,o,a,a,s,r,!1),e.flags&4&&a&&Vr(e,n.onUpdate)}else e.subtreeFlags&33554432&&ey(e);e=e.sibling}}var Xe=!1,ie=!1,xi=!1,Lf=!1,og=typeof WeakSet=="function"?WeakSet:Set,ke=null,Mi=!1,Uo=!1,mc=!1,dd=!1;function eT(e,t,n){if(e=e.containerInfo,bd=jr,e=Hv(e),Ip(e)){if("selectionStart"in e)var i={start:e.selectionStart,end:e.selectionEnd};else t:{i=(i=e.ownerDocument)&&i.defaultView||window;var a=i.getSelection&&i.getSelection();if(a&&a.rangeCount!==0){i=a.anchorNode;var s=a.anchorOffset,r=a.focusNode;a=a.focusOffset;try{i.nodeType,r.nodeType}catch{i=null;break t}var o=0,l=-1,u=-1,h=0,p=0,f=e,d=null;e:for(;;){for(var v;f!==i||s!==0&&f.nodeType!==3||(l=o+s),f!==r||a!==0&&f.nodeType!==3||(u=o+a),f.nodeType===3&&(o+=f.nodeValue.length),(v=f.firstChild)!==null;)d=f,f=v;for(;;){if(f===e)break e;if(d===i&&++h===s&&(l=o),d===r&&++p===a&&(u=o),(v=f.nextSibling)!==null)break;f=d,d=f.parentNode}f=v}i=l===-1||u===-1?null:{start:l,end:u}}else i=null}i=i||{start:0,end:0}}else i=null;for(Ad={focusedElem:e,selectionRange:i},jr=!1,n=(n&335544064)===n,ke=t,t=n?9270:1024;ke!==null;){if(e=ke,n&&(i=e.deletions,i!==null))for(s=0;s<i.length;s++)n&&fd(i[s]);if(e.alternate===null&&e.flags&2)n&&sg(e),kl(n);else{if(e.tag===22){if(i=e.alternate,e.memoizedState!==null){i!==null&&i.memoizedState===null&&n&&fd(i),kl(n);continue}else if(i!==null&&i.memoizedState!==null){n&&sg(e),kl(n);continue}}i=e.child,e.subtreeFlags&t&&i!==null?(i.return=e,ke=i):(n&&$S(e),kl(n))}}Fn=null}function kl(e){for(;ke!==null;){var t=ke,n=e,i=t.alternate,a=t.flags;switch(t.tag){case 0:case 11:case 15:break;case 1:if(a&1024&&i!==null){n=void 0,a=i.memoizedProps,i=i.memoizedState;var s=t.stateNode;try{var r=ws(t.type,a);n=s.getSnapshotBeforeUpdate(r,i),s.__reactInternalSnapshotBeforeUpdate=n}catch(o){le(t,t.return,o)}}break;case 3:if(a&1024){if(i=t.stateNode.containerInfo,n=i.nodeType,n===9)wd(i);else if(n===1)switch(i.nodeName){case"HEAD":case"HTML":case"BODY":wd(i);break;default:i.textContent=""}}break;case 5:case 26:case 27:case 6:case 4:case 17:break;case 30:n&&i!==null&&(n=$i(i.memoizedProps,i.stateNode),a=t.memoizedProps,a=oa(a.default,a.update),a!=="none"&&ro(i,n,a,i.memoizedState=[],!0));break;default:if(a&1024)throw Error(q(163))}if(i=t.sibling,i!==null){i.return=t.return,ke=i;break}ke=t.return}}function ny(e,t,n){var i=n.flags;switch(n.tag){case 0:case 11:case 15:Ei(e,n),i&4&&yl(5,n);break;case 1:if(Ei(e,n),i&4)if(e=n.stateNode,t===null)try{e.componentDidMount()}catch(r){le(n,n.return,r)}else{var a=ws(n.type,t.memoizedProps);t=t.memoizedState;try{e.componentDidUpdate(a,t,e.__reactInternalSnapshotBeforeUpdate)}catch(r){le(n,n.return,r)}}i&64&&jS(n),i&512&&bi(n,n.return);break;case 3:if(Ei(e,n),i&64&&(e=n.updateQueue,e!==null)){if(t=null,n.child!==null)switch(n.child.tag){case 27:case 5:t=n.child.stateNode;break;case 1:t=n.child.stateNode}try{aS(e,t)}catch(r){le(n,n.return,r)}}break;case 27:t===null&&i&4&&QS(n);case 26:case 5:Ei(e,n),t===null&&i&4&&od(n),i&512&&bi(n,n.return);break;case 12:Ei(e,n);break;case 31:Ei(e,n),i&4&&ry(e,n);break;case 13:Ei(e,n),i&4&&oy(e,n),i&64&&(e=n.memoizedState,e!==null&&(e=e.dehydrated,e!==null&&(n=dT.bind(null,n),jT(e,n))));break;case 22:if(i=n.memoizedState!==null||Xe,!i){var s=t!==null&&t.memoizedState!==null||ie;t=Xe,a=ie,Xe=i,(ie=s)&&!a?(i=2,n.subtreeFlags&8772&&(i|=1),hi(e,n,i)):Ei(e,n),Xe=t,ie=a}break;case 30:Ei(e,n),i&512&&bi(n,n.return);break;case 7:i&512&&bi(n,n.return);default:Ei(e,n)}}function pd(e,t){for(e=e.child;e!==null;)iy(e,t),e=e.sibling}function iy(e,t){switch(e.tag){case 5:case 26:try{var n=e.stateNode;if(t){var i=n.style;typeof i.setProperty=="function"?i.setProperty("display","none","important"):i.display="none"}else{var a=e.stateNode,s=e.memoizedProps.style,r=s!=null&&s.hasOwnProperty("display")?s.display:null;a.style.display=r==null||typeof r=="boolean"?"":(""+r).trim()}}catch(l){le(e,e.return,l)}md(e,t);break;case 6:try{e.stateNode.nodeValue=t?"":e.memoizedProps,Qt=!0}catch(l){le(e,e.return,l)}break;case 18:try{var o=e.stateNode;t?xg(o,!0):xg(e.stateNode,!1)}catch(l){le(e,e.return,l)}break;case 22:case 23:e.memoizedState===null&&pd(e,t);break;default:pd(e,t)}}function md(e,t){if(e.subtreeFlags&67108864)for(e=e.child;e!==null;){t:{var n=e,i=t;switch(n.tag){case 4:iy(n,i);break t;case 22:n.memoizedState===null&&md(n,i);break t;default:md(n,i)}}e=e.sibling}}function ay(e){var t=e.alternate;t!==null&&(e.alternate=null,ay(t)),e.child=null,e.deletions=null,e.sibling=null,e.tag===5&&(t=e.stateNode,t!==null&&Pc(t)),e.stateNode=null,e.return=null,e.dependencies=null,e.memoizedProps=null,e.memoizedState=null,e.pendingProps=null,e.stateNode=null,e.updateQueue=null}var Me=null,Sn=!1;function li(e,t,n){for(n=n.child;n!==null;)sy(e,t,n),n=n.sibling}function sy(e,t,n){if(Vn&&typeof Vn.onCommitFiberUnmount=="function")try{Vn.onCommitFiberUnmount(dl,n)}catch{}switch(n.tag){case 26:ie||Ze(n,t),li(e,t,n),n.memoizedState?n.memoizedState.count--:n.stateNode&&!ie&&(n=n.stateNode,n.parentNode.removeChild(n));break;case 27:ie||Ze(n,t),Yo(n);var i=Me,a=Sn;Qa(n.type)&&(Me=n.stateNode,Sn=!1),li(e,t,n),Yy(n.stateNode,n.type,n.memoizedProps),Me=i,Sn=a;break;case 5:ie||Ze(n,t),Yo(n);case 6:if(n.tag===6&&Yo(n),i=Me,a=Sn,Me=null,li(e,t,n),Me=i,Sn=a,Me!==null)if(Sn)try{(Me.nodeType===9?Me.body:Me.nodeName==="HTML"?Me.ownerDocument.body:Me).removeChild(n.stateNode),Qt=!0}catch(s){le(n,t,s)}else try{Me.removeChild(n.stateNode),Qt=!0}catch(s){le(n,t,s)}break;case 18:Me!==null&&(Sn?(e=Me,yg(e.nodeType===9?e.body:e.nodeName==="HTML"?e.ownerDocument.body:e,n.stateNode),Zr(e)):yg(Me,n.stateNode));break;case 4:i=Me,a=Sn,Me=n.stateNode.containerInfo,Sn=!0,li(e,t,n),Me=i,Sn=a;break;case 0:case 11:case 14:case 15:qa(2,n,t),ie||qa(4,n,t),li(e,t,n);break;case 1:ie||(Ze(n,t),i=n.stateNode,typeof i.componentWillUnmount=="function"&&ZS(n,t,i)),li(e,t,n);break;case 21:li(e,t,n);break;case 22:ie=(i=ie)||n.memoizedState!==null,li(e,t,n),ie=i;break;case 30:Ze(n,t),li(e,t,n);break;case 7:ie||Ze(n,t),li(e,t,n);break;default:li(e,t,n)}}function ry(e,t){if(t.memoizedState===null&&(e=t.alternate,e!==null&&(e=e.memoizedState,e!==null))){e=e.dehydrated;try{Zr(e)}catch(n){le(t,t.return,n)}}}function oy(e,t){if(t.memoizedState===null&&(e=t.alternate,e!==null&&(e=e.memoizedState,e!==null&&(e=e.dehydrated,e!==null))))try{Zr(e)}catch(n){le(t,t.return,n)}}function nT(e){switch(e.tag){case 31:case 13:case 19:var t=e.stateNode;return t===null&&(t=e.stateNode=new og),t;case 22:return e=e.stateNode,t=e._retryCache,t===null&&(t=e._retryCache=new og),t;default:throw Error(q(435,e.tag))}}function Yl(e,t){var n=nT(e);t.forEach(function(i){if(!n.has(i)){n.add(i);var a=pT.bind(null,e,i);i.then(a,a)}})}function ln(e,t,n){var i=t.deletions;if(i!==null)for(var a=0;a<i.length;a++){var s=i[a],r=e,o=t,l=o;t:for(;l!==null;){switch(l.tag){case 27:if(Qa(l.type)){Me=l.stateNode,Sn=!1;break t}break;case 5:Me=l.stateNode,Sn=!1;break t;case 3:case 4:Me=l.stateNode.containerInfo,Sn=!0;break t}l=l.return}if(Me===null)throw Error(q(160));sy(r,o,s),Me=null,Sn=!1,r=s.alternate,r!==null&&(r.return=null),s.return=null}if(t.subtreeFlags&13886)for(t=t.child;t!==null;)ly(t,e,n),t=t.sibling}var di=null;function ly(e,t,n){var i=e.alternate,a=e.flags;switch(e.tag){case 0:case 11:case 14:case 15:if(a&4&&(i=e.updateQueue,i=i!==null?i.events:null,i!==null))for(var s=0;s<i.length;s++){var r=i[s];r.ref.impl=r.nextImpl}ln(t,e,n),un(e),a&4&&(qa(3,e,e.return),yl(3,e),qa(5,e,e.return));break;case 1:ln(t,e,n),un(e),a&512&&(ie||i===null||Ze(i,i.return)),a&64&&Xe&&(e=e.updateQueue,e!==null&&(t=e.callbacks,t!==null&&(n=e.shared.hiddenCallbacks,e.shared.hiddenCallbacks=n===null?t:n.concat(t))));break;case 26:if(s=di,ln(t,e,n),un(e),a&512&&(ie||i===null||Ze(i,i.return)),a&4)if(a=i!==null?i.memoizedState:null,n=e.memoizedState,i===null)if(n===null)if(e.stateNode===null)if(Xe)e.stateNode=Py(e.type,e.memoizedProps,t.containerInfo,e);else{t:{t=e.type,n=e.memoizedProps,a=s.ownerDocument||s;e:switch(t){case"title":i=a.getElementsByTagName("title")[0],(!i||i[_l]||i[Ke]||i.namespaceURI==="http://www.w3.org/2000/svg"||i.hasAttribute("itemprop"))&&(i=a.createElement(t),a.head.insertBefore(i,a.querySelector("head > title"))),tn(i,t,n),i[Ke]=e,Ye(i),t=i;break t;case"link":if(s=wg("link","href",a).get(t+(n.href||""))){for(r=0;r<s.length;r++)if(i=s[r],i.getAttribute("href")===(n.href==null||n.href===""?null:n.href)&&i.getAttribute("rel")===(n.rel==null?null:n.rel)&&i.getAttribute("title")===(n.title==null?null:n.title)&&i.getAttribute("crossorigin")===(n.crossOrigin==null?null:n.crossOrigin)){s.splice(r,1);break e}}i=a.createElement(t),tn(i,t,n),a.head.appendChild(i);break;case"meta":if(s=wg("meta","content",a).get(t+(n.content||""))){for(r=0;r<s.length;r++)if(i=s[r],i.getAttribute("content")===(n.content==null?null:""+n.content)&&i.getAttribute("name")===(n.name==null?null:n.name)&&i.getAttribute("property")===(n.property==null?null:n.property)&&i.getAttribute("http-equiv")===(n.httpEquiv==null?null:n.httpEquiv)&&i.getAttribute("charset")===(n.charSet==null?null:n.charSet)){s.splice(r,1);break e}}i=a.createElement(t),tn(i,t,n),a.head.appendChild(i);break;default:throw Error(q(468,t))}i[Ke]=e,Ye(i),t=i}e.stateNode=t}else Xe||Nd(s,e.type,e.stateNode);else e.stateNode=Cg(s,n,e.memoizedProps);else a!==n?(a===null?(t=i.stateNode,t===null||ie||t.parentNode.removeChild(t)):a.count--,n===null?Xe||Nd(s,e.type,e.stateNode):Cg(s,n,e.memoizedProps)):n===null&&e.stateNode!==null&&Uf(e,e.memoizedProps,i.memoizedProps);break;case 27:ln(t,e,n),un(e),a&512&&(ie||i===null||Ze(i,i.return)),i!==null&&a&4&&Uf(e,e.memoizedProps,i.memoizedProps);break;case 5:if(s=xi,xi=!1,ln(t,e,n),xi=s,un(e),a&512&&(ie||i===null||Ze(i,i.return)),e.flags&32){t=e.stateNode;try{Fr(t,""),Qt=!0}catch(h){le(e,e.return,h)}}a&4&&e.stateNode!=null&&(t=e.memoizedProps,Uf(e,t,i!==null?i.memoizedProps:t)),a&1024&&(Lf=!0);break;case 6:if(ln(t,e,n),un(e),a&4){if(e.stateNode===null)throw Error(q(162));t=e.memoizedProps,n=e.stateNode;try{n.nodeValue=t,Qt=!0}catch(h){le(e,e.return,h)}}break;case 3:if(Qt=!1,Iu=null,s=di,di=ol(t.containerInfo),ln(t,e,n),di=s,un(e),a&4&&i!==null&&i.memoizedState.isDehydrated)try{Zr(t.containerInfo)}catch(h){le(e,e.return,h)}Lf&&(Lf=!1,uy(e)),Qt=!1;break;case 4:a=xi,xi=Xe,i=h_(),s=di,di=ol(e.stateNode.containerInfo),ln(t,e,n),un(e),di=s,Qt&&Uo&&(mc=!0),Qt=i,xi=a;break;case 12:ln(t,e,n),un(e);break;case 31:ln(t,e,n),un(e),a&4&&(t=e.updateQueue,t!==null&&(e.updateQueue=null,Yl(e,t)));break;case 13:ln(t,e,n),un(e),e.child.flags&8192&&e.memoizedState!==null!=(i!==null&&i.memoizedState!==null)&&(jc=Gn()),a&4&&(t=e.updateQueue,t!==null&&(e.updateQueue=null,Yl(e,t)));break;case 22:s=e.memoizedState!==null,r=i!==null&&i.memoizedState!==null;var o=Xe,l=ie,u=xi;Xe=o||s,xi=u||s,ie=l||r,ln(t,e,n),ie=l,xi=u,Xe=o,un(e),a&8192&&(t=e.stateNode,t._visibility=s?t._visibility&-2:t._visibility|1,!s||i===null||r||Xe||ie||(t=r||ie,n=Xe,i=ie,Xe=s||Xe,ie=t,Sa(e,2),Xe=n,ie=i),!s&&xi||pd(e,s)),a&4&&(t=e.updateQueue,t!==null&&(n=t.retryQueue,n!==null&&(t.retryQueue=null,Yl(e,n))));break;case 19:ln(t,e,n),un(e),a&4&&(t=e.updateQueue,t!==null&&(e.updateQueue=null,Yl(e,t)));break;case 30:a&512&&(ie||i===null||Ze(i,i.return)),a=h_(),s=Uo,r=(n&335544064)===n,o=e.memoizedProps,Uo=r&&oa(o.default,o.update)!=="none",ln(t,e,n),un(e),r&&i!==null&&Qt&&(e.flags|=4),Uo=s,Qt=a;break;case 21:break;case 7:a&512&&(ie||i===null||Ze(i,i.return)),i&&i.stateNode!==null&&(i.stateNode._fragmentFiber=e);default:ln(t,e,n),un(e)}}function un(e){var t=e.flags;if(t&2){try{for(var n,i=e.return;i!==null;){if(KS(i)){n=i;break}i=i.return}i=null;for(var a=e.return;a!==null;){if(cm(a)){var s=a.stateNode;i===null?i=[s]:i.push(s)}if(um(a))break;a=a.return}var r=i;if(n==null)throw Error(q(160));switch(n.tag){case 27:var o=n.stateNode,l=Nf(e);dc(e,l,o,r);break;case 5:var u=n.stateNode;n.flags&32&&(Fr(u,""),n.flags&=-33);var h=Nf(e);dc(e,h,u,r);break;case 3:case 4:var p=n.stateNode.containerInfo,f=Nf(e);ld(e,f,p,r);break;default:throw Error(q(161))}}catch(d){le(e,e.return,d)}e.flags&=-3}t&4096&&(e.flags&=-4097)}function uy(e){if(e.subtreeFlags&1024)for(e=e.child;e!==null;){var t=e;uy(t),t.tag===5&&t.flags&1024&&(t=t.stateNode,jr=!0,t.reset(),jr=!1),e=e.sibling}}function Xs(e,t){if(t.subtreeFlags&9270)for(t=t.child;t!==null;)cy(t,e),t=t.sibling;else ey(t)}function cy(e,t){var n=e.alternate;if(n===null)ud(e,!1);else switch(e.tag){case 3:if(dd=Mi=!1,rg(),Xs(t,e),!Mi&&!mc){if(e=Ri,e!==null)for(var i=0;i<e.length;i+=3){n=e[i];var a=e[i+1];Iy(n,e[i+2]),n=n.ownerDocument.documentElement,n!==null&&n.animate({opacity:[0,0],pointerEvents:["none","none"]},{duration:0,fill:"forwards",pseudoElement:"::view-transition-group("+a+")"})}e=t.containerInfo,e=e.nodeType===9?e.documentElement:e.ownerDocument.documentElement,e!==null&&e.style.viewTransitionName===""&&(e.style.viewTransitionName="none",e.animate({opacity:[0,0],pointerEvents:["none","none"]},{duration:0,fill:"forwards",pseudoElement:"::view-transition-group(root)"}),e.animate({width:[0,0],height:[0,0]},{duration:0,fill:"forwards",pseudoElement:"::view-transition"})),dd=!0}Ri=null;break;case 5:Xs(t,e);break;case 4:i=Mi,Mi=!1,Xs(t,e),Mi&&(mc=!0),Mi=i;break;case 22:e.memoizedState===null&&(n.memoizedState!==null?ud(e,!1):Xs(t,e));break;case 30:i=Mi,a=rg(),Mi=!1,Xs(t,e),Mi&&(e.flags|=4);var s=e.memoizedProps,r=e.stateNode;t=$i(s,r),r=$i(n.memoizedProps,r);var o=oa(s.default,s.update);o==="none"?t=!1:(s=n.memoizedState,n.memoizedState=null,n=e.child,xn=0,t=fm(e,n,t,r,o,s,!0),xn!==(s===null?0:s.length)&&(e.flags|=32)),e.flags&4&&t?(Vr(e,e.memoizedProps.onUpdate),Ri=a):a!==null&&(a.push.apply(a,Ri),Ri=a),Mi=e.flags&32?!0:i;break;default:Xs(t,e)}}function Ei(e,t){if(t.subtreeFlags&8772)for(t=t.child;t!==null;)ny(e,t.alternate,t),t=t.sibling}function Sa(e,t){for(e=e.child;e!==null;){var n=e,i=t;switch(n.tag){case 0:case 11:case 14:case 15:qa(4,n,n.return),Sa(n,i);break;case 1:Ze(n,n.return);var a=n.stateNode;typeof a.componentWillUnmount=="function"&&ZS(n,n.return,a),Sa(n,i);break;case 27:i&2&&Yy(n.stateNode,n.type,n.memoizedProps);case 5:Ze(n,n.return),n.tag!==5&&n.tag!==27||Yo(n),Sa(n,i);break;case 6:Yo(n);break;case 26:Ze(n,n.return),a=n.stateNode,n.memoizedState!==null||a===null||ie||a.parentNode.removeChild(a),Sa(n,i);break;case 22:n.memoizedState===null&&Sa(n,i);break;case 30:Ze(n,n.return),Sa(n,i);break;case 7:Ze(n,n.return);default:Sa(n,i)}e=e.sibling}}function hi(e,t,n){for(n=t.subtreeFlags&8772?n:n&-2,t=t.child;t!==null;){var i=t.alternate,a=e,s=t,r=s.flags,o=(n&1)!==0;switch(s.tag){case 0:case 11:case 15:hi(a,s,n),yl(4,s);break;case 1:if(hi(a,s,n),i=s,a=i.stateNode,typeof a.componentDidMount=="function")try{a.componentDidMount()}catch(h){le(i,i.return,h)}if(i=s,a=i.updateQueue,a!==null){var l=i.stateNode;try{var u=a.shared.hiddenCallbacks;if(u!==null)for(a.shared.hiddenCallbacks=null,a=0;a<u.length;a++)iS(u[a],l)}catch(h){le(i,i.return,h)}}o&&r&64&&jS(s),bi(s,s.return);break;case 27:n&2&&QS(s);case 5:s.tag!==5&&s.tag!==27||ag(s),hi(a,s,n),o&&i===null&&r&4&&od(s),bi(s,s.return);break;case 6:ag(s);break;case 26:l=s.stateNode,s.memoizedState!==null||l===null||Xe||Nd(ol(l.ownerDocument),s.type,l),hi(a,s,n),o&&i===null&&r&4&&od(s),bi(s,s.return);break;case 12:hi(a,s,n);break;case 31:hi(a,s,n),o&&r&4&&ry(a,s);break;case 13:hi(a,s,n),o&&r&4&&oy(a,s);break;case 22:s.memoizedState===null&&hi(a,s,n),bi(s,s.return);break;case 30:hi(a,s,n),bi(s,s.return);break;case 7:bi(s,s.return);default:hi(a,s,n)}t=t.sibling}}function hm(e,t){var n=null;e!==null&&e.memoizedState!==null&&e.memoizedState.cachePool!==null&&(n=e.memoizedState.cachePool.pool),e=null,t.memoizedState!==null&&t.memoizedState.cachePool!==null&&(e=t.memoizedState.cachePool.pool),e!==n&&(e!=null&&e.refCount++,n!=null&&vl(n))}function dm(e,t){e=null,t.alternate!==null&&(e=t.alternate.memoizedState.cache),t=t.memoizedState.cache,t!==e&&(t.refCount++,e!=null&&vl(e))}function jn(e,t,n,i){var a=(n&335544064)===n;if(t.subtreeFlags&(a?10262:10256))for(t=t.child;t!==null;)fy(e,t,n,i),t=t.sibling;else a&&ty(t)}function fy(e,t,n,i){var a=(n&335544064)===n;a&&t.alternate===null&&t.return!==null&&t.return.alternate!==null&&Lu(t);var s=t.flags;switch(t.tag){case 0:case 11:case 15:jn(e,t,n,i),s&2048&&yl(9,t);break;case 1:jn(e,t,n,i);break;case 3:jn(e,t,n,i),a&&dd&&(e=e.containerInfo,e=e.nodeType===9?e.body:e.nodeName==="HTML"?e.ownerDocument.body:e,e.style.viewTransitionName==="root"&&(e.style.viewTransitionName=""),e=e.ownerDocument.documentElement,e!==null&&e.style.viewTransitionName==="none"&&(e.style.viewTransitionName="")),s&2048&&(s=null,t.alternate!==null&&(s=t.alternate.memoizedState.cache),t=t.memoizedState.cache,t!==s&&(t.refCount++,s!=null&&vl(s)));break;case 12:if(s&2048){jn(e,t,n,i),s=t.stateNode;try{var r=t.memoizedProps,o=r.id,l=r.onPostCommit;typeof l=="function"&&l(o,t.alternate===null?"mount":"update",s.passiveEffectDuration,-0)}catch(u){le(t,t.return,u)}}else jn(e,t,n,i);break;case 31:jn(e,t,n,i);break;case 13:jn(e,t,n,i);break;case 23:break;case 22:r=t.stateNode,o=t.alternate,t.memoizedState!==null?(a&&o!==null&&o.memoizedState===null&&Lu(o),r._visibility&2?jn(e,t,n,i):qo(e,t)):(a&&o!==null&&o.memoizedState!==null&&Lu(t),r._visibility&2?jn(e,t,n,i):(r._visibility|=2,or(e,t,n,i,(t.subtreeFlags&10256)!==0||!1))),s&2048&&hm(o,t);break;case 24:jn(e,t,n,i),s&2048&&dm(t.alternate,t);break;case 30:a&&(s=t.alternate,s!==null&&(Oi(s.child,!0),Oi(t.child,!0))),jn(e,t,n,i);break;default:jn(e,t,n,i)}}function or(e,t,n,i,a){for(a=a&&((t.subtreeFlags&10256)!==0||!1),t=t.child;t!==null;){var s=e,r=t,o=n,l=i,u=r.flags;switch(r.tag){case 0:case 11:case 15:or(s,r,o,l,a),yl(8,r);break;case 23:break;case 22:var h=r.stateNode;r.memoizedState!==null?h._visibility&2?or(s,r,o,l,a):qo(s,r):(h._visibility|=2,or(s,r,o,l,a)),a&&u&2048&&hm(r.alternate,r);break;case 24:or(s,r,o,l,a),a&&u&2048&&dm(r.alternate,r);break;default:or(s,r,o,l,a)}t=t.sibling}}function qo(e,t){if(t.subtreeFlags&10256)for(t=t.child;t!==null;){var n=e,i=t,a=i.flags;switch(i.tag){case 22:qo(n,i),a&2048&&hm(i.alternate,i);break;case 24:qo(n,i),a&2048&&dm(i.alternate,i);break;default:qo(n,i)}t=t.sibling}}var cs=8192;function es(e,t,n){if(e.subtreeFlags&cs)for(e=e.child;e!==null;)hy(e,t,n),e=e.sibling}function hy(e,t,n){switch(e.tag){case 26:es(e,t,n),e.flags&cs&&(e.memoizedState!==null?lb(n,di,e.memoizedState,e.memoizedProps):(e=e.stateNode,(t&335544128)===t&&Ug(n,e)));break;case 5:es(e,t,n),e.flags&cs&&(e=e.stateNode,(t&335544128)===t&&Ug(n,e));break;case 3:case 4:var i=di;di=ol(e.stateNode.containerInfo),es(e,t,n),di=i;break;case 22:e.memoizedState===null&&(i=e.alternate,i!==null&&i.memoizedState!==null?(i=cs,cs=16777216,es(e,t,n),cs=i):es(e,t,n));break;case 30:if(e.flags&cs&&(i=e.memoizedProps.name,i!=null&&i!=="auto")){var a=e.stateNode;a.paired=null,Fn===null&&(Fn=new Map),Fn.set(i,a)}es(e,t,n);break;default:es(e,t,n)}}function dy(e){var t=e.alternate;if(t!==null&&(e=t.child,e!==null)){t.child=null;do t=e.sibling,e.sibling=null,e=t;while(e!==null)}}function go(e){var t=e.deletions;if(e.flags&16){if(t!==null)for(var n=0;n<t.length;n++){var i=t[n];ke=i,my(i,e)}dy(e)}if(e.subtreeFlags&10256)for(e=e.child;e!==null;)py(e),e=e.sibling}function py(e){switch(e.tag){case 0:case 11:case 15:go(e),e.flags&2048&&qa(9,e,e.return);break;case 3:go(e);break;case 12:go(e);break;case 22:var t=e.stateNode;e.memoizedState!==null&&t._visibility&2&&(e.return===null||e.return.tag!==13)?(t._visibility&=-3,Ou(e)):go(e);break;default:go(e)}}function Ou(e){var t=e.deletions;if(e.flags&16){if(t!==null)for(var n=0;n<t.length;n++){var i=t[n];ke=i,my(i,e)}dy(e)}for(e=e.child;e!==null;){switch(t=e,t.tag){case 0:case 11:case 15:qa(8,t,t.return),Ou(t);break;case 22:n=t.stateNode,n._visibility&2&&(n._visibility&=-3,Ou(t));break;default:Ou(t)}e=e.sibling}}function my(e,t){for(;ke!==null;){var n=ke;switch(n.tag){case 0:case 11:case 15:qa(8,n,t);break;case 23:case 22:if(n.memoizedState!==null&&n.memoizedState.cachePool!==null){var i=n.memoizedState.cachePool.pool;i!=null&&i.refCount++}break;case 24:vl(n.memoizedState.cache)}if(i=n.child,i!==null)i.return=n,ke=i;else t:for(n=e;ke!==null;){i=ke;var a=i.sibling,s=i.return;if(ay(i),i===n){ke=null;break t}if(a!==null){a.return=s,ke=a;break t}ke=s}}}var iT={getCacheForType:function(e){var t=Qe(Oe),n=t.data.get(e);return n===void 0&&(n=e(),t.data.set(e,n)),n},cacheSignal:function(){return Qe(Oe).controller.signal}},aT=typeof WeakMap=="function"?WeakMap:Map,$t=0,he=null,Bt=null,Gt=0,re=0,zn=null,Ca=!1,oo=!1,pm=!1,ia=0,Re=0,Wa=0,Ms=0,_c=0,Hn=0,Gr=0,Wo=null,yn=null,_d=!1,jc=0,_y=0,gc=1/0,vc=null,Ia=null,Ee=0,Si=null,Ds=null,Li=0,gd=0,vd=null,gy=null,Dr=null,Ur=null,Nr=null,jo=0,Pu=null;function kn(){return $t&2&&Gt!==0?Gt&-Gt:xt.T!==null?_m():xv()}function vy(){if(Hn===0)if(!(Gt&536870912)||zt){var e=Ol;Ol<<=1,!(Ol&3932160)&&(Ol=262144),Hn=e}else Hn=536870912;return e=nn.current,e!==null&&(e.flags|=32),Hn}function Vr(e,t){if(t!=null){var n=e.stateNode,i=n.ref;i===null&&(i=n.ref=By($i(e.memoizedProps,n))),Ur===null&&(Ur=[]),Ur.push(t.bind(null,i))}}function Tn(e,t,n){(e===he&&(re===2||re===9)||e.cancelPendingCommit!==null)&&(Xr(e,0),wa(e,Gt,Hn,!1)),ml(e,n),(!($t&2)||e!==he)&&(e===he&&(!($t&2)&&(Ms|=n),Re===4&&wa(e,Gt,Hn,!1)),zi(e))}function Sy(e,t,n){if($t&6)throw Error(q(327));var i=!n&&(t&127)===0&&(t&e.expiredLanes)===0||pl(e,t),a=i?oT(e,t):Of(e,t,!0),s=i;do{if(a===0){oo&&!i&&wa(e,t,0,!1);break}else{if(n=e.current.alternate,s&&!sT(n)){a=Of(e,t,!1),s=!1;continue}if(a===2){if(s=t,e.errorRecoveryDisabledLanes&s)var r=0;else r=e.pendingLanes&-536870913,r=r!==0?r:r&536870912?536870912:0;if(r!==0){t=r;t:{var o=e;a=Wo;var l=o.current.memoizedState.isDehydrated;if(l&&(Xr(o,r).flags|=256),r=Of(o,r,!1),r!==2&&r!==6){if(pm&&!l){o.errorRecoveryDisabledLanes|=s,Ms|=s,a=4;break t}s=yn,yn=a,s!==null&&(yn===null?yn=s:yn.push.apply(yn,s))}a=r}if(s=!1,a!==2)continue}}if(a===1){Xr(e,0),wa(e,t,0,!0);break}t:{switch(i=e,s=a,s){case 0:case 1:throw Error(q(345));case 4:if((t&4194048)!==t&&(t&62914560)!==t)break;case 6:wa(i,t,Hn,!Ca);break t;case 2:yn=null;break;case 3:case 5:break;default:throw Error(q(329))}if((t&62914560)===t&&(a=jc+300-Gn(),10<a)){if(wa(i,t,Hn,!Ca),Oc(i,0,!0)!==0)break t;Li=t,i.timeoutHandle=vm(lg.bind(null,i,n,yn,vc,_d,t,Hn,Ms,Gr,Ca,s,"Throttled",-0,0),a);break t}lg(i,n,yn,vc,_d,t,Hn,Ms,Gr,Ca,s,null,-0,0)}}break}while(!0);zi(e)}function lg(e,t,n,i,a,s,r,o,l,u,h,p,f,d){e.timeoutHandle=-1;var v=t.subtreeFlags,y=(s&335544064)===s;if(p=null,(y||v&8192||(v&16785408)===16785408)&&(p={stylesheets:null,count:0,imgCount:0,imgBytes:0,suspenseyImages:[],waitingForImages:!0,waitingForViewTransition:!1,unsuspend:wi},Fn=null,hy(t,s,p),y&&(v=p,y=e.containerInfo,y=(y.nodeType===9?y:y.ownerDocument).__reactViewTransition,y!=null&&(v.count++,v.waitingForViewTransition=!0,v=ll.bind(v),y.finished.then(v,v))),v=(s&62914560)===s?jc-Gn():(s&4194048)===s?_y-Gn():0,v=ub(p,v),v!==null)){Li=s,e.cancelPendingCommit=v(cg.bind(null,e,t,s,n,i,a,r,o,l,u,h,p,null,f,d)),wa(e,s,r,!u);return}cg(e,t,s,n,i,a,r,o,l,u,h,p)}function sT(e){for(var t=e;;){var n=t.tag;if((n===0||n===11||n===15)&&t.flags&16384&&(n=t.updateQueue,n!==null&&(n=n.stores,n!==null)))for(var i=0;i<n.length;i++){var a=n[i],s=a.getSnapshot;a=a.value;try{if(!Yn(s(),a))return!1}catch{return!1}}if(n=t.child,t.subtreeFlags&16384&&n!==null)n.return=t,t=n;else{if(t===e)break;for(;t.sibling===null;){if(t.return===null||t.return===e)return!0;t=t.return}t.sibling.return=t.return,t=t.sibling}}return!0}function wa(e,t,n,i){t=_v(e,t),t&=~_c,t&=~Ms,e.suspendedLanes|=t,e.pingedLanes&=~t,i&&(e.warmLanes|=t),i=e.expirationTimes;for(var a=t;0<a;){var s=31-Xn(a),r=1<<s;i[s]=-1,a&=~r}n!==0&&vv(e,n,t)}function Zc(){return $t&6?!0:(xl(0),!1)}function mm(){if(Bt!==null){if(re===0)var e=Bt.return;else e=Bt,Wi=Fs=null,Jp(e),Rr=null,el=0,e=Bt;for(;e!==null;)WS(e.alternate,e),e=e.return;Bt=null}}function Xr(e,t){var n=e.timeoutHandle;return n!==-1&&(e.timeoutHandle=-1,wT(n)),n=e.cancelPendingCommit,n!==null&&(e.cancelPendingCommit=null,n()),Li=0,mm(),he=e,Bt=n=Ki(e.current,null),Gt=t,re=0,zn=null,Ca=!1,oo=pl(e,t),pm=!1,Gr=Hn=_c=Ms=Wa=Re=0,yn=Wo=null,_d=!1,ia=_v(e,t),Fc(),n}function yy(e,t){Nt=null,xt.H=cc,t===so||t===Vc?(t=P_(),re=3):t===kp?(t=P_(),re=4):re=t===rm?8:t!==null&&typeof t=="object"&&typeof t.then=="function"?6:1,zn=t,Bt===null&&(Re=1,fc(e,ei(t,e.current)))}function xy(){var e=nn.current;return e===null?!0:(Gt&4194048)===Gt?rn===null:(Gt&62914560)===Gt||Gt&536870912?e===rn:!1}function My(){var e=xt.H;return xt.H=cc,e===null?cc:e}function Ey(){var e=xt.A;return xt.A=iT,e}function Sc(){Re=4,Ca||(Gt&4194048)!==Gt&&nn.current!==null||(oo=!0),!(Wa&134217727)&&!(Ms&134217727)||he===null||wa(he,Gt,Hn,!1)}function Of(e,t,n){var i=$t;$t|=2;var a=My(),s=Ey();(he!==e||Gt!==t)&&(vc=null,Xr(e,t)),t=!1;var r=Re;t:do try{if(re!==0&&Bt!==null){var o=Bt,l=zn;switch(re){case 8:mm(),r=6;break t;case 3:case 2:case 9:case 6:nn.current===null&&(t=!0);var u=re;if(re=0,zn=null,yr(e,o,l,u),n&&oo){r=0;break t}break;default:u=re,re=0,zn=null,yr(e,o,l,u)}}rT(),r=Re;break}catch(h){yy(e,h)}while(!0);return t&&e.shellSuspendCounter++,Wi=Fs=null,$t=i,xt.H=a,xt.A=s,Bt===null&&(he=null,Gt=0,Fc()),r}function rT(){for(;Bt!==null;)Ty(Bt)}function oT(e,t){var n=$t;$t|=2;var i=My(),a=Ey();he!==e||Gt!==t?(vc=null,gc=Gn()+500,Xr(e,t)):oo=pl(e,t);t:do try{if(re!==0&&Bt!==null){t=Bt;var s=zn;e:switch(re){case 1:re=0,zn=null,yr(e,t,s,1);break;case 2:case 9:if(O_(s)){re=0,zn=null,ug(t);break}t=function(){re!==2&&re!==9||he!==e||(re=7),zi(e)},s.then(t,t);break t;case 3:re=7;break t;case 4:re=5;break t;case 7:O_(s)?(re=0,zn=null,ug(t)):(re=0,zn=null,yr(e,t,s,7));break;case 5:var r=null;switch(Bt.tag){case 26:r=Bt.memoizedState;case 5:case 27:var o=Bt;if(r?jy(r):o.stateNode.complete){re=0,zn=null;var l=o.sibling;if(l!==null)Bt=l;else{var u=o.return;u!==null?(Bt=u,Kc(u)):Bt=null}break e}}re=0,zn=null,yr(e,t,s,5);break;case 6:re=0,zn=null,yr(e,t,s,6);break;case 8:mm(),Re=6;break t;default:throw Error(q(462))}}lT();break}catch(h){yy(e,h)}while(!0);return Wi=Fs=null,xt.H=i,xt.A=a,$t=n,Bt!==null?0:(he=null,Gt=0,Fc(),Re)}function lT(){for(;Bt!==null&&!bM();)Ty(Bt)}function Ty(e){var t=qS(e.alternate,e,ia);e.memoizedProps=e.pendingProps,t===null?Kc(e):Bt=t}function ug(e){var t=e,n=t.alternate;switch(t.tag){case 15:case 0:t=Q_(n,t,t.pendingProps,t.type,void 0,Gt);break;case 11:t=Q_(n,t,t.pendingProps,t.type.render,t.ref,Gt);break;case 5:Jp(t);var i=t;i===qe&&(zt?(ic(i),i.tag===5&&i.stateNode!=null&&(_e=i.stateNode)):(ic(i),zt=!0));default:WS(n,t),t=Bt=jv(t,ia),t=qS(n,t,ia)}e.memoizedProps=e.pendingProps,t===null?Kc(e):Bt=t}function yr(e,t,n,i){Wi=Fs=null,Jp(t),Rr=null,el=0;var a=t.return;try{if(ZE(e,a,t,n,Gt)){Re=1,fc(e,ei(n,e.current)),Bt=null;return}}catch(s){if(a!==null)throw Bt=a,s;Re=1,fc(e,ei(n,e.current)),Bt=null;return}t.flags&32768?(zt||i===1?e=!0:oo||Gt&536870912?e=!1:(Ca=e=!0,(i===2||i===9||i===3||i===6)&&(i=nn.current,i!==null&&i.tag===13&&(i.flags|=16384))),by(t,e)):Kc(t)}function Kc(e){var t=e;do{if(t.flags&32768){by(t,Ca);return}e=t.return;var n=$E(t.alternate,t,ia);if(n!==null){Bt=n;return}if(t=t.sibling,t!==null){Bt=t;return}Bt=t=e}while(t!==null);Re===0&&(Re=5)}function by(e,t){do{var n=tT(e.alternate,e);if(n!==null){n.flags&=32767,Bt=n;return}if(n=e.return,n!==null&&(n.flags|=32768,n.subtreeFlags=0,n.deletions=null),!t&&(e=e.sibling,e!==null)){Bt=e;return}Bt=e=n}while(e!==null);Re=6,Bt=null}function cg(e,t,n,i,a,s,r,o,l,u,h,p){e.cancelPendingCommit=null;do Qc();while(Ee!==0);if($t&6)throw Error(q(327));if(t!==null){if(t===e.current)throw Error(q(177));e===he&&(Bt=he=null,Gt=0),Ds=t,Si=e,Li=n,vd=a,gy=i,uT(e,t,n,r,o,l,p)}}function uT(e,t,n,i,a,s,r){var o=t.lanes|t.childLanes;if(gd=o,o|=Bp,PM(e,n,o,i,a,s),Ur=null,(n&335544064)===n?(Nr=IE(e),i=10262):(Nr=null,i=10256),t.subtreeFlags&i||t.flags&i?(e.callbackNode=null,e.callbackPriority=0,mT(Ju,function(){return Md(),null})):(e.callbackNode=null,e.callbackPriority=0),pc=!1,i=(t.flags&13878)!==0,t.subtreeFlags&13878||i){i=xt.T,xt.T=null,a=te.p,te.p=2,s=$t,$t|=4;try{eT(e,t,n)}finally{$t=s,te.p=a,xt.T=i}}Ee=1,pc?Dr=PT(r,e.containerInfo,Nr,Sd,yd,fT,xd,Md,cT):(Sd(),yd(),xd())}function cT(e){if(Ee!==0){var t=Si.onRecoverableError;t(e,{componentStack:null})}}function fT(){Ee===3&&(Ee=0,cy(Ds,Si),Ee=4)}function Sd(){if(Ee===1){Ee=0;var e=Si,t=Ds,n=Li,i=(t.flags&13878)!==0;if(t.subtreeFlags&13878||i){i=xt.T,xt.T=null;var a=te.p;te.p=2;var s=$t;$t|=4;try{Uo=mc=!1,ly(t,e,n),n=Ad;var r=Hv(e.containerInfo),o=n.focusedElem,l=n.selectionRange;if(r!==o&&o&&o.ownerDocument&&Fv(o.ownerDocument.documentElement,o)){if(l!==null&&Ip(o)){var u=l.start,h=l.end;if(h===void 0&&(h=u),"selectionStart"in o)o.selectionStart=u,o.selectionEnd=Math.min(h,o.value.length);else{var p=o.ownerDocument||document,f=p&&p.defaultView||window;if(f.getSelection){var d=f.getSelection(),v=o.textContent.length,y=Math.min(l.start,v),m=l.end===void 0?y:Math.min(l.end,v);!d.extend&&y>m&&(r=m,m=y,y=r);var c=A_(o,y),_=A_(o,m);if(c&&_&&(d.rangeCount!==1||d.anchorNode!==c.node||d.anchorOffset!==c.offset||d.focusNode!==_.node||d.focusOffset!==_.offset)){var g=p.createRange();g.setStart(c.node,c.offset),d.removeAllRanges(),y>m?(d.addRange(g),d.extend(_.node,_.offset)):(g.setEnd(_.node,_.offset),d.addRange(g))}}}}for(p=[],d=o;d=d.parentNode;)d.nodeType===1&&p.push({element:d,left:d.scrollLeft,top:d.scrollTop});for(typeof o.focus=="function"&&o.focus(),o=0;o<p.length;o++){var x=p[o];x.element.scrollLeft=x.left,x.element.scrollTop=x.top}}jr=!!bd,Ad=bd=null}finally{$t=s,te.p=a,xt.T=i}}e.current=t,Ee=2}}function yd(){if(Ee===2){Ee=0;var e=Si,t=Ds,n=(t.flags&8772)!==0;if(t.subtreeFlags&8772||n){n=xt.T,xt.T=null;var i=te.p;te.p=2;var a=$t;$t|=4;try{ny(e,t.alternate,t)}finally{$t=a,te.p=i,xt.T=n}}Ee=3}}function xd(){if(Ee===4||Ee===3){Ee=0;var e=Dr;Dr=null,AM();var t=Si,n=Ds,i=Li,a=gy,s=(i&335544064)===i?10262:10256;if(n.subtreeFlags&s||n.flags&s?Ee=5:(Ee=0,Ds=Si=null,Ay(t,t.pendingLanes)),s=t.pendingLanes,s===0&&(Ia=null),Up(i),n=n.stateNode,Vn&&typeof Vn.onCommitFiberRoot=="function")try{Vn.onCommitFiberRoot(dl,n,void 0,(n.current.flags&128)===128)}catch{}if(a!==null){n=xt.T,s=te.p,te.p=2,xt.T=null;try{for(var r=t.onRecoverableError,o=0;o<a.length;o++){var l=a[o];r(l.value,{componentStack:l.stack})}}finally{xt.T=n,te.p=s}}if(a=Ur,r=Nr,Nr=null,a!==null&&(Ur=null,r===null&&(r=[]),e!==null))for(l=0;l<a.length;l++)n=(0,a[l])(r),n!==void 0&&e.finished.finally(n);Li&3&&Qc(),zi(t),s=t.pendingLanes,i&261930&&s&42?t===Pu?jo++:(jo=0,Pu=t):(jo=0,Pu=null),xl(0)}}function Ay(e,t){(e.pooledCacheLanes&=t)===0&&(t=e.pooledCache,t!=null&&(e.pooledCache=null,vl(t)))}function Qc(){return Dr!==null&&(Dr.skipTransition(),Dr=null),Sd(),yd(),xd(),Md()}function Md(){if(Ee!==5)return!1;var e=Si,t=gd;gd=0;var n=Up(Li),i=xt.T,a=te.p;try{te.p=32>n?32:n,xt.T=null,n=vd,vd=null;var s=Si,r=Li;if(Ee=0,Ds=Si=null,Li=0,$t&6)throw Error(q(331));var o=$t;if($t|=4,py(s.current),fy(s,s.current,r,n),$t=o,xl(0,!1),Vn&&typeof Vn.onPostCommitFiberRoot=="function")try{Vn.onPostCommitFiberRoot(dl,s)}catch{}return!0}finally{te.p=a,xt.T=i,Ay(e,t)}}function fg(e,t,n){t=ei(n,t),t=ed(e.stateNode,t,2),e=Oa(e,t,2),e!==null&&(ml(e,2),zi(e))}function le(e,t,n){if(e.tag===3)fg(e,e,n);else for(;t!==null;){if(t.tag===3){fg(t,e,n);break}else if(t.tag===1){var i=t.stateNode;if(typeof t.type.getDerivedStateFromError=="function"||typeof i.componentDidCatch=="function"&&(Ia===null||!Ia.has(i))){e=ei(n,e),n=GS(2),i=Oa(t,n,2),i!==null&&(VS(n,i,t,e),ml(i,2),zi(i));break}}t=t.return}}function Pf(e,t,n){var i=e.pingCache;if(i===null){i=e.pingCache=new aT;var a=new Set;i.set(t,a)}else a=i.get(t),a===void 0&&(a=new Set,i.set(t,a));a.has(n)||(pm=!0,a.add(n),e=hT.bind(null,e,t,n),t.then(e,e))}function hT(e,t,n){var i=e.pingCache;i!==null&&i.delete(t),e.pingedLanes|=e.suspendedLanes&n,e.warmLanes&=~n,he===e&&(Gt&n)===n&&(Re===4||Re===3&&(Gt&62914560)===Gt&&300>Gn()-jc?$t&2?_c|=n:Xr(e,0):_c|=n,Gr===Gt&&(Gr=0)),zi(e)}function Ry(e,t){t===0&&(t=gv()),e=Bs(e,t),e!==null&&(ml(e,t),zi(e))}function dT(e){var t=e.memoizedState,n=0;t!==null&&(n=t.retryLane),Ry(e,n)}function pT(e,t){var n=0;switch(e.tag){case 31:case 13:var i=e.stateNode,a=e.memoizedState;a!==null&&(n=a.retryLane);break;case 19:i=e.stateNode;break;case 22:i=e.stateNode._retryCache;break;default:throw Error(q(314))}i!==null&&i.delete(t),Ry(e,n)}function mT(e,t){return wp(e,t)}var kr=null,lr=null,Ed=!1,yc=!1,zf=!1,Da=0;function zi(e){e!==lr&&e.next===null&&(lr===null?kr=lr=e:lr=lr.next=e),yc=!0,Ed||(Ed=!0,gT())}function xl(e,t){if(!zf&&yc){zf=!0;do for(var n=!1,i=kr;i!==null;){if(e!==0){var a=i.pendingLanes;if(a===0)var s=0;else{var r=i.suspendedLanes,o=i.pingedLanes;s=(1<<31-Xn(42|e)+1)-1,s&=a&~(r&~o),s=s&201326741?s&201326741|1:s?s|2:0}s!==0&&(n=!0,hg(i,s))}else s=Gt,s=Oc(i,i===he?s:0,i.cancelPendingCommit!==null||i.timeoutHandle!==-1),!(s&3)||pl(i,s)||(n=!0,hg(i,s));i=i.next}while(n);zf=!1}}function _T(){Cy()}function Cy(){yc=Ed=!1;var e=0;Da!==0&&CT()&&(e=Da);for(var t=Gn(),n=null,i=kr;i!==null;){var a=i.next,s=wy(i,t);s===0?(i.next=null,n===null?kr=a:n.next=a,a===null&&(lr=n)):(n=i,(e!==0||s&3)&&(yc=!0)),i=a}Ee!==0&&Ee!==5||xl(e),Da!==0&&(Da=0)}function wy(e,t){for(var n=e.suspendedLanes,i=e.pingedLanes,a=e.expirationTimes,s=e.pendingLanes&-62914561;0<s;){var r=31-Xn(s),o=1<<r,l=a[r];l===-1?(!(o&n)||o&i)&&(a[r]=OM(o,t)):l<=t&&(e.expiredLanes|=o),s&=~o}if(t=he,n=Gt,n=Oc(e,e===t?n:0,e.cancelPendingCommit!==null||e.timeoutHandle!==-1),i=e.callbackNode,n===0||e===t&&(re===2||re===9)||e.cancelPendingCommit!==null)return i!==null&&i!==null&&df(i),e.callbackNode=null,e.callbackPriority=0;if(!(n&3)||pl(e,n)){if(t=n&-n,t===e.callbackPriority)return t;switch(i!==null&&df(i),Up(n)){case 2:case 8:n=pv;break;case 32:n=Ju;break;case 268435456:n=mv;break;default:n=Ju}return i=Dy.bind(null,e),n=wp(n,i),e.callbackPriority=t,e.callbackNode=n,t}return i!==null&&i!==null&&df(i),e.callbackPriority=2,e.callbackNode=null,2}function Dy(e,t){if(Ee!==0&&Ee!==5)return e.callbackNode=null,e.callbackPriority=0,null;var n=e.callbackNode;if(Qc()&&e.callbackNode!==n)return null;var i=Gt;return i=Oc(e,e===he?i:0,e.cancelPendingCommit!==null||e.timeoutHandle!==-1),i===0?null:(Sy(e,i,t),wy(e,Gn()),e.callbackNode!=null&&e.callbackNode===n?Dy.bind(null,e):null)}function hg(e,t){if(Qc())return null;Sy(e,t,!0)}function gT(){DT(function(){$t&6?wp(dv,_T):Cy()})}function _m(){if(Da===0){var e=As;e===0&&(e=Ll,Ll<<=1,!(Ll&261888)&&(Ll=256)),Da=e}return Da}function dg(e){return e==null||typeof e=="symbol"||typeof e=="boolean"?null:typeof e=="function"?e:Eu(e)}function vT(e,t,n,i,a){if(t==="submit"&&n&&n.stateNode===a){var s=dg((a[Cn]||null).action),r=i.submitter;r&&(t=(t=r[Cn]||null)?dg(t.formAction):r.getAttribute("formAction"),t!==null&&(s=t,r=null));var o=new zc("action","action",null,i,a);e.push({event:o,listeners:[{instance:null,listener:function(){if(i.defaultPrevented){if(Da!==0){var l=new FormData(a,r);$h(n,{pending:!0,data:l,method:a.method,action:s},null,l)}}else typeof s=="function"&&(o.preventDefault(),l=new FormData(a,r),$h(n,{pending:!0,data:l,method:a.method,action:s},s,l))},currentTarget:a}]})}}for(var If=0;If<Vh.length;If++){var Bf=Vh[If],ST=Bf.toLowerCase(),yT=Bf[0].toUpperCase()+Bf.slice(1);yi(ST,"on"+yT)}yi(Vv,"onAnimationEnd");yi(Xv,"onAnimationIteration");yi(kv,"onAnimationStart");yi("dblclick","onDoubleClick");yi("focusin","onFocus");yi("focusout","onBlur");yi(wE,"onTransitionRun");yi(DE,"onTransitionStart");yi(UE,"onTransitionCancel");yi(Yv,"onTransitionEnd");Br("onMouseEnter",["mouseout","mouseover"]);Br("onMouseLeave",["mouseout","mouseover"]);Br("onPointerEnter",["pointerout","pointerover"]);Br("onPointerLeave",["pointerout","pointerover"]);zs("onChange","change click focusin focusout input keydown keyup selectionchange".split(" "));zs("onSelect","focusout contextmenu dragend focusin keydown keyup mousedown mouseup selectionchange".split(" "));zs("onBeforeInput",["compositionend","keypress","textInput","paste"]);zs("onCompositionEnd","compositionend focusout keydown keypress keyup mousedown".split(" "));zs("onCompositionStart","compositionstart focusout keydown keypress keyup mousedown".split(" "));zs("onCompositionUpdate","compositionupdate focusout keydown keypress keyup mousedown".split(" "));var al="abort canplay canplaythrough durationchange emptied encrypted ended error loadeddata loadedmetadata loadstart pause play playing progress ratechange resize seeked seeking stalled suspend timeupdate volumechange waiting".split(" "),xT=new Set("beforetoggle cancel close invalid load scroll scrollend toggle".split(" ").concat(al));function Uy(e,t){t=(t&4)!==0;for(var n=0;n<e.length;n++){var i=e[n],a=i.event;i=i.listeners;t:{var s=void 0;if(t)for(var r=i.length-1;0<=r;r--){var o=i[r],l=o.instance,u=o.currentTarget;if(o=o.listener,l!==s&&a.isPropagationStopped())break t;s=o,a.currentTarget=u;try{s(a)}catch(h){tc(h)}a.currentTarget=null,s=l}else for(r=0;r<i.length;r++){if(o=i[r],l=o.instance,u=o.currentTarget,o=o.listener,l!==s&&a.isPropagationStopped())break t;s=o,a.currentTarget=u;try{s(a)}catch(h){tc(h)}a.currentTarget=null,s=l}}}}function It(e,t){var n=t[l_];n===void 0&&(n=t[l_]=new Set);var i=e+"__bubble";n.has(i)||(Ny(t,e,2,!1),n.add(i))}function Ff(e,t,n){var i=0;t&&(i|=4),Ny(n,e,i,t)}var ql="_reactListening"+Math.random().toString(36).slice(2);function gm(e){if(!e[ql]){e[ql]=!0,Ev.forEach(function(n){n!=="selectionchange"&&(xT.has(n)||Ff(n,!1,e),Ff(n,!0,e))});var t=e.nodeType===9?e:e.ownerDocument;t===null||t[ql]||(t[ql]=!0,Ff("selectionchange",!1,t))}}function Ny(e,t,n,i){switch(ex(t)){case 2:var a=db;break;case 8:a=pb;break;default:a=Tm}n=a.bind(null,t,n,e),a=void 0,!Bh||t!=="touchstart"&&t!=="touchmove"&&t!=="wheel"||(a=!0),i?a!==void 0?e.addEventListener(t,n,{capture:!0,passive:a}):e.addEventListener(t,n,!0):a!==void 0?e.addEventListener(t,n,{passive:a}):e.addEventListener(t,n,!1)}function Hf(e,t,n,i,a){var s=i;if(!(t&1)&&!(t&2)&&i!==null)t:for(;;){if(i===null)return;var r=i.tag;if(r===3||r===4){var o=i.stateNode.containerInfo;if(o===a)break;if(r===4)for(r=i.return;r!==null;){var l=r.tag;if((l===3||l===4)&&r.stateNode.containerInfo===a)return;r=r.return}for(;o!==null;){if(r=ps(o),r===null)return;if(l=r.tag,l===5||l===6||l===26||l===27){i=s=r;continue t}o=o.parentNode}}i=i.return}Uv(function(){var u=s,h=Lp(n),p=[];t:{var f=qv.get(e);if(f!==void 0){var d=zc,v=e;switch(e){case"keypress":if(bu(n)===0)break t;case"keydown":case"keyup":d=sE;break;case"focusin":v="focus",d=Sf;break;case"focusout":v="blur",d=Sf;break;case"beforeblur":case"afterblur":d=Sf;break;case"click":if(n.button===2)break t;case"auxclick":case"dblclick":case"mousedown":case"mousemove":case"mouseup":case"mouseout":case"mouseover":case"contextmenu":d=__;break;case"drag":case"dragend":case"dragenter":case"dragexit":case"dragleave":case"dragover":case"dragstart":case"drop":d=WM;break;case"touchcancel":case"touchend":case"touchmove":case"touchstart":d=cE;break;case Vv:case Xv:case kv:d=KM;break;case Yv:d=hE;break;case"scroll":case"scrollend":d=YM;break;case"wheel":d=pE;break;case"copy":case"cut":case"paste":d=JM;break;case"gotpointercapture":case"lostpointercapture":case"pointercancel":case"pointerdown":case"pointermove":case"pointerout":case"pointerover":case"pointerup":d=v_;break;case"submit":d=lE;break;case"toggle":case"beforetoggle":d=_E}var y=(t&4)!==0,m=!y&&(e==="scroll"||e==="scrollend"),c=y?f!==null?f+"Capture":null:f;y=[];for(var _=u,g;_!==null;){var x=_;if(g=x.stateNode,x=x.tag,x!==5&&x!==26&&x!==27||g===null||c===null||(x=Ko(_,c),x!=null&&y.push(sl(_,x,g))),m)break;_=_.return}0<y.length&&(f=new d(f,v,null,n,h),p.push({event:f,listeners:y}))}}if(!(t&7)){t:{if(d=e==="mouseover"||e==="pointerover",f=e==="mouseout"||e==="pointerout",d&&n!==Ih&&(v=n.relatedTarget||n.fromElement)&&(ps(v)||v[io]))break t;(f||d)&&(v=h.window===h?h:(d=h.ownerDocument)?d.defaultView||d.parentWindow:window,f?(d=n.relatedTarget||n.toElement,f=u,d=d?ps(d):null,d!==null&&(m=hl(d),y=d.tag,d!==m||y!==5&&y!==27&&y!==6)&&(d=null)):(f=null,d=u),f!==d&&(y=__,x="onMouseLeave",c="onMouseEnter",_="mouse",(e==="pointerout"||e==="pointerover")&&(y=v_,x="onPointerLeave",c="onPointerEnter",_="pointer"),m=f==null?v:wo(f),g=d==null?v:wo(d),v=new y(x,_+"leave",f,n,h),v.target=m,v.relatedTarget=g,x=null,ps(h)===u&&(y=new y(c,_+"enter",d,n,h),y.target=g,y.relatedTarget=m,x=y),m=x,y=f&&d?bh(f,d,MT):null,f!==null&&pg(p,v,f,y,!1),d!==null&&m!==null&&pg(p,m,d,y,!0)))}t:{if(f=u?wo(u):window,d=f.nodeName&&f.nodeName.toLowerCase(),d==="select"||d==="input"&&f.type==="file")var C=M_;else if(x_(f))if(Iv)C=AE;else{C=TE;var R=EE}else d=f.nodeName,!d||d.toLowerCase()!=="input"||f.type!=="checkbox"&&f.type!=="radio"?u&&Np(u.elementType)&&(C=M_):C=bE;if(C&&(C=C(e,u))){zv(p,C,n,h);break t}R&&R(e,f,u)}switch(R=u?wo(u):window,e){case"focusin":(x_(R)||R.contentEditable==="true")&&(pr=R,Hh=u,Bo=null);break;case"focusout":Bo=Hh=pr=null;break;case"mousedown":Gh=!0;break;case"contextmenu":case"mouseup":case"dragend":Gh=!1,R_(p,n,h);break;case"selectionchange":if(CE)break;case"keydown":case"keyup":R_(p,n,h)}var b;if(zp)t:{switch(e){case"compositionstart":var w="onCompositionStart";break t;case"compositionend":w="onCompositionEnd";break t;case"compositionupdate":w="onCompositionUpdate";break t}w=void 0}else dr?Ov(e,n)&&(w="onCompositionEnd"):e==="keydown"&&n.keyCode===229&&(w="onCompositionStart");w&&(Lv&&n.locale!=="ko"&&(dr||w!=="onCompositionStart"?w==="onCompositionEnd"&&dr&&(b=Nv()):(Aa=h,Op="value"in Aa?Aa.value:Aa.textContent,dr=!0)),R=xc(u,w),0<R.length&&(w=new g_(w,e,null,n,h),p.push({event:w,listeners:R}),b?w.data=b:(b=Pv(n),b!==null&&(w.data=b)))),(b=vE?SE(e,n):yE(e,n))&&(w=xc(u,"onBeforeInput"),0<w.length&&(R=new g_("onBeforeInput","beforeinput",null,n,h),p.push({event:R,listeners:w}),R.data=b)),vT(p,e,u,n,h)}Uy(p,t)})}function sl(e,t,n){return{instance:e,listener:t,currentTarget:n}}function xc(e,t){for(var n=t+"Capture",i=[];e!==null;){var a=e,s=a.stateNode;if(a=a.tag,a!==5&&a!==26&&a!==27||s===null||(a=Ko(e,n),a!=null&&i.unshift(sl(e,a,s)),a=Ko(e,t),a!=null&&i.push(sl(e,a,s))),e.tag===3)return i;e=e.return}return[]}function MT(e){if(e===null)return null;do e=e.return;while(e&&e.tag!==5&&e.tag!==27);return e||null}function pg(e,t,n,i,a){for(var s=t._reactName,r=[];n!==null&&n!==i;){var o=n,l=o.alternate,u=o.stateNode;if(o=o.tag,l!==null&&l===i)break;o!==5&&o!==26&&o!==27||u===null||(l=u,a?(u=Ko(n,s),u!=null&&r.unshift(sl(n,u,l))):a||(u=Ko(n,s),u!=null&&r.push(sl(n,u,l)))),n=n.return}r.length!==0&&e.push({event:t,listeners:r})}var ET=/\r\n?/g,TT=/\u0000|\uFFFD/g;function mg(e){return(typeof e=="string"?e:""+e).replace(ET,`
`).replace(TT,"")}function Ly(e,t){return t=mg(t),mg(e)===t}function oe(e,t,n,i,a,s){switch(n){case"children":if(typeof i=="string")t==="body"||t==="textarea"&&i===""||Fr(e,i);else if(typeof i=="number"||typeof i=="bigint")t!=="body"&&Fr(e,""+i);else return;break;case"className":zl(e,"class",i);break;case"tabIndex":zl(e,"tabindex",i);break;case"dir":case"role":case"viewBox":case"width":case"height":zl(e,n,i);break;case"style":Dv(e,i,s);return;case"data":if(t!=="object"){zl(e,"data",i);break}case"src":case"href":if(i===""&&(t!=="a"||n!=="href")){e.removeAttribute(n);break}if(i==null||typeof i=="function"||typeof i=="symbol"||typeof i=="boolean"){e.removeAttribute(n);break}i=Eu(i),e.setAttribute(n,i);break;case"action":case"formAction":if(typeof i=="function"){e.setAttribute(n,"javascript:throw new Error('A React form was unexpectedly submitted. If you called form.submit() manually, consider using form.requestSubmit() instead. If you\\'re trying to use event.stopPropagation() in a submit event handler, consider also calling event.preventDefault().')");break}else typeof s=="function"&&(n==="formAction"?(t!=="input"&&oe(e,t,"name",a.name,a,null),oe(e,t,"formEncType",a.formEncType,a,null),oe(e,t,"formMethod",a.formMethod,a,null),oe(e,t,"formTarget",a.formTarget,a,null)):(oe(e,t,"encType",a.encType,a,null),oe(e,t,"method",a.method,a,null),oe(e,t,"target",a.target,a,null)));if(i==null||typeof i=="symbol"||typeof i=="boolean"){e.removeAttribute(n);break}i=Eu(i),e.setAttribute(n,i);break;case"onClick":i!=null&&(e.onclick=wi);return;case"onScroll":i!=null&&It("scroll",e);return;case"onScrollEnd":i!=null&&It("scrollend",e);return;case"dangerouslySetInnerHTML":if(i!=null){if(typeof i!="object"||!("__html"in i))throw Error(q(61));if(n=i.__html,n!=null){if(a.children!=null)throw Error(q(60));(s!=null?s.__html:void 0)!==n&&(e.innerHTML=n)}}break;case"multiple":e.multiple=i&&typeof i!="function"&&typeof i!="symbol";break;case"muted":e.muted=i&&typeof i!="function"&&typeof i!="symbol";break;case"suppressContentEditableWarning":case"suppressHydrationWarning":case"defaultValue":case"defaultChecked":case"innerHTML":case"ref":break;case"autoFocus":break;case"xlinkHref":if(i==null||typeof i=="function"||typeof i=="boolean"||typeof i=="symbol"){e.removeAttribute("xlink:href");break}n=Eu(i),e.setAttributeNS("http://www.w3.org/1999/xlink","xlink:href",n);break;case"contentEditable":case"spellCheck":case"draggable":case"value":case"autoReverse":case"externalResourcesRequired":case"focusable":case"preserveAlpha":i!=null&&typeof i!="function"&&typeof i!="symbol"?e.setAttribute(n,i):e.removeAttribute(n);break;case"inert":case"allowFullScreen":case"async":case"autoPlay":case"controls":case"credentialless":case"default":case"defer":case"disabled":case"disablePictureInPicture":case"disableRemotePlayback":case"formNoValidate":case"hidden":case"loop":case"noModule":case"noValidate":case"open":case"playsInline":case"readOnly":case"required":case"reversed":case"scoped":case"seamless":case"itemScope":i&&typeof i!="function"&&typeof i!="symbol"?e.setAttribute(n,""):e.removeAttribute(n);break;case"capture":case"download":i===!0?e.setAttribute(n,""):i!==!1&&i!=null&&typeof i!="function"&&typeof i!="symbol"?e.setAttribute(n,i):e.removeAttribute(n);break;case"cols":case"rows":case"size":case"span":i!=null&&typeof i!="function"&&typeof i!="symbol"&&!isNaN(i)&&1<=i?e.setAttribute(n,i):e.removeAttribute(n);break;case"rowSpan":case"start":i==null||typeof i=="function"||typeof i=="symbol"||isNaN(i)?e.removeAttribute(n):e.setAttribute(n,i);break;case"popover":It("beforetoggle",e),It("toggle",e),Mu(e,"popover",i);break;case"xlinkActuate":Bi(e,"http://www.w3.org/1999/xlink","xlink:actuate",i);break;case"xlinkArcrole":Bi(e,"http://www.w3.org/1999/xlink","xlink:arcrole",i);break;case"xlinkRole":Bi(e,"http://www.w3.org/1999/xlink","xlink:role",i);break;case"xlinkShow":Bi(e,"http://www.w3.org/1999/xlink","xlink:show",i);break;case"xlinkTitle":Bi(e,"http://www.w3.org/1999/xlink","xlink:title",i);break;case"xlinkType":Bi(e,"http://www.w3.org/1999/xlink","xlink:type",i);break;case"xmlBase":Bi(e,"http://www.w3.org/XML/1998/namespace","xml:base",i);break;case"xmlLang":Bi(e,"http://www.w3.org/XML/1998/namespace","xml:lang",i);break;case"xmlSpace":Bi(e,"http://www.w3.org/XML/1998/namespace","xml:space",i);break;case"is":Mu(e,"is",i);break;case"innerText":case"textContent":return;default:if(!(2<n.length)||n[0]!=="o"&&n[0]!=="O"||n[1]!=="n"&&n[1]!=="N")n=XM.get(n)||n,Mu(e,n,i);else return}Qt=!0}function Td(e,t,n,i,a,s){switch(n){case"style":Dv(e,i,s);return;case"dangerouslySetInnerHTML":if(i!=null){if(typeof i!="object"||!("__html"in i))throw Error(q(61));if(n=i.__html,n!=null){if(a.children!=null)throw Error(q(60));(s!=null?s.__html:void 0)!==n&&(e.innerHTML=n)}}break;case"children":if(typeof i=="string")Fr(e,i);else if(typeof i=="number"||typeof i=="bigint")Fr(e,""+i);else return;break;case"onScroll":i!=null&&It("scroll",e);return;case"onScrollEnd":i!=null&&It("scrollend",e);return;case"onClick":i!=null&&(e.onclick=wi);return;case"suppressContentEditableWarning":case"suppressHydrationWarning":case"innerHTML":case"ref":return;case"innerText":case"textContent":return;default:if(!Tv.hasOwnProperty(n))t:{if(n[0]==="o"&&n[1]==="n"&&(a=n.endsWith("Capture"),s=n.slice(2,a?n.length-7:void 0),t=e[Cn]||null,t=t!=null?t[n]:null,typeof t=="function"&&e.removeEventListener(s,t,a),typeof i=="function")){typeof t!="function"&&t!==null&&(n in e?e[n]=null:e.hasAttribute(n)&&e.removeAttribute(n)),e.addEventListener(s,i,a);break t}Qt=!0,n in e?e[n]=i:i===!0?e.setAttribute(n,""):Mu(e,n,i)}return}Qt=!0}function tn(e,t,n){switch(t){case"div":case"span":case"svg":case"path":case"a":case"g":case"p":case"li":break;case"img":It("error",e),It("load",e);var i=!1,a=!1,s;for(s in n)if(n.hasOwnProperty(s)){var r=n[s];if(r!=null)switch(s){case"src":i=!0;break;case"srcSet":a=!0;break;case"children":case"dangerouslySetInnerHTML":throw Error(q(137,t));default:oe(e,t,s,r,n,null)}}a&&oe(e,t,"srcSet",n.srcSet,n,null),i&&oe(e,t,"src",n.src,n,null);return;case"input":It("invalid",e);var o=s=r=a=null,l=null,u=null;for(i in n)if(n.hasOwnProperty(i)){var h=n[i];if(h!=null)switch(i){case"name":a=h;break;case"type":r=h;break;case"checked":l=h;break;case"defaultChecked":u=h;break;case"value":s=h;break;case"defaultValue":o=h;break;case"children":case"dangerouslySetInnerHTML":if(h!=null)throw Error(q(137,t));break;default:oe(e,t,i,h,n,null)}}Rv(e,s,o,l,u,r,a,!1);return;case"select":It("invalid",e),i=r=s=null;for(a in n)if(n.hasOwnProperty(a)&&(o=n[a],o!=null))switch(a){case"value":s=o;break;case"defaultValue":r=o;break;case"multiple":i=o;default:oe(e,t,a,o,n,null)}t=s,n=r,e.multiple=!!i,t!=null?Tr(e,!!i,t,!1):n!=null&&Tr(e,!!i,n,!0);return;case"textarea":It("invalid",e),s=a=i=null;for(r in n)if(n.hasOwnProperty(r)&&(o=n[r],o!=null))switch(r){case"value":i=o;break;case"defaultValue":a=o;break;case"children":s=o;break;case"dangerouslySetInnerHTML":if(o!=null)throw Error(q(91));break;default:oe(e,t,r,o,n,null)}wv(e,i,a,s);return;case"option":for(l in n)if(n.hasOwnProperty(l)&&(i=n[l],i!=null))switch(l){case"selected":e.selected=i&&typeof i!="function"&&typeof i!="symbol";break;default:oe(e,t,l,i,n,null)}return;case"dialog":It("beforetoggle",e),It("toggle",e),It("cancel",e),It("close",e);break;case"iframe":case"object":It("load",e);break;case"video":case"audio":for(i=0;i<al.length;i++)It(al[i],e);break;case"image":It("error",e),It("load",e);break;case"details":It("toggle",e);break;case"embed":case"source":case"link":It("error",e),It("load",e);case"area":case"base":case"br":case"col":case"hr":case"keygen":case"meta":case"param":case"track":case"wbr":case"menuitem":for(u in n)if(n.hasOwnProperty(u)&&(i=n[u],i!=null))switch(u){case"children":case"dangerouslySetInnerHTML":throw Error(q(137,t));default:oe(e,t,u,i,n,null)}return;default:if(Np(t)){for(h in n)n.hasOwnProperty(h)&&(i=n[h],i!==void 0&&Td(e,t,h,i,n,void 0));return}}for(o in n)n.hasOwnProperty(o)&&(i=n[o],i!=null&&oe(e,t,o,i,n,null))}var bT={};function AT(e,t,n,i){switch(t){case"div":case"span":case"svg":case"path":case"a":case"g":case"p":case"li":break;case"input":var a=null,s=null,r=null,o=null,l=null,u=null,h=null;for(d in n){var p=n[d];if(n.hasOwnProperty(d)&&p!=null)switch(d){case"checked":break;case"value":break;case"defaultValue":l=p;default:i.hasOwnProperty(d)||oe(e,t,d,null,i,p)}}for(var f in i){var d=i[f];if(p=n[f],i.hasOwnProperty(f)&&(d!=null||p!=null))switch(f){case"type":d!==p&&(Qt=!0),s=d;break;case"name":d!==p&&(Qt=!0),a=d;break;case"checked":d!==p&&(Qt=!0),u=d;break;case"defaultChecked":d!==p&&(Qt=!0),h=d;break;case"value":d!==p&&(Qt=!0),r=d;break;case"defaultValue":d!==p&&(Qt=!0),o=d;break;case"children":case"dangerouslySetInnerHTML":if(d!=null)throw Error(q(137,t));break;default:d!==p&&oe(e,t,f,d,i,p)}}zh(e,r,o,l,u,h,s,a);return;case"select":d=r=o=f=null;for(s in n)if(l=n[s],n.hasOwnProperty(s)&&l!=null)switch(s){case"value":break;case"multiple":d=l;default:i.hasOwnProperty(s)||oe(e,t,s,null,i,l)}for(a in i)if(s=i[a],l=n[a],i.hasOwnProperty(a)&&(s!=null||l!=null))switch(a){case"value":s!==l&&(Qt=!0),f=s;break;case"defaultValue":s!==l&&(Qt=!0),o=s;break;case"multiple":s!==l&&(Qt=!0),r=s;default:s!==l&&oe(e,t,a,s,i,l)}t=o,n=r,i=d,f!=null?Tr(e,!!n,f,!1):!!i!=!!n&&(t!=null?Tr(e,!!n,t,!0):Tr(e,!!n,n?[]:"",!1));return;case"textarea":d=f=null;for(o in n)if(a=n[o],n.hasOwnProperty(o)&&a!=null&&!i.hasOwnProperty(o))switch(o){case"value":break;case"children":break;default:oe(e,t,o,null,i,a)}for(r in i)if(a=i[r],s=n[r],i.hasOwnProperty(r)&&(a!=null||s!=null))switch(r){case"value":a!==s&&(Qt=!0),f=a;break;case"defaultValue":a!==s&&(Qt=!0),d=a;break;case"children":break;case"dangerouslySetInnerHTML":if(a!=null)throw Error(q(91));break;default:a!==s&&oe(e,t,r,a,i,s)}Cv(e,f,d);return;case"option":for(var v in n)if(f=n[v],n.hasOwnProperty(v)&&f!=null&&!i.hasOwnProperty(v))switch(v){case"selected":e.selected=!1;break;default:oe(e,t,v,null,i,f)}for(l in i)if(f=i[l],d=n[l],i.hasOwnProperty(l)&&f!==d&&(f!=null||d!=null))switch(l){case"selected":f!==d&&(Qt=!0),e.selected=f&&typeof f!="function"&&typeof f!="symbol";break;default:oe(e,t,l,f,i,d)}return;case"img":case"link":case"area":case"base":case"br":case"col":case"embed":case"hr":case"keygen":case"meta":case"param":case"source":case"track":case"wbr":case"menuitem":for(var y in n)f=n[y],n.hasOwnProperty(y)&&f!=null&&!i.hasOwnProperty(y)&&oe(e,t,y,null,i,f);for(u in i)if(f=i[u],d=n[u],i.hasOwnProperty(u)&&f!==d&&(f!=null||d!=null))switch(u){case"children":case"dangerouslySetInnerHTML":if(f!=null)throw Error(q(137,t));break;default:oe(e,t,u,f,i,d)}return;default:if(Np(t)){for(var m in n)f=n[m],n.hasOwnProperty(m)&&f!==void 0&&!i.hasOwnProperty(m)&&Td(e,t,m,void 0,i,f);for(h in i)f=i[h],d=n[h],!i.hasOwnProperty(h)||f===d||f===void 0&&d===void 0||Td(e,t,h,f,i,d);return}}for(var c in n)f=n[c],n.hasOwnProperty(c)&&f!=null&&!i.hasOwnProperty(c)&&oe(e,t,c,null,i,f);for(p in i)f=i[p],d=n[p],!i.hasOwnProperty(p)||f===d||f==null&&d==null||oe(e,t,p,f,i,d)}function _g(e){switch(e){case"css":case"script":case"font":case"img":case"image":case"input":case"link":return!0;default:return!1}}function RT(){if(typeof performance.getEntriesByType=="function"){for(var e=0,t=0,n=performance.getEntriesByType("resource"),i=0;i<n.length;i++){var a=n[i],s=a.transferSize,r=a.initiatorType,o=a.duration;if(s&&o&&_g(r)){for(r=0,o=a.responseEnd,i+=1;i<n.length;i++){var l=n[i],u=l.startTime;if(u>o)break;var h=l.transferSize,p=l.initiatorType;h&&_g(p)&&(l=l.responseEnd,r+=h*(l<o?1:(o-u)/(l-u)))}if(--i,t+=8*(s+r)/(a.duration/1e3),e++,10<e)break}}if(0<e)return t/e/1e6}return navigator.connection&&(e=navigator.connection.downlink,typeof e=="number")?e:5}var bd=null,Ad=null;function rl(e){return e.nodeType===9?e:e.ownerDocument}function gg(e){switch(e){case"http://www.w3.org/2000/svg":return 1;case"http://www.w3.org/1998/Math/MathML":return 2;default:return 0}}function Oy(e,t){if(e===0)switch(t){case"svg":return 1;case"math":return 2;default:return 0}return e===1&&t==="foreignObject"?0:e}function Py(e,t,n,i){return n=rl(n).createElement(e),n[Ke]=i,n[Cn]=t,tn(n,e,t),Ye(n),n}function Rd(e,t){return e==="textarea"||e==="noscript"||typeof t.children=="string"||typeof t.children=="number"||typeof t.children=="bigint"||typeof t.dangerouslySetInnerHTML=="object"&&t.dangerouslySetInnerHTML!==null&&t.dangerouslySetInnerHTML.__html!=null}var Gf=null;function CT(){var e=window.event;return e&&e.type==="popstate"?e===Gf?!1:(Gf=e,!0):(Gf=null,!1)}var vm=typeof setTimeout=="function"?setTimeout:void 0,wT=typeof clearTimeout=="function"?clearTimeout:void 0,vg=typeof Promise=="function"?Promise:void 0,Sg=typeof requestAnimationFrame=="function"?requestAnimationFrame:vm,DT=typeof queueMicrotask=="function"?queueMicrotask:typeof vg<"u"?function(e){return vg.resolve(null).then(e).catch(UT)}:vm;function UT(e){setTimeout(function(){throw e})}function Qa(e){return e==="head"}function yg(e,t){var n=t,i=0;do{var a=n.nextSibling;if(e.removeChild(n),a&&a.nodeType===8)if(n=a.data,n==="/$"||n==="/&"){if(i===0){e.removeChild(a),Zr(t);return}i--}else if(n==="$"||n==="$?"||n==="$~"||n==="$!"||n==="&")i++;else if(n==="html")Xf(e.ownerDocument.documentElement);else if(n==="head"){n=e.ownerDocument.head,Xf(n);for(var s=n.firstChild;s;){var r=s.nextSibling,o=s.nodeName;s[_l]||o==="SCRIPT"||o==="STYLE"||o==="LINK"&&s.rel.toLowerCase()==="stylesheet"||n.removeChild(s),s=r}}else n==="body"&&Xf(e.ownerDocument.body);n=a}while(n);Zr(t)}function xg(e,t){var n=e;e=0;do{var i=n.nextSibling;if(n.nodeType===1?t?(n._stashedDisplay=n.style.display,n.style.display="none"):(n.style.display=n._stashedDisplay||"",n.getAttribute("style")===""&&n.removeAttribute("style")):n.nodeType===3&&(t?(n._stashedText=n.nodeValue,n.nodeValue=""):n.nodeValue=n._stashedText||""),i&&i.nodeType===8)if(n=i.data,n==="/$"){if(e===0)break;e--}else n!=="$"&&n!=="$?"&&n!=="$~"&&n!=="$!"||e++;n=i}while(n)}function zy(e,t,n){if(t=CSS.escape(t)!==t?"r-"+btoa(t).replace(/=/g,""):t,e.style.viewTransitionName=t,n!=null&&(e.style.viewTransitionClass=n),n=getComputedStyle(e),n.display==="inline"){if(t=e.getClientRects(),t.length===1)var i=1;else for(var a=i=0;a<t.length;a++){var s=t[a];0<s.width&&0<s.height&&i++}i===1&&(e=e.style,e.display=t.length===1?"inline-block":"block",e.marginTop="-"+n.paddingTop,e.marginBottom="-"+n.paddingBottom)}}function Iy(e,t){e=e.style,t=t.style;var n=t!=null?t.hasOwnProperty("viewTransitionName")?t.viewTransitionName:t.hasOwnProperty("view-transition-name")?t["view-transition-name"]:null:null;e.viewTransitionName=n==null||typeof n=="boolean"?"":(""+n).trim(),n=t!=null?t.hasOwnProperty("viewTransitionClass")?t.viewTransitionClass:t.hasOwnProperty("view-transition-class")?t["view-transition-class"]:null:null,e.viewTransitionClass=n==null||typeof n=="boolean"?"":(""+n).trim(),e.display==="inline-block"&&(t==null?e.display=e.margin="":(n=t.display,e.display=n==null||typeof n=="boolean"?"":n,n=t.margin,n!=null?e.margin=n:(n=t.hasOwnProperty("marginTop")?t.marginTop:t["margin-top"],e.marginTop=n==null||typeof n=="boolean"?"":n,t=t.hasOwnProperty("marginBottom")?t.marginBottom:t["margin-bottom"],e.marginBottom=t==null||typeof t=="boolean"?"":t)))}function NT(e,t,n){return n=n.ownerDocument.defaultView,{rect:e,abs:t.position==="absolute"||t.position==="fixed",clip:t.clipPath!=="none"||t.overflow!=="visible"||t.filter!=="none"||t.mask!=="none"||t.mask!=="none"||t.borderRadius!=="0px",view:0<=e.bottom&&0<=e.right&&e.top<=n.innerHeight&&e.left<=n.innerWidth}}function Cd(e){var t=e.getBoundingClientRect(),n=getComputedStyle(e);return NT(t,n,e)}function LT(e){return e.documentElement.clientHeight}function OT(e){this.addEventListener("load",e),this.addEventListener("error",e)}function PT(e,t,n,i,a,s,r,o,l){var u=t.nodeType===9?t:t.ownerDocument;try{var h=u.startViewTransition({update:function(){var f=u.defaultView,d=f.navigation&&f.navigation.transition,v=u.fonts.status;i();var y=[];if(v==="loaded"&&(LT(u),u.fonts.status==="loading"&&y.push(u.fonts.ready)),v=y.length,e!==null)for(var m=e.suspenseyImages,c=0,_=0;_<m.length;_++){var g=m[_];if(!g.complete){var x=g.getBoundingClientRect();if(0<x.bottom&&0<x.right&&x.top<f.innerHeight&&x.left<f.innerWidth){if(c+=Zy(g),c>Bu){y.length=v;break}g=new Promise(OT.bind(g)),y.push(g)}}}if(0<y.length)return f=Promise.race([Promise.all(y),new Promise(function(C){return setTimeout(C,500)})]).then(a,a),(d?Promise.allSettled([d.finished,f]):f).then(s,s);if(a(),d)return d.finished.then(s,s);s()},types:n});u.__reactViewTransition=h;var p=[];return h.ready.then(function(){for(var f=u.documentElement.getAnimations({subtree:!0}),d=0;d<f.length;d++){var v=f[d],y=v.effect,m=y.pseudoElement;if(m!=null&&m.startsWith("::view-transition")){p.push(v),v=y.getKeyframes();for(var c=m=void 0,_=!0,g=0;g<v.length;g++){var x=v[g],C=x.width;if(m===void 0)m=C;else if(m!==C){_=!1;break}if(C=x.height,c===void 0)c=C;else if(c!==C){_=!1;break}delete x.width,delete x.height,x.transform==="none"&&delete x.transform}_&&m!==void 0&&c!==void 0&&(y.setKeyframes(v),_=getComputedStyle(y.target,y.pseudoElement),_.width!==m||_.height!==c)&&(_=v[0],_.width=m,_.height=c,_=v[v.length-1],_.width=m,_.height=c,y.setKeyframes(v))}}r()},function(f){u.__reactViewTransition===h&&(u.__reactViewTransition=null);try{if(typeof f=="object"&&f!==null)switch(f.name){case"InvalidStateError":(f.message==="View transition was skipped because document visibility state is hidden."||f.message==="Skipping view transition because document visibility state has become hidden."||f.message==="Skipping view transition because viewport size changed."||f.message==="Transition was aborted because of invalid state")&&(f=null)}f!==null&&l(f)}finally{i(),a(),r()}}),h.finished.finally(function(){for(var f=0;f<p.length;f++)p[f].cancel();u.__reactViewTransition===h&&(u.__reactViewTransition=null),o()}),h}catch{return i(),a(),r(),null}}function ms(e,t){this._scope=document.documentElement,this._selector="::view-transition-"+e+"("+t+")"}ms.prototype.animate=function(e,t){return t=typeof t=="number"?{duration:t}:de({},t),t.pseudoElement=this._selector,this._scope.animate(e,t)};ms.prototype.getAnimations=function(){for(var e=this._scope,t=this._selector,n=e.getAnimations({subtree:!0}),i=[],a=0;a<n.length;a++){var s=n[a].effect;s!==null&&s.target===e&&s.pseudoElement===t&&i.push(n[a])}return i};ms.prototype.getComputedStyle=function(){return getComputedStyle(this._scope,this._selector)};function By(e){return{name:e,group:new ms("group",e),imagePair:new ms("image-pair",e),old:new ms("old",e),new:new ms("new",e)}}function qn(e){this._fragmentFiber=e,this._observers=this._eventListeners=null}qn.prototype.addEventListener=function(e,t,n){var i=null,a=null;if(!(n!=null&&typeof n!="boolean"&&(i=n.signal||null,i!==null&&i.aborted))){this._eventListeners===null&&(this._eventListeners=[]);var s=this._eventListeners;if(Fy(s,e,t,n)===-1){var r=this,o=t;n!=null&&typeof n!="boolean"&&n.once===!0&&(o=function(l){r.removeEventListener(e,t,n),typeof t=="function"?t.call(this,l):t.handleEvent(l)}),i!==null&&(a=r.removeEventListener.bind(r,e,t,n),i.addEventListener("abort",a,{once:!0}),a=i.removeEventListener.bind(i,"abort",a)),i=Yr(n),s.push({type:e,listener:t,optionsOrUseCapture:n,attachedListener:o,cleanup:a}),Rn(this._fragmentFiber.child,!1,zT,e,o,i)}this._eventListeners=s}};function zT(e,t,n,i){return Be(e).addEventListener(t,n,i),!1}qn.prototype.removeEventListener=function(e,t,n){var i=this._eventListeners;if(i!==null&&(t=Fy(i,e,t,n),t!==-1)){var a=i[t];n=a.attachedListener;var s=a.cleanup;a=Yr(a.optionsOrUseCapture),Rn(this._fragmentFiber.child,!1,IT,e,n,a),i.splice(t,1),s!==null&&s()}};function IT(e,t,n,i){return Be(e).removeEventListener(t,n,i),!1}function Yr(e){return e!=null&&typeof e!="boolean"&&(e.once===!0||e.signal instanceof AbortSignal)?{capture:e.capture,passive:e.passive}:e}function Mg(e){return e==null?"c=0":typeof e=="boolean"?"c="+(e?"1":"0"):"c="+(e.capture?"1":"0")}function Fy(e,t,n,i){if(e.length===0)return-1;i=Mg(i);for(var a=0;a<e.length;a++){var s=e[a];if(s.type===t&&s.listener===n&&Mg(s.optionsOrUseCapture)===i)return a}return-1}qn.prototype.dispatchEvent=function(e){var t=Ps(this._fragmentFiber);if(t===null)return!0;t=Be(t);var n=this._eventListeners;if(n!==null&&0<n.length||!e.bubbles){var i=t.nodeType===9?t.createComment(""):document.createTextNode("");if(n)for(var a=0;a<n.length;a++){var s=n[a];i.addEventListener(s.type,s.attachedListener,Yr(s.optionsOrUseCapture))}if(t.appendChild(i),e=i.dispatchEvent(e),n)for(a=0;a<n.length;a++)s=n[a],i.removeEventListener(s.type,s.attachedListener,Yr(s.optionsOrUseCapture));return t.removeChild(i),e}return t.dispatchEvent(e)};qn.prototype.focus=function(e){Rn(this._fragmentFiber.child,!0,Hy,e,void 0,void 0)};function Hy(e,t){return e.tag===6?!1:(e=Be(e),ZT(e,t))}qn.prototype.focusLast=function(e){var t=[];Rn(this._fragmentFiber.child,!0,Sm,t,void 0,void 0);for(var n=t.length-1;0<=n&&!Hy(t[n],e);n--);};function Sm(e,t){return t.push(e),!1}qn.prototype.blur=function(){var e=Ps(this._fragmentFiber);e!==null&&(e=Be(e),e=rl(e).activeElement,e!==null&&Rn(this._fragmentFiber.child,!1,BT,e,void 0,void 0))};function BT(e,t){return e.tag===6?!1:(e=Be(e),e===t||e.contains(t)?(t.blur(),!0):!1)}qn.prototype.observeUsing=function(e){this._observers===null&&(this._observers=new Set),this._observers.add(e),Rn(this._fragmentFiber.child,!1,FT,e,void 0,void 0)};function FT(e,t){return e.tag===6||(e=Be(e),t.observe(e)),!1}qn.prototype.unobserveUsing=function(e){var t=this._observers;if(t!==null&&t.has(e)){t.delete(e),Rn(this._fragmentFiber.child,!1,HT,e,void 0,void 0);for(var n=t=0;n<gi.length;n++){var i=gi[n];i.fragmentInstance===this&&i.observer===e?e.unobserve(i.instance):gi[t++]=i}gi.length=t}};function HT(e,t){return e.tag===6||(e=Be(e),t.unobserve(e)),!1}var gi=[],Vf=!1;function GT(e,t,n){gi.push({fragmentInstance:e,observer:t,instance:n}),Vf||(Vf=!0,KT(function(){Vf=!1;var i=gi;gi=[];for(var a=0;a<i.length;a++){var s=i[a];s.observer.unobserve(s.instance)}}))}qn.prototype.getClientRects=function(){var e=[];return Rn(this._fragmentFiber.child,!1,VT,e,void 0,void 0),e};function VT(e,t){if(e.tag===6){e=e.stateNode;var n=e.ownerDocument.createRange();n.selectNodeContents(e),t.push.apply(t,n.getClientRects())}else e=Be(e),t.push.apply(t,e.getClientRects());return!1}qn.prototype.getRootNode=function(e){var t=Ps(this._fragmentFiber);return t===null?this:Be(t).getRootNode(e)};qn.prototype.compareDocumentPosition=function(e){var t=Ps(this._fragmentFiber);if(t===null)return Node.DOCUMENT_POSITION_DISCONNECTED;var n=[];Rn(this._fragmentFiber.child,!1,Sm,n,void 0,void 0);var i=Be(t);if(n.length===0){if(n=i,n_(this._fragmentFiber)){t:{for(t=this._fragmentFiber.return;t!==null;){if(t.tag===4){t=t.stateNode.containerInfo;break t}if(t.tag===3||t.tag===5||t.tag===27)break;t=t.return}t=null}t!=null&&(n=t)}t=this._fragmentFiber;var a=i=n.compareDocumentPosition(e);return n===e?a=Node.DOCUMENT_POSITION_CONTAINS:i&Node.DOCUMENT_POSITION_CONTAINED_BY&&(n=uv(t)[1],n===null?a=Node.DOCUMENT_POSITION_PRECEDING:(e=Be(n).compareDocumentPosition(e),a=e===0||e&Node.DOCUMENT_POSITION_FOLLOWING?Node.DOCUMENT_POSITION_FOLLOWING:Node.DOCUMENT_POSITION_PRECEDING)),a|=Node.DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC}t=Be(n[0]),a=Be(n[n.length-1]);var s=n_(this._fragmentFiber)?t.parentElement:i;if(s==null)return Node.DOCUMENT_POSITION_DISCONNECTED;i=s.compareDocumentPosition(t)&Node.DOCUMENT_POSITION_CONTAINED_BY,s=s.compareDocumentPosition(a)&Node.DOCUMENT_POSITION_CONTAINED_BY;var r=t.compareDocumentPosition(e),o=a.compareDocumentPosition(e),l=r&Node.DOCUMENT_POSITION_CONTAINED_BY||o&Node.DOCUMENT_POSITION_CONTAINED_BY;return o=i&&s&&r&Node.DOCUMENT_POSITION_FOLLOWING&&o&Node.DOCUMENT_POSITION_PRECEDING,t=i&&t===e||s&&a===e||l||o?Node.DOCUMENT_POSITION_CONTAINED_BY:!i&&t===e||!s&&a===e?Node.DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC:r,t&Node.DOCUMENT_POSITION_DISCONNECTED||t&Node.DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC||XT(t,this._fragmentFiber,n[0],n[n.length-1],e)?t:Node.DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC};function XT(e,t,n,i,a){var s=ps(a);if(e&Node.DOCUMENT_POSITION_CONTAINED_BY){if(n=!!s)t:{for(;s!==null;){if(s.tag===7&&(s===t||s.alternate===t)){n=!0;break t}s=s.return}n=!1}return n}if(e&Node.DOCUMENT_POSITION_CONTAINS){if(s===null)return s=a.ownerDocument,a===s||a===s.documentElement||a===s.body;t:{for(s=t,t=Ps(t);s!==null;){if(!(s.tag!==5&&s.tag!==3&&s.tag!==27||s!==t&&s.alternate!==t)){s=!0;break t}s=s.return}s=!1}return s}return e&Node.DOCUMENT_POSITION_PRECEDING?((t=!!s)&&!(t=s===n)&&(t=bh(n,s,i_),t===null?t=!1:(Rn(t,!0,gM,s,n),s=ur,ur=null,t=s!==null)),t):e&Node.DOCUMENT_POSITION_FOLLOWING?((t=!!s)&&!(t=s===i)&&(t=bh(i,s,i_),t===null?t=!1:(Rn(t,!0,vM,s,i),s=ur,Th=ur=null,t=s!==null)),t):!1}function Eg(e,t){var n=e.ownerDocument.createRange();n.selectNodeContents(e),e=n.getBoundingClientRect(),window.scrollTo(window.scrollX+e.left,t?window.scrollY+e.top:window.scrollY+e.bottom-window.innerHeight)}qn.prototype.scrollIntoView=function(e){if(typeof e=="object")throw Error(q(566));var t=[];Rn(this._fragmentFiber.child,!1,Sm,t,void 0,void 0);var n=e!==!1;if(t.length===0){var i=uv(this._fragmentFiber);if(i=n?i[1]||i[0]||Ps(this._fragmentFiber):i[0]||i[1],i===null)return;if(i.tag===6){e=Be(i),Eg(e,n);return}if(i=Be(i),i.nodeType!==9){if(i.nodeType===11){n="host"in i?i.host:null,n!==null&&n.scrollIntoView(e);return}i.scrollIntoView(e)}}for(i=n?t.length-1:0;i!==(n?-1:t.length);){var a=t[i];a.tag===6?(a=Be(a),Eg(a,n)):Be(a).scrollIntoView(e),i+=n?-1:1}};function kT(e,t){return e=Be(e),Gy(e,t),!1}function Gy(e,t){e.reactFragments==null&&(e.reactFragments=new Set),e.reactFragments.add(t)}function Vy(e,t){var n=t._eventListeners;if(n!==null)for(var i=0;i<n.length;i++){var a=n[i];e.addEventListener(a.type,a.attachedListener,Yr(a.optionsOrUseCapture))}e.nodeType!==3&&(n=t._observers,n!==null&&n.forEach(function(s){for(var r=0,o=0;o<gi.length;o++){var l=gi[o];(l.fragmentInstance!==t||l.observer!==s||l.instance!==e)&&(gi[r++]=l)}gi.length=r,s.observe(e)}),Gy(e,t))}function YT(e,t){var n=t._eventListeners;if(n!==null)for(var i=0;i<n.length;i++){var a=n[i];e.removeEventListener(a.type,a.attachedListener,Yr(a.optionsOrUseCapture))}e.nodeType!==3&&(n=t._observers,n!==null&&n.forEach(function(s){typeof s.rootMargin=="string"?GT(t,s,e):s.unobserve(e)}),e.reactFragments!=null&&e.reactFragments.delete(t))}function wd(e){var t=e.firstChild;for(t&&t.nodeType===10&&(t=t.nextSibling);t;){var n=t;switch(t=t.nextSibling,n.nodeName){case"HTML":case"HEAD":case"BODY":wd(n),Pc(n);continue;case"SCRIPT":case"STYLE":continue;case"LINK":if(n.rel.toLowerCase()==="stylesheet")continue}e.removeChild(n)}}function qT(e,t,n,i){for(;e.nodeType===1;){var a=n;if(e.nodeName.toLowerCase()!==t.toLowerCase()){if(!i&&(e.nodeName!=="INPUT"||e.type!=="hidden"))break}else if(i){if(!e[_l])switch(t){case"meta":if(!e.hasAttribute("itemprop"))break;return e;case"link":if(s=e.getAttribute("rel"),s==="stylesheet"&&e.hasAttribute("data-precedence"))break;if(s!==a.rel||e.getAttribute("href")!==(a.href==null||a.href===""?null:a.href)||e.getAttribute("crossorigin")!==(a.crossOrigin==null?null:a.crossOrigin)||e.getAttribute("title")!==(a.title==null?null:a.title))break;return e;case"style":if(e.hasAttribute("data-precedence"))break;return e;case"script":if(s=e.getAttribute("src"),(s!==(a.src==null?null:a.src)||e.getAttribute("type")!==(a.type==null?null:a.type)||e.getAttribute("crossorigin")!==(a.crossOrigin==null?null:a.crossOrigin))&&s&&e.hasAttribute("async")&&!e.hasAttribute("itemprop"))break;return e;default:return e}}else if(t==="input"&&e.type==="hidden"){var s=a.name==null?null:""+a.name;if(a.type==="hidden"&&e.getAttribute("name")===s)return e}else return e;if(e=ai(e.nextSibling),e===null)break}return null}function WT(e,t,n){if(t==="")return null;for(;e.nodeType!==3;)if((e.nodeType!==1||e.nodeName!=="INPUT"||e.type!=="hidden")&&!n||(e=ai(e.nextSibling),e===null))return null;return e}function Xy(e,t){for(;e.nodeType!==8;)if((e.nodeType!==1||e.nodeName!=="INPUT"||e.type!=="hidden")&&!t||(e=ai(e.nextSibling),e===null))return null;return e}function Dd(e){return e.data==="$?"||e.data==="$~"}function ym(e){return e.data==="$!"||e.data==="$?"&&e.ownerDocument.readyState!=="loading"}function jT(e,t){var n=e.ownerDocument;if(e.data==="$~")e._reactRetry=t;else if(e.data!=="$?"||n.readyState!=="loading")t();else{var i=function(){t(),n.removeEventListener("DOMContentLoaded",i)};n.addEventListener("DOMContentLoaded",i),e._reactRetry=i}}function ai(e){for(;e!=null;e=e.nextSibling){var t=e.nodeType;if(t===1||t===3)break;if(t===8){if(t=e.data,t==="$"||t==="$!"||t==="$?"||t==="$~"||t==="&"||t==="F!"||t==="F")break;if(t==="/$"||t==="/&")return null}}return e}var Ud=null;function Tg(e){e=e.nextSibling;for(var t=0;e;){if(e.nodeType===8){var n=e.data;if(n==="/$"||n==="/&"){if(t===0)return ai(e.nextSibling);t--}else n!=="$"&&n!=="$!"&&n!=="$?"&&n!=="$~"&&n!=="&"||t++}e=e.nextSibling}return null}function bg(e){e=e.previousSibling;for(var t=0;e;){if(e.nodeType===8){var n=e.data;if(n==="$"||n==="$!"||n==="$?"||n==="$~"||n==="&"){if(t===0)return e;t--}else n!=="/$"&&n!=="/&"||t++}e=e.previousSibling}return null}function ZT(e,t){function n(){i=!0}if(e.ownerDocument.activeElement===e)return!0;var i=!1;try{e.ownerDocument.addEventListener("focus",n,!0),(e.focus||HTMLElement.prototype.focus).call(e,t)}finally{e.ownerDocument.removeEventListener("focus",n,!0)}return i}function KT(e){Sg(function(){Sg(function(t){return e(t)})})}function ky(e,t,n){switch(t=rl(n),e){case"html":if(e=t.documentElement,!e)throw Error(q(452));return e;case"head":if(e=t.head,!e)throw Error(q(453));return e;case"body":if(e=t.body,!e)throw Error(q(454));return e;default:throw Error(q(451))}}function Yy(e,t,n){for(var i in n){var a=n[i];n.hasOwnProperty(i)&&a!=null&&oe(e,t,i,null,bT,a)}n.dangerouslySetInnerHTML!=null&&(e.textContent=""),e.onclick===wi&&(e.onclick=null),Pc(e)}function Xf(e){for(var t=e.attributes;t.length;)e.removeAttributeNode(t[0]);Pc(e)}var ri=new Map,Ag=new Set;function ol(e){if(typeof e.getRootNode=="function"){var t=e.getRootNode();if(t.nodeType===9||t.nodeType===11)return t}return e.nodeType===9?e:e.ownerDocument}var la=te.d;te.d={f:QT,r:JT,D:$T,C:tb,L:eb,m:nb,X:ab,S:ib,M:sb};function QT(){var e=la.f(),t=Zc();return e||t}function JT(e){var t=ao(e);t!==null&&t.tag===5&&t.type==="form"?DS(t):la.r(e)}var lo=typeof document>"u"?null:document;function qy(e,t,n){var i=lo;if(i&&typeof t=="string"&&t){var a=ti(t);a='link[rel="'+e+'"][href="'+a+'"]',typeof n=="string"&&(a+='[crossorigin="'+n+'"]'),Ag.has(a)||(Ag.add(a),e={rel:e,crossOrigin:n,href:t},i.querySelector(a)===null&&(t=i.createElement("link"),tn(t,"link",e),Ye(t),i.head.appendChild(t)))}}function $T(e){la.D(e),qy("dns-prefetch",e,null)}function tb(e,t){la.C(e,t),qy("preconnect",e,t)}function eb(e,t,n){la.L(e,t,n);var i=lo;if(i&&e&&t){var a='link[rel="preload"][as="'+ti(t)+'"]';t==="image"&&n&&n.imageSrcSet?(a+='[imagesrcset="'+ti(n.imageSrcSet)+'"]',typeof n.imageSizes=="string"&&(a+='[imagesizes="'+ti(n.imageSizes)+'"]')):a+='[href="'+ti(e)+'"]';var s=a;switch(t){case"style":s=qr(e);break;case"script":s=uo(e)}if(!(ri.has(s)||(e=de({rel:"preload",href:t==="image"&&n&&n.imageSrcSet?void 0:e,as:t},n),ri.set(s,e),i.querySelector(a)!==null||t==="style"&&i.querySelector(Ml(s))||t==="script"&&i.querySelector(El(s))))){var r=i.createElement("link");tn(r,"link",e),t==="style"&&(r[$u]=!0,r.onload=r.onerror=function(){Mv(r)}),Ye(r),i.head.appendChild(r)}}}function nb(e,t){la.m(e,t);var n=lo;if(n&&e){var i=t&&typeof t.as=="string"?t.as:"script",a='link[rel="modulepreload"][as="'+ti(i)+'"][href="'+ti(e)+'"]',s=a;switch(i){case"audioworklet":case"paintworklet":case"serviceworker":case"sharedworker":case"worker":case"script":s=uo(e)}if(!ri.has(s)&&(e=de({rel:"modulepreload",href:e},t),ri.set(s,e),n.querySelector(a)===null)){switch(i){case"audioworklet":case"paintworklet":case"serviceworker":case"sharedworker":case"worker":case"script":if(n.querySelector(El(s)))return}i=n.createElement("link"),tn(i,"link",e),Ye(i),n.head.appendChild(i)}}}function ib(e,t,n){la.S(e,t,n);var i=lo;if(i&&e){var a=Er(i).hoistableStyles,s=qr(e);t=t||"default";var r=a.get(s);if(!r){var o={loading:0,preload:null};if(r=i.querySelector(Ml(s)))o.loading=5;else{e=de({rel:"stylesheet",href:e,"data-precedence":t},n),(n=ri.get(s))&&xm(e,n);var l=r=i.createElement("link");Ye(l),tn(l,"link",e),l._p=new Promise(function(u,h){l.onload=u,l.onerror=h}),l.addEventListener("load",function(){o.loading|=1}),l.addEventListener("error",function(){o.loading|=2}),o.loading|=4,zu(r,t,i)}r={type:"stylesheet",instance:r,count:1,state:o},a.set(s,r)}}}function ab(e,t){la.X(e,t);var n=lo;if(n&&e){var i=Er(n).hoistableScripts,a=uo(e),s=i.get(a);s||(s=n.querySelector(El(a)),s||(e=de({src:e,async:!0},t),(t=ri.get(a))&&Mm(e,t),s=n.createElement("script"),Ye(s),tn(s,"link",e),n.head.appendChild(s)),s={type:"script",instance:s,count:1,state:null},i.set(a,s))}}function sb(e,t){la.M(e,t);var n=lo;if(n&&e){var i=Er(n).hoistableScripts,a=uo(e),s=i.get(a);s||(s=n.querySelector(El(a)),s||(e=de({src:e,async:!0,type:"module"},t),(t=ri.get(a))&&Mm(e,t),s=n.createElement("script"),Ye(s),tn(s,"link",e),n.head.appendChild(s)),s={type:"script",instance:s,count:1,state:null},i.set(a,s))}}function Rg(e,t,n,i){var a=(a=Ua.current)?ol(a):null;if(!a)throw Error(q(446));switch(e){case"meta":case"title":return null;case"style":return typeof n.precedence=="string"&&typeof n.href=="string"?(n=qr(n.href),t=Er(a).hoistableStyles,i=t.get(n),i||(i={type:"style",instance:null,count:0,state:null},t.set(n,i)),i):{type:"void",instance:null,count:0,state:null};case"link":if(n.rel==="stylesheet"&&typeof n.href=="string"&&typeof n.precedence=="string"){e=qr(n.href);var s=Er(a).hoistableStyles,r=s.get(e);if(r||(a=a.ownerDocument||a,r={type:"stylesheet",instance:null,count:0,state:{loading:0,preload:null}},s.set(e,r),(s=a.querySelector(Ml(e)))?s._p||(r.instance=s,r.state.loading=5):(s=ri.get(e),s||(s={rel:"preload",as:"style",href:n.href,crossOrigin:n.crossOrigin,integrity:n.integrity,media:n.media,hrefLang:n.hrefLang,referrerPolicy:n.referrerPolicy},ri.set(e,s)),rb(a,e,s,r.state))),t&&i===null)throw Error(q(528,""));return r}if(t&&i!==null)throw Error(q(529,""));return null;case"script":return t=n.async,n=n.src,typeof n=="string"&&t&&typeof t!="function"&&typeof t!="symbol"?(n=uo(n),t=Er(a).hoistableScripts,i=t.get(n),i||(i={type:"script",instance:null,count:0,state:null},t.set(n,i)),i):{type:"void",instance:null,count:0,state:null};default:throw Error(q(444,e))}}function qr(e){return'href="'+ti(e)+'"'}function Ml(e){return'link[rel="stylesheet"]['+e+"]"}function Wy(e){return de({},e,{"data-precedence":e.precedence,precedence:null})}function rb(e,t,n,i){if(t=e.querySelector('link[rel="preload"][as="style"]['+t+"]")){if(t[$u]!==!0){i.loading=1;return}}else t=e.createElement("link"),t[$u]=!0,t.onload=t.onerror=Mv.bind(null,t),tn(t,"link",n),Ye(t),e.head.appendChild(t);i.preload=t,t.addEventListener("load",function(){return i.loading|=1}),t.addEventListener("error",function(){return i.loading|=2})}function uo(e){return'[src="'+ti(e)+'"]'}function El(e){return"script[async]"+e}function Cg(e,t,n){if(t.count++,t.instance===null)switch(t.type){case"style":var i=e.querySelector('style[data-href~="'+ti(n.href)+'"]');if(i)return t.instance=i,Ye(i),i;var a=de({},n,{"data-href":n.href,"data-precedence":n.precedence,href:null,precedence:null});return i=(e.ownerDocument||e).createElement("style"),Ye(i),tn(i,"style",a),zu(i,n.precedence,e),t.instance=i;case"stylesheet":a=qr(n.href);var s=e.querySelector(Ml(a));if(s)return t.state.loading|=4,t.instance=s,Ye(s),s;i=Wy(n),(a=ri.get(a))&&xm(i,a),s=(e.ownerDocument||e).createElement("link"),Ye(s);var r=s;return r._p=new Promise(function(o,l){r.onload=o,r.onerror=l}),tn(s,"link",i),t.state.loading|=4,zu(s,n.precedence,e),t.instance=s;case"script":return s=uo(n.src),(a=e.querySelector(El(s)))?(t.instance=a,Ye(a),a):(i=n,(a=ri.get(s))&&(i=de({},n),Mm(i,a)),e=e.ownerDocument||e,a=e.createElement("script"),Ye(a),tn(a,"link",i),e.head.appendChild(a),t.instance=a);case"void":return null;default:throw Error(q(443,t.type))}else t.type==="stylesheet"&&!(t.state.loading&4)&&(i=t.instance,t.state.loading|=4,zu(i,n.precedence,e));return t.instance}function zu(e,t,n){for(var i=n.querySelectorAll('link[rel="stylesheet"][data-precedence],style[data-precedence]'),a=i.length?i[i.length-1]:null,s=a,r=0;r<i.length;r++){var o=i[r];if(o.dataset.precedence===t)s=o;else if(s!==a)break}s?s.parentNode.insertBefore(e,s.nextSibling):(t=n.nodeType===9?n.head:n,t.insertBefore(e,t.firstChild))}function xm(e,t){e.crossOrigin==null&&(e.crossOrigin=t.crossOrigin),e.referrerPolicy==null&&(e.referrerPolicy=t.referrerPolicy),e.title==null&&(e.title=t.title)}function Mm(e,t){e.crossOrigin==null&&(e.crossOrigin=t.crossOrigin),e.referrerPolicy==null&&(e.referrerPolicy=t.referrerPolicy),e.integrity==null&&(e.integrity=t.integrity)}var Iu=null;function wg(e,t,n){if(Iu===null){var i=new Map,a=Iu=new Map;a.set(n,i)}else a=Iu,i=a.get(n),i||(i=new Map,a.set(n,i));if(i.has(e))return i;for(i.set(e,null),n=n.getElementsByTagName(e),a=0;a<n.length;a++){var s=n[a];if(!(s[_l]||s[Ke]||e==="link"&&s.getAttribute("rel")==="stylesheet")&&s.namespaceURI!=="http://www.w3.org/2000/svg"){var r=s.getAttribute(t)||"";r=e+r;var o=i.get(r);o?o.push(s):i.set(r,[s])}}return i}function Nd(e,t,n){e=e.ownerDocument||e,e.head.insertBefore(n,t==="title"?e.querySelector("head > title"):null)}function ob(e,t,n){if(n===1||t.itemProp!=null)return!1;switch(e){case"meta":case"title":return!0;case"style":if(typeof t.precedence!="string"||typeof t.href!="string"||t.href==="")break;return!0;case"link":if(typeof t.rel!="string"||typeof t.href!="string"||t.href===""||t.onLoad||t.onError)break;switch(t.rel){case"stylesheet":return e=t.disabled,typeof t.precedence=="string"&&e==null;default:return!0}case"script":if(t.async&&typeof t.async!="function"&&typeof t.async!="symbol"&&!t.onLoad&&!t.onError&&t.src&&typeof t.src=="string")return!0}return!1}function Dg(e,t){return e==="img"&&t.src!=null&&t.src!==""&&t.onLoad==null&&t.loading!=="lazy"}function jy(e){return!(e.type==="stylesheet"&&!(e.state.loading&3))}function Zy(e){return(e.width||100)*(e.height||100)*(typeof devicePixelRatio=="number"?devicePixelRatio:1)*.25}function Ug(e,t){typeof t.decode=="function"&&(e.imgCount++,t.complete||(e.imgBytes+=Zy(t),e.suspenseyImages.push(t)),e=cb.bind(e),t.decode().then(e,e))}function lb(e,t,n,i){if(n.type==="stylesheet"&&(typeof i.media!="string"||matchMedia(i.media).matches!==!1)&&!(n.state.loading&4)){if(n.instance===null){var a=qr(i.href),s=t.querySelector(Ml(a));if(s){t=s._p,t!==null&&typeof t=="object"&&typeof t.then=="function"&&(e.count++,e=ll.bind(e),t.then(e,e)),n.state.loading|=4,n.instance=s,Ye(s);return}s=t.ownerDocument||t,i=Wy(i),(a=ri.get(a))&&xm(i,a),s=s.createElement("link"),Ye(s);var r=s;r._p=new Promise(function(o,l){r.onload=o,r.onerror=l}),tn(s,"link",i),n.instance=s}e.stylesheets===null&&(e.stylesheets=new Map),e.stylesheets.set(n,t),(t=n.state.preload)&&!(n.state.loading&3)&&(e.count++,n=ll.bind(e),t.addEventListener("load",n),t.addEventListener("error",n))}}var Bu=0;function ub(e,t){return e.stylesheets&&e.count===0&&Fu(e,e.stylesheets),0<e.count||0<e.imgCount?function(n){var i=setTimeout(function(){if(e.stylesheets&&Fu(e,e.stylesheets),e.unsuspend){var s=e.unsuspend;e.unsuspend=null,s()}},6e4+t);0<e.imgBytes&&Bu===0&&(Bu=62500*RT());var a=setTimeout(function(){if(e.waitingForImages=!1,e.count===0&&(e.stylesheets&&Fu(e,e.stylesheets),e.unsuspend)){var s=e.unsuspend;e.unsuspend=null,s()}},(e.imgBytes>Bu?50:800)+t);return e.unsuspend=n,function(){e.unsuspend=null,clearTimeout(i),clearTimeout(a)}}:null}function Ky(e){if(e.count===0&&(e.imgCount===0||!e.waitingForImages)){if(e.stylesheets)Fu(e,e.stylesheets);else if(e.unsuspend){var t=e.unsuspend;e.unsuspend=null,t()}}}function ll(){this.count--,Ky(this)}function cb(){this.imgCount--,Ky(this)}var Mc=null;function Fu(e,t){e.stylesheets=null,e.unsuspend!==null&&(e.count++,Mc=new Map,t.forEach(fb,e),Mc=null,ll.call(e))}function fb(e,t){if(!(t.state.loading&4)){var n=Mc.get(e);if(n)var i=n.get(null);else{n=new Map,Mc.set(e,n);for(var a=e.querySelectorAll("link[data-precedence],style[data-precedence]"),s=0;s<a.length;s++){var r=a[s];(r.nodeName==="LINK"||r.getAttribute("media")!=="not all")&&(n.set(r.dataset.precedence,r),i=r)}i&&n.set(null,i)}a=t.instance,r=a.getAttribute("data-precedence"),s=n.get(r)||i,s===i&&n.set(null,a),n.set(r,a),this.count++,i=ll.bind(this),a.addEventListener("load",i),a.addEventListener("error",i),s?s.parentNode.insertBefore(a,s.nextSibling):(e=e.nodeType===9?e.head:e,e.insertBefore(a,e.firstChild)),t.state.loading|=4}}var Wr={$$typeof:Ci,Provider:null,Consumer:null,_currentValue:vs,_currentValue2:vs,_threadCount:0};function hb(e,t,n,i,a,s,r,o,l){this.tag=1,this.containerInfo=e,this.pingCache=this.current=this.pendingChildren=null,this.timeoutHandle=-1,this.callbackNode=this.next=this.pendingContext=this.context=this.cancelPendingCommit=null,this.callbackPriority=0,this.expirationTimes=pf(-1),this.entangledLanes=this.shellSuspendCounter=this.errorRecoveryDisabledLanes=this.expiredLanes=this.warmLanes=this.pingedLanes=this.suspendedLanes=this.pendingLanes=0,this.entanglements=pf(0),this.hiddenUpdates=pf(null),this.identifierPrefix=i,this.onUncaughtError=a,this.onCaughtError=s,this.onRecoverableError=r,this.pooledCache=null,this.pooledCacheLanes=0,this.formState=l,this.transitionTypes=null,this.incompleteTransitions=new Map}function Qy(e,t,n,i,a,s,r,o,l,u,h,p){return e=new hb(e,t,n,r,l,u,h,p,o),t=1,s===!0&&(t|=24),s=Mn(3,null,null,t),e.current=s,s.stateNode=e,t=Vp(),t.refCount++,e.pooledCache=t,t.refCount++,s.memoizedState={element:i,isDehydrated:n,cache:t},Yp(s),e}function Jy(e){return e?(e=gr,e):gr}function $y(e,t,n,i,a,s){a=Jy(a),i.context===null?i.context=a:i.pendingContext=a,i=La(t),i.payload={element:n},s=s===void 0?null:s,s!==null&&(i.callback=s),n=Oa(e,i,t),n!==null&&(Tn(n,e,t),Ho(n,e,t))}function Ng(e,t){if(e=e.memoizedState,e!==null&&e.dehydrated!==null){var n=e.retryLane;e.retryLane=n!==0&&n<t?n:t}}function Em(e,t){Ng(e,t),(e=e.alternate)&&Ng(e,t)}function tx(e){if(e.tag===13||e.tag===31){var t=Bs(e,67108864);t!==null&&Tn(t,e,67108864),Em(e,67108864)}}function Lg(e){if(e.tag===13||e.tag===31){var t=kn();t=Dp(t);var n=Bs(e,t);n!==null&&Tn(n,e,t),Em(e,t)}}var jr=!0;function db(e,t,n,i){var a=xt.T;xt.T=null;var s=te.p;try{te.p=2,Tm(e,t,n,i)}finally{te.p=s,xt.T=a}}function pb(e,t,n,i){var a=xt.T;xt.T=null;var s=te.p;try{te.p=8,Tm(e,t,n,i)}finally{te.p=s,xt.T=a}}function Tm(e,t,n,i){if(jr){var a=Ld(i);if(a===null)Hf(e,t,i,Ec,n),Og(e,i);else if(_b(a,e,t,n,i))i.stopPropagation();else if(Og(e,i),t&4&&-1<mb.indexOf(e)){for(;a!==null;){var s=ao(a);if(s!==null)switch(s.tag){case 3:if(s=s.stateNode,s.current.memoizedState.isDehydrated){var r=ls(s.pendingLanes);if(r!==0){var o=s;for(o.pendingLanes|=2,o.entangledLanes|=2;r;){var l=1<<31-Xn(r);o.entanglements[1]|=l,r&=~l}zi(s),!($t&6)&&(gc=Gn()+500,xl(0))}}break;case 31:case 13:o=Bs(s,2),o!==null&&Tn(o,s,2),Zc(),Em(s,2)}if(s=Ld(i),s===null&&Hf(e,t,i,Ec,n),s===a)break;a=s}a!==null&&i.stopPropagation()}else Hf(e,t,i,null,n)}}function Ld(e){return e=Lp(e),bm(e)}var Ec=null;function bm(e){if(Ec=null,e=ps(e),e!==null){var t=hl(e);if(t===null)e=null;else{var n=t.tag;if(n===13){if(e=rv(t),e!==null)return e;e=null}else if(n===31){if(e=ov(t),e!==null)return e;e=null}else if(n===3){if(t.stateNode.current.memoizedState.isDehydrated)return t.tag===3?t.stateNode.containerInfo:null;e=null}else t!==e&&(e=null)}}return Ec=e,null}function ex(e){switch(e){case"beforetoggle":case"cancel":case"click":case"close":case"contextmenu":case"copy":case"cut":case"auxclick":case"dblclick":case"dragend":case"dragstart":case"drop":case"focusin":case"focusout":case"input":case"invalid":case"keydown":case"keypress":case"keyup":case"mousedown":case"mouseup":case"paste":case"pause":case"play":case"pointercancel":case"pointerdown":case"pointerup":case"ratechange":case"reset":case"seeked":case"submit":case"toggle":case"touchcancel":case"touchend":case"touchstart":case"volumechange":case"change":case"selectionchange":case"textInput":case"compositionstart":case"compositionend":case"compositionupdate":case"beforeblur":case"afterblur":case"beforeinput":case"blur":case"fullscreenchange":case"fullscreenerror":case"focus":case"hashchange":case"popstate":case"select":case"selectstart":return 2;case"drag":case"dragenter":case"dragexit":case"dragleave":case"dragover":case"mousemove":case"mouseout":case"mouseover":case"pointermove":case"pointerout":case"pointerover":case"resize":case"scroll":case"touchmove":case"wheel":case"mouseenter":case"mouseleave":case"pointerenter":case"pointerleave":return 8;case"message":switch(RM()){case dv:return 2;case pv:return 8;case Ju:case CM:return 32;case mv:return 268435456;default:return 32}default:return 32}}var Od=!1,Ba=null,Fa=null,Ha=null,ul=new Map,cl=new Map,Ea=[],mb="mousedown mouseup touchcancel touchend touchstart auxclick dblclick pointercancel pointerdown pointerup dragend dragstart drop compositionend compositionstart keydown keypress keyup input textInput copy cut paste click change contextmenu reset".split(" ");function Og(e,t){switch(e){case"focusin":case"focusout":Ba=null;break;case"dragenter":case"dragleave":Fa=null;break;case"mouseover":case"mouseout":Ha=null;break;case"pointerover":case"pointerout":ul.delete(t.pointerId);break;case"gotpointercapture":case"lostpointercapture":cl.delete(t.pointerId)}}function vo(e,t,n,i,a,s){return e===null||e.nativeEvent!==s?(e={blockedOn:t,domEventName:n,eventSystemFlags:i,nativeEvent:s,targetContainers:[a]},t!==null&&(t=ao(t),t!==null&&tx(t)),e):(e.eventSystemFlags|=i,t=e.targetContainers,a!==null&&t.indexOf(a)===-1&&t.push(a),e)}function _b(e,t,n,i,a){switch(t){case"focusin":return Ba=vo(Ba,e,t,n,i,a),!0;case"dragenter":return Fa=vo(Fa,e,t,n,i,a),!0;case"mouseover":return Ha=vo(Ha,e,t,n,i,a),!0;case"pointerover":var s=a.pointerId;return ul.set(s,vo(ul.get(s)||null,e,t,n,i,a)),!0;case"gotpointercapture":return s=a.pointerId,cl.set(s,vo(cl.get(s)||null,e,t,n,i,a)),!0}return!1}function nx(e){var t=ps(e.target);if(t!==null){var n=hl(t);if(n!==null){if(t=n.tag,t===13){if(t=rv(n),t!==null){e.blockedOn=t,o_(e.priority,function(){Lg(n)});return}}else if(t===31){if(t=ov(n),t!==null){e.blockedOn=t,o_(e.priority,function(){Lg(n)});return}}else if(t===3&&n.stateNode.current.memoizedState.isDehydrated){e.blockedOn=n.tag===3?n.stateNode.containerInfo:null;return}}}e.blockedOn=null}function Hu(e){if(e.blockedOn!==null)return!1;for(var t=e.targetContainers;0<t.length;){var n=Ld(e.nativeEvent);if(n===null){n=e.nativeEvent;var i=new n.constructor(n.type,n);Ih=i,n.target.dispatchEvent(i),Ih=null}else return t=ao(n),t!==null&&tx(t),e.blockedOn=n,!1;t.shift()}return!0}function Pg(e,t,n){Hu(e)&&n.delete(t)}function gb(){Od=!1,Ba!==null&&Hu(Ba)&&(Ba=null),Fa!==null&&Hu(Fa)&&(Fa=null),Ha!==null&&Hu(Ha)&&(Ha=null),ul.forEach(Pg),cl.forEach(Pg)}function Wl(e,t){e.blockedOn===t&&(e.blockedOn=null,Od||(Od=!0,Fe.unstable_scheduleCallback(Fe.unstable_NormalPriority,gb)))}var jl=null;function zg(e){jl!==e&&(jl=e,Fe.unstable_scheduleCallback(Fe.unstable_NormalPriority,function(){jl===e&&(jl=null);for(var t=0;t<e.length;t+=3){var n=e[t],i=e[t+1],a=e[t+2];if(typeof i!="function"){if(bm(i||n)===null)continue;break}var s=ao(n);s!==null&&(e.splice(t,3),t-=3,$h(s,{pending:!0,data:a,method:n.method,action:i},i,a))}}))}function Zr(e){function t(l){return Wl(l,e)}Ba!==null&&Wl(Ba,e),Fa!==null&&Wl(Fa,e),Ha!==null&&Wl(Ha,e),ul.forEach(t),cl.forEach(t);for(var n=0;n<Ea.length;n++){var i=Ea[n];i.blockedOn===e&&(i.blockedOn=null)}for(;0<Ea.length&&(n=Ea[0],n.blockedOn===null);)nx(n),n.blockedOn===null&&Ea.shift();if(n=(e.ownerDocument||e).$$reactFormReplay,n!=null)for(i=0;i<n.length;i+=3){var a=n[i],s=n[i+1],r=a[Cn]||null;if(typeof s=="function")r||zg(n);else if(r){var o=null;if(s&&s.hasAttribute("formAction")){if(a=s,r=s[Cn]||null)o=r.formAction;else if(bm(a)!==null)continue}else o=r.action;typeof o=="function"?n[i+1]=o:(n.splice(i,3),i-=3),zg(n)}}}function ix(){function e(s){s.canIntercept&&s.info==="react-transition"&&s.intercept({handler:function(){return new Promise(function(r){return a=r})},focusReset:"manual",scroll:"manual"})}function t(){a!==null&&(a(),a=null),i||setTimeout(n,20)}function n(){if(!i&&!navigation.transition){var s=navigation.currentEntry;s&&s.url!=null&&navigation.navigate(s.url,{state:s.getState(),info:"react-transition",history:"replace"})}}if(typeof navigation=="object"){var i=!1,a=null;return navigation.addEventListener("navigate",e),navigation.addEventListener("navigatesuccess",t),navigation.addEventListener("navigateerror",t),setTimeout(n,100),function(){i=!0,navigation.removeEventListener("navigate",e),navigation.removeEventListener("navigatesuccess",t),navigation.removeEventListener("navigateerror",t),a!==null&&(a(),a=null)}}}function Am(e){this._internalRoot=e}Jc.prototype.render=Am.prototype.render=function(e){var t=this._internalRoot;if(t===null)throw Error(q(409));var n=t.current,i=kn();$y(n,i,e,t,null,null)};Jc.prototype.unmount=Am.prototype.unmount=function(){var e=this._internalRoot;if(e!==null){this._internalRoot=null;var t=e.containerInfo;$y(e.current,2,null,e,null,null),Zc(),t[io]=null}};function Jc(e){this._internalRoot=e}Jc.prototype.unstable_scheduleHydration=function(e){if(e){var t=xv();e={blockedOn:null,target:e,priority:t};for(var n=0;n<Ea.length&&t!==0&&t<Ea[n].priority;n++);Ea.splice(n,0,e),n===0&&nx(e)}};var Ig=av.version;if(Ig!=="19.3.1")throw Error(q(527,Ig,"19.3.1"));te.findDOMNode=function(e){var t=e._reactInternals;if(t===void 0)throw typeof e.render=="function"?Error(q(188)):(e=Object.keys(e).join(","),Error(q(268,e)));return e=_M(t),e=e!==null?lv(e):null,e=e===null?null:e.stateNode,e};var vb={bundleType:0,version:"19.3.1",rendererPackageName:"react-dom",currentDispatcherRef:xt,reconcilerVersion:"19.3.1"};if(typeof __REACT_DEVTOOLS_GLOBAL_HOOK__<"u"){var Zl=__REACT_DEVTOOLS_GLOBAL_HOOK__;if(!Zl.isDisabled&&Zl.supportsFiber)try{dl=Zl.inject(vb),Vn=Zl}catch{}}Nc.createRoot=function(e,t){if(!sv(e))throw Error(q(299));var n=!1,i="",a=BS,s=FS,r=HS;return t!=null&&(t.unstable_strictMode===!0&&(n=!0),t.identifierPrefix!==void 0&&(i=t.identifierPrefix),t.onUncaughtError!==void 0&&(a=t.onUncaughtError),t.onCaughtError!==void 0&&(s=t.onCaughtError),t.onRecoverableError!==void 0&&(r=t.onRecoverableError)),t=Qy(e,1,!1,null,null,n,i,null,a,s,r,ix),e[io]=t.current,gm(e),new Am(t)};Nc.hydrateRoot=function(e,t,n){if(!sv(e))throw Error(q(299));var i=!1,a="",s=BS,r=FS,o=HS,l=null;return n!=null&&(n.unstable_strictMode===!0&&(i=!0),n.identifierPrefix!==void 0&&(a=n.identifierPrefix),n.onUncaughtError!==void 0&&(s=n.onUncaughtError),n.onCaughtError!==void 0&&(r=n.onCaughtError),n.onRecoverableError!==void 0&&(o=n.onRecoverableError),n.formState!==void 0&&(l=n.formState)),t=Qy(e,1,!0,t,n??null,i,a,l,s,r,o,ix),t.context=Jy(null),n=t.current,i=kn(),i=Dp(i),a=La(i),a.callback=null,Oa(n,a,i),n=i,t.current.lanes=n,ml(t,n),zi(t),e[io]=t.current,gm(e),new Jc(t)};Nc.version="19.3.1";function ax(){if(!(typeof __REACT_DEVTOOLS_GLOBAL_HOOK__>"u"||typeof __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE!="function"))try{__REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE(ax)}catch(e){console.error(e)}}ax(),J0.exports=Nc;var Sb=J0.exports;/**
 * @license
 * Copyright 2010-2024 Three.js Authors
 * SPDX-License-Identifier: MIT
 */const Rm="169",Lr={ROTATE:0,DOLLY:1,PAN:2},xr={ROTATE:0,PAN:1,DOLLY_PAN:2,DOLLY_ROTATE:3},yb=0,Bg=1,xb=2,sx=1,Mb=2,Yi=3,ja=0,bn=1,pi=2,Ga=0,Or=1,Fg=2,Hg=3,Gg=4,Eb=5,hs=100,Tb=101,bb=102,Ab=103,Rb=104,Cb=200,wb=201,Db=202,Ub=203,Pd=204,zd=205,Nb=206,Lb=207,Ob=208,Pb=209,zb=210,Ib=211,Bb=212,Fb=213,Hb=214,Id=0,Bd=1,Fd=2,Kr=3,Hd=4,Gd=5,Vd=6,Xd=7,rx=0,Gb=1,Vb=2,Va=0,Xb=1,kb=2,Yb=3,qb=4,Wb=5,jb=6,Zb=7,ox=300,Qr=301,Jr=302,kd=303,Yd=304,$c=306,qd=1e3,_s=1001,Wd=1002,ii=1003,Kb=1004,Kl=1005,mi=1006,kf=1007,gs=1008,aa=1009,lx=1010,ux=1011,fl=1012,Cm=1013,Us=1014,ji=1015,Tl=1016,wm=1017,Dm=1018,$r=1020,cx=35902,fx=1021,hx=1022,vi=1023,dx=1024,px=1025,Pr=1026,to=1027,mx=1028,Um=1029,_x=1030,Nm=1031,Lm=1033,Gu=33776,Vu=33777,Xu=33778,ku=33779,jd=35840,Zd=35841,Kd=35842,Qd=35843,Jd=36196,$d=37492,tp=37496,ep=37808,np=37809,ip=37810,ap=37811,sp=37812,rp=37813,op=37814,lp=37815,up=37816,cp=37817,fp=37818,hp=37819,dp=37820,pp=37821,Yu=36492,mp=36494,_p=36495,gx=36283,gp=36284,vp=36285,Sp=36286,Qb=3200,Jb=3201,$b=0,t1=1,Ta="",Ti="srgb",Ja="srgb-linear",Om="display-p3",tf="display-p3-linear",Tc="linear",xe="srgb",bc="rec709",Ac="p3",ks=7680,Vg=519,e1=512,n1=513,i1=514,vx=515,a1=516,s1=517,r1=518,o1=519,Xg=35044,kg="300 es",Zi=2e3,Rc=2001;class Hs{addEventListener(t,n){this._listeners===void 0&&(this._listeners={});const i=this._listeners;i[t]===void 0&&(i[t]=[]),i[t].indexOf(n)===-1&&i[t].push(n)}hasEventListener(t,n){if(this._listeners===void 0)return!1;const i=this._listeners;return i[t]!==void 0&&i[t].indexOf(n)!==-1}removeEventListener(t,n){if(this._listeners===void 0)return;const a=this._listeners[t];if(a!==void 0){const s=a.indexOf(n);s!==-1&&a.splice(s,1)}}dispatchEvent(t){if(this._listeners===void 0)return;const i=this._listeners[t.type];if(i!==void 0){t.target=this;const a=i.slice(0);for(let s=0,r=a.length;s<r;s++)a[s].call(this,t);t.target=null}}}const an=["00","01","02","03","04","05","06","07","08","09","0a","0b","0c","0d","0e","0f","10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","20","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","40","41","42","43","44","45","46","47","48","49","4a","4b","4c","4d","4e","4f","50","51","52","53","54","55","56","57","58","59","5a","5b","5c","5d","5e","5f","60","61","62","63","64","65","66","67","68","69","6a","6b","6c","6d","6e","6f","70","71","72","73","74","75","76","77","78","79","7a","7b","7c","7d","7e","7f","80","81","82","83","84","85","86","87","88","89","8a","8b","8c","8d","8e","8f","90","91","92","93","94","95","96","97","98","99","9a","9b","9c","9d","9e","9f","a0","a1","a2","a3","a4","a5","a6","a7","a8","a9","aa","ab","ac","ad","ae","af","b0","b1","b2","b3","b4","b5","b6","b7","b8","b9","ba","bb","bc","bd","be","bf","c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","ca","cb","cc","cd","ce","cf","d0","d1","d2","d3","d4","d5","d6","d7","d8","d9","da","db","dc","dd","de","df","e0","e1","e2","e3","e4","e5","e6","e7","e8","e9","ea","eb","ec","ed","ee","ef","f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","fa","fb","fc","fd","fe","ff"],qu=Math.PI/180,yp=180/Math.PI;function bl(){const e=Math.random()*4294967295|0,t=Math.random()*4294967295|0,n=Math.random()*4294967295|0,i=Math.random()*4294967295|0;return(an[e&255]+an[e>>8&255]+an[e>>16&255]+an[e>>24&255]+"-"+an[t&255]+an[t>>8&255]+"-"+an[t>>16&15|64]+an[t>>24&255]+"-"+an[n&63|128]+an[n>>8&255]+"-"+an[n>>16&255]+an[n>>24&255]+an[i&255]+an[i>>8&255]+an[i>>16&255]+an[i>>24&255]).toLowerCase()}function hn(e,t,n){return Math.max(t,Math.min(n,e))}function l1(e,t){return(e%t+t)%t}function Yf(e,t,n){return(1-n)*e+n*t}function So(e,t){switch(t.constructor){case Float32Array:return e;case Uint32Array:return e/4294967295;case Uint16Array:return e/65535;case Uint8Array:return e/255;case Int32Array:return Math.max(e/2147483647,-1);case Int16Array:return Math.max(e/32767,-1);case Int8Array:return Math.max(e/127,-1);default:throw new Error("Invalid component type.")}}function gn(e,t){switch(t.constructor){case Float32Array:return e;case Uint32Array:return Math.round(e*4294967295);case Uint16Array:return Math.round(e*65535);case Uint8Array:return Math.round(e*255);case Int32Array:return Math.round(e*2147483647);case Int16Array:return Math.round(e*32767);case Int8Array:return Math.round(e*127);default:throw new Error("Invalid component type.")}}const u1={DEG2RAD:qu};class Lt{constructor(t=0,n=0){Lt.prototype.isVector2=!0,this.x=t,this.y=n}get width(){return this.x}set width(t){this.x=t}get height(){return this.y}set height(t){this.y=t}set(t,n){return this.x=t,this.y=n,this}setScalar(t){return this.x=t,this.y=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setComponent(t,n){switch(t){case 0:this.x=n;break;case 1:this.y=n;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y)}copy(t){return this.x=t.x,this.y=t.y,this}add(t){return this.x+=t.x,this.y+=t.y,this}addScalar(t){return this.x+=t,this.y+=t,this}addVectors(t,n){return this.x=t.x+n.x,this.y=t.y+n.y,this}addScaledVector(t,n){return this.x+=t.x*n,this.y+=t.y*n,this}sub(t){return this.x-=t.x,this.y-=t.y,this}subScalar(t){return this.x-=t,this.y-=t,this}subVectors(t,n){return this.x=t.x-n.x,this.y=t.y-n.y,this}multiply(t){return this.x*=t.x,this.y*=t.y,this}multiplyScalar(t){return this.x*=t,this.y*=t,this}divide(t){return this.x/=t.x,this.y/=t.y,this}divideScalar(t){return this.multiplyScalar(1/t)}applyMatrix3(t){const n=this.x,i=this.y,a=t.elements;return this.x=a[0]*n+a[3]*i+a[6],this.y=a[1]*n+a[4]*i+a[7],this}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this}clamp(t,n){return this.x=Math.max(t.x,Math.min(n.x,this.x)),this.y=Math.max(t.y,Math.min(n.y,this.y)),this}clampScalar(t,n){return this.x=Math.max(t,Math.min(n,this.x)),this.y=Math.max(t,Math.min(n,this.y)),this}clampLength(t,n){const i=this.length();return this.divideScalar(i||1).multiplyScalar(Math.max(t,Math.min(n,i)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this}negate(){return this.x=-this.x,this.y=-this.y,this}dot(t){return this.x*t.x+this.y*t.y}cross(t){return this.x*t.y-this.y*t.x}lengthSq(){return this.x*this.x+this.y*this.y}length(){return Math.sqrt(this.x*this.x+this.y*this.y)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)}normalize(){return this.divideScalar(this.length()||1)}angle(){return Math.atan2(-this.y,-this.x)+Math.PI}angleTo(t){const n=Math.sqrt(this.lengthSq()*t.lengthSq());if(n===0)return Math.PI/2;const i=this.dot(t)/n;return Math.acos(hn(i,-1,1))}distanceTo(t){return Math.sqrt(this.distanceToSquared(t))}distanceToSquared(t){const n=this.x-t.x,i=this.y-t.y;return n*n+i*i}manhattanDistanceTo(t){return Math.abs(this.x-t.x)+Math.abs(this.y-t.y)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,n){return this.x+=(t.x-this.x)*n,this.y+=(t.y-this.y)*n,this}lerpVectors(t,n,i){return this.x=t.x+(n.x-t.x)*i,this.y=t.y+(n.y-t.y)*i,this}equals(t){return t.x===this.x&&t.y===this.y}fromArray(t,n=0){return this.x=t[n],this.y=t[n+1],this}toArray(t=[],n=0){return t[n]=this.x,t[n+1]=this.y,t}fromBufferAttribute(t,n){return this.x=t.getX(n),this.y=t.getY(n),this}rotateAround(t,n){const i=Math.cos(n),a=Math.sin(n),s=this.x-t.x,r=this.y-t.y;return this.x=s*i-r*a+t.x,this.y=s*a+r*i+t.y,this}random(){return this.x=Math.random(),this.y=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y}}class Pt{constructor(t,n,i,a,s,r,o,l,u){Pt.prototype.isMatrix3=!0,this.elements=[1,0,0,0,1,0,0,0,1],t!==void 0&&this.set(t,n,i,a,s,r,o,l,u)}set(t,n,i,a,s,r,o,l,u){const h=this.elements;return h[0]=t,h[1]=a,h[2]=o,h[3]=n,h[4]=s,h[5]=l,h[6]=i,h[7]=r,h[8]=u,this}identity(){return this.set(1,0,0,0,1,0,0,0,1),this}copy(t){const n=this.elements,i=t.elements;return n[0]=i[0],n[1]=i[1],n[2]=i[2],n[3]=i[3],n[4]=i[4],n[5]=i[5],n[6]=i[6],n[7]=i[7],n[8]=i[8],this}extractBasis(t,n,i){return t.setFromMatrix3Column(this,0),n.setFromMatrix3Column(this,1),i.setFromMatrix3Column(this,2),this}setFromMatrix4(t){const n=t.elements;return this.set(n[0],n[4],n[8],n[1],n[5],n[9],n[2],n[6],n[10]),this}multiply(t){return this.multiplyMatrices(this,t)}premultiply(t){return this.multiplyMatrices(t,this)}multiplyMatrices(t,n){const i=t.elements,a=n.elements,s=this.elements,r=i[0],o=i[3],l=i[6],u=i[1],h=i[4],p=i[7],f=i[2],d=i[5],v=i[8],y=a[0],m=a[3],c=a[6],_=a[1],g=a[4],x=a[7],C=a[2],R=a[5],b=a[8];return s[0]=r*y+o*_+l*C,s[3]=r*m+o*g+l*R,s[6]=r*c+o*x+l*b,s[1]=u*y+h*_+p*C,s[4]=u*m+h*g+p*R,s[7]=u*c+h*x+p*b,s[2]=f*y+d*_+v*C,s[5]=f*m+d*g+v*R,s[8]=f*c+d*x+v*b,this}multiplyScalar(t){const n=this.elements;return n[0]*=t,n[3]*=t,n[6]*=t,n[1]*=t,n[4]*=t,n[7]*=t,n[2]*=t,n[5]*=t,n[8]*=t,this}determinant(){const t=this.elements,n=t[0],i=t[1],a=t[2],s=t[3],r=t[4],o=t[5],l=t[6],u=t[7],h=t[8];return n*r*h-n*o*u-i*s*h+i*o*l+a*s*u-a*r*l}invert(){const t=this.elements,n=t[0],i=t[1],a=t[2],s=t[3],r=t[4],o=t[5],l=t[6],u=t[7],h=t[8],p=h*r-o*u,f=o*l-h*s,d=u*s-r*l,v=n*p+i*f+a*d;if(v===0)return this.set(0,0,0,0,0,0,0,0,0);const y=1/v;return t[0]=p*y,t[1]=(a*u-h*i)*y,t[2]=(o*i-a*r)*y,t[3]=f*y,t[4]=(h*n-a*l)*y,t[5]=(a*s-o*n)*y,t[6]=d*y,t[7]=(i*l-u*n)*y,t[8]=(r*n-i*s)*y,this}transpose(){let t;const n=this.elements;return t=n[1],n[1]=n[3],n[3]=t,t=n[2],n[2]=n[6],n[6]=t,t=n[5],n[5]=n[7],n[7]=t,this}getNormalMatrix(t){return this.setFromMatrix4(t).invert().transpose()}transposeIntoArray(t){const n=this.elements;return t[0]=n[0],t[1]=n[3],t[2]=n[6],t[3]=n[1],t[4]=n[4],t[5]=n[7],t[6]=n[2],t[7]=n[5],t[8]=n[8],this}setUvTransform(t,n,i,a,s,r,o){const l=Math.cos(s),u=Math.sin(s);return this.set(i*l,i*u,-i*(l*r+u*o)+r+t,-a*u,a*l,-a*(-u*r+l*o)+o+n,0,0,1),this}scale(t,n){return this.premultiply(qf.makeScale(t,n)),this}rotate(t){return this.premultiply(qf.makeRotation(-t)),this}translate(t,n){return this.premultiply(qf.makeTranslation(t,n)),this}makeTranslation(t,n){return t.isVector2?this.set(1,0,t.x,0,1,t.y,0,0,1):this.set(1,0,t,0,1,n,0,0,1),this}makeRotation(t){const n=Math.cos(t),i=Math.sin(t);return this.set(n,-i,0,i,n,0,0,0,1),this}makeScale(t,n){return this.set(t,0,0,0,n,0,0,0,1),this}equals(t){const n=this.elements,i=t.elements;for(let a=0;a<9;a++)if(n[a]!==i[a])return!1;return!0}fromArray(t,n=0){for(let i=0;i<9;i++)this.elements[i]=t[i+n];return this}toArray(t=[],n=0){const i=this.elements;return t[n]=i[0],t[n+1]=i[1],t[n+2]=i[2],t[n+3]=i[3],t[n+4]=i[4],t[n+5]=i[5],t[n+6]=i[6],t[n+7]=i[7],t[n+8]=i[8],t}clone(){return new this.constructor().fromArray(this.elements)}}const qf=new Pt;function Sx(e){for(let t=e.length-1;t>=0;--t)if(e[t]>=65535)return!0;return!1}function Cc(e){return document.createElementNS("http://www.w3.org/1999/xhtml",e)}function c1(){const e=Cc("canvas");return e.style.display="block",e}const Yg={};function Wu(e){e in Yg||(Yg[e]=!0,console.warn(e))}function f1(e,t,n){return new Promise(function(i,a){function s(){switch(e.clientWaitSync(t,e.SYNC_FLUSH_COMMANDS_BIT,0)){case e.WAIT_FAILED:a();break;case e.TIMEOUT_EXPIRED:setTimeout(s,n);break;default:i()}}setTimeout(s,n)})}function h1(e){const t=e.elements;t[2]=.5*t[2]+.5*t[3],t[6]=.5*t[6]+.5*t[7],t[10]=.5*t[10]+.5*t[11],t[14]=.5*t[14]+.5*t[15]}function d1(e){const t=e.elements;t[11]===-1?(t[10]=-t[10]-1,t[14]=-t[14]):(t[10]=-t[10],t[14]=-t[14]+1)}const qg=new Pt().set(.8224621,.177538,0,.0331941,.9668058,0,.0170827,.0723974,.9105199),Wg=new Pt().set(1.2249401,-.2249404,0,-.0420569,1.0420571,0,-.0196376,-.0786361,1.0982735),yo={[Ja]:{transfer:Tc,primaries:bc,luminanceCoefficients:[.2126,.7152,.0722],toReference:e=>e,fromReference:e=>e},[Ti]:{transfer:xe,primaries:bc,luminanceCoefficients:[.2126,.7152,.0722],toReference:e=>e.convertSRGBToLinear(),fromReference:e=>e.convertLinearToSRGB()},[tf]:{transfer:Tc,primaries:Ac,luminanceCoefficients:[.2289,.6917,.0793],toReference:e=>e.applyMatrix3(Wg),fromReference:e=>e.applyMatrix3(qg)},[Om]:{transfer:xe,primaries:Ac,luminanceCoefficients:[.2289,.6917,.0793],toReference:e=>e.convertSRGBToLinear().applyMatrix3(Wg),fromReference:e=>e.applyMatrix3(qg).convertLinearToSRGB()}},p1=new Set([Ja,tf]),ae={enabled:!0,_workingColorSpace:Ja,get workingColorSpace(){return this._workingColorSpace},set workingColorSpace(e){if(!p1.has(e))throw new Error(`Unsupported working color space, "${e}".`);this._workingColorSpace=e},convert:function(e,t,n){if(this.enabled===!1||t===n||!t||!n)return e;const i=yo[t].toReference,a=yo[n].fromReference;return a(i(e))},fromWorkingColorSpace:function(e,t){return this.convert(e,this._workingColorSpace,t)},toWorkingColorSpace:function(e,t){return this.convert(e,t,this._workingColorSpace)},getPrimaries:function(e){return yo[e].primaries},getTransfer:function(e){return e===Ta?Tc:yo[e].transfer},getLuminanceCoefficients:function(e,t=this._workingColorSpace){return e.fromArray(yo[t].luminanceCoefficients)}};function zr(e){return e<.04045?e*.0773993808:Math.pow(e*.9478672986+.0521327014,2.4)}function Wf(e){return e<.0031308?e*12.92:1.055*Math.pow(e,.41666)-.055}let Ys;class m1{static getDataURL(t){if(/^data:/i.test(t.src)||typeof HTMLCanvasElement>"u")return t.src;let n;if(t instanceof HTMLCanvasElement)n=t;else{Ys===void 0&&(Ys=Cc("canvas")),Ys.width=t.width,Ys.height=t.height;const i=Ys.getContext("2d");t instanceof ImageData?i.putImageData(t,0,0):i.drawImage(t,0,0,t.width,t.height),n=Ys}return n.width>2048||n.height>2048?(console.warn("THREE.ImageUtils.getDataURL: Image converted to jpg for performance reasons",t),n.toDataURL("image/jpeg",.6)):n.toDataURL("image/png")}static sRGBToLinear(t){if(typeof HTMLImageElement<"u"&&t instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&t instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&t instanceof ImageBitmap){const n=Cc("canvas");n.width=t.width,n.height=t.height;const i=n.getContext("2d");i.drawImage(t,0,0,t.width,t.height);const a=i.getImageData(0,0,t.width,t.height),s=a.data;for(let r=0;r<s.length;r++)s[r]=zr(s[r]/255)*255;return i.putImageData(a,0,0),n}else if(t.data){const n=t.data.slice(0);for(let i=0;i<n.length;i++)n instanceof Uint8Array||n instanceof Uint8ClampedArray?n[i]=Math.floor(zr(n[i]/255)*255):n[i]=zr(n[i]);return{data:n,width:t.width,height:t.height}}else return console.warn("THREE.ImageUtils.sRGBToLinear(): Unsupported image type. No color space conversion applied."),t}}let _1=0;class yx{constructor(t=null){this.isSource=!0,Object.defineProperty(this,"id",{value:_1++}),this.uuid=bl(),this.data=t,this.dataReady=!0,this.version=0}set needsUpdate(t){t===!0&&this.version++}toJSON(t){const n=t===void 0||typeof t=="string";if(!n&&t.images[this.uuid]!==void 0)return t.images[this.uuid];const i={uuid:this.uuid,url:""},a=this.data;if(a!==null){let s;if(Array.isArray(a)){s=[];for(let r=0,o=a.length;r<o;r++)a[r].isDataTexture?s.push(jf(a[r].image)):s.push(jf(a[r]))}else s=jf(a);i.url=s}return n||(t.images[this.uuid]=i),i}}function jf(e){return typeof HTMLImageElement<"u"&&e instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&e instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&e instanceof ImageBitmap?m1.getDataURL(e):e.data?{data:Array.from(e.data),width:e.width,height:e.height,type:e.data.constructor.name}:(console.warn("THREE.Texture: Unable to serialize Texture."),{})}let g1=0;class An extends Hs{constructor(t=An.DEFAULT_IMAGE,n=An.DEFAULT_MAPPING,i=_s,a=_s,s=mi,r=gs,o=vi,l=aa,u=An.DEFAULT_ANISOTROPY,h=Ta){super(),this.isTexture=!0,Object.defineProperty(this,"id",{value:g1++}),this.uuid=bl(),this.name="",this.source=new yx(t),this.mipmaps=[],this.mapping=n,this.channel=0,this.wrapS=i,this.wrapT=a,this.magFilter=s,this.minFilter=r,this.anisotropy=u,this.format=o,this.internalFormat=null,this.type=l,this.offset=new Lt(0,0),this.repeat=new Lt(1,1),this.center=new Lt(0,0),this.rotation=0,this.matrixAutoUpdate=!0,this.matrix=new Pt,this.generateMipmaps=!0,this.premultiplyAlpha=!1,this.flipY=!0,this.unpackAlignment=4,this.colorSpace=h,this.userData={},this.version=0,this.onUpdate=null,this.isRenderTargetTexture=!1,this.pmremVersion=0}get image(){return this.source.data}set image(t=null){this.source.data=t}updateMatrix(){this.matrix.setUvTransform(this.offset.x,this.offset.y,this.repeat.x,this.repeat.y,this.rotation,this.center.x,this.center.y)}clone(){return new this.constructor().copy(this)}copy(t){return this.name=t.name,this.source=t.source,this.mipmaps=t.mipmaps.slice(0),this.mapping=t.mapping,this.channel=t.channel,this.wrapS=t.wrapS,this.wrapT=t.wrapT,this.magFilter=t.magFilter,this.minFilter=t.minFilter,this.anisotropy=t.anisotropy,this.format=t.format,this.internalFormat=t.internalFormat,this.type=t.type,this.offset.copy(t.offset),this.repeat.copy(t.repeat),this.center.copy(t.center),this.rotation=t.rotation,this.matrixAutoUpdate=t.matrixAutoUpdate,this.matrix.copy(t.matrix),this.generateMipmaps=t.generateMipmaps,this.premultiplyAlpha=t.premultiplyAlpha,this.flipY=t.flipY,this.unpackAlignment=t.unpackAlignment,this.colorSpace=t.colorSpace,this.userData=JSON.parse(JSON.stringify(t.userData)),this.needsUpdate=!0,this}toJSON(t){const n=t===void 0||typeof t=="string";if(!n&&t.textures[this.uuid]!==void 0)return t.textures[this.uuid];const i={metadata:{version:4.6,type:"Texture",generator:"Texture.toJSON"},uuid:this.uuid,name:this.name,image:this.source.toJSON(t).uuid,mapping:this.mapping,channel:this.channel,repeat:[this.repeat.x,this.repeat.y],offset:[this.offset.x,this.offset.y],center:[this.center.x,this.center.y],rotation:this.rotation,wrap:[this.wrapS,this.wrapT],format:this.format,internalFormat:this.internalFormat,type:this.type,colorSpace:this.colorSpace,minFilter:this.minFilter,magFilter:this.magFilter,anisotropy:this.anisotropy,flipY:this.flipY,generateMipmaps:this.generateMipmaps,premultiplyAlpha:this.premultiplyAlpha,unpackAlignment:this.unpackAlignment};return Object.keys(this.userData).length>0&&(i.userData=this.userData),n||(t.textures[this.uuid]=i),i}dispose(){this.dispatchEvent({type:"dispose"})}transformUv(t){if(this.mapping!==ox)return t;if(t.applyMatrix3(this.matrix),t.x<0||t.x>1)switch(this.wrapS){case qd:t.x=t.x-Math.floor(t.x);break;case _s:t.x=t.x<0?0:1;break;case Wd:Math.abs(Math.floor(t.x)%2)===1?t.x=Math.ceil(t.x)-t.x:t.x=t.x-Math.floor(t.x);break}if(t.y<0||t.y>1)switch(this.wrapT){case qd:t.y=t.y-Math.floor(t.y);break;case _s:t.y=t.y<0?0:1;break;case Wd:Math.abs(Math.floor(t.y)%2)===1?t.y=Math.ceil(t.y)-t.y:t.y=t.y-Math.floor(t.y);break}return this.flipY&&(t.y=1-t.y),t}set needsUpdate(t){t===!0&&(this.version++,this.source.needsUpdate=!0)}set needsPMREMUpdate(t){t===!0&&this.pmremVersion++}}An.DEFAULT_IMAGE=null;An.DEFAULT_MAPPING=ox;An.DEFAULT_ANISOTROPY=1;class Ce{constructor(t=0,n=0,i=0,a=1){Ce.prototype.isVector4=!0,this.x=t,this.y=n,this.z=i,this.w=a}get width(){return this.z}set width(t){this.z=t}get height(){return this.w}set height(t){this.w=t}set(t,n,i,a){return this.x=t,this.y=n,this.z=i,this.w=a,this}setScalar(t){return this.x=t,this.y=t,this.z=t,this.w=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setZ(t){return this.z=t,this}setW(t){return this.w=t,this}setComponent(t,n){switch(t){case 0:this.x=n;break;case 1:this.y=n;break;case 2:this.z=n;break;case 3:this.w=n;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;case 2:return this.z;case 3:return this.w;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y,this.z,this.w)}copy(t){return this.x=t.x,this.y=t.y,this.z=t.z,this.w=t.w!==void 0?t.w:1,this}add(t){return this.x+=t.x,this.y+=t.y,this.z+=t.z,this.w+=t.w,this}addScalar(t){return this.x+=t,this.y+=t,this.z+=t,this.w+=t,this}addVectors(t,n){return this.x=t.x+n.x,this.y=t.y+n.y,this.z=t.z+n.z,this.w=t.w+n.w,this}addScaledVector(t,n){return this.x+=t.x*n,this.y+=t.y*n,this.z+=t.z*n,this.w+=t.w*n,this}sub(t){return this.x-=t.x,this.y-=t.y,this.z-=t.z,this.w-=t.w,this}subScalar(t){return this.x-=t,this.y-=t,this.z-=t,this.w-=t,this}subVectors(t,n){return this.x=t.x-n.x,this.y=t.y-n.y,this.z=t.z-n.z,this.w=t.w-n.w,this}multiply(t){return this.x*=t.x,this.y*=t.y,this.z*=t.z,this.w*=t.w,this}multiplyScalar(t){return this.x*=t,this.y*=t,this.z*=t,this.w*=t,this}applyMatrix4(t){const n=this.x,i=this.y,a=this.z,s=this.w,r=t.elements;return this.x=r[0]*n+r[4]*i+r[8]*a+r[12]*s,this.y=r[1]*n+r[5]*i+r[9]*a+r[13]*s,this.z=r[2]*n+r[6]*i+r[10]*a+r[14]*s,this.w=r[3]*n+r[7]*i+r[11]*a+r[15]*s,this}divideScalar(t){return this.multiplyScalar(1/t)}setAxisAngleFromQuaternion(t){this.w=2*Math.acos(t.w);const n=Math.sqrt(1-t.w*t.w);return n<1e-4?(this.x=1,this.y=0,this.z=0):(this.x=t.x/n,this.y=t.y/n,this.z=t.z/n),this}setAxisAngleFromRotationMatrix(t){let n,i,a,s;const l=t.elements,u=l[0],h=l[4],p=l[8],f=l[1],d=l[5],v=l[9],y=l[2],m=l[6],c=l[10];if(Math.abs(h-f)<.01&&Math.abs(p-y)<.01&&Math.abs(v-m)<.01){if(Math.abs(h+f)<.1&&Math.abs(p+y)<.1&&Math.abs(v+m)<.1&&Math.abs(u+d+c-3)<.1)return this.set(1,0,0,0),this;n=Math.PI;const g=(u+1)/2,x=(d+1)/2,C=(c+1)/2,R=(h+f)/4,b=(p+y)/4,w=(v+m)/4;return g>x&&g>C?g<.01?(i=0,a=.707106781,s=.707106781):(i=Math.sqrt(g),a=R/i,s=b/i):x>C?x<.01?(i=.707106781,a=0,s=.707106781):(a=Math.sqrt(x),i=R/a,s=w/a):C<.01?(i=.707106781,a=.707106781,s=0):(s=Math.sqrt(C),i=b/s,a=w/s),this.set(i,a,s,n),this}let _=Math.sqrt((m-v)*(m-v)+(p-y)*(p-y)+(f-h)*(f-h));return Math.abs(_)<.001&&(_=1),this.x=(m-v)/_,this.y=(p-y)/_,this.z=(f-h)/_,this.w=Math.acos((u+d+c-1)/2),this}setFromMatrixPosition(t){const n=t.elements;return this.x=n[12],this.y=n[13],this.z=n[14],this.w=n[15],this}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this.z=Math.min(this.z,t.z),this.w=Math.min(this.w,t.w),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this.z=Math.max(this.z,t.z),this.w=Math.max(this.w,t.w),this}clamp(t,n){return this.x=Math.max(t.x,Math.min(n.x,this.x)),this.y=Math.max(t.y,Math.min(n.y,this.y)),this.z=Math.max(t.z,Math.min(n.z,this.z)),this.w=Math.max(t.w,Math.min(n.w,this.w)),this}clampScalar(t,n){return this.x=Math.max(t,Math.min(n,this.x)),this.y=Math.max(t,Math.min(n,this.y)),this.z=Math.max(t,Math.min(n,this.z)),this.w=Math.max(t,Math.min(n,this.w)),this}clampLength(t,n){const i=this.length();return this.divideScalar(i||1).multiplyScalar(Math.max(t,Math.min(n,i)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this.w=Math.floor(this.w),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this.w=Math.ceil(this.w),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this.w=Math.round(this.w),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this.w=Math.trunc(this.w),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this.w=-this.w,this}dot(t){return this.x*t.x+this.y*t.y+this.z*t.z+this.w*t.w}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)+Math.abs(this.w)}normalize(){return this.divideScalar(this.length()||1)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,n){return this.x+=(t.x-this.x)*n,this.y+=(t.y-this.y)*n,this.z+=(t.z-this.z)*n,this.w+=(t.w-this.w)*n,this}lerpVectors(t,n,i){return this.x=t.x+(n.x-t.x)*i,this.y=t.y+(n.y-t.y)*i,this.z=t.z+(n.z-t.z)*i,this.w=t.w+(n.w-t.w)*i,this}equals(t){return t.x===this.x&&t.y===this.y&&t.z===this.z&&t.w===this.w}fromArray(t,n=0){return this.x=t[n],this.y=t[n+1],this.z=t[n+2],this.w=t[n+3],this}toArray(t=[],n=0){return t[n]=this.x,t[n+1]=this.y,t[n+2]=this.z,t[n+3]=this.w,t}fromBufferAttribute(t,n){return this.x=t.getX(n),this.y=t.getY(n),this.z=t.getZ(n),this.w=t.getW(n),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this.w=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z,yield this.w}}class v1 extends Hs{constructor(t=1,n=1,i={}){super(),this.isRenderTarget=!0,this.width=t,this.height=n,this.depth=1,this.scissor=new Ce(0,0,t,n),this.scissorTest=!1,this.viewport=new Ce(0,0,t,n);const a={width:t,height:n,depth:1};i=Object.assign({generateMipmaps:!1,internalFormat:null,minFilter:mi,depthBuffer:!0,stencilBuffer:!1,resolveDepthBuffer:!0,resolveStencilBuffer:!0,depthTexture:null,samples:0,count:1},i);const s=new An(a,i.mapping,i.wrapS,i.wrapT,i.magFilter,i.minFilter,i.format,i.type,i.anisotropy,i.colorSpace);s.flipY=!1,s.generateMipmaps=i.generateMipmaps,s.internalFormat=i.internalFormat,this.textures=[];const r=i.count;for(let o=0;o<r;o++)this.textures[o]=s.clone(),this.textures[o].isRenderTargetTexture=!0;this.depthBuffer=i.depthBuffer,this.stencilBuffer=i.stencilBuffer,this.resolveDepthBuffer=i.resolveDepthBuffer,this.resolveStencilBuffer=i.resolveStencilBuffer,this.depthTexture=i.depthTexture,this.samples=i.samples}get texture(){return this.textures[0]}set texture(t){this.textures[0]=t}setSize(t,n,i=1){if(this.width!==t||this.height!==n||this.depth!==i){this.width=t,this.height=n,this.depth=i;for(let a=0,s=this.textures.length;a<s;a++)this.textures[a].image.width=t,this.textures[a].image.height=n,this.textures[a].image.depth=i;this.dispose()}this.viewport.set(0,0,t,n),this.scissor.set(0,0,t,n)}clone(){return new this.constructor().copy(this)}copy(t){this.width=t.width,this.height=t.height,this.depth=t.depth,this.scissor.copy(t.scissor),this.scissorTest=t.scissorTest,this.viewport.copy(t.viewport),this.textures.length=0;for(let i=0,a=t.textures.length;i<a;i++)this.textures[i]=t.textures[i].clone(),this.textures[i].isRenderTargetTexture=!0;const n=Object.assign({},t.texture.image);return this.texture.source=new yx(n),this.depthBuffer=t.depthBuffer,this.stencilBuffer=t.stencilBuffer,this.resolveDepthBuffer=t.resolveDepthBuffer,this.resolveStencilBuffer=t.resolveStencilBuffer,t.depthTexture!==null&&(this.depthTexture=t.depthTexture.clone()),this.samples=t.samples,this}dispose(){this.dispatchEvent({type:"dispose"})}}class Ns extends v1{constructor(t=1,n=1,i={}){super(t,n,i),this.isWebGLRenderTarget=!0}}class xx extends An{constructor(t=null,n=1,i=1,a=1){super(null),this.isDataArrayTexture=!0,this.image={data:t,width:n,height:i,depth:a},this.magFilter=ii,this.minFilter=ii,this.wrapR=_s,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1,this.layerUpdates=new Set}addLayerUpdate(t){this.layerUpdates.add(t)}clearLayerUpdates(){this.layerUpdates.clear()}}class S1 extends An{constructor(t=null,n=1,i=1,a=1){super(null),this.isData3DTexture=!0,this.image={data:t,width:n,height:i,depth:a},this.magFilter=ii,this.minFilter=ii,this.wrapR=_s,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}}class Ls{constructor(t=0,n=0,i=0,a=1){this.isQuaternion=!0,this._x=t,this._y=n,this._z=i,this._w=a}static slerpFlat(t,n,i,a,s,r,o){let l=i[a+0],u=i[a+1],h=i[a+2],p=i[a+3];const f=s[r+0],d=s[r+1],v=s[r+2],y=s[r+3];if(o===0){t[n+0]=l,t[n+1]=u,t[n+2]=h,t[n+3]=p;return}if(o===1){t[n+0]=f,t[n+1]=d,t[n+2]=v,t[n+3]=y;return}if(p!==y||l!==f||u!==d||h!==v){let m=1-o;const c=l*f+u*d+h*v+p*y,_=c>=0?1:-1,g=1-c*c;if(g>Number.EPSILON){const C=Math.sqrt(g),R=Math.atan2(C,c*_);m=Math.sin(m*R)/C,o=Math.sin(o*R)/C}const x=o*_;if(l=l*m+f*x,u=u*m+d*x,h=h*m+v*x,p=p*m+y*x,m===1-o){const C=1/Math.sqrt(l*l+u*u+h*h+p*p);l*=C,u*=C,h*=C,p*=C}}t[n]=l,t[n+1]=u,t[n+2]=h,t[n+3]=p}static multiplyQuaternionsFlat(t,n,i,a,s,r){const o=i[a],l=i[a+1],u=i[a+2],h=i[a+3],p=s[r],f=s[r+1],d=s[r+2],v=s[r+3];return t[n]=o*v+h*p+l*d-u*f,t[n+1]=l*v+h*f+u*p-o*d,t[n+2]=u*v+h*d+o*f-l*p,t[n+3]=h*v-o*p-l*f-u*d,t}get x(){return this._x}set x(t){this._x=t,this._onChangeCallback()}get y(){return this._y}set y(t){this._y=t,this._onChangeCallback()}get z(){return this._z}set z(t){this._z=t,this._onChangeCallback()}get w(){return this._w}set w(t){this._w=t,this._onChangeCallback()}set(t,n,i,a){return this._x=t,this._y=n,this._z=i,this._w=a,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._w)}copy(t){return this._x=t.x,this._y=t.y,this._z=t.z,this._w=t.w,this._onChangeCallback(),this}setFromEuler(t,n=!0){const i=t._x,a=t._y,s=t._z,r=t._order,o=Math.cos,l=Math.sin,u=o(i/2),h=o(a/2),p=o(s/2),f=l(i/2),d=l(a/2),v=l(s/2);switch(r){case"XYZ":this._x=f*h*p+u*d*v,this._y=u*d*p-f*h*v,this._z=u*h*v+f*d*p,this._w=u*h*p-f*d*v;break;case"YXZ":this._x=f*h*p+u*d*v,this._y=u*d*p-f*h*v,this._z=u*h*v-f*d*p,this._w=u*h*p+f*d*v;break;case"ZXY":this._x=f*h*p-u*d*v,this._y=u*d*p+f*h*v,this._z=u*h*v+f*d*p,this._w=u*h*p-f*d*v;break;case"ZYX":this._x=f*h*p-u*d*v,this._y=u*d*p+f*h*v,this._z=u*h*v-f*d*p,this._w=u*h*p+f*d*v;break;case"YZX":this._x=f*h*p+u*d*v,this._y=u*d*p+f*h*v,this._z=u*h*v-f*d*p,this._w=u*h*p-f*d*v;break;case"XZY":this._x=f*h*p-u*d*v,this._y=u*d*p-f*h*v,this._z=u*h*v+f*d*p,this._w=u*h*p+f*d*v;break;default:console.warn("THREE.Quaternion: .setFromEuler() encountered an unknown order: "+r)}return n===!0&&this._onChangeCallback(),this}setFromAxisAngle(t,n){const i=n/2,a=Math.sin(i);return this._x=t.x*a,this._y=t.y*a,this._z=t.z*a,this._w=Math.cos(i),this._onChangeCallback(),this}setFromRotationMatrix(t){const n=t.elements,i=n[0],a=n[4],s=n[8],r=n[1],o=n[5],l=n[9],u=n[2],h=n[6],p=n[10],f=i+o+p;if(f>0){const d=.5/Math.sqrt(f+1);this._w=.25/d,this._x=(h-l)*d,this._y=(s-u)*d,this._z=(r-a)*d}else if(i>o&&i>p){const d=2*Math.sqrt(1+i-o-p);this._w=(h-l)/d,this._x=.25*d,this._y=(a+r)/d,this._z=(s+u)/d}else if(o>p){const d=2*Math.sqrt(1+o-i-p);this._w=(s-u)/d,this._x=(a+r)/d,this._y=.25*d,this._z=(l+h)/d}else{const d=2*Math.sqrt(1+p-i-o);this._w=(r-a)/d,this._x=(s+u)/d,this._y=(l+h)/d,this._z=.25*d}return this._onChangeCallback(),this}setFromUnitVectors(t,n){let i=t.dot(n)+1;return i<Number.EPSILON?(i=0,Math.abs(t.x)>Math.abs(t.z)?(this._x=-t.y,this._y=t.x,this._z=0,this._w=i):(this._x=0,this._y=-t.z,this._z=t.y,this._w=i)):(this._x=t.y*n.z-t.z*n.y,this._y=t.z*n.x-t.x*n.z,this._z=t.x*n.y-t.y*n.x,this._w=i),this.normalize()}angleTo(t){return 2*Math.acos(Math.abs(hn(this.dot(t),-1,1)))}rotateTowards(t,n){const i=this.angleTo(t);if(i===0)return this;const a=Math.min(1,n/i);return this.slerp(t,a),this}identity(){return this.set(0,0,0,1)}invert(){return this.conjugate()}conjugate(){return this._x*=-1,this._y*=-1,this._z*=-1,this._onChangeCallback(),this}dot(t){return this._x*t._x+this._y*t._y+this._z*t._z+this._w*t._w}lengthSq(){return this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w}length(){return Math.sqrt(this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w)}normalize(){let t=this.length();return t===0?(this._x=0,this._y=0,this._z=0,this._w=1):(t=1/t,this._x=this._x*t,this._y=this._y*t,this._z=this._z*t,this._w=this._w*t),this._onChangeCallback(),this}multiply(t){return this.multiplyQuaternions(this,t)}premultiply(t){return this.multiplyQuaternions(t,this)}multiplyQuaternions(t,n){const i=t._x,a=t._y,s=t._z,r=t._w,o=n._x,l=n._y,u=n._z,h=n._w;return this._x=i*h+r*o+a*u-s*l,this._y=a*h+r*l+s*o-i*u,this._z=s*h+r*u+i*l-a*o,this._w=r*h-i*o-a*l-s*u,this._onChangeCallback(),this}slerp(t,n){if(n===0)return this;if(n===1)return this.copy(t);const i=this._x,a=this._y,s=this._z,r=this._w;let o=r*t._w+i*t._x+a*t._y+s*t._z;if(o<0?(this._w=-t._w,this._x=-t._x,this._y=-t._y,this._z=-t._z,o=-o):this.copy(t),o>=1)return this._w=r,this._x=i,this._y=a,this._z=s,this;const l=1-o*o;if(l<=Number.EPSILON){const d=1-n;return this._w=d*r+n*this._w,this._x=d*i+n*this._x,this._y=d*a+n*this._y,this._z=d*s+n*this._z,this.normalize(),this}const u=Math.sqrt(l),h=Math.atan2(u,o),p=Math.sin((1-n)*h)/u,f=Math.sin(n*h)/u;return this._w=r*p+this._w*f,this._x=i*p+this._x*f,this._y=a*p+this._y*f,this._z=s*p+this._z*f,this._onChangeCallback(),this}slerpQuaternions(t,n,i){return this.copy(t).slerp(n,i)}random(){const t=2*Math.PI*Math.random(),n=2*Math.PI*Math.random(),i=Math.random(),a=Math.sqrt(1-i),s=Math.sqrt(i);return this.set(a*Math.sin(t),a*Math.cos(t),s*Math.sin(n),s*Math.cos(n))}equals(t){return t._x===this._x&&t._y===this._y&&t._z===this._z&&t._w===this._w}fromArray(t,n=0){return this._x=t[n],this._y=t[n+1],this._z=t[n+2],this._w=t[n+3],this._onChangeCallback(),this}toArray(t=[],n=0){return t[n]=this._x,t[n+1]=this._y,t[n+2]=this._z,t[n+3]=this._w,t}fromBufferAttribute(t,n){return this._x=t.getX(n),this._y=t.getY(n),this._z=t.getZ(n),this._w=t.getW(n),this._onChangeCallback(),this}toJSON(){return this.toArray()}_onChange(t){return this._onChangeCallback=t,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._w}}class P{constructor(t=0,n=0,i=0){P.prototype.isVector3=!0,this.x=t,this.y=n,this.z=i}set(t,n,i){return i===void 0&&(i=this.z),this.x=t,this.y=n,this.z=i,this}setScalar(t){return this.x=t,this.y=t,this.z=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setZ(t){return this.z=t,this}setComponent(t,n){switch(t){case 0:this.x=n;break;case 1:this.y=n;break;case 2:this.z=n;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;case 2:return this.z;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y,this.z)}copy(t){return this.x=t.x,this.y=t.y,this.z=t.z,this}add(t){return this.x+=t.x,this.y+=t.y,this.z+=t.z,this}addScalar(t){return this.x+=t,this.y+=t,this.z+=t,this}addVectors(t,n){return this.x=t.x+n.x,this.y=t.y+n.y,this.z=t.z+n.z,this}addScaledVector(t,n){return this.x+=t.x*n,this.y+=t.y*n,this.z+=t.z*n,this}sub(t){return this.x-=t.x,this.y-=t.y,this.z-=t.z,this}subScalar(t){return this.x-=t,this.y-=t,this.z-=t,this}subVectors(t,n){return this.x=t.x-n.x,this.y=t.y-n.y,this.z=t.z-n.z,this}multiply(t){return this.x*=t.x,this.y*=t.y,this.z*=t.z,this}multiplyScalar(t){return this.x*=t,this.y*=t,this.z*=t,this}multiplyVectors(t,n){return this.x=t.x*n.x,this.y=t.y*n.y,this.z=t.z*n.z,this}applyEuler(t){return this.applyQuaternion(jg.setFromEuler(t))}applyAxisAngle(t,n){return this.applyQuaternion(jg.setFromAxisAngle(t,n))}applyMatrix3(t){const n=this.x,i=this.y,a=this.z,s=t.elements;return this.x=s[0]*n+s[3]*i+s[6]*a,this.y=s[1]*n+s[4]*i+s[7]*a,this.z=s[2]*n+s[5]*i+s[8]*a,this}applyNormalMatrix(t){return this.applyMatrix3(t).normalize()}applyMatrix4(t){const n=this.x,i=this.y,a=this.z,s=t.elements,r=1/(s[3]*n+s[7]*i+s[11]*a+s[15]);return this.x=(s[0]*n+s[4]*i+s[8]*a+s[12])*r,this.y=(s[1]*n+s[5]*i+s[9]*a+s[13])*r,this.z=(s[2]*n+s[6]*i+s[10]*a+s[14])*r,this}applyQuaternion(t){const n=this.x,i=this.y,a=this.z,s=t.x,r=t.y,o=t.z,l=t.w,u=2*(r*a-o*i),h=2*(o*n-s*a),p=2*(s*i-r*n);return this.x=n+l*u+r*p-o*h,this.y=i+l*h+o*u-s*p,this.z=a+l*p+s*h-r*u,this}project(t){return this.applyMatrix4(t.matrixWorldInverse).applyMatrix4(t.projectionMatrix)}unproject(t){return this.applyMatrix4(t.projectionMatrixInverse).applyMatrix4(t.matrixWorld)}transformDirection(t){const n=this.x,i=this.y,a=this.z,s=t.elements;return this.x=s[0]*n+s[4]*i+s[8]*a,this.y=s[1]*n+s[5]*i+s[9]*a,this.z=s[2]*n+s[6]*i+s[10]*a,this.normalize()}divide(t){return this.x/=t.x,this.y/=t.y,this.z/=t.z,this}divideScalar(t){return this.multiplyScalar(1/t)}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this.z=Math.min(this.z,t.z),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this.z=Math.max(this.z,t.z),this}clamp(t,n){return this.x=Math.max(t.x,Math.min(n.x,this.x)),this.y=Math.max(t.y,Math.min(n.y,this.y)),this.z=Math.max(t.z,Math.min(n.z,this.z)),this}clampScalar(t,n){return this.x=Math.max(t,Math.min(n,this.x)),this.y=Math.max(t,Math.min(n,this.y)),this.z=Math.max(t,Math.min(n,this.z)),this}clampLength(t,n){const i=this.length();return this.divideScalar(i||1).multiplyScalar(Math.max(t,Math.min(n,i)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this}dot(t){return this.x*t.x+this.y*t.y+this.z*t.z}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)}normalize(){return this.divideScalar(this.length()||1)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,n){return this.x+=(t.x-this.x)*n,this.y+=(t.y-this.y)*n,this.z+=(t.z-this.z)*n,this}lerpVectors(t,n,i){return this.x=t.x+(n.x-t.x)*i,this.y=t.y+(n.y-t.y)*i,this.z=t.z+(n.z-t.z)*i,this}cross(t){return this.crossVectors(this,t)}crossVectors(t,n){const i=t.x,a=t.y,s=t.z,r=n.x,o=n.y,l=n.z;return this.x=a*l-s*o,this.y=s*r-i*l,this.z=i*o-a*r,this}projectOnVector(t){const n=t.lengthSq();if(n===0)return this.set(0,0,0);const i=t.dot(this)/n;return this.copy(t).multiplyScalar(i)}projectOnPlane(t){return Zf.copy(this).projectOnVector(t),this.sub(Zf)}reflect(t){return this.sub(Zf.copy(t).multiplyScalar(2*this.dot(t)))}angleTo(t){const n=Math.sqrt(this.lengthSq()*t.lengthSq());if(n===0)return Math.PI/2;const i=this.dot(t)/n;return Math.acos(hn(i,-1,1))}distanceTo(t){return Math.sqrt(this.distanceToSquared(t))}distanceToSquared(t){const n=this.x-t.x,i=this.y-t.y,a=this.z-t.z;return n*n+i*i+a*a}manhattanDistanceTo(t){return Math.abs(this.x-t.x)+Math.abs(this.y-t.y)+Math.abs(this.z-t.z)}setFromSpherical(t){return this.setFromSphericalCoords(t.radius,t.phi,t.theta)}setFromSphericalCoords(t,n,i){const a=Math.sin(n)*t;return this.x=a*Math.sin(i),this.y=Math.cos(n)*t,this.z=a*Math.cos(i),this}setFromCylindrical(t){return this.setFromCylindricalCoords(t.radius,t.theta,t.y)}setFromCylindricalCoords(t,n,i){return this.x=t*Math.sin(n),this.y=i,this.z=t*Math.cos(n),this}setFromMatrixPosition(t){const n=t.elements;return this.x=n[12],this.y=n[13],this.z=n[14],this}setFromMatrixScale(t){const n=this.setFromMatrixColumn(t,0).length(),i=this.setFromMatrixColumn(t,1).length(),a=this.setFromMatrixColumn(t,2).length();return this.x=n,this.y=i,this.z=a,this}setFromMatrixColumn(t,n){return this.fromArray(t.elements,n*4)}setFromMatrix3Column(t,n){return this.fromArray(t.elements,n*3)}setFromEuler(t){return this.x=t._x,this.y=t._y,this.z=t._z,this}setFromColor(t){return this.x=t.r,this.y=t.g,this.z=t.b,this}equals(t){return t.x===this.x&&t.y===this.y&&t.z===this.z}fromArray(t,n=0){return this.x=t[n],this.y=t[n+1],this.z=t[n+2],this}toArray(t=[],n=0){return t[n]=this.x,t[n+1]=this.y,t[n+2]=this.z,t}fromBufferAttribute(t,n){return this.x=t.getX(n),this.y=t.getY(n),this.z=t.getZ(n),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this}randomDirection(){const t=Math.random()*Math.PI*2,n=Math.random()*2-1,i=Math.sqrt(1-n*n);return this.x=i*Math.cos(t),this.y=n,this.z=i*Math.sin(t),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z}}const Zf=new P,jg=new Ls;class Al{constructor(t=new P(1/0,1/0,1/0),n=new P(-1/0,-1/0,-1/0)){this.isBox3=!0,this.min=t,this.max=n}set(t,n){return this.min.copy(t),this.max.copy(n),this}setFromArray(t){this.makeEmpty();for(let n=0,i=t.length;n<i;n+=3)this.expandByPoint(ui.fromArray(t,n));return this}setFromBufferAttribute(t){this.makeEmpty();for(let n=0,i=t.count;n<i;n++)this.expandByPoint(ui.fromBufferAttribute(t,n));return this}setFromPoints(t){this.makeEmpty();for(let n=0,i=t.length;n<i;n++)this.expandByPoint(t[n]);return this}setFromCenterAndSize(t,n){const i=ui.copy(n).multiplyScalar(.5);return this.min.copy(t).sub(i),this.max.copy(t).add(i),this}setFromObject(t,n=!1){return this.makeEmpty(),this.expandByObject(t,n)}clone(){return new this.constructor().copy(this)}copy(t){return this.min.copy(t.min),this.max.copy(t.max),this}makeEmpty(){return this.min.x=this.min.y=this.min.z=1/0,this.max.x=this.max.y=this.max.z=-1/0,this}isEmpty(){return this.max.x<this.min.x||this.max.y<this.min.y||this.max.z<this.min.z}getCenter(t){return this.isEmpty()?t.set(0,0,0):t.addVectors(this.min,this.max).multiplyScalar(.5)}getSize(t){return this.isEmpty()?t.set(0,0,0):t.subVectors(this.max,this.min)}expandByPoint(t){return this.min.min(t),this.max.max(t),this}expandByVector(t){return this.min.sub(t),this.max.add(t),this}expandByScalar(t){return this.min.addScalar(-t),this.max.addScalar(t),this}expandByObject(t,n=!1){t.updateWorldMatrix(!1,!1);const i=t.geometry;if(i!==void 0){const s=i.getAttribute("position");if(n===!0&&s!==void 0&&t.isInstancedMesh!==!0)for(let r=0,o=s.count;r<o;r++)t.isMesh===!0?t.getVertexPosition(r,ui):ui.fromBufferAttribute(s,r),ui.applyMatrix4(t.matrixWorld),this.expandByPoint(ui);else t.boundingBox!==void 0?(t.boundingBox===null&&t.computeBoundingBox(),Ql.copy(t.boundingBox)):(i.boundingBox===null&&i.computeBoundingBox(),Ql.copy(i.boundingBox)),Ql.applyMatrix4(t.matrixWorld),this.union(Ql)}const a=t.children;for(let s=0,r=a.length;s<r;s++)this.expandByObject(a[s],n);return this}containsPoint(t){return t.x>=this.min.x&&t.x<=this.max.x&&t.y>=this.min.y&&t.y<=this.max.y&&t.z>=this.min.z&&t.z<=this.max.z}containsBox(t){return this.min.x<=t.min.x&&t.max.x<=this.max.x&&this.min.y<=t.min.y&&t.max.y<=this.max.y&&this.min.z<=t.min.z&&t.max.z<=this.max.z}getParameter(t,n){return n.set((t.x-this.min.x)/(this.max.x-this.min.x),(t.y-this.min.y)/(this.max.y-this.min.y),(t.z-this.min.z)/(this.max.z-this.min.z))}intersectsBox(t){return t.max.x>=this.min.x&&t.min.x<=this.max.x&&t.max.y>=this.min.y&&t.min.y<=this.max.y&&t.max.z>=this.min.z&&t.min.z<=this.max.z}intersectsSphere(t){return this.clampPoint(t.center,ui),ui.distanceToSquared(t.center)<=t.radius*t.radius}intersectsPlane(t){let n,i;return t.normal.x>0?(n=t.normal.x*this.min.x,i=t.normal.x*this.max.x):(n=t.normal.x*this.max.x,i=t.normal.x*this.min.x),t.normal.y>0?(n+=t.normal.y*this.min.y,i+=t.normal.y*this.max.y):(n+=t.normal.y*this.max.y,i+=t.normal.y*this.min.y),t.normal.z>0?(n+=t.normal.z*this.min.z,i+=t.normal.z*this.max.z):(n+=t.normal.z*this.max.z,i+=t.normal.z*this.min.z),n<=-t.constant&&i>=-t.constant}intersectsTriangle(t){if(this.isEmpty())return!1;this.getCenter(xo),Jl.subVectors(this.max,xo),qs.subVectors(t.a,xo),Ws.subVectors(t.b,xo),js.subVectors(t.c,xo),ha.subVectors(Ws,qs),da.subVectors(js,Ws),ns.subVectors(qs,js);let n=[0,-ha.z,ha.y,0,-da.z,da.y,0,-ns.z,ns.y,ha.z,0,-ha.x,da.z,0,-da.x,ns.z,0,-ns.x,-ha.y,ha.x,0,-da.y,da.x,0,-ns.y,ns.x,0];return!Kf(n,qs,Ws,js,Jl)||(n=[1,0,0,0,1,0,0,0,1],!Kf(n,qs,Ws,js,Jl))?!1:($l.crossVectors(ha,da),n=[$l.x,$l.y,$l.z],Kf(n,qs,Ws,js,Jl))}clampPoint(t,n){return n.copy(t).clamp(this.min,this.max)}distanceToPoint(t){return this.clampPoint(t,ui).distanceTo(t)}getBoundingSphere(t){return this.isEmpty()?t.makeEmpty():(this.getCenter(t.center),t.radius=this.getSize(ui).length()*.5),t}intersect(t){return this.min.max(t.min),this.max.min(t.max),this.isEmpty()&&this.makeEmpty(),this}union(t){return this.min.min(t.min),this.max.max(t.max),this}applyMatrix4(t){return this.isEmpty()?this:(Hi[0].set(this.min.x,this.min.y,this.min.z).applyMatrix4(t),Hi[1].set(this.min.x,this.min.y,this.max.z).applyMatrix4(t),Hi[2].set(this.min.x,this.max.y,this.min.z).applyMatrix4(t),Hi[3].set(this.min.x,this.max.y,this.max.z).applyMatrix4(t),Hi[4].set(this.max.x,this.min.y,this.min.z).applyMatrix4(t),Hi[5].set(this.max.x,this.min.y,this.max.z).applyMatrix4(t),Hi[6].set(this.max.x,this.max.y,this.min.z).applyMatrix4(t),Hi[7].set(this.max.x,this.max.y,this.max.z).applyMatrix4(t),this.setFromPoints(Hi),this)}translate(t){return this.min.add(t),this.max.add(t),this}equals(t){return t.min.equals(this.min)&&t.max.equals(this.max)}}const Hi=[new P,new P,new P,new P,new P,new P,new P,new P],ui=new P,Ql=new Al,qs=new P,Ws=new P,js=new P,ha=new P,da=new P,ns=new P,xo=new P,Jl=new P,$l=new P,is=new P;function Kf(e,t,n,i,a){for(let s=0,r=e.length-3;s<=r;s+=3){is.fromArray(e,s);const o=a.x*Math.abs(is.x)+a.y*Math.abs(is.y)+a.z*Math.abs(is.z),l=t.dot(is),u=n.dot(is),h=i.dot(is);if(Math.max(-Math.max(l,u,h),Math.min(l,u,h))>o)return!1}return!0}const y1=new Al,Mo=new P,Qf=new P;class ef{constructor(t=new P,n=-1){this.isSphere=!0,this.center=t,this.radius=n}set(t,n){return this.center.copy(t),this.radius=n,this}setFromPoints(t,n){const i=this.center;n!==void 0?i.copy(n):y1.setFromPoints(t).getCenter(i);let a=0;for(let s=0,r=t.length;s<r;s++)a=Math.max(a,i.distanceToSquared(t[s]));return this.radius=Math.sqrt(a),this}copy(t){return this.center.copy(t.center),this.radius=t.radius,this}isEmpty(){return this.radius<0}makeEmpty(){return this.center.set(0,0,0),this.radius=-1,this}containsPoint(t){return t.distanceToSquared(this.center)<=this.radius*this.radius}distanceToPoint(t){return t.distanceTo(this.center)-this.radius}intersectsSphere(t){const n=this.radius+t.radius;return t.center.distanceToSquared(this.center)<=n*n}intersectsBox(t){return t.intersectsSphere(this)}intersectsPlane(t){return Math.abs(t.distanceToPoint(this.center))<=this.radius}clampPoint(t,n){const i=this.center.distanceToSquared(t);return n.copy(t),i>this.radius*this.radius&&(n.sub(this.center).normalize(),n.multiplyScalar(this.radius).add(this.center)),n}getBoundingBox(t){return this.isEmpty()?(t.makeEmpty(),t):(t.set(this.center,this.center),t.expandByScalar(this.radius),t)}applyMatrix4(t){return this.center.applyMatrix4(t),this.radius=this.radius*t.getMaxScaleOnAxis(),this}translate(t){return this.center.add(t),this}expandByPoint(t){if(this.isEmpty())return this.center.copy(t),this.radius=0,this;Mo.subVectors(t,this.center);const n=Mo.lengthSq();if(n>this.radius*this.radius){const i=Math.sqrt(n),a=(i-this.radius)*.5;this.center.addScaledVector(Mo,a/i),this.radius+=a}return this}union(t){return t.isEmpty()?this:this.isEmpty()?(this.copy(t),this):(this.center.equals(t.center)===!0?this.radius=Math.max(this.radius,t.radius):(Qf.subVectors(t.center,this.center).setLength(t.radius),this.expandByPoint(Mo.copy(t.center).add(Qf)),this.expandByPoint(Mo.copy(t.center).sub(Qf))),this)}equals(t){return t.center.equals(this.center)&&t.radius===this.radius}clone(){return new this.constructor().copy(this)}}const Gi=new P,Jf=new P,tu=new P,pa=new P,$f=new P,eu=new P,th=new P;class Pm{constructor(t=new P,n=new P(0,0,-1)){this.origin=t,this.direction=n}set(t,n){return this.origin.copy(t),this.direction.copy(n),this}copy(t){return this.origin.copy(t.origin),this.direction.copy(t.direction),this}at(t,n){return n.copy(this.origin).addScaledVector(this.direction,t)}lookAt(t){return this.direction.copy(t).sub(this.origin).normalize(),this}recast(t){return this.origin.copy(this.at(t,Gi)),this}closestPointToPoint(t,n){n.subVectors(t,this.origin);const i=n.dot(this.direction);return i<0?n.copy(this.origin):n.copy(this.origin).addScaledVector(this.direction,i)}distanceToPoint(t){return Math.sqrt(this.distanceSqToPoint(t))}distanceSqToPoint(t){const n=Gi.subVectors(t,this.origin).dot(this.direction);return n<0?this.origin.distanceToSquared(t):(Gi.copy(this.origin).addScaledVector(this.direction,n),Gi.distanceToSquared(t))}distanceSqToSegment(t,n,i,a){Jf.copy(t).add(n).multiplyScalar(.5),tu.copy(n).sub(t).normalize(),pa.copy(this.origin).sub(Jf);const s=t.distanceTo(n)*.5,r=-this.direction.dot(tu),o=pa.dot(this.direction),l=-pa.dot(tu),u=pa.lengthSq(),h=Math.abs(1-r*r);let p,f,d,v;if(h>0)if(p=r*l-o,f=r*o-l,v=s*h,p>=0)if(f>=-v)if(f<=v){const y=1/h;p*=y,f*=y,d=p*(p+r*f+2*o)+f*(r*p+f+2*l)+u}else f=s,p=Math.max(0,-(r*f+o)),d=-p*p+f*(f+2*l)+u;else f=-s,p=Math.max(0,-(r*f+o)),d=-p*p+f*(f+2*l)+u;else f<=-v?(p=Math.max(0,-(-r*s+o)),f=p>0?-s:Math.min(Math.max(-s,-l),s),d=-p*p+f*(f+2*l)+u):f<=v?(p=0,f=Math.min(Math.max(-s,-l),s),d=f*(f+2*l)+u):(p=Math.max(0,-(r*s+o)),f=p>0?s:Math.min(Math.max(-s,-l),s),d=-p*p+f*(f+2*l)+u);else f=r>0?-s:s,p=Math.max(0,-(r*f+o)),d=-p*p+f*(f+2*l)+u;return i&&i.copy(this.origin).addScaledVector(this.direction,p),a&&a.copy(Jf).addScaledVector(tu,f),d}intersectSphere(t,n){Gi.subVectors(t.center,this.origin);const i=Gi.dot(this.direction),a=Gi.dot(Gi)-i*i,s=t.radius*t.radius;if(a>s)return null;const r=Math.sqrt(s-a),o=i-r,l=i+r;return l<0?null:o<0?this.at(l,n):this.at(o,n)}intersectsSphere(t){return this.distanceSqToPoint(t.center)<=t.radius*t.radius}distanceToPlane(t){const n=t.normal.dot(this.direction);if(n===0)return t.distanceToPoint(this.origin)===0?0:null;const i=-(this.origin.dot(t.normal)+t.constant)/n;return i>=0?i:null}intersectPlane(t,n){const i=this.distanceToPlane(t);return i===null?null:this.at(i,n)}intersectsPlane(t){const n=t.distanceToPoint(this.origin);return n===0||t.normal.dot(this.direction)*n<0}intersectBox(t,n){let i,a,s,r,o,l;const u=1/this.direction.x,h=1/this.direction.y,p=1/this.direction.z,f=this.origin;return u>=0?(i=(t.min.x-f.x)*u,a=(t.max.x-f.x)*u):(i=(t.max.x-f.x)*u,a=(t.min.x-f.x)*u),h>=0?(s=(t.min.y-f.y)*h,r=(t.max.y-f.y)*h):(s=(t.max.y-f.y)*h,r=(t.min.y-f.y)*h),i>r||s>a||((s>i||isNaN(i))&&(i=s),(r<a||isNaN(a))&&(a=r),p>=0?(o=(t.min.z-f.z)*p,l=(t.max.z-f.z)*p):(o=(t.max.z-f.z)*p,l=(t.min.z-f.z)*p),i>l||o>a)||((o>i||i!==i)&&(i=o),(l<a||a!==a)&&(a=l),a<0)?null:this.at(i>=0?i:a,n)}intersectsBox(t){return this.intersectBox(t,Gi)!==null}intersectTriangle(t,n,i,a,s){$f.subVectors(n,t),eu.subVectors(i,t),th.crossVectors($f,eu);let r=this.direction.dot(th),o;if(r>0){if(a)return null;o=1}else if(r<0)o=-1,r=-r;else return null;pa.subVectors(this.origin,t);const l=o*this.direction.dot(eu.crossVectors(pa,eu));if(l<0)return null;const u=o*this.direction.dot($f.cross(pa));if(u<0||l+u>r)return null;const h=-o*pa.dot(th);return h<0?null:this.at(h/r,s)}applyMatrix4(t){return this.origin.applyMatrix4(t),this.direction.transformDirection(t),this}equals(t){return t.origin.equals(this.origin)&&t.direction.equals(this.direction)}clone(){return new this.constructor().copy(this)}}class Te{constructor(t,n,i,a,s,r,o,l,u,h,p,f,d,v,y,m){Te.prototype.isMatrix4=!0,this.elements=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],t!==void 0&&this.set(t,n,i,a,s,r,o,l,u,h,p,f,d,v,y,m)}set(t,n,i,a,s,r,o,l,u,h,p,f,d,v,y,m){const c=this.elements;return c[0]=t,c[4]=n,c[8]=i,c[12]=a,c[1]=s,c[5]=r,c[9]=o,c[13]=l,c[2]=u,c[6]=h,c[10]=p,c[14]=f,c[3]=d,c[7]=v,c[11]=y,c[15]=m,this}identity(){return this.set(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),this}clone(){return new Te().fromArray(this.elements)}copy(t){const n=this.elements,i=t.elements;return n[0]=i[0],n[1]=i[1],n[2]=i[2],n[3]=i[3],n[4]=i[4],n[5]=i[5],n[6]=i[6],n[7]=i[7],n[8]=i[8],n[9]=i[9],n[10]=i[10],n[11]=i[11],n[12]=i[12],n[13]=i[13],n[14]=i[14],n[15]=i[15],this}copyPosition(t){const n=this.elements,i=t.elements;return n[12]=i[12],n[13]=i[13],n[14]=i[14],this}setFromMatrix3(t){const n=t.elements;return this.set(n[0],n[3],n[6],0,n[1],n[4],n[7],0,n[2],n[5],n[8],0,0,0,0,1),this}extractBasis(t,n,i){return t.setFromMatrixColumn(this,0),n.setFromMatrixColumn(this,1),i.setFromMatrixColumn(this,2),this}makeBasis(t,n,i){return this.set(t.x,n.x,i.x,0,t.y,n.y,i.y,0,t.z,n.z,i.z,0,0,0,0,1),this}extractRotation(t){const n=this.elements,i=t.elements,a=1/Zs.setFromMatrixColumn(t,0).length(),s=1/Zs.setFromMatrixColumn(t,1).length(),r=1/Zs.setFromMatrixColumn(t,2).length();return n[0]=i[0]*a,n[1]=i[1]*a,n[2]=i[2]*a,n[3]=0,n[4]=i[4]*s,n[5]=i[5]*s,n[6]=i[6]*s,n[7]=0,n[8]=i[8]*r,n[9]=i[9]*r,n[10]=i[10]*r,n[11]=0,n[12]=0,n[13]=0,n[14]=0,n[15]=1,this}makeRotationFromEuler(t){const n=this.elements,i=t.x,a=t.y,s=t.z,r=Math.cos(i),o=Math.sin(i),l=Math.cos(a),u=Math.sin(a),h=Math.cos(s),p=Math.sin(s);if(t.order==="XYZ"){const f=r*h,d=r*p,v=o*h,y=o*p;n[0]=l*h,n[4]=-l*p,n[8]=u,n[1]=d+v*u,n[5]=f-y*u,n[9]=-o*l,n[2]=y-f*u,n[6]=v+d*u,n[10]=r*l}else if(t.order==="YXZ"){const f=l*h,d=l*p,v=u*h,y=u*p;n[0]=f+y*o,n[4]=v*o-d,n[8]=r*u,n[1]=r*p,n[5]=r*h,n[9]=-o,n[2]=d*o-v,n[6]=y+f*o,n[10]=r*l}else if(t.order==="ZXY"){const f=l*h,d=l*p,v=u*h,y=u*p;n[0]=f-y*o,n[4]=-r*p,n[8]=v+d*o,n[1]=d+v*o,n[5]=r*h,n[9]=y-f*o,n[2]=-r*u,n[6]=o,n[10]=r*l}else if(t.order==="ZYX"){const f=r*h,d=r*p,v=o*h,y=o*p;n[0]=l*h,n[4]=v*u-d,n[8]=f*u+y,n[1]=l*p,n[5]=y*u+f,n[9]=d*u-v,n[2]=-u,n[6]=o*l,n[10]=r*l}else if(t.order==="YZX"){const f=r*l,d=r*u,v=o*l,y=o*u;n[0]=l*h,n[4]=y-f*p,n[8]=v*p+d,n[1]=p,n[5]=r*h,n[9]=-o*h,n[2]=-u*h,n[6]=d*p+v,n[10]=f-y*p}else if(t.order==="XZY"){const f=r*l,d=r*u,v=o*l,y=o*u;n[0]=l*h,n[4]=-p,n[8]=u*h,n[1]=f*p+y,n[5]=r*h,n[9]=d*p-v,n[2]=v*p-d,n[6]=o*h,n[10]=y*p+f}return n[3]=0,n[7]=0,n[11]=0,n[12]=0,n[13]=0,n[14]=0,n[15]=1,this}makeRotationFromQuaternion(t){return this.compose(x1,t,M1)}lookAt(t,n,i){const a=this.elements;return Ln.subVectors(t,n),Ln.lengthSq()===0&&(Ln.z=1),Ln.normalize(),ma.crossVectors(i,Ln),ma.lengthSq()===0&&(Math.abs(i.z)===1?Ln.x+=1e-4:Ln.z+=1e-4,Ln.normalize(),ma.crossVectors(i,Ln)),ma.normalize(),nu.crossVectors(Ln,ma),a[0]=ma.x,a[4]=nu.x,a[8]=Ln.x,a[1]=ma.y,a[5]=nu.y,a[9]=Ln.y,a[2]=ma.z,a[6]=nu.z,a[10]=Ln.z,this}multiply(t){return this.multiplyMatrices(this,t)}premultiply(t){return this.multiplyMatrices(t,this)}multiplyMatrices(t,n){const i=t.elements,a=n.elements,s=this.elements,r=i[0],o=i[4],l=i[8],u=i[12],h=i[1],p=i[5],f=i[9],d=i[13],v=i[2],y=i[6],m=i[10],c=i[14],_=i[3],g=i[7],x=i[11],C=i[15],R=a[0],b=a[4],w=a[8],W=a[12],S=a[1],T=a[5],F=a[9],G=a[13],Y=a[2],K=a[6],D=a[10],V=a[14],z=a[3],tt=a[7],it=a[11],ht=a[15];return s[0]=r*R+o*S+l*Y+u*z,s[4]=r*b+o*T+l*K+u*tt,s[8]=r*w+o*F+l*D+u*it,s[12]=r*W+o*G+l*V+u*ht,s[1]=h*R+p*S+f*Y+d*z,s[5]=h*b+p*T+f*K+d*tt,s[9]=h*w+p*F+f*D+d*it,s[13]=h*W+p*G+f*V+d*ht,s[2]=v*R+y*S+m*Y+c*z,s[6]=v*b+y*T+m*K+c*tt,s[10]=v*w+y*F+m*D+c*it,s[14]=v*W+y*G+m*V+c*ht,s[3]=_*R+g*S+x*Y+C*z,s[7]=_*b+g*T+x*K+C*tt,s[11]=_*w+g*F+x*D+C*it,s[15]=_*W+g*G+x*V+C*ht,this}multiplyScalar(t){const n=this.elements;return n[0]*=t,n[4]*=t,n[8]*=t,n[12]*=t,n[1]*=t,n[5]*=t,n[9]*=t,n[13]*=t,n[2]*=t,n[6]*=t,n[10]*=t,n[14]*=t,n[3]*=t,n[7]*=t,n[11]*=t,n[15]*=t,this}determinant(){const t=this.elements,n=t[0],i=t[4],a=t[8],s=t[12],r=t[1],o=t[5],l=t[9],u=t[13],h=t[2],p=t[6],f=t[10],d=t[14],v=t[3],y=t[7],m=t[11],c=t[15];return v*(+s*l*p-a*u*p-s*o*f+i*u*f+a*o*d-i*l*d)+y*(+n*l*d-n*u*f+s*r*f-a*r*d+a*u*h-s*l*h)+m*(+n*u*p-n*o*d-s*r*p+i*r*d+s*o*h-i*u*h)+c*(-a*o*h-n*l*p+n*o*f+a*r*p-i*r*f+i*l*h)}transpose(){const t=this.elements;let n;return n=t[1],t[1]=t[4],t[4]=n,n=t[2],t[2]=t[8],t[8]=n,n=t[6],t[6]=t[9],t[9]=n,n=t[3],t[3]=t[12],t[12]=n,n=t[7],t[7]=t[13],t[13]=n,n=t[11],t[11]=t[14],t[14]=n,this}setPosition(t,n,i){const a=this.elements;return t.isVector3?(a[12]=t.x,a[13]=t.y,a[14]=t.z):(a[12]=t,a[13]=n,a[14]=i),this}invert(){const t=this.elements,n=t[0],i=t[1],a=t[2],s=t[3],r=t[4],o=t[5],l=t[6],u=t[7],h=t[8],p=t[9],f=t[10],d=t[11],v=t[12],y=t[13],m=t[14],c=t[15],_=p*m*u-y*f*u+y*l*d-o*m*d-p*l*c+o*f*c,g=v*f*u-h*m*u-v*l*d+r*m*d+h*l*c-r*f*c,x=h*y*u-v*p*u+v*o*d-r*y*d-h*o*c+r*p*c,C=v*p*l-h*y*l-v*o*f+r*y*f+h*o*m-r*p*m,R=n*_+i*g+a*x+s*C;if(R===0)return this.set(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);const b=1/R;return t[0]=_*b,t[1]=(y*f*s-p*m*s-y*a*d+i*m*d+p*a*c-i*f*c)*b,t[2]=(o*m*s-y*l*s+y*a*u-i*m*u-o*a*c+i*l*c)*b,t[3]=(p*l*s-o*f*s-p*a*u+i*f*u+o*a*d-i*l*d)*b,t[4]=g*b,t[5]=(h*m*s-v*f*s+v*a*d-n*m*d-h*a*c+n*f*c)*b,t[6]=(v*l*s-r*m*s-v*a*u+n*m*u+r*a*c-n*l*c)*b,t[7]=(r*f*s-h*l*s+h*a*u-n*f*u-r*a*d+n*l*d)*b,t[8]=x*b,t[9]=(v*p*s-h*y*s-v*i*d+n*y*d+h*i*c-n*p*c)*b,t[10]=(r*y*s-v*o*s+v*i*u-n*y*u-r*i*c+n*o*c)*b,t[11]=(h*o*s-r*p*s-h*i*u+n*p*u+r*i*d-n*o*d)*b,t[12]=C*b,t[13]=(h*y*a-v*p*a+v*i*f-n*y*f-h*i*m+n*p*m)*b,t[14]=(v*o*a-r*y*a-v*i*l+n*y*l+r*i*m-n*o*m)*b,t[15]=(r*p*a-h*o*a+h*i*l-n*p*l-r*i*f+n*o*f)*b,this}scale(t){const n=this.elements,i=t.x,a=t.y,s=t.z;return n[0]*=i,n[4]*=a,n[8]*=s,n[1]*=i,n[5]*=a,n[9]*=s,n[2]*=i,n[6]*=a,n[10]*=s,n[3]*=i,n[7]*=a,n[11]*=s,this}getMaxScaleOnAxis(){const t=this.elements,n=t[0]*t[0]+t[1]*t[1]+t[2]*t[2],i=t[4]*t[4]+t[5]*t[5]+t[6]*t[6],a=t[8]*t[8]+t[9]*t[9]+t[10]*t[10];return Math.sqrt(Math.max(n,i,a))}makeTranslation(t,n,i){return t.isVector3?this.set(1,0,0,t.x,0,1,0,t.y,0,0,1,t.z,0,0,0,1):this.set(1,0,0,t,0,1,0,n,0,0,1,i,0,0,0,1),this}makeRotationX(t){const n=Math.cos(t),i=Math.sin(t);return this.set(1,0,0,0,0,n,-i,0,0,i,n,0,0,0,0,1),this}makeRotationY(t){const n=Math.cos(t),i=Math.sin(t);return this.set(n,0,i,0,0,1,0,0,-i,0,n,0,0,0,0,1),this}makeRotationZ(t){const n=Math.cos(t),i=Math.sin(t);return this.set(n,-i,0,0,i,n,0,0,0,0,1,0,0,0,0,1),this}makeRotationAxis(t,n){const i=Math.cos(n),a=Math.sin(n),s=1-i,r=t.x,o=t.y,l=t.z,u=s*r,h=s*o;return this.set(u*r+i,u*o-a*l,u*l+a*o,0,u*o+a*l,h*o+i,h*l-a*r,0,u*l-a*o,h*l+a*r,s*l*l+i,0,0,0,0,1),this}makeScale(t,n,i){return this.set(t,0,0,0,0,n,0,0,0,0,i,0,0,0,0,1),this}makeShear(t,n,i,a,s,r){return this.set(1,i,s,0,t,1,r,0,n,a,1,0,0,0,0,1),this}compose(t,n,i){const a=this.elements,s=n._x,r=n._y,o=n._z,l=n._w,u=s+s,h=r+r,p=o+o,f=s*u,d=s*h,v=s*p,y=r*h,m=r*p,c=o*p,_=l*u,g=l*h,x=l*p,C=i.x,R=i.y,b=i.z;return a[0]=(1-(y+c))*C,a[1]=(d+x)*C,a[2]=(v-g)*C,a[3]=0,a[4]=(d-x)*R,a[5]=(1-(f+c))*R,a[6]=(m+_)*R,a[7]=0,a[8]=(v+g)*b,a[9]=(m-_)*b,a[10]=(1-(f+y))*b,a[11]=0,a[12]=t.x,a[13]=t.y,a[14]=t.z,a[15]=1,this}decompose(t,n,i){const a=this.elements;let s=Zs.set(a[0],a[1],a[2]).length();const r=Zs.set(a[4],a[5],a[6]).length(),o=Zs.set(a[8],a[9],a[10]).length();this.determinant()<0&&(s=-s),t.x=a[12],t.y=a[13],t.z=a[14],ci.copy(this);const u=1/s,h=1/r,p=1/o;return ci.elements[0]*=u,ci.elements[1]*=u,ci.elements[2]*=u,ci.elements[4]*=h,ci.elements[5]*=h,ci.elements[6]*=h,ci.elements[8]*=p,ci.elements[9]*=p,ci.elements[10]*=p,n.setFromRotationMatrix(ci),i.x=s,i.y=r,i.z=o,this}makePerspective(t,n,i,a,s,r,o=Zi){const l=this.elements,u=2*s/(n-t),h=2*s/(i-a),p=(n+t)/(n-t),f=(i+a)/(i-a);let d,v;if(o===Zi)d=-(r+s)/(r-s),v=-2*r*s/(r-s);else if(o===Rc)d=-r/(r-s),v=-r*s/(r-s);else throw new Error("THREE.Matrix4.makePerspective(): Invalid coordinate system: "+o);return l[0]=u,l[4]=0,l[8]=p,l[12]=0,l[1]=0,l[5]=h,l[9]=f,l[13]=0,l[2]=0,l[6]=0,l[10]=d,l[14]=v,l[3]=0,l[7]=0,l[11]=-1,l[15]=0,this}makeOrthographic(t,n,i,a,s,r,o=Zi){const l=this.elements,u=1/(n-t),h=1/(i-a),p=1/(r-s),f=(n+t)*u,d=(i+a)*h;let v,y;if(o===Zi)v=(r+s)*p,y=-2*p;else if(o===Rc)v=s*p,y=-1*p;else throw new Error("THREE.Matrix4.makeOrthographic(): Invalid coordinate system: "+o);return l[0]=2*u,l[4]=0,l[8]=0,l[12]=-f,l[1]=0,l[5]=2*h,l[9]=0,l[13]=-d,l[2]=0,l[6]=0,l[10]=y,l[14]=-v,l[3]=0,l[7]=0,l[11]=0,l[15]=1,this}equals(t){const n=this.elements,i=t.elements;for(let a=0;a<16;a++)if(n[a]!==i[a])return!1;return!0}fromArray(t,n=0){for(let i=0;i<16;i++)this.elements[i]=t[i+n];return this}toArray(t=[],n=0){const i=this.elements;return t[n]=i[0],t[n+1]=i[1],t[n+2]=i[2],t[n+3]=i[3],t[n+4]=i[4],t[n+5]=i[5],t[n+6]=i[6],t[n+7]=i[7],t[n+8]=i[8],t[n+9]=i[9],t[n+10]=i[10],t[n+11]=i[11],t[n+12]=i[12],t[n+13]=i[13],t[n+14]=i[14],t[n+15]=i[15],t}}const Zs=new P,ci=new Te,x1=new P(0,0,0),M1=new P(1,1,1),ma=new P,nu=new P,Ln=new P,Zg=new Te,Kg=new Ls;class sa{constructor(t=0,n=0,i=0,a=sa.DEFAULT_ORDER){this.isEuler=!0,this._x=t,this._y=n,this._z=i,this._order=a}get x(){return this._x}set x(t){this._x=t,this._onChangeCallback()}get y(){return this._y}set y(t){this._y=t,this._onChangeCallback()}get z(){return this._z}set z(t){this._z=t,this._onChangeCallback()}get order(){return this._order}set order(t){this._order=t,this._onChangeCallback()}set(t,n,i,a=this._order){return this._x=t,this._y=n,this._z=i,this._order=a,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._order)}copy(t){return this._x=t._x,this._y=t._y,this._z=t._z,this._order=t._order,this._onChangeCallback(),this}setFromRotationMatrix(t,n=this._order,i=!0){const a=t.elements,s=a[0],r=a[4],o=a[8],l=a[1],u=a[5],h=a[9],p=a[2],f=a[6],d=a[10];switch(n){case"XYZ":this._y=Math.asin(hn(o,-1,1)),Math.abs(o)<.9999999?(this._x=Math.atan2(-h,d),this._z=Math.atan2(-r,s)):(this._x=Math.atan2(f,u),this._z=0);break;case"YXZ":this._x=Math.asin(-hn(h,-1,1)),Math.abs(h)<.9999999?(this._y=Math.atan2(o,d),this._z=Math.atan2(l,u)):(this._y=Math.atan2(-p,s),this._z=0);break;case"ZXY":this._x=Math.asin(hn(f,-1,1)),Math.abs(f)<.9999999?(this._y=Math.atan2(-p,d),this._z=Math.atan2(-r,u)):(this._y=0,this._z=Math.atan2(l,s));break;case"ZYX":this._y=Math.asin(-hn(p,-1,1)),Math.abs(p)<.9999999?(this._x=Math.atan2(f,d),this._z=Math.atan2(l,s)):(this._x=0,this._z=Math.atan2(-r,u));break;case"YZX":this._z=Math.asin(hn(l,-1,1)),Math.abs(l)<.9999999?(this._x=Math.atan2(-h,u),this._y=Math.atan2(-p,s)):(this._x=0,this._y=Math.atan2(o,d));break;case"XZY":this._z=Math.asin(-hn(r,-1,1)),Math.abs(r)<.9999999?(this._x=Math.atan2(f,u),this._y=Math.atan2(o,s)):(this._x=Math.atan2(-h,d),this._y=0);break;default:console.warn("THREE.Euler: .setFromRotationMatrix() encountered an unknown order: "+n)}return this._order=n,i===!0&&this._onChangeCallback(),this}setFromQuaternion(t,n,i){return Zg.makeRotationFromQuaternion(t),this.setFromRotationMatrix(Zg,n,i)}setFromVector3(t,n=this._order){return this.set(t.x,t.y,t.z,n)}reorder(t){return Kg.setFromEuler(this),this.setFromQuaternion(Kg,t)}equals(t){return t._x===this._x&&t._y===this._y&&t._z===this._z&&t._order===this._order}fromArray(t){return this._x=t[0],this._y=t[1],this._z=t[2],t[3]!==void 0&&(this._order=t[3]),this._onChangeCallback(),this}toArray(t=[],n=0){return t[n]=this._x,t[n+1]=this._y,t[n+2]=this._z,t[n+3]=this._order,t}_onChange(t){return this._onChangeCallback=t,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._order}}sa.DEFAULT_ORDER="XYZ";class Mx{constructor(){this.mask=1}set(t){this.mask=(1<<t|0)>>>0}enable(t){this.mask|=1<<t|0}enableAll(){this.mask=-1}toggle(t){this.mask^=1<<t|0}disable(t){this.mask&=~(1<<t|0)}disableAll(){this.mask=0}test(t){return(this.mask&t.mask)!==0}isEnabled(t){return(this.mask&(1<<t|0))!==0}}let E1=0;const Qg=new P,Ks=new Ls,Vi=new Te,iu=new P,Eo=new P,T1=new P,b1=new Ls,Jg=new P(1,0,0),$g=new P(0,1,0),t0=new P(0,0,1),e0={type:"added"},A1={type:"removed"},Qs={type:"childadded",child:null},eh={type:"childremoved",child:null};class en extends Hs{constructor(){super(),this.isObject3D=!0,Object.defineProperty(this,"id",{value:E1++}),this.uuid=bl(),this.name="",this.type="Object3D",this.parent=null,this.children=[],this.up=en.DEFAULT_UP.clone();const t=new P,n=new sa,i=new Ls,a=new P(1,1,1);function s(){i.setFromEuler(n,!1)}function r(){n.setFromQuaternion(i,void 0,!1)}n._onChange(s),i._onChange(r),Object.defineProperties(this,{position:{configurable:!0,enumerable:!0,value:t},rotation:{configurable:!0,enumerable:!0,value:n},quaternion:{configurable:!0,enumerable:!0,value:i},scale:{configurable:!0,enumerable:!0,value:a},modelViewMatrix:{value:new Te},normalMatrix:{value:new Pt}}),this.matrix=new Te,this.matrixWorld=new Te,this.matrixAutoUpdate=en.DEFAULT_MATRIX_AUTO_UPDATE,this.matrixWorldAutoUpdate=en.DEFAULT_MATRIX_WORLD_AUTO_UPDATE,this.matrixWorldNeedsUpdate=!1,this.layers=new Mx,this.visible=!0,this.castShadow=!1,this.receiveShadow=!1,this.frustumCulled=!0,this.renderOrder=0,this.animations=[],this.userData={}}onBeforeShadow(){}onAfterShadow(){}onBeforeRender(){}onAfterRender(){}applyMatrix4(t){this.matrixAutoUpdate&&this.updateMatrix(),this.matrix.premultiply(t),this.matrix.decompose(this.position,this.quaternion,this.scale)}applyQuaternion(t){return this.quaternion.premultiply(t),this}setRotationFromAxisAngle(t,n){this.quaternion.setFromAxisAngle(t,n)}setRotationFromEuler(t){this.quaternion.setFromEuler(t,!0)}setRotationFromMatrix(t){this.quaternion.setFromRotationMatrix(t)}setRotationFromQuaternion(t){this.quaternion.copy(t)}rotateOnAxis(t,n){return Ks.setFromAxisAngle(t,n),this.quaternion.multiply(Ks),this}rotateOnWorldAxis(t,n){return Ks.setFromAxisAngle(t,n),this.quaternion.premultiply(Ks),this}rotateX(t){return this.rotateOnAxis(Jg,t)}rotateY(t){return this.rotateOnAxis($g,t)}rotateZ(t){return this.rotateOnAxis(t0,t)}translateOnAxis(t,n){return Qg.copy(t).applyQuaternion(this.quaternion),this.position.add(Qg.multiplyScalar(n)),this}translateX(t){return this.translateOnAxis(Jg,t)}translateY(t){return this.translateOnAxis($g,t)}translateZ(t){return this.translateOnAxis(t0,t)}localToWorld(t){return this.updateWorldMatrix(!0,!1),t.applyMatrix4(this.matrixWorld)}worldToLocal(t){return this.updateWorldMatrix(!0,!1),t.applyMatrix4(Vi.copy(this.matrixWorld).invert())}lookAt(t,n,i){t.isVector3?iu.copy(t):iu.set(t,n,i);const a=this.parent;this.updateWorldMatrix(!0,!1),Eo.setFromMatrixPosition(this.matrixWorld),this.isCamera||this.isLight?Vi.lookAt(Eo,iu,this.up):Vi.lookAt(iu,Eo,this.up),this.quaternion.setFromRotationMatrix(Vi),a&&(Vi.extractRotation(a.matrixWorld),Ks.setFromRotationMatrix(Vi),this.quaternion.premultiply(Ks.invert()))}add(t){if(arguments.length>1){for(let n=0;n<arguments.length;n++)this.add(arguments[n]);return this}return t===this?(console.error("THREE.Object3D.add: object can't be added as a child of itself.",t),this):(t&&t.isObject3D?(t.removeFromParent(),t.parent=this,this.children.push(t),t.dispatchEvent(e0),Qs.child=t,this.dispatchEvent(Qs),Qs.child=null):console.error("THREE.Object3D.add: object not an instance of THREE.Object3D.",t),this)}remove(t){if(arguments.length>1){for(let i=0;i<arguments.length;i++)this.remove(arguments[i]);return this}const n=this.children.indexOf(t);return n!==-1&&(t.parent=null,this.children.splice(n,1),t.dispatchEvent(A1),eh.child=t,this.dispatchEvent(eh),eh.child=null),this}removeFromParent(){const t=this.parent;return t!==null&&t.remove(this),this}clear(){return this.remove(...this.children)}attach(t){return this.updateWorldMatrix(!0,!1),Vi.copy(this.matrixWorld).invert(),t.parent!==null&&(t.parent.updateWorldMatrix(!0,!1),Vi.multiply(t.parent.matrixWorld)),t.applyMatrix4(Vi),t.removeFromParent(),t.parent=this,this.children.push(t),t.updateWorldMatrix(!1,!0),t.dispatchEvent(e0),Qs.child=t,this.dispatchEvent(Qs),Qs.child=null,this}getObjectById(t){return this.getObjectByProperty("id",t)}getObjectByName(t){return this.getObjectByProperty("name",t)}getObjectByProperty(t,n){if(this[t]===n)return this;for(let i=0,a=this.children.length;i<a;i++){const r=this.children[i].getObjectByProperty(t,n);if(r!==void 0)return r}}getObjectsByProperty(t,n,i=[]){this[t]===n&&i.push(this);const a=this.children;for(let s=0,r=a.length;s<r;s++)a[s].getObjectsByProperty(t,n,i);return i}getWorldPosition(t){return this.updateWorldMatrix(!0,!1),t.setFromMatrixPosition(this.matrixWorld)}getWorldQuaternion(t){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(Eo,t,T1),t}getWorldScale(t){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(Eo,b1,t),t}getWorldDirection(t){this.updateWorldMatrix(!0,!1);const n=this.matrixWorld.elements;return t.set(n[8],n[9],n[10]).normalize()}raycast(){}traverse(t){t(this);const n=this.children;for(let i=0,a=n.length;i<a;i++)n[i].traverse(t)}traverseVisible(t){if(this.visible===!1)return;t(this);const n=this.children;for(let i=0,a=n.length;i<a;i++)n[i].traverseVisible(t)}traverseAncestors(t){const n=this.parent;n!==null&&(t(n),n.traverseAncestors(t))}updateMatrix(){this.matrix.compose(this.position,this.quaternion,this.scale),this.matrixWorldNeedsUpdate=!0}updateMatrixWorld(t){this.matrixAutoUpdate&&this.updateMatrix(),(this.matrixWorldNeedsUpdate||t)&&(this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),this.matrixWorldNeedsUpdate=!1,t=!0);const n=this.children;for(let i=0,a=n.length;i<a;i++)n[i].updateMatrixWorld(t)}updateWorldMatrix(t,n){const i=this.parent;if(t===!0&&i!==null&&i.updateWorldMatrix(!0,!1),this.matrixAutoUpdate&&this.updateMatrix(),this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),n===!0){const a=this.children;for(let s=0,r=a.length;s<r;s++)a[s].updateWorldMatrix(!1,!0)}}toJSON(t){const n=t===void 0||typeof t=="string",i={};n&&(t={geometries:{},materials:{},textures:{},images:{},shapes:{},skeletons:{},animations:{},nodes:{}},i.metadata={version:4.6,type:"Object",generator:"Object3D.toJSON"});const a={};a.uuid=this.uuid,a.type=this.type,this.name!==""&&(a.name=this.name),this.castShadow===!0&&(a.castShadow=!0),this.receiveShadow===!0&&(a.receiveShadow=!0),this.visible===!1&&(a.visible=!1),this.frustumCulled===!1&&(a.frustumCulled=!1),this.renderOrder!==0&&(a.renderOrder=this.renderOrder),Object.keys(this.userData).length>0&&(a.userData=this.userData),a.layers=this.layers.mask,a.matrix=this.matrix.toArray(),a.up=this.up.toArray(),this.matrixAutoUpdate===!1&&(a.matrixAutoUpdate=!1),this.isInstancedMesh&&(a.type="InstancedMesh",a.count=this.count,a.instanceMatrix=this.instanceMatrix.toJSON(),this.instanceColor!==null&&(a.instanceColor=this.instanceColor.toJSON())),this.isBatchedMesh&&(a.type="BatchedMesh",a.perObjectFrustumCulled=this.perObjectFrustumCulled,a.sortObjects=this.sortObjects,a.drawRanges=this._drawRanges,a.reservedRanges=this._reservedRanges,a.visibility=this._visibility,a.active=this._active,a.bounds=this._bounds.map(o=>({boxInitialized:o.boxInitialized,boxMin:o.box.min.toArray(),boxMax:o.box.max.toArray(),sphereInitialized:o.sphereInitialized,sphereRadius:o.sphere.radius,sphereCenter:o.sphere.center.toArray()})),a.maxInstanceCount=this._maxInstanceCount,a.maxVertexCount=this._maxVertexCount,a.maxIndexCount=this._maxIndexCount,a.geometryInitialized=this._geometryInitialized,a.geometryCount=this._geometryCount,a.matricesTexture=this._matricesTexture.toJSON(t),this._colorsTexture!==null&&(a.colorsTexture=this._colorsTexture.toJSON(t)),this.boundingSphere!==null&&(a.boundingSphere={center:a.boundingSphere.center.toArray(),radius:a.boundingSphere.radius}),this.boundingBox!==null&&(a.boundingBox={min:a.boundingBox.min.toArray(),max:a.boundingBox.max.toArray()}));function s(o,l){return o[l.uuid]===void 0&&(o[l.uuid]=l.toJSON(t)),l.uuid}if(this.isScene)this.background&&(this.background.isColor?a.background=this.background.toJSON():this.background.isTexture&&(a.background=this.background.toJSON(t).uuid)),this.environment&&this.environment.isTexture&&this.environment.isRenderTargetTexture!==!0&&(a.environment=this.environment.toJSON(t).uuid);else if(this.isMesh||this.isLine||this.isPoints){a.geometry=s(t.geometries,this.geometry);const o=this.geometry.parameters;if(o!==void 0&&o.shapes!==void 0){const l=o.shapes;if(Array.isArray(l))for(let u=0,h=l.length;u<h;u++){const p=l[u];s(t.shapes,p)}else s(t.shapes,l)}}if(this.isSkinnedMesh&&(a.bindMode=this.bindMode,a.bindMatrix=this.bindMatrix.toArray(),this.skeleton!==void 0&&(s(t.skeletons,this.skeleton),a.skeleton=this.skeleton.uuid)),this.material!==void 0)if(Array.isArray(this.material)){const o=[];for(let l=0,u=this.material.length;l<u;l++)o.push(s(t.materials,this.material[l]));a.material=o}else a.material=s(t.materials,this.material);if(this.children.length>0){a.children=[];for(let o=0;o<this.children.length;o++)a.children.push(this.children[o].toJSON(t).object)}if(this.animations.length>0){a.animations=[];for(let o=0;o<this.animations.length;o++){const l=this.animations[o];a.animations.push(s(t.animations,l))}}if(n){const o=r(t.geometries),l=r(t.materials),u=r(t.textures),h=r(t.images),p=r(t.shapes),f=r(t.skeletons),d=r(t.animations),v=r(t.nodes);o.length>0&&(i.geometries=o),l.length>0&&(i.materials=l),u.length>0&&(i.textures=u),h.length>0&&(i.images=h),p.length>0&&(i.shapes=p),f.length>0&&(i.skeletons=f),d.length>0&&(i.animations=d),v.length>0&&(i.nodes=v)}return i.object=a,i;function r(o){const l=[];for(const u in o){const h=o[u];delete h.metadata,l.push(h)}return l}}clone(t){return new this.constructor().copy(this,t)}copy(t,n=!0){if(this.name=t.name,this.up.copy(t.up),this.position.copy(t.position),this.rotation.order=t.rotation.order,this.quaternion.copy(t.quaternion),this.scale.copy(t.scale),this.matrix.copy(t.matrix),this.matrixWorld.copy(t.matrixWorld),this.matrixAutoUpdate=t.matrixAutoUpdate,this.matrixWorldAutoUpdate=t.matrixWorldAutoUpdate,this.matrixWorldNeedsUpdate=t.matrixWorldNeedsUpdate,this.layers.mask=t.layers.mask,this.visible=t.visible,this.castShadow=t.castShadow,this.receiveShadow=t.receiveShadow,this.frustumCulled=t.frustumCulled,this.renderOrder=t.renderOrder,this.animations=t.animations.slice(),this.userData=JSON.parse(JSON.stringify(t.userData)),n===!0)for(let i=0;i<t.children.length;i++){const a=t.children[i];this.add(a.clone())}return this}}en.DEFAULT_UP=new P(0,1,0);en.DEFAULT_MATRIX_AUTO_UPDATE=!0;en.DEFAULT_MATRIX_WORLD_AUTO_UPDATE=!0;const fi=new P,Xi=new P,nh=new P,ki=new P,Js=new P,$s=new P,n0=new P,ih=new P,ah=new P,sh=new P,rh=new Ce,oh=new Ce,lh=new Ce;class _i{constructor(t=new P,n=new P,i=new P){this.a=t,this.b=n,this.c=i}static getNormal(t,n,i,a){a.subVectors(i,n),fi.subVectors(t,n),a.cross(fi);const s=a.lengthSq();return s>0?a.multiplyScalar(1/Math.sqrt(s)):a.set(0,0,0)}static getBarycoord(t,n,i,a,s){fi.subVectors(a,n),Xi.subVectors(i,n),nh.subVectors(t,n);const r=fi.dot(fi),o=fi.dot(Xi),l=fi.dot(nh),u=Xi.dot(Xi),h=Xi.dot(nh),p=r*u-o*o;if(p===0)return s.set(0,0,0),null;const f=1/p,d=(u*l-o*h)*f,v=(r*h-o*l)*f;return s.set(1-d-v,v,d)}static containsPoint(t,n,i,a){return this.getBarycoord(t,n,i,a,ki)===null?!1:ki.x>=0&&ki.y>=0&&ki.x+ki.y<=1}static getInterpolation(t,n,i,a,s,r,o,l){return this.getBarycoord(t,n,i,a,ki)===null?(l.x=0,l.y=0,"z"in l&&(l.z=0),"w"in l&&(l.w=0),null):(l.setScalar(0),l.addScaledVector(s,ki.x),l.addScaledVector(r,ki.y),l.addScaledVector(o,ki.z),l)}static getInterpolatedAttribute(t,n,i,a,s,r){return rh.setScalar(0),oh.setScalar(0),lh.setScalar(0),rh.fromBufferAttribute(t,n),oh.fromBufferAttribute(t,i),lh.fromBufferAttribute(t,a),r.setScalar(0),r.addScaledVector(rh,s.x),r.addScaledVector(oh,s.y),r.addScaledVector(lh,s.z),r}static isFrontFacing(t,n,i,a){return fi.subVectors(i,n),Xi.subVectors(t,n),fi.cross(Xi).dot(a)<0}set(t,n,i){return this.a.copy(t),this.b.copy(n),this.c.copy(i),this}setFromPointsAndIndices(t,n,i,a){return this.a.copy(t[n]),this.b.copy(t[i]),this.c.copy(t[a]),this}setFromAttributeAndIndices(t,n,i,a){return this.a.fromBufferAttribute(t,n),this.b.fromBufferAttribute(t,i),this.c.fromBufferAttribute(t,a),this}clone(){return new this.constructor().copy(this)}copy(t){return this.a.copy(t.a),this.b.copy(t.b),this.c.copy(t.c),this}getArea(){return fi.subVectors(this.c,this.b),Xi.subVectors(this.a,this.b),fi.cross(Xi).length()*.5}getMidpoint(t){return t.addVectors(this.a,this.b).add(this.c).multiplyScalar(1/3)}getNormal(t){return _i.getNormal(this.a,this.b,this.c,t)}getPlane(t){return t.setFromCoplanarPoints(this.a,this.b,this.c)}getBarycoord(t,n){return _i.getBarycoord(t,this.a,this.b,this.c,n)}getInterpolation(t,n,i,a,s){return _i.getInterpolation(t,this.a,this.b,this.c,n,i,a,s)}containsPoint(t){return _i.containsPoint(t,this.a,this.b,this.c)}isFrontFacing(t){return _i.isFrontFacing(this.a,this.b,this.c,t)}intersectsBox(t){return t.intersectsTriangle(this)}closestPointToPoint(t,n){const i=this.a,a=this.b,s=this.c;let r,o;Js.subVectors(a,i),$s.subVectors(s,i),ih.subVectors(t,i);const l=Js.dot(ih),u=$s.dot(ih);if(l<=0&&u<=0)return n.copy(i);ah.subVectors(t,a);const h=Js.dot(ah),p=$s.dot(ah);if(h>=0&&p<=h)return n.copy(a);const f=l*p-h*u;if(f<=0&&l>=0&&h<=0)return r=l/(l-h),n.copy(i).addScaledVector(Js,r);sh.subVectors(t,s);const d=Js.dot(sh),v=$s.dot(sh);if(v>=0&&d<=v)return n.copy(s);const y=d*u-l*v;if(y<=0&&u>=0&&v<=0)return o=u/(u-v),n.copy(i).addScaledVector($s,o);const m=h*v-d*p;if(m<=0&&p-h>=0&&d-v>=0)return n0.subVectors(s,a),o=(p-h)/(p-h+(d-v)),n.copy(a).addScaledVector(n0,o);const c=1/(m+y+f);return r=y*c,o=f*c,n.copy(i).addScaledVector(Js,r).addScaledVector($s,o)}equals(t){return t.a.equals(this.a)&&t.b.equals(this.b)&&t.c.equals(this.c)}}const Ex={aliceblue:15792383,antiquewhite:16444375,aqua:65535,aquamarine:8388564,azure:15794175,beige:16119260,bisque:16770244,black:0,blanchedalmond:16772045,blue:255,blueviolet:9055202,brown:10824234,burlywood:14596231,cadetblue:6266528,chartreuse:8388352,chocolate:13789470,coral:16744272,cornflowerblue:6591981,cornsilk:16775388,crimson:14423100,cyan:65535,darkblue:139,darkcyan:35723,darkgoldenrod:12092939,darkgray:11119017,darkgreen:25600,darkgrey:11119017,darkkhaki:12433259,darkmagenta:9109643,darkolivegreen:5597999,darkorange:16747520,darkorchid:10040012,darkred:9109504,darksalmon:15308410,darkseagreen:9419919,darkslateblue:4734347,darkslategray:3100495,darkslategrey:3100495,darkturquoise:52945,darkviolet:9699539,deeppink:16716947,deepskyblue:49151,dimgray:6908265,dimgrey:6908265,dodgerblue:2003199,firebrick:11674146,floralwhite:16775920,forestgreen:2263842,fuchsia:16711935,gainsboro:14474460,ghostwhite:16316671,gold:16766720,goldenrod:14329120,gray:8421504,green:32768,greenyellow:11403055,grey:8421504,honeydew:15794160,hotpink:16738740,indianred:13458524,indigo:4915330,ivory:16777200,khaki:15787660,lavender:15132410,lavenderblush:16773365,lawngreen:8190976,lemonchiffon:16775885,lightblue:11393254,lightcoral:15761536,lightcyan:14745599,lightgoldenrodyellow:16448210,lightgray:13882323,lightgreen:9498256,lightgrey:13882323,lightpink:16758465,lightsalmon:16752762,lightseagreen:2142890,lightskyblue:8900346,lightslategray:7833753,lightslategrey:7833753,lightsteelblue:11584734,lightyellow:16777184,lime:65280,limegreen:3329330,linen:16445670,magenta:16711935,maroon:8388608,mediumaquamarine:6737322,mediumblue:205,mediumorchid:12211667,mediumpurple:9662683,mediumseagreen:3978097,mediumslateblue:8087790,mediumspringgreen:64154,mediumturquoise:4772300,mediumvioletred:13047173,midnightblue:1644912,mintcream:16121850,mistyrose:16770273,moccasin:16770229,navajowhite:16768685,navy:128,oldlace:16643558,olive:8421376,olivedrab:7048739,orange:16753920,orangered:16729344,orchid:14315734,palegoldenrod:15657130,palegreen:10025880,paleturquoise:11529966,palevioletred:14381203,papayawhip:16773077,peachpuff:16767673,peru:13468991,pink:16761035,plum:14524637,powderblue:11591910,purple:8388736,rebeccapurple:6697881,red:16711680,rosybrown:12357519,royalblue:4286945,saddlebrown:9127187,salmon:16416882,sandybrown:16032864,seagreen:3050327,seashell:16774638,sienna:10506797,silver:12632256,skyblue:8900331,slateblue:6970061,slategray:7372944,slategrey:7372944,snow:16775930,springgreen:65407,steelblue:4620980,tan:13808780,teal:32896,thistle:14204888,tomato:16737095,turquoise:4251856,violet:15631086,wheat:16113331,white:16777215,whitesmoke:16119285,yellow:16776960,yellowgreen:10145074},_a={h:0,s:0,l:0},au={h:0,s:0,l:0};function uh(e,t,n){return n<0&&(n+=1),n>1&&(n-=1),n<1/6?e+(t-e)*6*n:n<1/2?t:n<2/3?e+(t-e)*6*(2/3-n):e}class Ht{constructor(t,n,i){return this.isColor=!0,this.r=1,this.g=1,this.b=1,this.set(t,n,i)}set(t,n,i){if(n===void 0&&i===void 0){const a=t;a&&a.isColor?this.copy(a):typeof a=="number"?this.setHex(a):typeof a=="string"&&this.setStyle(a)}else this.setRGB(t,n,i);return this}setScalar(t){return this.r=t,this.g=t,this.b=t,this}setHex(t,n=Ti){return t=Math.floor(t),this.r=(t>>16&255)/255,this.g=(t>>8&255)/255,this.b=(t&255)/255,ae.toWorkingColorSpace(this,n),this}setRGB(t,n,i,a=ae.workingColorSpace){return this.r=t,this.g=n,this.b=i,ae.toWorkingColorSpace(this,a),this}setHSL(t,n,i,a=ae.workingColorSpace){if(t=l1(t,1),n=hn(n,0,1),i=hn(i,0,1),n===0)this.r=this.g=this.b=i;else{const s=i<=.5?i*(1+n):i+n-i*n,r=2*i-s;this.r=uh(r,s,t+1/3),this.g=uh(r,s,t),this.b=uh(r,s,t-1/3)}return ae.toWorkingColorSpace(this,a),this}setStyle(t,n=Ti){function i(s){s!==void 0&&parseFloat(s)<1&&console.warn("THREE.Color: Alpha component of "+t+" will be ignored.")}let a;if(a=/^(\w+)\(([^\)]*)\)/.exec(t)){let s;const r=a[1],o=a[2];switch(r){case"rgb":case"rgba":if(s=/^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return i(s[4]),this.setRGB(Math.min(255,parseInt(s[1],10))/255,Math.min(255,parseInt(s[2],10))/255,Math.min(255,parseInt(s[3],10))/255,n);if(s=/^\s*(\d+)\%\s*,\s*(\d+)\%\s*,\s*(\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return i(s[4]),this.setRGB(Math.min(100,parseInt(s[1],10))/100,Math.min(100,parseInt(s[2],10))/100,Math.min(100,parseInt(s[3],10))/100,n);break;case"hsl":case"hsla":if(s=/^\s*(\d*\.?\d+)\s*,\s*(\d*\.?\d+)\%\s*,\s*(\d*\.?\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return i(s[4]),this.setHSL(parseFloat(s[1])/360,parseFloat(s[2])/100,parseFloat(s[3])/100,n);break;default:console.warn("THREE.Color: Unknown color model "+t)}}else if(a=/^\#([A-Fa-f\d]+)$/.exec(t)){const s=a[1],r=s.length;if(r===3)return this.setRGB(parseInt(s.charAt(0),16)/15,parseInt(s.charAt(1),16)/15,parseInt(s.charAt(2),16)/15,n);if(r===6)return this.setHex(parseInt(s,16),n);console.warn("THREE.Color: Invalid hex color "+t)}else if(t&&t.length>0)return this.setColorName(t,n);return this}setColorName(t,n=Ti){const i=Ex[t.toLowerCase()];return i!==void 0?this.setHex(i,n):console.warn("THREE.Color: Unknown color "+t),this}clone(){return new this.constructor(this.r,this.g,this.b)}copy(t){return this.r=t.r,this.g=t.g,this.b=t.b,this}copySRGBToLinear(t){return this.r=zr(t.r),this.g=zr(t.g),this.b=zr(t.b),this}copyLinearToSRGB(t){return this.r=Wf(t.r),this.g=Wf(t.g),this.b=Wf(t.b),this}convertSRGBToLinear(){return this.copySRGBToLinear(this),this}convertLinearToSRGB(){return this.copyLinearToSRGB(this),this}getHex(t=Ti){return ae.fromWorkingColorSpace(sn.copy(this),t),Math.round(hn(sn.r*255,0,255))*65536+Math.round(hn(sn.g*255,0,255))*256+Math.round(hn(sn.b*255,0,255))}getHexString(t=Ti){return("000000"+this.getHex(t).toString(16)).slice(-6)}getHSL(t,n=ae.workingColorSpace){ae.fromWorkingColorSpace(sn.copy(this),n);const i=sn.r,a=sn.g,s=sn.b,r=Math.max(i,a,s),o=Math.min(i,a,s);let l,u;const h=(o+r)/2;if(o===r)l=0,u=0;else{const p=r-o;switch(u=h<=.5?p/(r+o):p/(2-r-o),r){case i:l=(a-s)/p+(a<s?6:0);break;case a:l=(s-i)/p+2;break;case s:l=(i-a)/p+4;break}l/=6}return t.h=l,t.s=u,t.l=h,t}getRGB(t,n=ae.workingColorSpace){return ae.fromWorkingColorSpace(sn.copy(this),n),t.r=sn.r,t.g=sn.g,t.b=sn.b,t}getStyle(t=Ti){ae.fromWorkingColorSpace(sn.copy(this),t);const n=sn.r,i=sn.g,a=sn.b;return t!==Ti?`color(${t} ${n.toFixed(3)} ${i.toFixed(3)} ${a.toFixed(3)})`:`rgb(${Math.round(n*255)},${Math.round(i*255)},${Math.round(a*255)})`}offsetHSL(t,n,i){return this.getHSL(_a),this.setHSL(_a.h+t,_a.s+n,_a.l+i)}add(t){return this.r+=t.r,this.g+=t.g,this.b+=t.b,this}addColors(t,n){return this.r=t.r+n.r,this.g=t.g+n.g,this.b=t.b+n.b,this}addScalar(t){return this.r+=t,this.g+=t,this.b+=t,this}sub(t){return this.r=Math.max(0,this.r-t.r),this.g=Math.max(0,this.g-t.g),this.b=Math.max(0,this.b-t.b),this}multiply(t){return this.r*=t.r,this.g*=t.g,this.b*=t.b,this}multiplyScalar(t){return this.r*=t,this.g*=t,this.b*=t,this}lerp(t,n){return this.r+=(t.r-this.r)*n,this.g+=(t.g-this.g)*n,this.b+=(t.b-this.b)*n,this}lerpColors(t,n,i){return this.r=t.r+(n.r-t.r)*i,this.g=t.g+(n.g-t.g)*i,this.b=t.b+(n.b-t.b)*i,this}lerpHSL(t,n){this.getHSL(_a),t.getHSL(au);const i=Yf(_a.h,au.h,n),a=Yf(_a.s,au.s,n),s=Yf(_a.l,au.l,n);return this.setHSL(i,a,s),this}setFromVector3(t){return this.r=t.x,this.g=t.y,this.b=t.z,this}applyMatrix3(t){const n=this.r,i=this.g,a=this.b,s=t.elements;return this.r=s[0]*n+s[3]*i+s[6]*a,this.g=s[1]*n+s[4]*i+s[7]*a,this.b=s[2]*n+s[5]*i+s[8]*a,this}equals(t){return t.r===this.r&&t.g===this.g&&t.b===this.b}fromArray(t,n=0){return this.r=t[n],this.g=t[n+1],this.b=t[n+2],this}toArray(t=[],n=0){return t[n]=this.r,t[n+1]=this.g,t[n+2]=this.b,t}fromBufferAttribute(t,n){return this.r=t.getX(n),this.g=t.getY(n),this.b=t.getZ(n),this}toJSON(){return this.getHex()}*[Symbol.iterator](){yield this.r,yield this.g,yield this.b}}const sn=new Ht;Ht.NAMES=Ex;let R1=0;class Rl extends Hs{constructor(){super(),this.isMaterial=!0,Object.defineProperty(this,"id",{value:R1++}),this.uuid=bl(),this.name="",this.type="Material",this.blending=Or,this.side=ja,this.vertexColors=!1,this.opacity=1,this.transparent=!1,this.alphaHash=!1,this.blendSrc=Pd,this.blendDst=zd,this.blendEquation=hs,this.blendSrcAlpha=null,this.blendDstAlpha=null,this.blendEquationAlpha=null,this.blendColor=new Ht(0,0,0),this.blendAlpha=0,this.depthFunc=Kr,this.depthTest=!0,this.depthWrite=!0,this.stencilWriteMask=255,this.stencilFunc=Vg,this.stencilRef=0,this.stencilFuncMask=255,this.stencilFail=ks,this.stencilZFail=ks,this.stencilZPass=ks,this.stencilWrite=!1,this.clippingPlanes=null,this.clipIntersection=!1,this.clipShadows=!1,this.shadowSide=null,this.colorWrite=!0,this.precision=null,this.polygonOffset=!1,this.polygonOffsetFactor=0,this.polygonOffsetUnits=0,this.dithering=!1,this.alphaToCoverage=!1,this.premultipliedAlpha=!1,this.forceSinglePass=!1,this.visible=!0,this.toneMapped=!0,this.userData={},this.version=0,this._alphaTest=0}get alphaTest(){return this._alphaTest}set alphaTest(t){this._alphaTest>0!=t>0&&this.version++,this._alphaTest=t}onBeforeRender(){}onBeforeCompile(){}customProgramCacheKey(){return this.onBeforeCompile.toString()}setValues(t){if(t!==void 0)for(const n in t){const i=t[n];if(i===void 0){console.warn(`THREE.Material: parameter '${n}' has value of undefined.`);continue}const a=this[n];if(a===void 0){console.warn(`THREE.Material: '${n}' is not a property of THREE.${this.type}.`);continue}a&&a.isColor?a.set(i):a&&a.isVector3&&i&&i.isVector3?a.copy(i):this[n]=i}}toJSON(t){const n=t===void 0||typeof t=="string";n&&(t={textures:{},images:{}});const i={metadata:{version:4.6,type:"Material",generator:"Material.toJSON"}};i.uuid=this.uuid,i.type=this.type,this.name!==""&&(i.name=this.name),this.color&&this.color.isColor&&(i.color=this.color.getHex()),this.roughness!==void 0&&(i.roughness=this.roughness),this.metalness!==void 0&&(i.metalness=this.metalness),this.sheen!==void 0&&(i.sheen=this.sheen),this.sheenColor&&this.sheenColor.isColor&&(i.sheenColor=this.sheenColor.getHex()),this.sheenRoughness!==void 0&&(i.sheenRoughness=this.sheenRoughness),this.emissive&&this.emissive.isColor&&(i.emissive=this.emissive.getHex()),this.emissiveIntensity!==void 0&&this.emissiveIntensity!==1&&(i.emissiveIntensity=this.emissiveIntensity),this.specular&&this.specular.isColor&&(i.specular=this.specular.getHex()),this.specularIntensity!==void 0&&(i.specularIntensity=this.specularIntensity),this.specularColor&&this.specularColor.isColor&&(i.specularColor=this.specularColor.getHex()),this.shininess!==void 0&&(i.shininess=this.shininess),this.clearcoat!==void 0&&(i.clearcoat=this.clearcoat),this.clearcoatRoughness!==void 0&&(i.clearcoatRoughness=this.clearcoatRoughness),this.clearcoatMap&&this.clearcoatMap.isTexture&&(i.clearcoatMap=this.clearcoatMap.toJSON(t).uuid),this.clearcoatRoughnessMap&&this.clearcoatRoughnessMap.isTexture&&(i.clearcoatRoughnessMap=this.clearcoatRoughnessMap.toJSON(t).uuid),this.clearcoatNormalMap&&this.clearcoatNormalMap.isTexture&&(i.clearcoatNormalMap=this.clearcoatNormalMap.toJSON(t).uuid,i.clearcoatNormalScale=this.clearcoatNormalScale.toArray()),this.dispersion!==void 0&&(i.dispersion=this.dispersion),this.iridescence!==void 0&&(i.iridescence=this.iridescence),this.iridescenceIOR!==void 0&&(i.iridescenceIOR=this.iridescenceIOR),this.iridescenceThicknessRange!==void 0&&(i.iridescenceThicknessRange=this.iridescenceThicknessRange),this.iridescenceMap&&this.iridescenceMap.isTexture&&(i.iridescenceMap=this.iridescenceMap.toJSON(t).uuid),this.iridescenceThicknessMap&&this.iridescenceThicknessMap.isTexture&&(i.iridescenceThicknessMap=this.iridescenceThicknessMap.toJSON(t).uuid),this.anisotropy!==void 0&&(i.anisotropy=this.anisotropy),this.anisotropyRotation!==void 0&&(i.anisotropyRotation=this.anisotropyRotation),this.anisotropyMap&&this.anisotropyMap.isTexture&&(i.anisotropyMap=this.anisotropyMap.toJSON(t).uuid),this.map&&this.map.isTexture&&(i.map=this.map.toJSON(t).uuid),this.matcap&&this.matcap.isTexture&&(i.matcap=this.matcap.toJSON(t).uuid),this.alphaMap&&this.alphaMap.isTexture&&(i.alphaMap=this.alphaMap.toJSON(t).uuid),this.lightMap&&this.lightMap.isTexture&&(i.lightMap=this.lightMap.toJSON(t).uuid,i.lightMapIntensity=this.lightMapIntensity),this.aoMap&&this.aoMap.isTexture&&(i.aoMap=this.aoMap.toJSON(t).uuid,i.aoMapIntensity=this.aoMapIntensity),this.bumpMap&&this.bumpMap.isTexture&&(i.bumpMap=this.bumpMap.toJSON(t).uuid,i.bumpScale=this.bumpScale),this.normalMap&&this.normalMap.isTexture&&(i.normalMap=this.normalMap.toJSON(t).uuid,i.normalMapType=this.normalMapType,i.normalScale=this.normalScale.toArray()),this.displacementMap&&this.displacementMap.isTexture&&(i.displacementMap=this.displacementMap.toJSON(t).uuid,i.displacementScale=this.displacementScale,i.displacementBias=this.displacementBias),this.roughnessMap&&this.roughnessMap.isTexture&&(i.roughnessMap=this.roughnessMap.toJSON(t).uuid),this.metalnessMap&&this.metalnessMap.isTexture&&(i.metalnessMap=this.metalnessMap.toJSON(t).uuid),this.emissiveMap&&this.emissiveMap.isTexture&&(i.emissiveMap=this.emissiveMap.toJSON(t).uuid),this.specularMap&&this.specularMap.isTexture&&(i.specularMap=this.specularMap.toJSON(t).uuid),this.specularIntensityMap&&this.specularIntensityMap.isTexture&&(i.specularIntensityMap=this.specularIntensityMap.toJSON(t).uuid),this.specularColorMap&&this.specularColorMap.isTexture&&(i.specularColorMap=this.specularColorMap.toJSON(t).uuid),this.envMap&&this.envMap.isTexture&&(i.envMap=this.envMap.toJSON(t).uuid,this.combine!==void 0&&(i.combine=this.combine)),this.envMapRotation!==void 0&&(i.envMapRotation=this.envMapRotation.toArray()),this.envMapIntensity!==void 0&&(i.envMapIntensity=this.envMapIntensity),this.reflectivity!==void 0&&(i.reflectivity=this.reflectivity),this.refractionRatio!==void 0&&(i.refractionRatio=this.refractionRatio),this.gradientMap&&this.gradientMap.isTexture&&(i.gradientMap=this.gradientMap.toJSON(t).uuid),this.transmission!==void 0&&(i.transmission=this.transmission),this.transmissionMap&&this.transmissionMap.isTexture&&(i.transmissionMap=this.transmissionMap.toJSON(t).uuid),this.thickness!==void 0&&(i.thickness=this.thickness),this.thicknessMap&&this.thicknessMap.isTexture&&(i.thicknessMap=this.thicknessMap.toJSON(t).uuid),this.attenuationDistance!==void 0&&this.attenuationDistance!==1/0&&(i.attenuationDistance=this.attenuationDistance),this.attenuationColor!==void 0&&(i.attenuationColor=this.attenuationColor.getHex()),this.size!==void 0&&(i.size=this.size),this.shadowSide!==null&&(i.shadowSide=this.shadowSide),this.sizeAttenuation!==void 0&&(i.sizeAttenuation=this.sizeAttenuation),this.blending!==Or&&(i.blending=this.blending),this.side!==ja&&(i.side=this.side),this.vertexColors===!0&&(i.vertexColors=!0),this.opacity<1&&(i.opacity=this.opacity),this.transparent===!0&&(i.transparent=!0),this.blendSrc!==Pd&&(i.blendSrc=this.blendSrc),this.blendDst!==zd&&(i.blendDst=this.blendDst),this.blendEquation!==hs&&(i.blendEquation=this.blendEquation),this.blendSrcAlpha!==null&&(i.blendSrcAlpha=this.blendSrcAlpha),this.blendDstAlpha!==null&&(i.blendDstAlpha=this.blendDstAlpha),this.blendEquationAlpha!==null&&(i.blendEquationAlpha=this.blendEquationAlpha),this.blendColor&&this.blendColor.isColor&&(i.blendColor=this.blendColor.getHex()),this.blendAlpha!==0&&(i.blendAlpha=this.blendAlpha),this.depthFunc!==Kr&&(i.depthFunc=this.depthFunc),this.depthTest===!1&&(i.depthTest=this.depthTest),this.depthWrite===!1&&(i.depthWrite=this.depthWrite),this.colorWrite===!1&&(i.colorWrite=this.colorWrite),this.stencilWriteMask!==255&&(i.stencilWriteMask=this.stencilWriteMask),this.stencilFunc!==Vg&&(i.stencilFunc=this.stencilFunc),this.stencilRef!==0&&(i.stencilRef=this.stencilRef),this.stencilFuncMask!==255&&(i.stencilFuncMask=this.stencilFuncMask),this.stencilFail!==ks&&(i.stencilFail=this.stencilFail),this.stencilZFail!==ks&&(i.stencilZFail=this.stencilZFail),this.stencilZPass!==ks&&(i.stencilZPass=this.stencilZPass),this.stencilWrite===!0&&(i.stencilWrite=this.stencilWrite),this.rotation!==void 0&&this.rotation!==0&&(i.rotation=this.rotation),this.polygonOffset===!0&&(i.polygonOffset=!0),this.polygonOffsetFactor!==0&&(i.polygonOffsetFactor=this.polygonOffsetFactor),this.polygonOffsetUnits!==0&&(i.polygonOffsetUnits=this.polygonOffsetUnits),this.linewidth!==void 0&&this.linewidth!==1&&(i.linewidth=this.linewidth),this.dashSize!==void 0&&(i.dashSize=this.dashSize),this.gapSize!==void 0&&(i.gapSize=this.gapSize),this.scale!==void 0&&(i.scale=this.scale),this.dithering===!0&&(i.dithering=!0),this.alphaTest>0&&(i.alphaTest=this.alphaTest),this.alphaHash===!0&&(i.alphaHash=!0),this.alphaToCoverage===!0&&(i.alphaToCoverage=!0),this.premultipliedAlpha===!0&&(i.premultipliedAlpha=!0),this.forceSinglePass===!0&&(i.forceSinglePass=!0),this.wireframe===!0&&(i.wireframe=!0),this.wireframeLinewidth>1&&(i.wireframeLinewidth=this.wireframeLinewidth),this.wireframeLinecap!=="round"&&(i.wireframeLinecap=this.wireframeLinecap),this.wireframeLinejoin!=="round"&&(i.wireframeLinejoin=this.wireframeLinejoin),this.flatShading===!0&&(i.flatShading=!0),this.visible===!1&&(i.visible=!1),this.toneMapped===!1&&(i.toneMapped=!1),this.fog===!1&&(i.fog=!1),Object.keys(this.userData).length>0&&(i.userData=this.userData);function a(s){const r=[];for(const o in s){const l=s[o];delete l.metadata,r.push(l)}return r}if(n){const s=a(t.textures),r=a(t.images);s.length>0&&(i.textures=s),r.length>0&&(i.images=r)}return i}clone(){return new this.constructor().copy(this)}copy(t){this.name=t.name,this.blending=t.blending,this.side=t.side,this.vertexColors=t.vertexColors,this.opacity=t.opacity,this.transparent=t.transparent,this.blendSrc=t.blendSrc,this.blendDst=t.blendDst,this.blendEquation=t.blendEquation,this.blendSrcAlpha=t.blendSrcAlpha,this.blendDstAlpha=t.blendDstAlpha,this.blendEquationAlpha=t.blendEquationAlpha,this.blendColor.copy(t.blendColor),this.blendAlpha=t.blendAlpha,this.depthFunc=t.depthFunc,this.depthTest=t.depthTest,this.depthWrite=t.depthWrite,this.stencilWriteMask=t.stencilWriteMask,this.stencilFunc=t.stencilFunc,this.stencilRef=t.stencilRef,this.stencilFuncMask=t.stencilFuncMask,this.stencilFail=t.stencilFail,this.stencilZFail=t.stencilZFail,this.stencilZPass=t.stencilZPass,this.stencilWrite=t.stencilWrite;const n=t.clippingPlanes;let i=null;if(n!==null){const a=n.length;i=new Array(a);for(let s=0;s!==a;++s)i[s]=n[s].clone()}return this.clippingPlanes=i,this.clipIntersection=t.clipIntersection,this.clipShadows=t.clipShadows,this.shadowSide=t.shadowSide,this.colorWrite=t.colorWrite,this.precision=t.precision,this.polygonOffset=t.polygonOffset,this.polygonOffsetFactor=t.polygonOffsetFactor,this.polygonOffsetUnits=t.polygonOffsetUnits,this.dithering=t.dithering,this.alphaTest=t.alphaTest,this.alphaHash=t.alphaHash,this.alphaToCoverage=t.alphaToCoverage,this.premultipliedAlpha=t.premultipliedAlpha,this.forceSinglePass=t.forceSinglePass,this.visible=t.visible,this.toneMapped=t.toneMapped,this.userData=JSON.parse(JSON.stringify(t.userData)),this}dispose(){this.dispatchEvent({type:"dispose"})}set needsUpdate(t){t===!0&&this.version++}onBuild(){console.warn("Material: onBuild() has been removed.")}}class Os extends Rl{constructor(t){super(),this.isMeshBasicMaterial=!0,this.type="MeshBasicMaterial",this.color=new Ht(16777215),this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.specularMap=null,this.alphaMap=null,this.envMap=null,this.envMapRotation=new sa,this.combine=rx,this.reflectivity=1,this.refractionRatio=.98,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.color.copy(t.color),this.map=t.map,this.lightMap=t.lightMap,this.lightMapIntensity=t.lightMapIntensity,this.aoMap=t.aoMap,this.aoMapIntensity=t.aoMapIntensity,this.specularMap=t.specularMap,this.alphaMap=t.alphaMap,this.envMap=t.envMap,this.envMapRotation.copy(t.envMapRotation),this.combine=t.combine,this.reflectivity=t.reflectivity,this.refractionRatio=t.refractionRatio,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.wireframeLinecap=t.wireframeLinecap,this.wireframeLinejoin=t.wireframeLinejoin,this.fog=t.fog,this}}const Ne=new P,su=new Lt;class si{constructor(t,n,i=!1){if(Array.isArray(t))throw new TypeError("THREE.BufferAttribute: array should be a Typed Array.");this.isBufferAttribute=!0,this.name="",this.array=t,this.itemSize=n,this.count=t!==void 0?t.length/n:0,this.normalized=i,this.usage=Xg,this.updateRanges=[],this.gpuType=ji,this.version=0}onUploadCallback(){}set needsUpdate(t){t===!0&&this.version++}setUsage(t){return this.usage=t,this}addUpdateRange(t,n){this.updateRanges.push({start:t,count:n})}clearUpdateRanges(){this.updateRanges.length=0}copy(t){return this.name=t.name,this.array=new t.array.constructor(t.array),this.itemSize=t.itemSize,this.count=t.count,this.normalized=t.normalized,this.usage=t.usage,this.gpuType=t.gpuType,this}copyAt(t,n,i){t*=this.itemSize,i*=n.itemSize;for(let a=0,s=this.itemSize;a<s;a++)this.array[t+a]=n.array[i+a];return this}copyArray(t){return this.array.set(t),this}applyMatrix3(t){if(this.itemSize===2)for(let n=0,i=this.count;n<i;n++)su.fromBufferAttribute(this,n),su.applyMatrix3(t),this.setXY(n,su.x,su.y);else if(this.itemSize===3)for(let n=0,i=this.count;n<i;n++)Ne.fromBufferAttribute(this,n),Ne.applyMatrix3(t),this.setXYZ(n,Ne.x,Ne.y,Ne.z);return this}applyMatrix4(t){for(let n=0,i=this.count;n<i;n++)Ne.fromBufferAttribute(this,n),Ne.applyMatrix4(t),this.setXYZ(n,Ne.x,Ne.y,Ne.z);return this}applyNormalMatrix(t){for(let n=0,i=this.count;n<i;n++)Ne.fromBufferAttribute(this,n),Ne.applyNormalMatrix(t),this.setXYZ(n,Ne.x,Ne.y,Ne.z);return this}transformDirection(t){for(let n=0,i=this.count;n<i;n++)Ne.fromBufferAttribute(this,n),Ne.transformDirection(t),this.setXYZ(n,Ne.x,Ne.y,Ne.z);return this}set(t,n=0){return this.array.set(t,n),this}getComponent(t,n){let i=this.array[t*this.itemSize+n];return this.normalized&&(i=So(i,this.array)),i}setComponent(t,n,i){return this.normalized&&(i=gn(i,this.array)),this.array[t*this.itemSize+n]=i,this}getX(t){let n=this.array[t*this.itemSize];return this.normalized&&(n=So(n,this.array)),n}setX(t,n){return this.normalized&&(n=gn(n,this.array)),this.array[t*this.itemSize]=n,this}getY(t){let n=this.array[t*this.itemSize+1];return this.normalized&&(n=So(n,this.array)),n}setY(t,n){return this.normalized&&(n=gn(n,this.array)),this.array[t*this.itemSize+1]=n,this}getZ(t){let n=this.array[t*this.itemSize+2];return this.normalized&&(n=So(n,this.array)),n}setZ(t,n){return this.normalized&&(n=gn(n,this.array)),this.array[t*this.itemSize+2]=n,this}getW(t){let n=this.array[t*this.itemSize+3];return this.normalized&&(n=So(n,this.array)),n}setW(t,n){return this.normalized&&(n=gn(n,this.array)),this.array[t*this.itemSize+3]=n,this}setXY(t,n,i){return t*=this.itemSize,this.normalized&&(n=gn(n,this.array),i=gn(i,this.array)),this.array[t+0]=n,this.array[t+1]=i,this}setXYZ(t,n,i,a){return t*=this.itemSize,this.normalized&&(n=gn(n,this.array),i=gn(i,this.array),a=gn(a,this.array)),this.array[t+0]=n,this.array[t+1]=i,this.array[t+2]=a,this}setXYZW(t,n,i,a,s){return t*=this.itemSize,this.normalized&&(n=gn(n,this.array),i=gn(i,this.array),a=gn(a,this.array),s=gn(s,this.array)),this.array[t+0]=n,this.array[t+1]=i,this.array[t+2]=a,this.array[t+3]=s,this}onUpload(t){return this.onUploadCallback=t,this}clone(){return new this.constructor(this.array,this.itemSize).copy(this)}toJSON(){const t={itemSize:this.itemSize,type:this.array.constructor.name,array:Array.from(this.array),normalized:this.normalized};return this.name!==""&&(t.name=this.name),this.usage!==Xg&&(t.usage=this.usage),t}}class Tx extends si{constructor(t,n,i){super(new Uint16Array(t),n,i)}}class bx extends si{constructor(t,n,i){super(new Uint32Array(t),n,i)}}class We extends si{constructor(t,n,i){super(new Float32Array(t),n,i)}}let C1=0;const Zn=new Te,ch=new en,tr=new P,On=new Al,To=new Al,Ve=new P;class wn extends Hs{constructor(){super(),this.isBufferGeometry=!0,Object.defineProperty(this,"id",{value:C1++}),this.uuid=bl(),this.name="",this.type="BufferGeometry",this.index=null,this.attributes={},this.morphAttributes={},this.morphTargetsRelative=!1,this.groups=[],this.boundingBox=null,this.boundingSphere=null,this.drawRange={start:0,count:1/0},this.userData={}}getIndex(){return this.index}setIndex(t){return Array.isArray(t)?this.index=new(Sx(t)?bx:Tx)(t,1):this.index=t,this}getAttribute(t){return this.attributes[t]}setAttribute(t,n){return this.attributes[t]=n,this}deleteAttribute(t){return delete this.attributes[t],this}hasAttribute(t){return this.attributes[t]!==void 0}addGroup(t,n,i=0){this.groups.push({start:t,count:n,materialIndex:i})}clearGroups(){this.groups=[]}setDrawRange(t,n){this.drawRange.start=t,this.drawRange.count=n}applyMatrix4(t){const n=this.attributes.position;n!==void 0&&(n.applyMatrix4(t),n.needsUpdate=!0);const i=this.attributes.normal;if(i!==void 0){const s=new Pt().getNormalMatrix(t);i.applyNormalMatrix(s),i.needsUpdate=!0}const a=this.attributes.tangent;return a!==void 0&&(a.transformDirection(t),a.needsUpdate=!0),this.boundingBox!==null&&this.computeBoundingBox(),this.boundingSphere!==null&&this.computeBoundingSphere(),this}applyQuaternion(t){return Zn.makeRotationFromQuaternion(t),this.applyMatrix4(Zn),this}rotateX(t){return Zn.makeRotationX(t),this.applyMatrix4(Zn),this}rotateY(t){return Zn.makeRotationY(t),this.applyMatrix4(Zn),this}rotateZ(t){return Zn.makeRotationZ(t),this.applyMatrix4(Zn),this}translate(t,n,i){return Zn.makeTranslation(t,n,i),this.applyMatrix4(Zn),this}scale(t,n,i){return Zn.makeScale(t,n,i),this.applyMatrix4(Zn),this}lookAt(t){return ch.lookAt(t),ch.updateMatrix(),this.applyMatrix4(ch.matrix),this}center(){return this.computeBoundingBox(),this.boundingBox.getCenter(tr).negate(),this.translate(tr.x,tr.y,tr.z),this}setFromPoints(t){const n=[];for(let i=0,a=t.length;i<a;i++){const s=t[i];n.push(s.x,s.y,s.z||0)}return this.setAttribute("position",new We(n,3)),this}computeBoundingBox(){this.boundingBox===null&&(this.boundingBox=new Al);const t=this.attributes.position,n=this.morphAttributes.position;if(t&&t.isGLBufferAttribute){console.error("THREE.BufferGeometry.computeBoundingBox(): GLBufferAttribute requires a manual bounding box.",this),this.boundingBox.set(new P(-1/0,-1/0,-1/0),new P(1/0,1/0,1/0));return}if(t!==void 0){if(this.boundingBox.setFromBufferAttribute(t),n)for(let i=0,a=n.length;i<a;i++){const s=n[i];On.setFromBufferAttribute(s),this.morphTargetsRelative?(Ve.addVectors(this.boundingBox.min,On.min),this.boundingBox.expandByPoint(Ve),Ve.addVectors(this.boundingBox.max,On.max),this.boundingBox.expandByPoint(Ve)):(this.boundingBox.expandByPoint(On.min),this.boundingBox.expandByPoint(On.max))}}else this.boundingBox.makeEmpty();(isNaN(this.boundingBox.min.x)||isNaN(this.boundingBox.min.y)||isNaN(this.boundingBox.min.z))&&console.error('THREE.BufferGeometry.computeBoundingBox(): Computed min/max have NaN values. The "position" attribute is likely to have NaN values.',this)}computeBoundingSphere(){this.boundingSphere===null&&(this.boundingSphere=new ef);const t=this.attributes.position,n=this.morphAttributes.position;if(t&&t.isGLBufferAttribute){console.error("THREE.BufferGeometry.computeBoundingSphere(): GLBufferAttribute requires a manual bounding sphere.",this),this.boundingSphere.set(new P,1/0);return}if(t){const i=this.boundingSphere.center;if(On.setFromBufferAttribute(t),n)for(let s=0,r=n.length;s<r;s++){const o=n[s];To.setFromBufferAttribute(o),this.morphTargetsRelative?(Ve.addVectors(On.min,To.min),On.expandByPoint(Ve),Ve.addVectors(On.max,To.max),On.expandByPoint(Ve)):(On.expandByPoint(To.min),On.expandByPoint(To.max))}On.getCenter(i);let a=0;for(let s=0,r=t.count;s<r;s++)Ve.fromBufferAttribute(t,s),a=Math.max(a,i.distanceToSquared(Ve));if(n)for(let s=0,r=n.length;s<r;s++){const o=n[s],l=this.morphTargetsRelative;for(let u=0,h=o.count;u<h;u++)Ve.fromBufferAttribute(o,u),l&&(tr.fromBufferAttribute(t,u),Ve.add(tr)),a=Math.max(a,i.distanceToSquared(Ve))}this.boundingSphere.radius=Math.sqrt(a),isNaN(this.boundingSphere.radius)&&console.error('THREE.BufferGeometry.computeBoundingSphere(): Computed radius is NaN. The "position" attribute is likely to have NaN values.',this)}}computeTangents(){const t=this.index,n=this.attributes;if(t===null||n.position===void 0||n.normal===void 0||n.uv===void 0){console.error("THREE.BufferGeometry: .computeTangents() failed. Missing required attributes (index, position, normal or uv)");return}const i=n.position,a=n.normal,s=n.uv;this.hasAttribute("tangent")===!1&&this.setAttribute("tangent",new si(new Float32Array(4*i.count),4));const r=this.getAttribute("tangent"),o=[],l=[];for(let w=0;w<i.count;w++)o[w]=new P,l[w]=new P;const u=new P,h=new P,p=new P,f=new Lt,d=new Lt,v=new Lt,y=new P,m=new P;function c(w,W,S){u.fromBufferAttribute(i,w),h.fromBufferAttribute(i,W),p.fromBufferAttribute(i,S),f.fromBufferAttribute(s,w),d.fromBufferAttribute(s,W),v.fromBufferAttribute(s,S),h.sub(u),p.sub(u),d.sub(f),v.sub(f);const T=1/(d.x*v.y-v.x*d.y);isFinite(T)&&(y.copy(h).multiplyScalar(v.y).addScaledVector(p,-d.y).multiplyScalar(T),m.copy(p).multiplyScalar(d.x).addScaledVector(h,-v.x).multiplyScalar(T),o[w].add(y),o[W].add(y),o[S].add(y),l[w].add(m),l[W].add(m),l[S].add(m))}let _=this.groups;_.length===0&&(_=[{start:0,count:t.count}]);for(let w=0,W=_.length;w<W;++w){const S=_[w],T=S.start,F=S.count;for(let G=T,Y=T+F;G<Y;G+=3)c(t.getX(G+0),t.getX(G+1),t.getX(G+2))}const g=new P,x=new P,C=new P,R=new P;function b(w){C.fromBufferAttribute(a,w),R.copy(C);const W=o[w];g.copy(W),g.sub(C.multiplyScalar(C.dot(W))).normalize(),x.crossVectors(R,W);const T=x.dot(l[w])<0?-1:1;r.setXYZW(w,g.x,g.y,g.z,T)}for(let w=0,W=_.length;w<W;++w){const S=_[w],T=S.start,F=S.count;for(let G=T,Y=T+F;G<Y;G+=3)b(t.getX(G+0)),b(t.getX(G+1)),b(t.getX(G+2))}}computeVertexNormals(){const t=this.index,n=this.getAttribute("position");if(n!==void 0){let i=this.getAttribute("normal");if(i===void 0)i=new si(new Float32Array(n.count*3),3),this.setAttribute("normal",i);else for(let f=0,d=i.count;f<d;f++)i.setXYZ(f,0,0,0);const a=new P,s=new P,r=new P,o=new P,l=new P,u=new P,h=new P,p=new P;if(t)for(let f=0,d=t.count;f<d;f+=3){const v=t.getX(f+0),y=t.getX(f+1),m=t.getX(f+2);a.fromBufferAttribute(n,v),s.fromBufferAttribute(n,y),r.fromBufferAttribute(n,m),h.subVectors(r,s),p.subVectors(a,s),h.cross(p),o.fromBufferAttribute(i,v),l.fromBufferAttribute(i,y),u.fromBufferAttribute(i,m),o.add(h),l.add(h),u.add(h),i.setXYZ(v,o.x,o.y,o.z),i.setXYZ(y,l.x,l.y,l.z),i.setXYZ(m,u.x,u.y,u.z)}else for(let f=0,d=n.count;f<d;f+=3)a.fromBufferAttribute(n,f+0),s.fromBufferAttribute(n,f+1),r.fromBufferAttribute(n,f+2),h.subVectors(r,s),p.subVectors(a,s),h.cross(p),i.setXYZ(f+0,h.x,h.y,h.z),i.setXYZ(f+1,h.x,h.y,h.z),i.setXYZ(f+2,h.x,h.y,h.z);this.normalizeNormals(),i.needsUpdate=!0}}normalizeNormals(){const t=this.attributes.normal;for(let n=0,i=t.count;n<i;n++)Ve.fromBufferAttribute(t,n),Ve.normalize(),t.setXYZ(n,Ve.x,Ve.y,Ve.z)}toNonIndexed(){function t(o,l){const u=o.array,h=o.itemSize,p=o.normalized,f=new u.constructor(l.length*h);let d=0,v=0;for(let y=0,m=l.length;y<m;y++){o.isInterleavedBufferAttribute?d=l[y]*o.data.stride+o.offset:d=l[y]*h;for(let c=0;c<h;c++)f[v++]=u[d++]}return new si(f,h,p)}if(this.index===null)return console.warn("THREE.BufferGeometry.toNonIndexed(): BufferGeometry is already non-indexed."),this;const n=new wn,i=this.index.array,a=this.attributes;for(const o in a){const l=a[o],u=t(l,i);n.setAttribute(o,u)}const s=this.morphAttributes;for(const o in s){const l=[],u=s[o];for(let h=0,p=u.length;h<p;h++){const f=u[h],d=t(f,i);l.push(d)}n.morphAttributes[o]=l}n.morphTargetsRelative=this.morphTargetsRelative;const r=this.groups;for(let o=0,l=r.length;o<l;o++){const u=r[o];n.addGroup(u.start,u.count,u.materialIndex)}return n}toJSON(){const t={metadata:{version:4.6,type:"BufferGeometry",generator:"BufferGeometry.toJSON"}};if(t.uuid=this.uuid,t.type=this.type,this.name!==""&&(t.name=this.name),Object.keys(this.userData).length>0&&(t.userData=this.userData),this.parameters!==void 0){const l=this.parameters;for(const u in l)l[u]!==void 0&&(t[u]=l[u]);return t}t.data={attributes:{}};const n=this.index;n!==null&&(t.data.index={type:n.array.constructor.name,array:Array.prototype.slice.call(n.array)});const i=this.attributes;for(const l in i){const u=i[l];t.data.attributes[l]=u.toJSON(t.data)}const a={};let s=!1;for(const l in this.morphAttributes){const u=this.morphAttributes[l],h=[];for(let p=0,f=u.length;p<f;p++){const d=u[p];h.push(d.toJSON(t.data))}h.length>0&&(a[l]=h,s=!0)}s&&(t.data.morphAttributes=a,t.data.morphTargetsRelative=this.morphTargetsRelative);const r=this.groups;r.length>0&&(t.data.groups=JSON.parse(JSON.stringify(r)));const o=this.boundingSphere;return o!==null&&(t.data.boundingSphere={center:o.center.toArray(),radius:o.radius}),t}clone(){return new this.constructor().copy(this)}copy(t){this.index=null,this.attributes={},this.morphAttributes={},this.groups=[],this.boundingBox=null,this.boundingSphere=null;const n={};this.name=t.name;const i=t.index;i!==null&&this.setIndex(i.clone(n));const a=t.attributes;for(const u in a){const h=a[u];this.setAttribute(u,h.clone(n))}const s=t.morphAttributes;for(const u in s){const h=[],p=s[u];for(let f=0,d=p.length;f<d;f++)h.push(p[f].clone(n));this.morphAttributes[u]=h}this.morphTargetsRelative=t.morphTargetsRelative;const r=t.groups;for(let u=0,h=r.length;u<h;u++){const p=r[u];this.addGroup(p.start,p.count,p.materialIndex)}const o=t.boundingBox;o!==null&&(this.boundingBox=o.clone());const l=t.boundingSphere;return l!==null&&(this.boundingSphere=l.clone()),this.drawRange.start=t.drawRange.start,this.drawRange.count=t.drawRange.count,this.userData=t.userData,this}dispose(){this.dispatchEvent({type:"dispose"})}}const i0=new Te,as=new Pm,ru=new ef,a0=new P,ou=new P,lu=new P,uu=new P,fh=new P,cu=new P,s0=new P,fu=new P;class En extends en{constructor(t=new wn,n=new Os){super(),this.isMesh=!0,this.type="Mesh",this.geometry=t,this.material=n,this.updateMorphTargets()}copy(t,n){return super.copy(t,n),t.morphTargetInfluences!==void 0&&(this.morphTargetInfluences=t.morphTargetInfluences.slice()),t.morphTargetDictionary!==void 0&&(this.morphTargetDictionary=Object.assign({},t.morphTargetDictionary)),this.material=Array.isArray(t.material)?t.material.slice():t.material,this.geometry=t.geometry,this}updateMorphTargets(){const n=this.geometry.morphAttributes,i=Object.keys(n);if(i.length>0){const a=n[i[0]];if(a!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let s=0,r=a.length;s<r;s++){const o=a[s].name||String(s);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=s}}}}getVertexPosition(t,n){const i=this.geometry,a=i.attributes.position,s=i.morphAttributes.position,r=i.morphTargetsRelative;n.fromBufferAttribute(a,t);const o=this.morphTargetInfluences;if(s&&o){cu.set(0,0,0);for(let l=0,u=s.length;l<u;l++){const h=o[l],p=s[l];h!==0&&(fh.fromBufferAttribute(p,t),r?cu.addScaledVector(fh,h):cu.addScaledVector(fh.sub(n),h))}n.add(cu)}return n}raycast(t,n){const i=this.geometry,a=this.material,s=this.matrixWorld;a!==void 0&&(i.boundingSphere===null&&i.computeBoundingSphere(),ru.copy(i.boundingSphere),ru.applyMatrix4(s),as.copy(t.ray).recast(t.near),!(ru.containsPoint(as.origin)===!1&&(as.intersectSphere(ru,a0)===null||as.origin.distanceToSquared(a0)>(t.far-t.near)**2))&&(i0.copy(s).invert(),as.copy(t.ray).applyMatrix4(i0),!(i.boundingBox!==null&&as.intersectsBox(i.boundingBox)===!1)&&this._computeIntersections(t,n,as)))}_computeIntersections(t,n,i){let a;const s=this.geometry,r=this.material,o=s.index,l=s.attributes.position,u=s.attributes.uv,h=s.attributes.uv1,p=s.attributes.normal,f=s.groups,d=s.drawRange;if(o!==null)if(Array.isArray(r))for(let v=0,y=f.length;v<y;v++){const m=f[v],c=r[m.materialIndex],_=Math.max(m.start,d.start),g=Math.min(o.count,Math.min(m.start+m.count,d.start+d.count));for(let x=_,C=g;x<C;x+=3){const R=o.getX(x),b=o.getX(x+1),w=o.getX(x+2);a=hu(this,c,t,i,u,h,p,R,b,w),a&&(a.faceIndex=Math.floor(x/3),a.face.materialIndex=m.materialIndex,n.push(a))}}else{const v=Math.max(0,d.start),y=Math.min(o.count,d.start+d.count);for(let m=v,c=y;m<c;m+=3){const _=o.getX(m),g=o.getX(m+1),x=o.getX(m+2);a=hu(this,r,t,i,u,h,p,_,g,x),a&&(a.faceIndex=Math.floor(m/3),n.push(a))}}else if(l!==void 0)if(Array.isArray(r))for(let v=0,y=f.length;v<y;v++){const m=f[v],c=r[m.materialIndex],_=Math.max(m.start,d.start),g=Math.min(l.count,Math.min(m.start+m.count,d.start+d.count));for(let x=_,C=g;x<C;x+=3){const R=x,b=x+1,w=x+2;a=hu(this,c,t,i,u,h,p,R,b,w),a&&(a.faceIndex=Math.floor(x/3),a.face.materialIndex=m.materialIndex,n.push(a))}}else{const v=Math.max(0,d.start),y=Math.min(l.count,d.start+d.count);for(let m=v,c=y;m<c;m+=3){const _=m,g=m+1,x=m+2;a=hu(this,r,t,i,u,h,p,_,g,x),a&&(a.faceIndex=Math.floor(m/3),n.push(a))}}}}function w1(e,t,n,i,a,s,r,o){let l;if(t.side===bn?l=i.intersectTriangle(r,s,a,!0,o):l=i.intersectTriangle(a,s,r,t.side===ja,o),l===null)return null;fu.copy(o),fu.applyMatrix4(e.matrixWorld);const u=n.ray.origin.distanceTo(fu);return u<n.near||u>n.far?null:{distance:u,point:fu.clone(),object:e}}function hu(e,t,n,i,a,s,r,o,l,u){e.getVertexPosition(o,ou),e.getVertexPosition(l,lu),e.getVertexPosition(u,uu);const h=w1(e,t,n,i,ou,lu,uu,s0);if(h){const p=new P;_i.getBarycoord(s0,ou,lu,uu,p),a&&(h.uv=_i.getInterpolatedAttribute(a,o,l,u,p,new Lt)),s&&(h.uv1=_i.getInterpolatedAttribute(s,o,l,u,p,new Lt)),r&&(h.normal=_i.getInterpolatedAttribute(r,o,l,u,p,new P),h.normal.dot(i.direction)>0&&h.normal.multiplyScalar(-1));const f={a:o,b:l,c:u,normal:new P,materialIndex:0};_i.getNormal(ou,lu,uu,f.normal),h.face=f,h.barycoord=p}return h}class co extends wn{constructor(t=1,n=1,i=1,a=1,s=1,r=1){super(),this.type="BoxGeometry",this.parameters={width:t,height:n,depth:i,widthSegments:a,heightSegments:s,depthSegments:r};const o=this;a=Math.floor(a),s=Math.floor(s),r=Math.floor(r);const l=[],u=[],h=[],p=[];let f=0,d=0;v("z","y","x",-1,-1,i,n,t,r,s,0),v("z","y","x",1,-1,i,n,-t,r,s,1),v("x","z","y",1,1,t,i,n,a,r,2),v("x","z","y",1,-1,t,i,-n,a,r,3),v("x","y","z",1,-1,t,n,i,a,s,4),v("x","y","z",-1,-1,t,n,-i,a,s,5),this.setIndex(l),this.setAttribute("position",new We(u,3)),this.setAttribute("normal",new We(h,3)),this.setAttribute("uv",new We(p,2));function v(y,m,c,_,g,x,C,R,b,w,W){const S=x/b,T=C/w,F=x/2,G=C/2,Y=R/2,K=b+1,D=w+1;let V=0,z=0;const tt=new P;for(let it=0;it<D;it++){const ht=it*T-G;for(let Ft=0;Ft<K;Ft++){const kt=Ft*S-F;tt[y]=kt*_,tt[m]=ht*g,tt[c]=Y,u.push(tt.x,tt.y,tt.z),tt[y]=0,tt[m]=0,tt[c]=R>0?1:-1,h.push(tt.x,tt.y,tt.z),p.push(Ft/b),p.push(1-it/w),V+=1}}for(let it=0;it<w;it++)for(let ht=0;ht<b;ht++){const Ft=f+ht+K*it,kt=f+ht+K*(it+1),k=f+(ht+1)+K*(it+1),$=f+(ht+1)+K*it;l.push(Ft,kt,$),l.push(kt,k,$),z+=6}o.addGroup(d,z,W),d+=z,f+=V}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new co(t.width,t.height,t.depth,t.widthSegments,t.heightSegments,t.depthSegments)}}function eo(e){const t={};for(const n in e){t[n]={};for(const i in e[n]){const a=e[n][i];a&&(a.isColor||a.isMatrix3||a.isMatrix4||a.isVector2||a.isVector3||a.isVector4||a.isTexture||a.isQuaternion)?a.isRenderTargetTexture?(console.warn("UniformsUtils: Textures of render targets cannot be cloned via cloneUniforms() or mergeUniforms()."),t[n][i]=null):t[n][i]=a.clone():Array.isArray(a)?t[n][i]=a.slice():t[n][i]=a}}return t}function cn(e){const t={};for(let n=0;n<e.length;n++){const i=eo(e[n]);for(const a in i)t[a]=i[a]}return t}function D1(e){const t=[];for(let n=0;n<e.length;n++)t.push(e[n].clone());return t}function Ax(e){const t=e.getRenderTarget();return t===null?e.outputColorSpace:t.isXRRenderTarget===!0?t.texture.colorSpace:ae.workingColorSpace}const U1={clone:eo,merge:cn};var N1=`void main() {
	gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
}`,L1=`void main() {
	gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0 );
}`;class Za extends Rl{constructor(t){super(),this.isShaderMaterial=!0,this.type="ShaderMaterial",this.defines={},this.uniforms={},this.uniformsGroups=[],this.vertexShader=N1,this.fragmentShader=L1,this.linewidth=1,this.wireframe=!1,this.wireframeLinewidth=1,this.fog=!1,this.lights=!1,this.clipping=!1,this.forceSinglePass=!0,this.extensions={clipCullDistance:!1,multiDraw:!1},this.defaultAttributeValues={color:[1,1,1],uv:[0,0],uv1:[0,0]},this.index0AttributeName=void 0,this.uniformsNeedUpdate=!1,this.glslVersion=null,t!==void 0&&this.setValues(t)}copy(t){return super.copy(t),this.fragmentShader=t.fragmentShader,this.vertexShader=t.vertexShader,this.uniforms=eo(t.uniforms),this.uniformsGroups=D1(t.uniformsGroups),this.defines=Object.assign({},t.defines),this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.fog=t.fog,this.lights=t.lights,this.clipping=t.clipping,this.extensions=Object.assign({},t.extensions),this.glslVersion=t.glslVersion,this}toJSON(t){const n=super.toJSON(t);n.glslVersion=this.glslVersion,n.uniforms={};for(const a in this.uniforms){const r=this.uniforms[a].value;r&&r.isTexture?n.uniforms[a]={type:"t",value:r.toJSON(t).uuid}:r&&r.isColor?n.uniforms[a]={type:"c",value:r.getHex()}:r&&r.isVector2?n.uniforms[a]={type:"v2",value:r.toArray()}:r&&r.isVector3?n.uniforms[a]={type:"v3",value:r.toArray()}:r&&r.isVector4?n.uniforms[a]={type:"v4",value:r.toArray()}:r&&r.isMatrix3?n.uniforms[a]={type:"m3",value:r.toArray()}:r&&r.isMatrix4?n.uniforms[a]={type:"m4",value:r.toArray()}:n.uniforms[a]={value:r}}Object.keys(this.defines).length>0&&(n.defines=this.defines),n.vertexShader=this.vertexShader,n.fragmentShader=this.fragmentShader,n.lights=this.lights,n.clipping=this.clipping;const i={};for(const a in this.extensions)this.extensions[a]===!0&&(i[a]=!0);return Object.keys(i).length>0&&(n.extensions=i),n}}class Rx extends en{constructor(){super(),this.isCamera=!0,this.type="Camera",this.matrixWorldInverse=new Te,this.projectionMatrix=new Te,this.projectionMatrixInverse=new Te,this.coordinateSystem=Zi}copy(t,n){return super.copy(t,n),this.matrixWorldInverse.copy(t.matrixWorldInverse),this.projectionMatrix.copy(t.projectionMatrix),this.projectionMatrixInverse.copy(t.projectionMatrixInverse),this.coordinateSystem=t.coordinateSystem,this}getWorldDirection(t){return super.getWorldDirection(t).negate()}updateMatrixWorld(t){super.updateMatrixWorld(t),this.matrixWorldInverse.copy(this.matrixWorld).invert()}updateWorldMatrix(t,n){super.updateWorldMatrix(t,n),this.matrixWorldInverse.copy(this.matrixWorld).invert()}clone(){return new this.constructor().copy(this)}}const ga=new P,r0=new Lt,o0=new Lt;class $n extends Rx{constructor(t=50,n=1,i=.1,a=2e3){super(),this.isPerspectiveCamera=!0,this.type="PerspectiveCamera",this.fov=t,this.zoom=1,this.near=i,this.far=a,this.focus=10,this.aspect=n,this.view=null,this.filmGauge=35,this.filmOffset=0,this.updateProjectionMatrix()}copy(t,n){return super.copy(t,n),this.fov=t.fov,this.zoom=t.zoom,this.near=t.near,this.far=t.far,this.focus=t.focus,this.aspect=t.aspect,this.view=t.view===null?null:Object.assign({},t.view),this.filmGauge=t.filmGauge,this.filmOffset=t.filmOffset,this}setFocalLength(t){const n=.5*this.getFilmHeight()/t;this.fov=yp*2*Math.atan(n),this.updateProjectionMatrix()}getFocalLength(){const t=Math.tan(qu*.5*this.fov);return .5*this.getFilmHeight()/t}getEffectiveFOV(){return yp*2*Math.atan(Math.tan(qu*.5*this.fov)/this.zoom)}getFilmWidth(){return this.filmGauge*Math.min(this.aspect,1)}getFilmHeight(){return this.filmGauge/Math.max(this.aspect,1)}getViewBounds(t,n,i){ga.set(-1,-1,.5).applyMatrix4(this.projectionMatrixInverse),n.set(ga.x,ga.y).multiplyScalar(-t/ga.z),ga.set(1,1,.5).applyMatrix4(this.projectionMatrixInverse),i.set(ga.x,ga.y).multiplyScalar(-t/ga.z)}getViewSize(t,n){return this.getViewBounds(t,r0,o0),n.subVectors(o0,r0)}setViewOffset(t,n,i,a,s,r){this.aspect=t/n,this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=t,this.view.fullHeight=n,this.view.offsetX=i,this.view.offsetY=a,this.view.width=s,this.view.height=r,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){const t=this.near;let n=t*Math.tan(qu*.5*this.fov)/this.zoom,i=2*n,a=this.aspect*i,s=-.5*a;const r=this.view;if(this.view!==null&&this.view.enabled){const l=r.fullWidth,u=r.fullHeight;s+=r.offsetX*a/l,n-=r.offsetY*i/u,a*=r.width/l,i*=r.height/u}const o=this.filmOffset;o!==0&&(s+=t*o/this.getFilmWidth()),this.projectionMatrix.makePerspective(s,s+a,n,n-i,t,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(t){const n=super.toJSON(t);return n.object.fov=this.fov,n.object.zoom=this.zoom,n.object.near=this.near,n.object.far=this.far,n.object.focus=this.focus,n.object.aspect=this.aspect,this.view!==null&&(n.object.view=Object.assign({},this.view)),n.object.filmGauge=this.filmGauge,n.object.filmOffset=this.filmOffset,n}}const er=-90,nr=1;class O1 extends en{constructor(t,n,i){super(),this.type="CubeCamera",this.renderTarget=i,this.coordinateSystem=null,this.activeMipmapLevel=0;const a=new $n(er,nr,t,n);a.layers=this.layers,this.add(a);const s=new $n(er,nr,t,n);s.layers=this.layers,this.add(s);const r=new $n(er,nr,t,n);r.layers=this.layers,this.add(r);const o=new $n(er,nr,t,n);o.layers=this.layers,this.add(o);const l=new $n(er,nr,t,n);l.layers=this.layers,this.add(l);const u=new $n(er,nr,t,n);u.layers=this.layers,this.add(u)}updateCoordinateSystem(){const t=this.coordinateSystem,n=this.children.concat(),[i,a,s,r,o,l]=n;for(const u of n)this.remove(u);if(t===Zi)i.up.set(0,1,0),i.lookAt(1,0,0),a.up.set(0,1,0),a.lookAt(-1,0,0),s.up.set(0,0,-1),s.lookAt(0,1,0),r.up.set(0,0,1),r.lookAt(0,-1,0),o.up.set(0,1,0),o.lookAt(0,0,1),l.up.set(0,1,0),l.lookAt(0,0,-1);else if(t===Rc)i.up.set(0,-1,0),i.lookAt(-1,0,0),a.up.set(0,-1,0),a.lookAt(1,0,0),s.up.set(0,0,1),s.lookAt(0,1,0),r.up.set(0,0,-1),r.lookAt(0,-1,0),o.up.set(0,-1,0),o.lookAt(0,0,1),l.up.set(0,-1,0),l.lookAt(0,0,-1);else throw new Error("THREE.CubeCamera.updateCoordinateSystem(): Invalid coordinate system: "+t);for(const u of n)this.add(u),u.updateMatrixWorld()}update(t,n){this.parent===null&&this.updateMatrixWorld();const{renderTarget:i,activeMipmapLevel:a}=this;this.coordinateSystem!==t.coordinateSystem&&(this.coordinateSystem=t.coordinateSystem,this.updateCoordinateSystem());const[s,r,o,l,u,h]=this.children,p=t.getRenderTarget(),f=t.getActiveCubeFace(),d=t.getActiveMipmapLevel(),v=t.xr.enabled;t.xr.enabled=!1;const y=i.texture.generateMipmaps;i.texture.generateMipmaps=!1,t.setRenderTarget(i,0,a),t.render(n,s),t.setRenderTarget(i,1,a),t.render(n,r),t.setRenderTarget(i,2,a),t.render(n,o),t.setRenderTarget(i,3,a),t.render(n,l),t.setRenderTarget(i,4,a),t.render(n,u),i.texture.generateMipmaps=y,t.setRenderTarget(i,5,a),t.render(n,h),t.setRenderTarget(p,f,d),t.xr.enabled=v,i.texture.needsPMREMUpdate=!0}}class Cx extends An{constructor(t,n,i,a,s,r,o,l,u,h){t=t!==void 0?t:[],n=n!==void 0?n:Qr,super(t,n,i,a,s,r,o,l,u,h),this.isCubeTexture=!0,this.flipY=!1}get images(){return this.image}set images(t){this.image=t}}class P1 extends Ns{constructor(t=1,n={}){super(t,t,n),this.isWebGLCubeRenderTarget=!0;const i={width:t,height:t,depth:1},a=[i,i,i,i,i,i];this.texture=new Cx(a,n.mapping,n.wrapS,n.wrapT,n.magFilter,n.minFilter,n.format,n.type,n.anisotropy,n.colorSpace),this.texture.isRenderTargetTexture=!0,this.texture.generateMipmaps=n.generateMipmaps!==void 0?n.generateMipmaps:!1,this.texture.minFilter=n.minFilter!==void 0?n.minFilter:mi}fromEquirectangularTexture(t,n){this.texture.type=n.type,this.texture.colorSpace=n.colorSpace,this.texture.generateMipmaps=n.generateMipmaps,this.texture.minFilter=n.minFilter,this.texture.magFilter=n.magFilter;const i={uniforms:{tEquirect:{value:null}},vertexShader:`

				varying vec3 vWorldDirection;

				vec3 transformDirection( in vec3 dir, in mat4 matrix ) {

					return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );

				}

				void main() {

					vWorldDirection = transformDirection( position, modelMatrix );

					#include <begin_vertex>
					#include <project_vertex>

				}
			`,fragmentShader:`

				uniform sampler2D tEquirect;

				varying vec3 vWorldDirection;

				#include <common>

				void main() {

					vec3 direction = normalize( vWorldDirection );

					vec2 sampleUV = equirectUv( direction );

					gl_FragColor = texture2D( tEquirect, sampleUV );

				}
			`},a=new co(5,5,5),s=new Za({name:"CubemapFromEquirect",uniforms:eo(i.uniforms),vertexShader:i.vertexShader,fragmentShader:i.fragmentShader,side:bn,blending:Ga});s.uniforms.tEquirect.value=n;const r=new En(a,s),o=n.minFilter;return n.minFilter===gs&&(n.minFilter=mi),new O1(1,10,this).update(t,r),n.minFilter=o,r.geometry.dispose(),r.material.dispose(),this}clear(t,n,i,a){const s=t.getRenderTarget();for(let r=0;r<6;r++)t.setRenderTarget(this,r),t.clear(n,i,a);t.setRenderTarget(s)}}const hh=new P,z1=new P,I1=new Pt;class Ma{constructor(t=new P(1,0,0),n=0){this.isPlane=!0,this.normal=t,this.constant=n}set(t,n){return this.normal.copy(t),this.constant=n,this}setComponents(t,n,i,a){return this.normal.set(t,n,i),this.constant=a,this}setFromNormalAndCoplanarPoint(t,n){return this.normal.copy(t),this.constant=-n.dot(this.normal),this}setFromCoplanarPoints(t,n,i){const a=hh.subVectors(i,n).cross(z1.subVectors(t,n)).normalize();return this.setFromNormalAndCoplanarPoint(a,t),this}copy(t){return this.normal.copy(t.normal),this.constant=t.constant,this}normalize(){const t=1/this.normal.length();return this.normal.multiplyScalar(t),this.constant*=t,this}negate(){return this.constant*=-1,this.normal.negate(),this}distanceToPoint(t){return this.normal.dot(t)+this.constant}distanceToSphere(t){return this.distanceToPoint(t.center)-t.radius}projectPoint(t,n){return n.copy(t).addScaledVector(this.normal,-this.distanceToPoint(t))}intersectLine(t,n){const i=t.delta(hh),a=this.normal.dot(i);if(a===0)return this.distanceToPoint(t.start)===0?n.copy(t.start):null;const s=-(t.start.dot(this.normal)+this.constant)/a;return s<0||s>1?null:n.copy(t.start).addScaledVector(i,s)}intersectsLine(t){const n=this.distanceToPoint(t.start),i=this.distanceToPoint(t.end);return n<0&&i>0||i<0&&n>0}intersectsBox(t){return t.intersectsPlane(this)}intersectsSphere(t){return t.intersectsPlane(this)}coplanarPoint(t){return t.copy(this.normal).multiplyScalar(-this.constant)}applyMatrix4(t,n){const i=n||I1.getNormalMatrix(t),a=this.coplanarPoint(hh).applyMatrix4(t),s=this.normal.applyMatrix3(i).normalize();return this.constant=-a.dot(s),this}translate(t){return this.constant-=t.dot(this.normal),this}equals(t){return t.normal.equals(this.normal)&&t.constant===this.constant}clone(){return new this.constructor().copy(this)}}const ss=new ef,du=new P;class zm{constructor(t=new Ma,n=new Ma,i=new Ma,a=new Ma,s=new Ma,r=new Ma){this.planes=[t,n,i,a,s,r]}set(t,n,i,a,s,r){const o=this.planes;return o[0].copy(t),o[1].copy(n),o[2].copy(i),o[3].copy(a),o[4].copy(s),o[5].copy(r),this}copy(t){const n=this.planes;for(let i=0;i<6;i++)n[i].copy(t.planes[i]);return this}setFromProjectionMatrix(t,n=Zi){const i=this.planes,a=t.elements,s=a[0],r=a[1],o=a[2],l=a[3],u=a[4],h=a[5],p=a[6],f=a[7],d=a[8],v=a[9],y=a[10],m=a[11],c=a[12],_=a[13],g=a[14],x=a[15];if(i[0].setComponents(l-s,f-u,m-d,x-c).normalize(),i[1].setComponents(l+s,f+u,m+d,x+c).normalize(),i[2].setComponents(l+r,f+h,m+v,x+_).normalize(),i[3].setComponents(l-r,f-h,m-v,x-_).normalize(),i[4].setComponents(l-o,f-p,m-y,x-g).normalize(),n===Zi)i[5].setComponents(l+o,f+p,m+y,x+g).normalize();else if(n===Rc)i[5].setComponents(o,p,y,g).normalize();else throw new Error("THREE.Frustum.setFromProjectionMatrix(): Invalid coordinate system: "+n);return this}intersectsObject(t){if(t.boundingSphere!==void 0)t.boundingSphere===null&&t.computeBoundingSphere(),ss.copy(t.boundingSphere).applyMatrix4(t.matrixWorld);else{const n=t.geometry;n.boundingSphere===null&&n.computeBoundingSphere(),ss.copy(n.boundingSphere).applyMatrix4(t.matrixWorld)}return this.intersectsSphere(ss)}intersectsSprite(t){return ss.center.set(0,0,0),ss.radius=.7071067811865476,ss.applyMatrix4(t.matrixWorld),this.intersectsSphere(ss)}intersectsSphere(t){const n=this.planes,i=t.center,a=-t.radius;for(let s=0;s<6;s++)if(n[s].distanceToPoint(i)<a)return!1;return!0}intersectsBox(t){const n=this.planes;for(let i=0;i<6;i++){const a=n[i];if(du.x=a.normal.x>0?t.max.x:t.min.x,du.y=a.normal.y>0?t.max.y:t.min.y,du.z=a.normal.z>0?t.max.z:t.min.z,a.distanceToPoint(du)<0)return!1}return!0}containsPoint(t){const n=this.planes;for(let i=0;i<6;i++)if(n[i].distanceToPoint(t)<0)return!1;return!0}clone(){return new this.constructor().copy(this)}}function wx(){let e=null,t=!1,n=null,i=null;function a(s,r){n(s,r),i=e.requestAnimationFrame(a)}return{start:function(){t!==!0&&n!==null&&(i=e.requestAnimationFrame(a),t=!0)},stop:function(){e.cancelAnimationFrame(i),t=!1},setAnimationLoop:function(s){n=s},setContext:function(s){e=s}}}function B1(e){const t=new WeakMap;function n(o,l){const u=o.array,h=o.usage,p=u.byteLength,f=e.createBuffer();e.bindBuffer(l,f),e.bufferData(l,u,h),o.onUploadCallback();let d;if(u instanceof Float32Array)d=e.FLOAT;else if(u instanceof Uint16Array)o.isFloat16BufferAttribute?d=e.HALF_FLOAT:d=e.UNSIGNED_SHORT;else if(u instanceof Int16Array)d=e.SHORT;else if(u instanceof Uint32Array)d=e.UNSIGNED_INT;else if(u instanceof Int32Array)d=e.INT;else if(u instanceof Int8Array)d=e.BYTE;else if(u instanceof Uint8Array)d=e.UNSIGNED_BYTE;else if(u instanceof Uint8ClampedArray)d=e.UNSIGNED_BYTE;else throw new Error("THREE.WebGLAttributes: Unsupported buffer data format: "+u);return{buffer:f,type:d,bytesPerElement:u.BYTES_PER_ELEMENT,version:o.version,size:p}}function i(o,l,u){const h=l.array,p=l.updateRanges;if(e.bindBuffer(u,o),p.length===0)e.bufferSubData(u,0,h);else{p.sort((d,v)=>d.start-v.start);let f=0;for(let d=1;d<p.length;d++){const v=p[f],y=p[d];y.start<=v.start+v.count+1?v.count=Math.max(v.count,y.start+y.count-v.start):(++f,p[f]=y)}p.length=f+1;for(let d=0,v=p.length;d<v;d++){const y=p[d];e.bufferSubData(u,y.start*h.BYTES_PER_ELEMENT,h,y.start,y.count)}l.clearUpdateRanges()}l.onUploadCallback()}function a(o){return o.isInterleavedBufferAttribute&&(o=o.data),t.get(o)}function s(o){o.isInterleavedBufferAttribute&&(o=o.data);const l=t.get(o);l&&(e.deleteBuffer(l.buffer),t.delete(o))}function r(o,l){if(o.isInterleavedBufferAttribute&&(o=o.data),o.isGLBufferAttribute){const h=t.get(o);(!h||h.version<o.version)&&t.set(o,{buffer:o.buffer,type:o.type,bytesPerElement:o.elementSize,version:o.version});return}const u=t.get(o);if(u===void 0)t.set(o,n(o,l));else if(u.version<o.version){if(u.size!==o.array.byteLength)throw new Error("THREE.WebGLAttributes: The size of the buffer attribute's array buffer does not match the original size. Resizing buffer attributes is not supported.");i(u.buffer,o,l),u.version=o.version}}return{get:a,remove:s,update:r}}class Cl extends wn{constructor(t=1,n=1,i=1,a=1){super(),this.type="PlaneGeometry",this.parameters={width:t,height:n,widthSegments:i,heightSegments:a};const s=t/2,r=n/2,o=Math.floor(i),l=Math.floor(a),u=o+1,h=l+1,p=t/o,f=n/l,d=[],v=[],y=[],m=[];for(let c=0;c<h;c++){const _=c*f-r;for(let g=0;g<u;g++){const x=g*p-s;v.push(x,-_,0),y.push(0,0,1),m.push(g/o),m.push(1-c/l)}}for(let c=0;c<l;c++)for(let _=0;_<o;_++){const g=_+u*c,x=_+u*(c+1),C=_+1+u*(c+1),R=_+1+u*c;d.push(g,x,R),d.push(x,C,R)}this.setIndex(d),this.setAttribute("position",new We(v,3)),this.setAttribute("normal",new We(y,3)),this.setAttribute("uv",new We(m,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new Cl(t.width,t.height,t.widthSegments,t.heightSegments)}}var F1=`#ifdef USE_ALPHAHASH
	if ( diffuseColor.a < getAlphaHashThreshold( vPosition ) ) discard;
#endif`,H1=`#ifdef USE_ALPHAHASH
	const float ALPHA_HASH_SCALE = 0.05;
	float hash2D( vec2 value ) {
		return fract( 1.0e4 * sin( 17.0 * value.x + 0.1 * value.y ) * ( 0.1 + abs( sin( 13.0 * value.y + value.x ) ) ) );
	}
	float hash3D( vec3 value ) {
		return hash2D( vec2( hash2D( value.xy ), value.z ) );
	}
	float getAlphaHashThreshold( vec3 position ) {
		float maxDeriv = max(
			length( dFdx( position.xyz ) ),
			length( dFdy( position.xyz ) )
		);
		float pixScale = 1.0 / ( ALPHA_HASH_SCALE * maxDeriv );
		vec2 pixScales = vec2(
			exp2( floor( log2( pixScale ) ) ),
			exp2( ceil( log2( pixScale ) ) )
		);
		vec2 alpha = vec2(
			hash3D( floor( pixScales.x * position.xyz ) ),
			hash3D( floor( pixScales.y * position.xyz ) )
		);
		float lerpFactor = fract( log2( pixScale ) );
		float x = ( 1.0 - lerpFactor ) * alpha.x + lerpFactor * alpha.y;
		float a = min( lerpFactor, 1.0 - lerpFactor );
		vec3 cases = vec3(
			x * x / ( 2.0 * a * ( 1.0 - a ) ),
			( x - 0.5 * a ) / ( 1.0 - a ),
			1.0 - ( ( 1.0 - x ) * ( 1.0 - x ) / ( 2.0 * a * ( 1.0 - a ) ) )
		);
		float threshold = ( x < ( 1.0 - a ) )
			? ( ( x < a ) ? cases.x : cases.y )
			: cases.z;
		return clamp( threshold , 1.0e-6, 1.0 );
	}
#endif`,G1=`#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, vAlphaMapUv ).g;
#endif`,V1=`#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,X1=`#ifdef USE_ALPHATEST
	#ifdef ALPHA_TO_COVERAGE
	diffuseColor.a = smoothstep( alphaTest, alphaTest + fwidth( diffuseColor.a ), diffuseColor.a );
	if ( diffuseColor.a == 0.0 ) discard;
	#else
	if ( diffuseColor.a < alphaTest ) discard;
	#endif
#endif`,k1=`#ifdef USE_ALPHATEST
	uniform float alphaTest;
#endif`,Y1=`#ifdef USE_AOMAP
	float ambientOcclusion = ( texture2D( aoMap, vAoMapUv ).r - 1.0 ) * aoMapIntensity + 1.0;
	reflectedLight.indirectDiffuse *= ambientOcclusion;
	#if defined( USE_CLEARCOAT ) 
		clearcoatSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_SHEEN ) 
		sheenSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD )
		float dotNV = saturate( dot( geometryNormal, geometryViewDir ) );
		reflectedLight.indirectSpecular *= computeSpecularOcclusion( dotNV, ambientOcclusion, material.roughness );
	#endif
#endif`,q1=`#ifdef USE_AOMAP
	uniform sampler2D aoMap;
	uniform float aoMapIntensity;
#endif`,W1=`#ifdef USE_BATCHING
	#if ! defined( GL_ANGLE_multi_draw )
	#define gl_DrawID _gl_DrawID
	uniform int _gl_DrawID;
	#endif
	uniform highp sampler2D batchingTexture;
	uniform highp usampler2D batchingIdTexture;
	mat4 getBatchingMatrix( const in float i ) {
		int size = textureSize( batchingTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( batchingTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( batchingTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( batchingTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( batchingTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
	float getIndirectIndex( const in int i ) {
		int size = textureSize( batchingIdTexture, 0 ).x;
		int x = i % size;
		int y = i / size;
		return float( texelFetch( batchingIdTexture, ivec2( x, y ), 0 ).r );
	}
#endif
#ifdef USE_BATCHING_COLOR
	uniform sampler2D batchingColorTexture;
	vec3 getBatchingColor( const in float i ) {
		int size = textureSize( batchingColorTexture, 0 ).x;
		int j = int( i );
		int x = j % size;
		int y = j / size;
		return texelFetch( batchingColorTexture, ivec2( x, y ), 0 ).rgb;
	}
#endif`,j1=`#ifdef USE_BATCHING
	mat4 batchingMatrix = getBatchingMatrix( getIndirectIndex( gl_DrawID ) );
#endif`,Z1=`vec3 transformed = vec3( position );
#ifdef USE_ALPHAHASH
	vPosition = vec3( position );
#endif`,K1=`vec3 objectNormal = vec3( normal );
#ifdef USE_TANGENT
	vec3 objectTangent = vec3( tangent.xyz );
#endif`,Q1=`float G_BlinnPhong_Implicit( ) {
	return 0.25;
}
float D_BlinnPhong( const in float shininess, const in float dotNH ) {
	return RECIPROCAL_PI * ( shininess * 0.5 + 1.0 ) * pow( dotNH, shininess );
}
vec3 BRDF_BlinnPhong( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in vec3 specularColor, const in float shininess ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( specularColor, 1.0, dotVH );
	float G = G_BlinnPhong_Implicit( );
	float D = D_BlinnPhong( shininess, dotNH );
	return F * ( G * D );
} // validated`,J1=`#ifdef USE_IRIDESCENCE
	const mat3 XYZ_TO_REC709 = mat3(
		 3.2404542, -0.9692660,  0.0556434,
		-1.5371385,  1.8760108, -0.2040259,
		-0.4985314,  0.0415560,  1.0572252
	);
	vec3 Fresnel0ToIor( vec3 fresnel0 ) {
		vec3 sqrtF0 = sqrt( fresnel0 );
		return ( vec3( 1.0 ) + sqrtF0 ) / ( vec3( 1.0 ) - sqrtF0 );
	}
	vec3 IorToFresnel0( vec3 transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - vec3( incidentIor ) ) / ( transmittedIor + vec3( incidentIor ) ) );
	}
	float IorToFresnel0( float transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - incidentIor ) / ( transmittedIor + incidentIor ));
	}
	vec3 evalSensitivity( float OPD, vec3 shift ) {
		float phase = 2.0 * PI * OPD * 1.0e-9;
		vec3 val = vec3( 5.4856e-13, 4.4201e-13, 5.2481e-13 );
		vec3 pos = vec3( 1.6810e+06, 1.7953e+06, 2.2084e+06 );
		vec3 var = vec3( 4.3278e+09, 9.3046e+09, 6.6121e+09 );
		vec3 xyz = val * sqrt( 2.0 * PI * var ) * cos( pos * phase + shift ) * exp( - pow2( phase ) * var );
		xyz.x += 9.7470e-14 * sqrt( 2.0 * PI * 4.5282e+09 ) * cos( 2.2399e+06 * phase + shift[ 0 ] ) * exp( - 4.5282e+09 * pow2( phase ) );
		xyz /= 1.0685e-7;
		vec3 rgb = XYZ_TO_REC709 * xyz;
		return rgb;
	}
	vec3 evalIridescence( float outsideIOR, float eta2, float cosTheta1, float thinFilmThickness, vec3 baseF0 ) {
		vec3 I;
		float iridescenceIOR = mix( outsideIOR, eta2, smoothstep( 0.0, 0.03, thinFilmThickness ) );
		float sinTheta2Sq = pow2( outsideIOR / iridescenceIOR ) * ( 1.0 - pow2( cosTheta1 ) );
		float cosTheta2Sq = 1.0 - sinTheta2Sq;
		if ( cosTheta2Sq < 0.0 ) {
			return vec3( 1.0 );
		}
		float cosTheta2 = sqrt( cosTheta2Sq );
		float R0 = IorToFresnel0( iridescenceIOR, outsideIOR );
		float R12 = F_Schlick( R0, 1.0, cosTheta1 );
		float T121 = 1.0 - R12;
		float phi12 = 0.0;
		if ( iridescenceIOR < outsideIOR ) phi12 = PI;
		float phi21 = PI - phi12;
		vec3 baseIOR = Fresnel0ToIor( clamp( baseF0, 0.0, 0.9999 ) );		vec3 R1 = IorToFresnel0( baseIOR, iridescenceIOR );
		vec3 R23 = F_Schlick( R1, 1.0, cosTheta2 );
		vec3 phi23 = vec3( 0.0 );
		if ( baseIOR[ 0 ] < iridescenceIOR ) phi23[ 0 ] = PI;
		if ( baseIOR[ 1 ] < iridescenceIOR ) phi23[ 1 ] = PI;
		if ( baseIOR[ 2 ] < iridescenceIOR ) phi23[ 2 ] = PI;
		float OPD = 2.0 * iridescenceIOR * thinFilmThickness * cosTheta2;
		vec3 phi = vec3( phi21 ) + phi23;
		vec3 R123 = clamp( R12 * R23, 1e-5, 0.9999 );
		vec3 r123 = sqrt( R123 );
		vec3 Rs = pow2( T121 ) * R23 / ( vec3( 1.0 ) - R123 );
		vec3 C0 = R12 + Rs;
		I = C0;
		vec3 Cm = Rs - T121;
		for ( int m = 1; m <= 2; ++ m ) {
			Cm *= r123;
			vec3 Sm = 2.0 * evalSensitivity( float( m ) * OPD, float( m ) * phi );
			I += Cm * Sm;
		}
		return max( I, vec3( 0.0 ) );
	}
#endif`,$1=`#ifdef USE_BUMPMAP
	uniform sampler2D bumpMap;
	uniform float bumpScale;
	vec2 dHdxy_fwd() {
		vec2 dSTdx = dFdx( vBumpMapUv );
		vec2 dSTdy = dFdy( vBumpMapUv );
		float Hll = bumpScale * texture2D( bumpMap, vBumpMapUv ).x;
		float dBx = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdx ).x - Hll;
		float dBy = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdy ).x - Hll;
		return vec2( dBx, dBy );
	}
	vec3 perturbNormalArb( vec3 surf_pos, vec3 surf_norm, vec2 dHdxy, float faceDirection ) {
		vec3 vSigmaX = normalize( dFdx( surf_pos.xyz ) );
		vec3 vSigmaY = normalize( dFdy( surf_pos.xyz ) );
		vec3 vN = surf_norm;
		vec3 R1 = cross( vSigmaY, vN );
		vec3 R2 = cross( vN, vSigmaX );
		float fDet = dot( vSigmaX, R1 ) * faceDirection;
		vec3 vGrad = sign( fDet ) * ( dHdxy.x * R1 + dHdxy.y * R2 );
		return normalize( abs( fDet ) * surf_norm - vGrad );
	}
#endif`,tA=`#if NUM_CLIPPING_PLANES > 0
	vec4 plane;
	#ifdef ALPHA_TO_COVERAGE
		float distanceToPlane, distanceGradient;
		float clipOpacity = 1.0;
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
			distanceGradient = fwidth( distanceToPlane ) / 2.0;
			clipOpacity *= smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			if ( clipOpacity == 0.0 ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			float unionClipOpacity = 1.0;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
				distanceGradient = fwidth( distanceToPlane ) / 2.0;
				unionClipOpacity *= 1.0 - smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			}
			#pragma unroll_loop_end
			clipOpacity *= 1.0 - unionClipOpacity;
		#endif
		diffuseColor.a *= clipOpacity;
		if ( diffuseColor.a == 0.0 ) discard;
	#else
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			if ( dot( vClipPosition, plane.xyz ) > plane.w ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			bool clipped = true;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				clipped = ( dot( vClipPosition, plane.xyz ) > plane.w ) && clipped;
			}
			#pragma unroll_loop_end
			if ( clipped ) discard;
		#endif
	#endif
#endif`,eA=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
	uniform vec4 clippingPlanes[ NUM_CLIPPING_PLANES ];
#endif`,nA=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
#endif`,iA=`#if NUM_CLIPPING_PLANES > 0
	vClipPosition = - mvPosition.xyz;
#endif`,aA=`#if defined( USE_COLOR_ALPHA )
	diffuseColor *= vColor;
#elif defined( USE_COLOR )
	diffuseColor.rgb *= vColor;
#endif`,sA=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR )
	varying vec3 vColor;
#endif`,rA=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	varying vec3 vColor;
#endif`,oA=`#if defined( USE_COLOR_ALPHA )
	vColor = vec4( 1.0 );
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	vColor = vec3( 1.0 );
#endif
#ifdef USE_COLOR
	vColor *= color;
#endif
#ifdef USE_INSTANCING_COLOR
	vColor.xyz *= instanceColor.xyz;
#endif
#ifdef USE_BATCHING_COLOR
	vec3 batchingColor = getBatchingColor( getIndirectIndex( gl_DrawID ) );
	vColor.xyz *= batchingColor.xyz;
#endif`,lA=`#define PI 3.141592653589793
#define PI2 6.283185307179586
#define PI_HALF 1.5707963267948966
#define RECIPROCAL_PI 0.3183098861837907
#define RECIPROCAL_PI2 0.15915494309189535
#define EPSILON 1e-6
#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
#define whiteComplement( a ) ( 1.0 - saturate( a ) )
float pow2( const in float x ) { return x*x; }
vec3 pow2( const in vec3 x ) { return x*x; }
float pow3( const in float x ) { return x*x*x; }
float pow4( const in float x ) { float x2 = x*x; return x2*x2; }
float max3( const in vec3 v ) { return max( max( v.x, v.y ), v.z ); }
float average( const in vec3 v ) { return dot( v, vec3( 0.3333333 ) ); }
highp float rand( const in vec2 uv ) {
	const highp float a = 12.9898, b = 78.233, c = 43758.5453;
	highp float dt = dot( uv.xy, vec2( a,b ) ), sn = mod( dt, PI );
	return fract( sin( sn ) * c );
}
#ifdef HIGH_PRECISION
	float precisionSafeLength( vec3 v ) { return length( v ); }
#else
	float precisionSafeLength( vec3 v ) {
		float maxComponent = max3( abs( v ) );
		return length( v / maxComponent ) * maxComponent;
	}
#endif
struct IncidentLight {
	vec3 color;
	vec3 direction;
	bool visible;
};
struct ReflectedLight {
	vec3 directDiffuse;
	vec3 directSpecular;
	vec3 indirectDiffuse;
	vec3 indirectSpecular;
};
#ifdef USE_ALPHAHASH
	varying vec3 vPosition;
#endif
vec3 transformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );
}
vec3 inverseTransformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( vec4( dir, 0.0 ) * matrix ).xyz );
}
mat3 transposeMat3( const in mat3 m ) {
	mat3 tmp;
	tmp[ 0 ] = vec3( m[ 0 ].x, m[ 1 ].x, m[ 2 ].x );
	tmp[ 1 ] = vec3( m[ 0 ].y, m[ 1 ].y, m[ 2 ].y );
	tmp[ 2 ] = vec3( m[ 0 ].z, m[ 1 ].z, m[ 2 ].z );
	return tmp;
}
bool isPerspectiveMatrix( mat4 m ) {
	return m[ 2 ][ 3 ] == - 1.0;
}
vec2 equirectUv( in vec3 dir ) {
	float u = atan( dir.z, dir.x ) * RECIPROCAL_PI2 + 0.5;
	float v = asin( clamp( dir.y, - 1.0, 1.0 ) ) * RECIPROCAL_PI + 0.5;
	return vec2( u, v );
}
vec3 BRDF_Lambert( const in vec3 diffuseColor ) {
	return RECIPROCAL_PI * diffuseColor;
}
vec3 F_Schlick( const in vec3 f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
}
float F_Schlick( const in float f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
} // validated`,uA=`#ifdef ENVMAP_TYPE_CUBE_UV
	#define cubeUV_minMipLevel 4.0
	#define cubeUV_minTileSize 16.0
	float getFace( vec3 direction ) {
		vec3 absDirection = abs( direction );
		float face = - 1.0;
		if ( absDirection.x > absDirection.z ) {
			if ( absDirection.x > absDirection.y )
				face = direction.x > 0.0 ? 0.0 : 3.0;
			else
				face = direction.y > 0.0 ? 1.0 : 4.0;
		} else {
			if ( absDirection.z > absDirection.y )
				face = direction.z > 0.0 ? 2.0 : 5.0;
			else
				face = direction.y > 0.0 ? 1.0 : 4.0;
		}
		return face;
	}
	vec2 getUV( vec3 direction, float face ) {
		vec2 uv;
		if ( face == 0.0 ) {
			uv = vec2( direction.z, direction.y ) / abs( direction.x );
		} else if ( face == 1.0 ) {
			uv = vec2( - direction.x, - direction.z ) / abs( direction.y );
		} else if ( face == 2.0 ) {
			uv = vec2( - direction.x, direction.y ) / abs( direction.z );
		} else if ( face == 3.0 ) {
			uv = vec2( - direction.z, direction.y ) / abs( direction.x );
		} else if ( face == 4.0 ) {
			uv = vec2( - direction.x, direction.z ) / abs( direction.y );
		} else {
			uv = vec2( direction.x, direction.y ) / abs( direction.z );
		}
		return 0.5 * ( uv + 1.0 );
	}
	vec3 bilinearCubeUV( sampler2D envMap, vec3 direction, float mipInt ) {
		float face = getFace( direction );
		float filterInt = max( cubeUV_minMipLevel - mipInt, 0.0 );
		mipInt = max( mipInt, cubeUV_minMipLevel );
		float faceSize = exp2( mipInt );
		highp vec2 uv = getUV( direction, face ) * ( faceSize - 2.0 ) + 1.0;
		if ( face > 2.0 ) {
			uv.y += faceSize;
			face -= 3.0;
		}
		uv.x += face * faceSize;
		uv.x += filterInt * 3.0 * cubeUV_minTileSize;
		uv.y += 4.0 * ( exp2( CUBEUV_MAX_MIP ) - faceSize );
		uv.x *= CUBEUV_TEXEL_WIDTH;
		uv.y *= CUBEUV_TEXEL_HEIGHT;
		#ifdef texture2DGradEXT
			return texture2DGradEXT( envMap, uv, vec2( 0.0 ), vec2( 0.0 ) ).rgb;
		#else
			return texture2D( envMap, uv ).rgb;
		#endif
	}
	#define cubeUV_r0 1.0
	#define cubeUV_m0 - 2.0
	#define cubeUV_r1 0.8
	#define cubeUV_m1 - 1.0
	#define cubeUV_r4 0.4
	#define cubeUV_m4 2.0
	#define cubeUV_r5 0.305
	#define cubeUV_m5 3.0
	#define cubeUV_r6 0.21
	#define cubeUV_m6 4.0
	float roughnessToMip( float roughness ) {
		float mip = 0.0;
		if ( roughness >= cubeUV_r1 ) {
			mip = ( cubeUV_r0 - roughness ) * ( cubeUV_m1 - cubeUV_m0 ) / ( cubeUV_r0 - cubeUV_r1 ) + cubeUV_m0;
		} else if ( roughness >= cubeUV_r4 ) {
			mip = ( cubeUV_r1 - roughness ) * ( cubeUV_m4 - cubeUV_m1 ) / ( cubeUV_r1 - cubeUV_r4 ) + cubeUV_m1;
		} else if ( roughness >= cubeUV_r5 ) {
			mip = ( cubeUV_r4 - roughness ) * ( cubeUV_m5 - cubeUV_m4 ) / ( cubeUV_r4 - cubeUV_r5 ) + cubeUV_m4;
		} else if ( roughness >= cubeUV_r6 ) {
			mip = ( cubeUV_r5 - roughness ) * ( cubeUV_m6 - cubeUV_m5 ) / ( cubeUV_r5 - cubeUV_r6 ) + cubeUV_m5;
		} else {
			mip = - 2.0 * log2( 1.16 * roughness );		}
		return mip;
	}
	vec4 textureCubeUV( sampler2D envMap, vec3 sampleDir, float roughness ) {
		float mip = clamp( roughnessToMip( roughness ), cubeUV_m0, CUBEUV_MAX_MIP );
		float mipF = fract( mip );
		float mipInt = floor( mip );
		vec3 color0 = bilinearCubeUV( envMap, sampleDir, mipInt );
		if ( mipF == 0.0 ) {
			return vec4( color0, 1.0 );
		} else {
			vec3 color1 = bilinearCubeUV( envMap, sampleDir, mipInt + 1.0 );
			return vec4( mix( color0, color1, mipF ), 1.0 );
		}
	}
#endif`,cA=`vec3 transformedNormal = objectNormal;
#ifdef USE_TANGENT
	vec3 transformedTangent = objectTangent;
#endif
#ifdef USE_BATCHING
	mat3 bm = mat3( batchingMatrix );
	transformedNormal /= vec3( dot( bm[ 0 ], bm[ 0 ] ), dot( bm[ 1 ], bm[ 1 ] ), dot( bm[ 2 ], bm[ 2 ] ) );
	transformedNormal = bm * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = bm * transformedTangent;
	#endif
#endif
#ifdef USE_INSTANCING
	mat3 im = mat3( instanceMatrix );
	transformedNormal /= vec3( dot( im[ 0 ], im[ 0 ] ), dot( im[ 1 ], im[ 1 ] ), dot( im[ 2 ], im[ 2 ] ) );
	transformedNormal = im * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = im * transformedTangent;
	#endif
#endif
transformedNormal = normalMatrix * transformedNormal;
#ifdef FLIP_SIDED
	transformedNormal = - transformedNormal;
#endif
#ifdef USE_TANGENT
	transformedTangent = ( modelViewMatrix * vec4( transformedTangent, 0.0 ) ).xyz;
	#ifdef FLIP_SIDED
		transformedTangent = - transformedTangent;
	#endif
#endif`,fA=`#ifdef USE_DISPLACEMENTMAP
	uniform sampler2D displacementMap;
	uniform float displacementScale;
	uniform float displacementBias;
#endif`,hA=`#ifdef USE_DISPLACEMENTMAP
	transformed += normalize( objectNormal ) * ( texture2D( displacementMap, vDisplacementMapUv ).x * displacementScale + displacementBias );
#endif`,dA=`#ifdef USE_EMISSIVEMAP
	vec4 emissiveColor = texture2D( emissiveMap, vEmissiveMapUv );
	totalEmissiveRadiance *= emissiveColor.rgb;
#endif`,pA=`#ifdef USE_EMISSIVEMAP
	uniform sampler2D emissiveMap;
#endif`,mA="gl_FragColor = linearToOutputTexel( gl_FragColor );",_A=`
const mat3 LINEAR_SRGB_TO_LINEAR_DISPLAY_P3 = mat3(
	vec3( 0.8224621, 0.177538, 0.0 ),
	vec3( 0.0331941, 0.9668058, 0.0 ),
	vec3( 0.0170827, 0.0723974, 0.9105199 )
);
const mat3 LINEAR_DISPLAY_P3_TO_LINEAR_SRGB = mat3(
	vec3( 1.2249401, - 0.2249404, 0.0 ),
	vec3( - 0.0420569, 1.0420571, 0.0 ),
	vec3( - 0.0196376, - 0.0786361, 1.0982735 )
);
vec4 LinearSRGBToLinearDisplayP3( in vec4 value ) {
	return vec4( value.rgb * LINEAR_SRGB_TO_LINEAR_DISPLAY_P3, value.a );
}
vec4 LinearDisplayP3ToLinearSRGB( in vec4 value ) {
	return vec4( value.rgb * LINEAR_DISPLAY_P3_TO_LINEAR_SRGB, value.a );
}
vec4 LinearTransferOETF( in vec4 value ) {
	return value;
}
vec4 sRGBTransferOETF( in vec4 value ) {
	return vec4( mix( pow( value.rgb, vec3( 0.41666 ) ) * 1.055 - vec3( 0.055 ), value.rgb * 12.92, vec3( lessThanEqual( value.rgb, vec3( 0.0031308 ) ) ) ), value.a );
}`,gA=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vec3 cameraToFrag;
		if ( isOrthographic ) {
			cameraToFrag = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToFrag = normalize( vWorldPosition - cameraPosition );
		}
		vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vec3 reflectVec = reflect( cameraToFrag, worldNormal );
		#else
			vec3 reflectVec = refract( cameraToFrag, worldNormal, refractionRatio );
		#endif
	#else
		vec3 reflectVec = vReflect;
	#endif
	#ifdef ENVMAP_TYPE_CUBE
		vec4 envColor = textureCube( envMap, envMapRotation * vec3( flipEnvMap * reflectVec.x, reflectVec.yz ) );
	#else
		vec4 envColor = vec4( 0.0 );
	#endif
	#ifdef ENVMAP_BLENDING_MULTIPLY
		outgoingLight = mix( outgoingLight, outgoingLight * envColor.xyz, specularStrength * reflectivity );
	#elif defined( ENVMAP_BLENDING_MIX )
		outgoingLight = mix( outgoingLight, envColor.xyz, specularStrength * reflectivity );
	#elif defined( ENVMAP_BLENDING_ADD )
		outgoingLight += envColor.xyz * specularStrength * reflectivity;
	#endif
#endif`,vA=`#ifdef USE_ENVMAP
	uniform float envMapIntensity;
	uniform float flipEnvMap;
	uniform mat3 envMapRotation;
	#ifdef ENVMAP_TYPE_CUBE
		uniform samplerCube envMap;
	#else
		uniform sampler2D envMap;
	#endif
	
#endif`,SA=`#ifdef USE_ENVMAP
	uniform float reflectivity;
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		varying vec3 vWorldPosition;
		uniform float refractionRatio;
	#else
		varying vec3 vReflect;
	#endif
#endif`,yA=`#ifdef USE_ENVMAP
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		
		varying vec3 vWorldPosition;
	#else
		varying vec3 vReflect;
		uniform float refractionRatio;
	#endif
#endif`,xA=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vWorldPosition = worldPosition.xyz;
	#else
		vec3 cameraToVertex;
		if ( isOrthographic ) {
			cameraToVertex = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToVertex = normalize( worldPosition.xyz - cameraPosition );
		}
		vec3 worldNormal = inverseTransformDirection( transformedNormal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vReflect = reflect( cameraToVertex, worldNormal );
		#else
			vReflect = refract( cameraToVertex, worldNormal, refractionRatio );
		#endif
	#endif
#endif`,MA=`#ifdef USE_FOG
	vFogDepth = - mvPosition.z;
#endif`,EA=`#ifdef USE_FOG
	varying float vFogDepth;
#endif`,TA=`#ifdef USE_FOG
	#ifdef FOG_EXP2
		float fogFactor = 1.0 - exp( - fogDensity * fogDensity * vFogDepth * vFogDepth );
	#else
		float fogFactor = smoothstep( fogNear, fogFar, vFogDepth );
	#endif
	gl_FragColor.rgb = mix( gl_FragColor.rgb, fogColor, fogFactor );
#endif`,bA=`#ifdef USE_FOG
	uniform vec3 fogColor;
	varying float vFogDepth;
	#ifdef FOG_EXP2
		uniform float fogDensity;
	#else
		uniform float fogNear;
		uniform float fogFar;
	#endif
#endif`,AA=`#ifdef USE_GRADIENTMAP
	uniform sampler2D gradientMap;
#endif
vec3 getGradientIrradiance( vec3 normal, vec3 lightDirection ) {
	float dotNL = dot( normal, lightDirection );
	vec2 coord = vec2( dotNL * 0.5 + 0.5, 0.0 );
	#ifdef USE_GRADIENTMAP
		return vec3( texture2D( gradientMap, coord ).r );
	#else
		vec2 fw = fwidth( coord ) * 0.5;
		return mix( vec3( 0.7 ), vec3( 1.0 ), smoothstep( 0.7 - fw.x, 0.7 + fw.x, coord.x ) );
	#endif
}`,RA=`#ifdef USE_LIGHTMAP
	uniform sampler2D lightMap;
	uniform float lightMapIntensity;
#endif`,CA=`LambertMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularStrength = specularStrength;`,wA=`varying vec3 vViewPosition;
struct LambertMaterial {
	vec3 diffuseColor;
	float specularStrength;
};
void RE_Direct_Lambert( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Lambert( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Lambert
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Lambert`,DA=`uniform bool receiveShadow;
uniform vec3 ambientLightColor;
#if defined( USE_LIGHT_PROBES )
	uniform vec3 lightProbe[ 9 ];
#endif
vec3 shGetIrradianceAt( in vec3 normal, in vec3 shCoefficients[ 9 ] ) {
	float x = normal.x, y = normal.y, z = normal.z;
	vec3 result = shCoefficients[ 0 ] * 0.886227;
	result += shCoefficients[ 1 ] * 2.0 * 0.511664 * y;
	result += shCoefficients[ 2 ] * 2.0 * 0.511664 * z;
	result += shCoefficients[ 3 ] * 2.0 * 0.511664 * x;
	result += shCoefficients[ 4 ] * 2.0 * 0.429043 * x * y;
	result += shCoefficients[ 5 ] * 2.0 * 0.429043 * y * z;
	result += shCoefficients[ 6 ] * ( 0.743125 * z * z - 0.247708 );
	result += shCoefficients[ 7 ] * 2.0 * 0.429043 * x * z;
	result += shCoefficients[ 8 ] * 0.429043 * ( x * x - y * y );
	return result;
}
vec3 getLightProbeIrradiance( const in vec3 lightProbe[ 9 ], const in vec3 normal ) {
	vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
	vec3 irradiance = shGetIrradianceAt( worldNormal, lightProbe );
	return irradiance;
}
vec3 getAmbientLightIrradiance( const in vec3 ambientLightColor ) {
	vec3 irradiance = ambientLightColor;
	return irradiance;
}
float getDistanceAttenuation( const in float lightDistance, const in float cutoffDistance, const in float decayExponent ) {
	float distanceFalloff = 1.0 / max( pow( lightDistance, decayExponent ), 0.01 );
	if ( cutoffDistance > 0.0 ) {
		distanceFalloff *= pow2( saturate( 1.0 - pow4( lightDistance / cutoffDistance ) ) );
	}
	return distanceFalloff;
}
float getSpotAttenuation( const in float coneCosine, const in float penumbraCosine, const in float angleCosine ) {
	return smoothstep( coneCosine, penumbraCosine, angleCosine );
}
#if NUM_DIR_LIGHTS > 0
	struct DirectionalLight {
		vec3 direction;
		vec3 color;
	};
	uniform DirectionalLight directionalLights[ NUM_DIR_LIGHTS ];
	void getDirectionalLightInfo( const in DirectionalLight directionalLight, out IncidentLight light ) {
		light.color = directionalLight.color;
		light.direction = directionalLight.direction;
		light.visible = true;
	}
#endif
#if NUM_POINT_LIGHTS > 0
	struct PointLight {
		vec3 position;
		vec3 color;
		float distance;
		float decay;
	};
	uniform PointLight pointLights[ NUM_POINT_LIGHTS ];
	void getPointLightInfo( const in PointLight pointLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = pointLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float lightDistance = length( lVector );
		light.color = pointLight.color;
		light.color *= getDistanceAttenuation( lightDistance, pointLight.distance, pointLight.decay );
		light.visible = ( light.color != vec3( 0.0 ) );
	}
#endif
#if NUM_SPOT_LIGHTS > 0
	struct SpotLight {
		vec3 position;
		vec3 direction;
		vec3 color;
		float distance;
		float decay;
		float coneCos;
		float penumbraCos;
	};
	uniform SpotLight spotLights[ NUM_SPOT_LIGHTS ];
	void getSpotLightInfo( const in SpotLight spotLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = spotLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float angleCos = dot( light.direction, spotLight.direction );
		float spotAttenuation = getSpotAttenuation( spotLight.coneCos, spotLight.penumbraCos, angleCos );
		if ( spotAttenuation > 0.0 ) {
			float lightDistance = length( lVector );
			light.color = spotLight.color * spotAttenuation;
			light.color *= getDistanceAttenuation( lightDistance, spotLight.distance, spotLight.decay );
			light.visible = ( light.color != vec3( 0.0 ) );
		} else {
			light.color = vec3( 0.0 );
			light.visible = false;
		}
	}
#endif
#if NUM_RECT_AREA_LIGHTS > 0
	struct RectAreaLight {
		vec3 color;
		vec3 position;
		vec3 halfWidth;
		vec3 halfHeight;
	};
	uniform sampler2D ltc_1;	uniform sampler2D ltc_2;
	uniform RectAreaLight rectAreaLights[ NUM_RECT_AREA_LIGHTS ];
#endif
#if NUM_HEMI_LIGHTS > 0
	struct HemisphereLight {
		vec3 direction;
		vec3 skyColor;
		vec3 groundColor;
	};
	uniform HemisphereLight hemisphereLights[ NUM_HEMI_LIGHTS ];
	vec3 getHemisphereLightIrradiance( const in HemisphereLight hemiLight, const in vec3 normal ) {
		float dotNL = dot( normal, hemiLight.direction );
		float hemiDiffuseWeight = 0.5 * dotNL + 0.5;
		vec3 irradiance = mix( hemiLight.groundColor, hemiLight.skyColor, hemiDiffuseWeight );
		return irradiance;
	}
#endif`,UA=`#ifdef USE_ENVMAP
	vec3 getIBLIrradiance( const in vec3 normal ) {
		#ifdef ENVMAP_TYPE_CUBE_UV
			vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
			vec4 envMapColor = textureCubeUV( envMap, envMapRotation * worldNormal, 1.0 );
			return PI * envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	vec3 getIBLRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness ) {
		#ifdef ENVMAP_TYPE_CUBE_UV
			vec3 reflectVec = reflect( - viewDir, normal );
			reflectVec = normalize( mix( reflectVec, normal, roughness * roughness) );
			reflectVec = inverseTransformDirection( reflectVec, viewMatrix );
			vec4 envMapColor = textureCubeUV( envMap, envMapRotation * reflectVec, roughness );
			return envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	#ifdef USE_ANISOTROPY
		vec3 getIBLAnisotropyRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness, const in vec3 bitangent, const in float anisotropy ) {
			#ifdef ENVMAP_TYPE_CUBE_UV
				vec3 bentNormal = cross( bitangent, viewDir );
				bentNormal = normalize( cross( bentNormal, bitangent ) );
				bentNormal = normalize( mix( bentNormal, normal, pow2( pow2( 1.0 - anisotropy * ( 1.0 - roughness ) ) ) ) );
				return getIBLRadiance( viewDir, bentNormal, roughness );
			#else
				return vec3( 0.0 );
			#endif
		}
	#endif
#endif`,NA=`ToonMaterial material;
material.diffuseColor = diffuseColor.rgb;`,LA=`varying vec3 vViewPosition;
struct ToonMaterial {
	vec3 diffuseColor;
};
void RE_Direct_Toon( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	vec3 irradiance = getGradientIrradiance( geometryNormal, directLight.direction ) * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Toon( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Toon
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Toon`,OA=`BlinnPhongMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularColor = specular;
material.specularShininess = shininess;
material.specularStrength = specularStrength;`,PA=`varying vec3 vViewPosition;
struct BlinnPhongMaterial {
	vec3 diffuseColor;
	vec3 specularColor;
	float specularShininess;
	float specularStrength;
};
void RE_Direct_BlinnPhong( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
	reflectedLight.directSpecular += irradiance * BRDF_BlinnPhong( directLight.direction, geometryViewDir, geometryNormal, material.specularColor, material.specularShininess ) * material.specularStrength;
}
void RE_IndirectDiffuse_BlinnPhong( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_BlinnPhong
#define RE_IndirectDiffuse		RE_IndirectDiffuse_BlinnPhong`,zA=`PhysicalMaterial material;
material.diffuseColor = diffuseColor.rgb * ( 1.0 - metalnessFactor );
vec3 dxy = max( abs( dFdx( nonPerturbedNormal ) ), abs( dFdy( nonPerturbedNormal ) ) );
float geometryRoughness = max( max( dxy.x, dxy.y ), dxy.z );
material.roughness = max( roughnessFactor, 0.0525 );material.roughness += geometryRoughness;
material.roughness = min( material.roughness, 1.0 );
#ifdef IOR
	material.ior = ior;
	#ifdef USE_SPECULAR
		float specularIntensityFactor = specularIntensity;
		vec3 specularColorFactor = specularColor;
		#ifdef USE_SPECULAR_COLORMAP
			specularColorFactor *= texture2D( specularColorMap, vSpecularColorMapUv ).rgb;
		#endif
		#ifdef USE_SPECULAR_INTENSITYMAP
			specularIntensityFactor *= texture2D( specularIntensityMap, vSpecularIntensityMapUv ).a;
		#endif
		material.specularF90 = mix( specularIntensityFactor, 1.0, metalnessFactor );
	#else
		float specularIntensityFactor = 1.0;
		vec3 specularColorFactor = vec3( 1.0 );
		material.specularF90 = 1.0;
	#endif
	material.specularColor = mix( min( pow2( ( material.ior - 1.0 ) / ( material.ior + 1.0 ) ) * specularColorFactor, vec3( 1.0 ) ) * specularIntensityFactor, diffuseColor.rgb, metalnessFactor );
#else
	material.specularColor = mix( vec3( 0.04 ), diffuseColor.rgb, metalnessFactor );
	material.specularF90 = 1.0;
#endif
#ifdef USE_CLEARCOAT
	material.clearcoat = clearcoat;
	material.clearcoatRoughness = clearcoatRoughness;
	material.clearcoatF0 = vec3( 0.04 );
	material.clearcoatF90 = 1.0;
	#ifdef USE_CLEARCOATMAP
		material.clearcoat *= texture2D( clearcoatMap, vClearcoatMapUv ).x;
	#endif
	#ifdef USE_CLEARCOAT_ROUGHNESSMAP
		material.clearcoatRoughness *= texture2D( clearcoatRoughnessMap, vClearcoatRoughnessMapUv ).y;
	#endif
	material.clearcoat = saturate( material.clearcoat );	material.clearcoatRoughness = max( material.clearcoatRoughness, 0.0525 );
	material.clearcoatRoughness += geometryRoughness;
	material.clearcoatRoughness = min( material.clearcoatRoughness, 1.0 );
#endif
#ifdef USE_DISPERSION
	material.dispersion = dispersion;
#endif
#ifdef USE_IRIDESCENCE
	material.iridescence = iridescence;
	material.iridescenceIOR = iridescenceIOR;
	#ifdef USE_IRIDESCENCEMAP
		material.iridescence *= texture2D( iridescenceMap, vIridescenceMapUv ).r;
	#endif
	#ifdef USE_IRIDESCENCE_THICKNESSMAP
		material.iridescenceThickness = (iridescenceThicknessMaximum - iridescenceThicknessMinimum) * texture2D( iridescenceThicknessMap, vIridescenceThicknessMapUv ).g + iridescenceThicknessMinimum;
	#else
		material.iridescenceThickness = iridescenceThicknessMaximum;
	#endif
#endif
#ifdef USE_SHEEN
	material.sheenColor = sheenColor;
	#ifdef USE_SHEEN_COLORMAP
		material.sheenColor *= texture2D( sheenColorMap, vSheenColorMapUv ).rgb;
	#endif
	material.sheenRoughness = clamp( sheenRoughness, 0.07, 1.0 );
	#ifdef USE_SHEEN_ROUGHNESSMAP
		material.sheenRoughness *= texture2D( sheenRoughnessMap, vSheenRoughnessMapUv ).a;
	#endif
#endif
#ifdef USE_ANISOTROPY
	#ifdef USE_ANISOTROPYMAP
		mat2 anisotropyMat = mat2( anisotropyVector.x, anisotropyVector.y, - anisotropyVector.y, anisotropyVector.x );
		vec3 anisotropyPolar = texture2D( anisotropyMap, vAnisotropyMapUv ).rgb;
		vec2 anisotropyV = anisotropyMat * normalize( 2.0 * anisotropyPolar.rg - vec2( 1.0 ) ) * anisotropyPolar.b;
	#else
		vec2 anisotropyV = anisotropyVector;
	#endif
	material.anisotropy = length( anisotropyV );
	if( material.anisotropy == 0.0 ) {
		anisotropyV = vec2( 1.0, 0.0 );
	} else {
		anisotropyV /= material.anisotropy;
		material.anisotropy = saturate( material.anisotropy );
	}
	material.alphaT = mix( pow2( material.roughness ), 1.0, pow2( material.anisotropy ) );
	material.anisotropyT = tbn[ 0 ] * anisotropyV.x + tbn[ 1 ] * anisotropyV.y;
	material.anisotropyB = tbn[ 1 ] * anisotropyV.x - tbn[ 0 ] * anisotropyV.y;
#endif`,IA=`struct PhysicalMaterial {
	vec3 diffuseColor;
	float roughness;
	vec3 specularColor;
	float specularF90;
	float dispersion;
	#ifdef USE_CLEARCOAT
		float clearcoat;
		float clearcoatRoughness;
		vec3 clearcoatF0;
		float clearcoatF90;
	#endif
	#ifdef USE_IRIDESCENCE
		float iridescence;
		float iridescenceIOR;
		float iridescenceThickness;
		vec3 iridescenceFresnel;
		vec3 iridescenceF0;
	#endif
	#ifdef USE_SHEEN
		vec3 sheenColor;
		float sheenRoughness;
	#endif
	#ifdef IOR
		float ior;
	#endif
	#ifdef USE_TRANSMISSION
		float transmission;
		float transmissionAlpha;
		float thickness;
		float attenuationDistance;
		vec3 attenuationColor;
	#endif
	#ifdef USE_ANISOTROPY
		float anisotropy;
		float alphaT;
		vec3 anisotropyT;
		vec3 anisotropyB;
	#endif
};
vec3 clearcoatSpecularDirect = vec3( 0.0 );
vec3 clearcoatSpecularIndirect = vec3( 0.0 );
vec3 sheenSpecularDirect = vec3( 0.0 );
vec3 sheenSpecularIndirect = vec3(0.0 );
vec3 Schlick_to_F0( const in vec3 f, const in float f90, const in float dotVH ) {
    float x = clamp( 1.0 - dotVH, 0.0, 1.0 );
    float x2 = x * x;
    float x5 = clamp( x * x2 * x2, 0.0, 0.9999 );
    return ( f - vec3( f90 ) * x5 ) / ( 1.0 - x5 );
}
float V_GGX_SmithCorrelated( const in float alpha, const in float dotNL, const in float dotNV ) {
	float a2 = pow2( alpha );
	float gv = dotNL * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNV ) );
	float gl = dotNV * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNL ) );
	return 0.5 / max( gv + gl, EPSILON );
}
float D_GGX( const in float alpha, const in float dotNH ) {
	float a2 = pow2( alpha );
	float denom = pow2( dotNH ) * ( a2 - 1.0 ) + 1.0;
	return RECIPROCAL_PI * a2 / pow2( denom );
}
#ifdef USE_ANISOTROPY
	float V_GGX_SmithCorrelated_Anisotropic( const in float alphaT, const in float alphaB, const in float dotTV, const in float dotBV, const in float dotTL, const in float dotBL, const in float dotNV, const in float dotNL ) {
		float gv = dotNL * length( vec3( alphaT * dotTV, alphaB * dotBV, dotNV ) );
		float gl = dotNV * length( vec3( alphaT * dotTL, alphaB * dotBL, dotNL ) );
		float v = 0.5 / ( gv + gl );
		return saturate(v);
	}
	float D_GGX_Anisotropic( const in float alphaT, const in float alphaB, const in float dotNH, const in float dotTH, const in float dotBH ) {
		float a2 = alphaT * alphaB;
		highp vec3 v = vec3( alphaB * dotTH, alphaT * dotBH, a2 * dotNH );
		highp float v2 = dot( v, v );
		float w2 = a2 / v2;
		return RECIPROCAL_PI * a2 * pow2 ( w2 );
	}
#endif
#ifdef USE_CLEARCOAT
	vec3 BRDF_GGX_Clearcoat( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material) {
		vec3 f0 = material.clearcoatF0;
		float f90 = material.clearcoatF90;
		float roughness = material.clearcoatRoughness;
		float alpha = pow2( roughness );
		vec3 halfDir = normalize( lightDir + viewDir );
		float dotNL = saturate( dot( normal, lightDir ) );
		float dotNV = saturate( dot( normal, viewDir ) );
		float dotNH = saturate( dot( normal, halfDir ) );
		float dotVH = saturate( dot( viewDir, halfDir ) );
		vec3 F = F_Schlick( f0, f90, dotVH );
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
		return F * ( V * D );
	}
#endif
vec3 BRDF_GGX( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material ) {
	vec3 f0 = material.specularColor;
	float f90 = material.specularF90;
	float roughness = material.roughness;
	float alpha = pow2( roughness );
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( f0, f90, dotVH );
	#ifdef USE_IRIDESCENCE
		F = mix( F, material.iridescenceFresnel, material.iridescence );
	#endif
	#ifdef USE_ANISOTROPY
		float dotTL = dot( material.anisotropyT, lightDir );
		float dotTV = dot( material.anisotropyT, viewDir );
		float dotTH = dot( material.anisotropyT, halfDir );
		float dotBL = dot( material.anisotropyB, lightDir );
		float dotBV = dot( material.anisotropyB, viewDir );
		float dotBH = dot( material.anisotropyB, halfDir );
		float V = V_GGX_SmithCorrelated_Anisotropic( material.alphaT, alpha, dotTV, dotBV, dotTL, dotBL, dotNV, dotNL );
		float D = D_GGX_Anisotropic( material.alphaT, alpha, dotNH, dotTH, dotBH );
	#else
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
	#endif
	return F * ( V * D );
}
vec2 LTC_Uv( const in vec3 N, const in vec3 V, const in float roughness ) {
	const float LUT_SIZE = 64.0;
	const float LUT_SCALE = ( LUT_SIZE - 1.0 ) / LUT_SIZE;
	const float LUT_BIAS = 0.5 / LUT_SIZE;
	float dotNV = saturate( dot( N, V ) );
	vec2 uv = vec2( roughness, sqrt( 1.0 - dotNV ) );
	uv = uv * LUT_SCALE + LUT_BIAS;
	return uv;
}
float LTC_ClippedSphereFormFactor( const in vec3 f ) {
	float l = length( f );
	return max( ( l * l + f.z ) / ( l + 1.0 ), 0.0 );
}
vec3 LTC_EdgeVectorFormFactor( const in vec3 v1, const in vec3 v2 ) {
	float x = dot( v1, v2 );
	float y = abs( x );
	float a = 0.8543985 + ( 0.4965155 + 0.0145206 * y ) * y;
	float b = 3.4175940 + ( 4.1616724 + y ) * y;
	float v = a / b;
	float theta_sintheta = ( x > 0.0 ) ? v : 0.5 * inversesqrt( max( 1.0 - x * x, 1e-7 ) ) - v;
	return cross( v1, v2 ) * theta_sintheta;
}
vec3 LTC_Evaluate( const in vec3 N, const in vec3 V, const in vec3 P, const in mat3 mInv, const in vec3 rectCoords[ 4 ] ) {
	vec3 v1 = rectCoords[ 1 ] - rectCoords[ 0 ];
	vec3 v2 = rectCoords[ 3 ] - rectCoords[ 0 ];
	vec3 lightNormal = cross( v1, v2 );
	if( dot( lightNormal, P - rectCoords[ 0 ] ) < 0.0 ) return vec3( 0.0 );
	vec3 T1, T2;
	T1 = normalize( V - N * dot( V, N ) );
	T2 = - cross( N, T1 );
	mat3 mat = mInv * transposeMat3( mat3( T1, T2, N ) );
	vec3 coords[ 4 ];
	coords[ 0 ] = mat * ( rectCoords[ 0 ] - P );
	coords[ 1 ] = mat * ( rectCoords[ 1 ] - P );
	coords[ 2 ] = mat * ( rectCoords[ 2 ] - P );
	coords[ 3 ] = mat * ( rectCoords[ 3 ] - P );
	coords[ 0 ] = normalize( coords[ 0 ] );
	coords[ 1 ] = normalize( coords[ 1 ] );
	coords[ 2 ] = normalize( coords[ 2 ] );
	coords[ 3 ] = normalize( coords[ 3 ] );
	vec3 vectorFormFactor = vec3( 0.0 );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 0 ], coords[ 1 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 1 ], coords[ 2 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 2 ], coords[ 3 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 3 ], coords[ 0 ] );
	float result = LTC_ClippedSphereFormFactor( vectorFormFactor );
	return vec3( result );
}
#if defined( USE_SHEEN )
float D_Charlie( float roughness, float dotNH ) {
	float alpha = pow2( roughness );
	float invAlpha = 1.0 / alpha;
	float cos2h = dotNH * dotNH;
	float sin2h = max( 1.0 - cos2h, 0.0078125 );
	return ( 2.0 + invAlpha ) * pow( sin2h, invAlpha * 0.5 ) / ( 2.0 * PI );
}
float V_Neubelt( float dotNV, float dotNL ) {
	return saturate( 1.0 / ( 4.0 * ( dotNL + dotNV - dotNL * dotNV ) ) );
}
vec3 BRDF_Sheen( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, vec3 sheenColor, const in float sheenRoughness ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float D = D_Charlie( sheenRoughness, dotNH );
	float V = V_Neubelt( dotNV, dotNL );
	return sheenColor * ( D * V );
}
#endif
float IBLSheenBRDF( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	float r2 = roughness * roughness;
	float a = roughness < 0.25 ? -339.2 * r2 + 161.4 * roughness - 25.9 : -8.48 * r2 + 14.3 * roughness - 9.95;
	float b = roughness < 0.25 ? 44.0 * r2 - 23.7 * roughness + 3.26 : 1.97 * r2 - 3.27 * roughness + 0.72;
	float DG = exp( a * dotNV + b ) + ( roughness < 0.25 ? 0.0 : 0.1 * ( roughness - 0.25 ) );
	return saturate( DG * RECIPROCAL_PI );
}
vec2 DFGApprox( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	const vec4 c0 = vec4( - 1, - 0.0275, - 0.572, 0.022 );
	const vec4 c1 = vec4( 1, 0.0425, 1.04, - 0.04 );
	vec4 r = roughness * c0 + c1;
	float a004 = min( r.x * r.x, exp2( - 9.28 * dotNV ) ) * r.x + r.y;
	vec2 fab = vec2( - 1.04, 1.04 ) * a004 + r.zw;
	return fab;
}
vec3 EnvironmentBRDF( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness ) {
	vec2 fab = DFGApprox( normal, viewDir, roughness );
	return specularColor * fab.x + specularF90 * fab.y;
}
#ifdef USE_IRIDESCENCE
void computeMultiscatteringIridescence( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float iridescence, const in vec3 iridescenceF0, const in float roughness, inout vec3 singleScatter, inout vec3 multiScatter ) {
#else
void computeMultiscattering( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness, inout vec3 singleScatter, inout vec3 multiScatter ) {
#endif
	vec2 fab = DFGApprox( normal, viewDir, roughness );
	#ifdef USE_IRIDESCENCE
		vec3 Fr = mix( specularColor, iridescenceF0, iridescence );
	#else
		vec3 Fr = specularColor;
	#endif
	vec3 FssEss = Fr * fab.x + specularF90 * fab.y;
	float Ess = fab.x + fab.y;
	float Ems = 1.0 - Ess;
	vec3 Favg = Fr + ( 1.0 - Fr ) * 0.047619;	vec3 Fms = FssEss * Favg / ( 1.0 - Ems * Favg );
	singleScatter += FssEss;
	multiScatter += Fms * Ems;
}
#if NUM_RECT_AREA_LIGHTS > 0
	void RE_Direct_RectArea_Physical( const in RectAreaLight rectAreaLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
		vec3 normal = geometryNormal;
		vec3 viewDir = geometryViewDir;
		vec3 position = geometryPosition;
		vec3 lightPos = rectAreaLight.position;
		vec3 halfWidth = rectAreaLight.halfWidth;
		vec3 halfHeight = rectAreaLight.halfHeight;
		vec3 lightColor = rectAreaLight.color;
		float roughness = material.roughness;
		vec3 rectCoords[ 4 ];
		rectCoords[ 0 ] = lightPos + halfWidth - halfHeight;		rectCoords[ 1 ] = lightPos - halfWidth - halfHeight;
		rectCoords[ 2 ] = lightPos - halfWidth + halfHeight;
		rectCoords[ 3 ] = lightPos + halfWidth + halfHeight;
		vec2 uv = LTC_Uv( normal, viewDir, roughness );
		vec4 t1 = texture2D( ltc_1, uv );
		vec4 t2 = texture2D( ltc_2, uv );
		mat3 mInv = mat3(
			vec3( t1.x, 0, t1.y ),
			vec3(    0, 1,    0 ),
			vec3( t1.z, 0, t1.w )
		);
		vec3 fresnel = ( material.specularColor * t2.x + ( vec3( 1.0 ) - material.specularColor ) * t2.y );
		reflectedLight.directSpecular += lightColor * fresnel * LTC_Evaluate( normal, viewDir, position, mInv, rectCoords );
		reflectedLight.directDiffuse += lightColor * material.diffuseColor * LTC_Evaluate( normal, viewDir, position, mat3( 1.0 ), rectCoords );
	}
#endif
void RE_Direct_Physical( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	#ifdef USE_CLEARCOAT
		float dotNLcc = saturate( dot( geometryClearcoatNormal, directLight.direction ) );
		vec3 ccIrradiance = dotNLcc * directLight.color;
		clearcoatSpecularDirect += ccIrradiance * BRDF_GGX_Clearcoat( directLight.direction, geometryViewDir, geometryClearcoatNormal, material );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularDirect += irradiance * BRDF_Sheen( directLight.direction, geometryViewDir, geometryNormal, material.sheenColor, material.sheenRoughness );
	#endif
	reflectedLight.directSpecular += irradiance * BRDF_GGX( directLight.direction, geometryViewDir, geometryNormal, material );
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Physical( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectSpecular_Physical( const in vec3 radiance, const in vec3 irradiance, const in vec3 clearcoatRadiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight) {
	#ifdef USE_CLEARCOAT
		clearcoatSpecularIndirect += clearcoatRadiance * EnvironmentBRDF( geometryClearcoatNormal, geometryViewDir, material.clearcoatF0, material.clearcoatF90, material.clearcoatRoughness );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularIndirect += irradiance * material.sheenColor * IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness );
	#endif
	vec3 singleScattering = vec3( 0.0 );
	vec3 multiScattering = vec3( 0.0 );
	vec3 cosineWeightedIrradiance = irradiance * RECIPROCAL_PI;
	#ifdef USE_IRIDESCENCE
		computeMultiscatteringIridescence( geometryNormal, geometryViewDir, material.specularColor, material.specularF90, material.iridescence, material.iridescenceFresnel, material.roughness, singleScattering, multiScattering );
	#else
		computeMultiscattering( geometryNormal, geometryViewDir, material.specularColor, material.specularF90, material.roughness, singleScattering, multiScattering );
	#endif
	vec3 totalScattering = singleScattering + multiScattering;
	vec3 diffuse = material.diffuseColor * ( 1.0 - max( max( totalScattering.r, totalScattering.g ), totalScattering.b ) );
	reflectedLight.indirectSpecular += radiance * singleScattering;
	reflectedLight.indirectSpecular += multiScattering * cosineWeightedIrradiance;
	reflectedLight.indirectDiffuse += diffuse * cosineWeightedIrradiance;
}
#define RE_Direct				RE_Direct_Physical
#define RE_Direct_RectArea		RE_Direct_RectArea_Physical
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Physical
#define RE_IndirectSpecular		RE_IndirectSpecular_Physical
float computeSpecularOcclusion( const in float dotNV, const in float ambientOcclusion, const in float roughness ) {
	return saturate( pow( dotNV + ambientOcclusion, exp2( - 16.0 * roughness - 1.0 ) ) - 1.0 + ambientOcclusion );
}`,BA=`
vec3 geometryPosition = - vViewPosition;
vec3 geometryNormal = normal;
vec3 geometryViewDir = ( isOrthographic ) ? vec3( 0, 0, 1 ) : normalize( vViewPosition );
vec3 geometryClearcoatNormal = vec3( 0.0 );
#ifdef USE_CLEARCOAT
	geometryClearcoatNormal = clearcoatNormal;
#endif
#ifdef USE_IRIDESCENCE
	float dotNVi = saturate( dot( normal, geometryViewDir ) );
	if ( material.iridescenceThickness == 0.0 ) {
		material.iridescence = 0.0;
	} else {
		material.iridescence = saturate( material.iridescence );
	}
	if ( material.iridescence > 0.0 ) {
		material.iridescenceFresnel = evalIridescence( 1.0, material.iridescenceIOR, dotNVi, material.iridescenceThickness, material.specularColor );
		material.iridescenceF0 = Schlick_to_F0( material.iridescenceFresnel, 1.0, dotNVi );
	}
#endif
IncidentLight directLight;
#if ( NUM_POINT_LIGHTS > 0 ) && defined( RE_Direct )
	PointLight pointLight;
	#if defined( USE_SHADOWMAP ) && NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHTS; i ++ ) {
		pointLight = pointLights[ i ];
		getPointLightInfo( pointLight, geometryPosition, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_POINT_LIGHT_SHADOWS )
		pointLightShadow = pointLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getPointShadow( pointShadowMap[ i ], pointLightShadow.shadowMapSize, pointLightShadow.shadowIntensity, pointLightShadow.shadowBias, pointLightShadow.shadowRadius, vPointShadowCoord[ i ], pointLightShadow.shadowCameraNear, pointLightShadow.shadowCameraFar ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_SPOT_LIGHTS > 0 ) && defined( RE_Direct )
	SpotLight spotLight;
	vec4 spotColor;
	vec3 spotLightCoord;
	bool inSpotLightMap;
	#if defined( USE_SHADOWMAP ) && NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHTS; i ++ ) {
		spotLight = spotLights[ i ];
		getSpotLightInfo( spotLight, geometryPosition, directLight );
		#if ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#define SPOT_LIGHT_MAP_INDEX UNROLLED_LOOP_INDEX
		#elif ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		#define SPOT_LIGHT_MAP_INDEX NUM_SPOT_LIGHT_MAPS
		#else
		#define SPOT_LIGHT_MAP_INDEX ( UNROLLED_LOOP_INDEX - NUM_SPOT_LIGHT_SHADOWS + NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#endif
		#if ( SPOT_LIGHT_MAP_INDEX < NUM_SPOT_LIGHT_MAPS )
			spotLightCoord = vSpotLightCoord[ i ].xyz / vSpotLightCoord[ i ].w;
			inSpotLightMap = all( lessThan( abs( spotLightCoord * 2. - 1. ), vec3( 1.0 ) ) );
			spotColor = texture2D( spotLightMap[ SPOT_LIGHT_MAP_INDEX ], spotLightCoord.xy );
			directLight.color = inSpotLightMap ? directLight.color * spotColor.rgb : directLight.color;
		#endif
		#undef SPOT_LIGHT_MAP_INDEX
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		spotLightShadow = spotLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( spotShadowMap[ i ], spotLightShadow.shadowMapSize, spotLightShadow.shadowIntensity, spotLightShadow.shadowBias, spotLightShadow.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_DIR_LIGHTS > 0 ) && defined( RE_Direct )
	DirectionalLight directionalLight;
	#if defined( USE_SHADOWMAP ) && NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHTS; i ++ ) {
		directionalLight = directionalLights[ i ];
		getDirectionalLightInfo( directionalLight, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_DIR_LIGHT_SHADOWS )
		directionalLightShadow = directionalLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( directionalShadowMap[ i ], directionalLightShadow.shadowMapSize, directionalLightShadow.shadowIntensity, directionalLightShadow.shadowBias, directionalLightShadow.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_RECT_AREA_LIGHTS > 0 ) && defined( RE_Direct_RectArea )
	RectAreaLight rectAreaLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_RECT_AREA_LIGHTS; i ++ ) {
		rectAreaLight = rectAreaLights[ i ];
		RE_Direct_RectArea( rectAreaLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if defined( RE_IndirectDiffuse )
	vec3 iblIrradiance = vec3( 0.0 );
	vec3 irradiance = getAmbientLightIrradiance( ambientLightColor );
	#if defined( USE_LIGHT_PROBES )
		irradiance += getLightProbeIrradiance( lightProbe, geometryNormal );
	#endif
	#if ( NUM_HEMI_LIGHTS > 0 )
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_HEMI_LIGHTS; i ++ ) {
			irradiance += getHemisphereLightIrradiance( hemisphereLights[ i ], geometryNormal );
		}
		#pragma unroll_loop_end
	#endif
#endif
#if defined( RE_IndirectSpecular )
	vec3 radiance = vec3( 0.0 );
	vec3 clearcoatRadiance = vec3( 0.0 );
#endif`,FA=`#if defined( RE_IndirectDiffuse )
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		vec3 lightMapIrradiance = lightMapTexel.rgb * lightMapIntensity;
		irradiance += lightMapIrradiance;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD ) && defined( ENVMAP_TYPE_CUBE_UV )
		iblIrradiance += getIBLIrradiance( geometryNormal );
	#endif
#endif
#if defined( USE_ENVMAP ) && defined( RE_IndirectSpecular )
	#ifdef USE_ANISOTROPY
		radiance += getIBLAnisotropyRadiance( geometryViewDir, geometryNormal, material.roughness, material.anisotropyB, material.anisotropy );
	#else
		radiance += getIBLRadiance( geometryViewDir, geometryNormal, material.roughness );
	#endif
	#ifdef USE_CLEARCOAT
		clearcoatRadiance += getIBLRadiance( geometryViewDir, geometryClearcoatNormal, material.clearcoatRoughness );
	#endif
#endif`,HA=`#if defined( RE_IndirectDiffuse )
	RE_IndirectDiffuse( irradiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif
#if defined( RE_IndirectSpecular )
	RE_IndirectSpecular( radiance, iblIrradiance, clearcoatRadiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif`,GA=`#if defined( USE_LOGDEPTHBUF )
	gl_FragDepth = vIsPerspective == 0.0 ? gl_FragCoord.z : log2( vFragDepth ) * logDepthBufFC * 0.5;
#endif`,VA=`#if defined( USE_LOGDEPTHBUF )
	uniform float logDepthBufFC;
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,XA=`#ifdef USE_LOGDEPTHBUF
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,kA=`#ifdef USE_LOGDEPTHBUF
	vFragDepth = 1.0 + gl_Position.w;
	vIsPerspective = float( isPerspectiveMatrix( projectionMatrix ) );
#endif`,YA=`#ifdef USE_MAP
	vec4 sampledDiffuseColor = texture2D( map, vMapUv );
	#ifdef DECODE_VIDEO_TEXTURE
		sampledDiffuseColor = vec4( mix( pow( sampledDiffuseColor.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), sampledDiffuseColor.rgb * 0.0773993808, vec3( lessThanEqual( sampledDiffuseColor.rgb, vec3( 0.04045 ) ) ) ), sampledDiffuseColor.w );
	
	#endif
	diffuseColor *= sampledDiffuseColor;
#endif`,qA=`#ifdef USE_MAP
	uniform sampler2D map;
#endif`,WA=`#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
	#if defined( USE_POINTS_UV )
		vec2 uv = vUv;
	#else
		vec2 uv = ( uvTransform * vec3( gl_PointCoord.x, 1.0 - gl_PointCoord.y, 1 ) ).xy;
	#endif
#endif
#ifdef USE_MAP
	diffuseColor *= texture2D( map, uv );
#endif
#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, uv ).g;
#endif`,jA=`#if defined( USE_POINTS_UV )
	varying vec2 vUv;
#else
	#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
		uniform mat3 uvTransform;
	#endif
#endif
#ifdef USE_MAP
	uniform sampler2D map;
#endif
#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,ZA=`float metalnessFactor = metalness;
#ifdef USE_METALNESSMAP
	vec4 texelMetalness = texture2D( metalnessMap, vMetalnessMapUv );
	metalnessFactor *= texelMetalness.b;
#endif`,KA=`#ifdef USE_METALNESSMAP
	uniform sampler2D metalnessMap;
#endif`,QA=`#ifdef USE_INSTANCING_MORPH
	float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	float morphTargetBaseInfluence = texelFetch( morphTexture, ivec2( 0, gl_InstanceID ), 0 ).r;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		morphTargetInfluences[i] =  texelFetch( morphTexture, ivec2( i + 1, gl_InstanceID ), 0 ).r;
	}
#endif`,JA=`#if defined( USE_MORPHCOLORS )
	vColor *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		#if defined( USE_COLOR_ALPHA )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ) * morphTargetInfluences[ i ];
		#elif defined( USE_COLOR )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ).rgb * morphTargetInfluences[ i ];
		#endif
	}
#endif`,$A=`#ifdef USE_MORPHNORMALS
	objectNormal *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) objectNormal += getMorph( gl_VertexID, i, 1 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,tR=`#ifdef USE_MORPHTARGETS
	#ifndef USE_INSTANCING_MORPH
		uniform float morphTargetBaseInfluence;
		uniform float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	#endif
	uniform sampler2DArray morphTargetsTexture;
	uniform ivec2 morphTargetsTextureSize;
	vec4 getMorph( const in int vertexIndex, const in int morphTargetIndex, const in int offset ) {
		int texelIndex = vertexIndex * MORPHTARGETS_TEXTURE_STRIDE + offset;
		int y = texelIndex / morphTargetsTextureSize.x;
		int x = texelIndex - y * morphTargetsTextureSize.x;
		ivec3 morphUV = ivec3( x, y, morphTargetIndex );
		return texelFetch( morphTargetsTexture, morphUV, 0 );
	}
#endif`,eR=`#ifdef USE_MORPHTARGETS
	transformed *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) transformed += getMorph( gl_VertexID, i, 0 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,nR=`float faceDirection = gl_FrontFacing ? 1.0 : - 1.0;
#ifdef FLAT_SHADED
	vec3 fdx = dFdx( vViewPosition );
	vec3 fdy = dFdy( vViewPosition );
	vec3 normal = normalize( cross( fdx, fdy ) );
#else
	vec3 normal = normalize( vNormal );
	#ifdef DOUBLE_SIDED
		normal *= faceDirection;
	#endif
#endif
#if defined( USE_NORMALMAP_TANGENTSPACE ) || defined( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY )
	#ifdef USE_TANGENT
		mat3 tbn = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn = getTangentFrame( - vViewPosition, normal,
		#if defined( USE_NORMALMAP )
			vNormalMapUv
		#elif defined( USE_CLEARCOAT_NORMALMAP )
			vClearcoatNormalMapUv
		#else
			vUv
		#endif
		);
	#endif
	#if defined( DOUBLE_SIDED ) && ! defined( FLAT_SHADED )
		tbn[0] *= faceDirection;
		tbn[1] *= faceDirection;
	#endif
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	#ifdef USE_TANGENT
		mat3 tbn2 = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn2 = getTangentFrame( - vViewPosition, normal, vClearcoatNormalMapUv );
	#endif
	#if defined( DOUBLE_SIDED ) && ! defined( FLAT_SHADED )
		tbn2[0] *= faceDirection;
		tbn2[1] *= faceDirection;
	#endif
#endif
vec3 nonPerturbedNormal = normal;`,iR=`#ifdef USE_NORMALMAP_OBJECTSPACE
	normal = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	#ifdef FLIP_SIDED
		normal = - normal;
	#endif
	#ifdef DOUBLE_SIDED
		normal = normal * faceDirection;
	#endif
	normal = normalize( normalMatrix * normal );
#elif defined( USE_NORMALMAP_TANGENTSPACE )
	vec3 mapN = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	mapN.xy *= normalScale;
	normal = normalize( tbn * mapN );
#elif defined( USE_BUMPMAP )
	normal = perturbNormalArb( - vViewPosition, normal, dHdxy_fwd(), faceDirection );
#endif`,aR=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,sR=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,rR=`#ifndef FLAT_SHADED
	vNormal = normalize( transformedNormal );
	#ifdef USE_TANGENT
		vTangent = normalize( transformedTangent );
		vBitangent = normalize( cross( vNormal, vTangent ) * tangent.w );
	#endif
#endif`,oR=`#ifdef USE_NORMALMAP
	uniform sampler2D normalMap;
	uniform vec2 normalScale;
#endif
#ifdef USE_NORMALMAP_OBJECTSPACE
	uniform mat3 normalMatrix;
#endif
#if ! defined ( USE_TANGENT ) && ( defined ( USE_NORMALMAP_TANGENTSPACE ) || defined ( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY ) )
	mat3 getTangentFrame( vec3 eye_pos, vec3 surf_norm, vec2 uv ) {
		vec3 q0 = dFdx( eye_pos.xyz );
		vec3 q1 = dFdy( eye_pos.xyz );
		vec2 st0 = dFdx( uv.st );
		vec2 st1 = dFdy( uv.st );
		vec3 N = surf_norm;
		vec3 q1perp = cross( q1, N );
		vec3 q0perp = cross( N, q0 );
		vec3 T = q1perp * st0.x + q0perp * st1.x;
		vec3 B = q1perp * st0.y + q0perp * st1.y;
		float det = max( dot( T, T ), dot( B, B ) );
		float scale = ( det == 0.0 ) ? 0.0 : inversesqrt( det );
		return mat3( T * scale, B * scale, N );
	}
#endif`,lR=`#ifdef USE_CLEARCOAT
	vec3 clearcoatNormal = nonPerturbedNormal;
#endif`,uR=`#ifdef USE_CLEARCOAT_NORMALMAP
	vec3 clearcoatMapN = texture2D( clearcoatNormalMap, vClearcoatNormalMapUv ).xyz * 2.0 - 1.0;
	clearcoatMapN.xy *= clearcoatNormalScale;
	clearcoatNormal = normalize( tbn2 * clearcoatMapN );
#endif`,cR=`#ifdef USE_CLEARCOATMAP
	uniform sampler2D clearcoatMap;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform sampler2D clearcoatNormalMap;
	uniform vec2 clearcoatNormalScale;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform sampler2D clearcoatRoughnessMap;
#endif`,fR=`#ifdef USE_IRIDESCENCEMAP
	uniform sampler2D iridescenceMap;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform sampler2D iridescenceThicknessMap;
#endif`,hR=`#ifdef OPAQUE
diffuseColor.a = 1.0;
#endif
#ifdef USE_TRANSMISSION
diffuseColor.a *= material.transmissionAlpha;
#endif
gl_FragColor = vec4( outgoingLight, diffuseColor.a );`,dR=`vec3 packNormalToRGB( const in vec3 normal ) {
	return normalize( normal ) * 0.5 + 0.5;
}
vec3 unpackRGBToNormal( const in vec3 rgb ) {
	return 2.0 * rgb.xyz - 1.0;
}
const float PackUpscale = 256. / 255.;const float UnpackDownscale = 255. / 256.;const float ShiftRight8 = 1. / 256.;
const float Inv255 = 1. / 255.;
const vec4 PackFactors = vec4( 1.0, 256.0, 256.0 * 256.0, 256.0 * 256.0 * 256.0 );
const vec2 UnpackFactors2 = vec2( UnpackDownscale, 1.0 / PackFactors.g );
const vec3 UnpackFactors3 = vec3( UnpackDownscale / PackFactors.rg, 1.0 / PackFactors.b );
const vec4 UnpackFactors4 = vec4( UnpackDownscale / PackFactors.rgb, 1.0 / PackFactors.a );
vec4 packDepthToRGBA( const in float v ) {
	if( v <= 0.0 )
		return vec4( 0., 0., 0., 0. );
	if( v >= 1.0 )
		return vec4( 1., 1., 1., 1. );
	float vuf;
	float af = modf( v * PackFactors.a, vuf );
	float bf = modf( vuf * ShiftRight8, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec4( vuf * Inv255, gf * PackUpscale, bf * PackUpscale, af );
}
vec3 packDepthToRGB( const in float v ) {
	if( v <= 0.0 )
		return vec3( 0., 0., 0. );
	if( v >= 1.0 )
		return vec3( 1., 1., 1. );
	float vuf;
	float bf = modf( v * PackFactors.b, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec3( vuf * Inv255, gf * PackUpscale, bf );
}
vec2 packDepthToRG( const in float v ) {
	if( v <= 0.0 )
		return vec2( 0., 0. );
	if( v >= 1.0 )
		return vec2( 1., 1. );
	float vuf;
	float gf = modf( v * 256., vuf );
	return vec2( vuf * Inv255, gf );
}
float unpackRGBAToDepth( const in vec4 v ) {
	return dot( v, UnpackFactors4 );
}
float unpackRGBToDepth( const in vec3 v ) {
	return dot( v, UnpackFactors3 );
}
float unpackRGToDepth( const in vec2 v ) {
	return v.r * UnpackFactors2.r + v.g * UnpackFactors2.g;
}
vec4 pack2HalfToRGBA( const in vec2 v ) {
	vec4 r = vec4( v.x, fract( v.x * 255.0 ), v.y, fract( v.y * 255.0 ) );
	return vec4( r.x - r.y / 255.0, r.y, r.z - r.w / 255.0, r.w );
}
vec2 unpackRGBATo2Half( const in vec4 v ) {
	return vec2( v.x + ( v.y / 255.0 ), v.z + ( v.w / 255.0 ) );
}
float viewZToOrthographicDepth( const in float viewZ, const in float near, const in float far ) {
	return ( viewZ + near ) / ( near - far );
}
float orthographicDepthToViewZ( const in float depth, const in float near, const in float far ) {
	return depth * ( near - far ) - near;
}
float viewZToPerspectiveDepth( const in float viewZ, const in float near, const in float far ) {
	return ( ( near + viewZ ) * far ) / ( ( far - near ) * viewZ );
}
float perspectiveDepthToViewZ( const in float depth, const in float near, const in float far ) {
	return ( near * far ) / ( ( far - near ) * depth - far );
}`,pR=`#ifdef PREMULTIPLIED_ALPHA
	gl_FragColor.rgb *= gl_FragColor.a;
#endif`,mR=`vec4 mvPosition = vec4( transformed, 1.0 );
#ifdef USE_BATCHING
	mvPosition = batchingMatrix * mvPosition;
#endif
#ifdef USE_INSTANCING
	mvPosition = instanceMatrix * mvPosition;
#endif
mvPosition = modelViewMatrix * mvPosition;
gl_Position = projectionMatrix * mvPosition;`,_R=`#ifdef DITHERING
	gl_FragColor.rgb = dithering( gl_FragColor.rgb );
#endif`,gR=`#ifdef DITHERING
	vec3 dithering( vec3 color ) {
		float grid_position = rand( gl_FragCoord.xy );
		vec3 dither_shift_RGB = vec3( 0.25 / 255.0, -0.25 / 255.0, 0.25 / 255.0 );
		dither_shift_RGB = mix( 2.0 * dither_shift_RGB, -2.0 * dither_shift_RGB, grid_position );
		return color + dither_shift_RGB;
	}
#endif`,vR=`float roughnessFactor = roughness;
#ifdef USE_ROUGHNESSMAP
	vec4 texelRoughness = texture2D( roughnessMap, vRoughnessMapUv );
	roughnessFactor *= texelRoughness.g;
#endif`,SR=`#ifdef USE_ROUGHNESSMAP
	uniform sampler2D roughnessMap;
#endif`,yR=`#if NUM_SPOT_LIGHT_COORDS > 0
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#if NUM_SPOT_LIGHT_MAPS > 0
	uniform sampler2D spotLightMap[ NUM_SPOT_LIGHT_MAPS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform sampler2D directionalShadowMap[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		uniform sampler2D spotShadowMap[ NUM_SPOT_LIGHT_SHADOWS ];
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform sampler2D pointShadowMap[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
	float texture2DCompare( sampler2D depths, vec2 uv, float compare ) {
		return step( compare, unpackRGBAToDepth( texture2D( depths, uv ) ) );
	}
	vec2 texture2DDistribution( sampler2D shadow, vec2 uv ) {
		return unpackRGBATo2Half( texture2D( shadow, uv ) );
	}
	float VSMShadow (sampler2D shadow, vec2 uv, float compare ){
		float occlusion = 1.0;
		vec2 distribution = texture2DDistribution( shadow, uv );
		float hard_shadow = step( compare , distribution.x );
		if (hard_shadow != 1.0 ) {
			float distance = compare - distribution.x ;
			float variance = max( 0.00000, distribution.y * distribution.y );
			float softness_probability = variance / (variance + distance * distance );			softness_probability = clamp( ( softness_probability - 0.3 ) / ( 0.95 - 0.3 ), 0.0, 1.0 );			occlusion = clamp( max( hard_shadow, softness_probability ), 0.0, 1.0 );
		}
		return occlusion;
	}
	float getShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord ) {
		float shadow = 1.0;
		shadowCoord.xyz /= shadowCoord.w;
		shadowCoord.z += shadowBias;
		bool inFrustum = shadowCoord.x >= 0.0 && shadowCoord.x <= 1.0 && shadowCoord.y >= 0.0 && shadowCoord.y <= 1.0;
		bool frustumTest = inFrustum && shadowCoord.z <= 1.0;
		if ( frustumTest ) {
		#if defined( SHADOWMAP_TYPE_PCF )
			vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
			float dx0 = - texelSize.x * shadowRadius;
			float dy0 = - texelSize.y * shadowRadius;
			float dx1 = + texelSize.x * shadowRadius;
			float dy1 = + texelSize.y * shadowRadius;
			float dx2 = dx0 / 2.0;
			float dy2 = dy0 / 2.0;
			float dx3 = dx1 / 2.0;
			float dy3 = dy1 / 2.0;
			shadow = (
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy, shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, dy1 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy1 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, dy1 ), shadowCoord.z )
			) * ( 1.0 / 17.0 );
		#elif defined( SHADOWMAP_TYPE_PCF_SOFT )
			vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
			float dx = texelSize.x;
			float dy = texelSize.y;
			vec2 uv = shadowCoord.xy;
			vec2 f = fract( uv * shadowMapSize + 0.5 );
			uv -= f * texelSize;
			shadow = (
				texture2DCompare( shadowMap, uv, shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + vec2( dx, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + vec2( 0.0, dy ), shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + texelSize, shadowCoord.z ) +
				mix( texture2DCompare( shadowMap, uv + vec2( -dx, 0.0 ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, 0.0 ), shadowCoord.z ),
					 f.x ) +
				mix( texture2DCompare( shadowMap, uv + vec2( -dx, dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, dy ), shadowCoord.z ),
					 f.x ) +
				mix( texture2DCompare( shadowMap, uv + vec2( 0.0, -dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 0.0, 2.0 * dy ), shadowCoord.z ),
					 f.y ) +
				mix( texture2DCompare( shadowMap, uv + vec2( dx, -dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( dx, 2.0 * dy ), shadowCoord.z ),
					 f.y ) +
				mix( mix( texture2DCompare( shadowMap, uv + vec2( -dx, -dy ), shadowCoord.z ),
						  texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, -dy ), shadowCoord.z ),
						  f.x ),
					 mix( texture2DCompare( shadowMap, uv + vec2( -dx, 2.0 * dy ), shadowCoord.z ),
						  texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, 2.0 * dy ), shadowCoord.z ),
						  f.x ),
					 f.y )
			) * ( 1.0 / 9.0 );
		#elif defined( SHADOWMAP_TYPE_VSM )
			shadow = VSMShadow( shadowMap, shadowCoord.xy, shadowCoord.z );
		#else
			shadow = texture2DCompare( shadowMap, shadowCoord.xy, shadowCoord.z );
		#endif
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
	vec2 cubeToUV( vec3 v, float texelSizeY ) {
		vec3 absV = abs( v );
		float scaleToCube = 1.0 / max( absV.x, max( absV.y, absV.z ) );
		absV *= scaleToCube;
		v *= scaleToCube * ( 1.0 - 2.0 * texelSizeY );
		vec2 planar = v.xy;
		float almostATexel = 1.5 * texelSizeY;
		float almostOne = 1.0 - almostATexel;
		if ( absV.z >= almostOne ) {
			if ( v.z > 0.0 )
				planar.x = 4.0 - v.x;
		} else if ( absV.x >= almostOne ) {
			float signX = sign( v.x );
			planar.x = v.z * signX + 2.0 * signX;
		} else if ( absV.y >= almostOne ) {
			float signY = sign( v.y );
			planar.x = v.x + 2.0 * signY + 2.0;
			planar.y = v.z * signY - 2.0;
		}
		return vec2( 0.125, 0.25 ) * planar + vec2( 0.375, 0.75 );
	}
	float getPointShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord, float shadowCameraNear, float shadowCameraFar ) {
		float shadow = 1.0;
		vec3 lightToPosition = shadowCoord.xyz;
		
		float lightToPositionLength = length( lightToPosition );
		if ( lightToPositionLength - shadowCameraFar <= 0.0 && lightToPositionLength - shadowCameraNear >= 0.0 ) {
			float dp = ( lightToPositionLength - shadowCameraNear ) / ( shadowCameraFar - shadowCameraNear );			dp += shadowBias;
			vec3 bd3D = normalize( lightToPosition );
			vec2 texelSize = vec2( 1.0 ) / ( shadowMapSize * vec2( 4.0, 2.0 ) );
			#if defined( SHADOWMAP_TYPE_PCF ) || defined( SHADOWMAP_TYPE_PCF_SOFT ) || defined( SHADOWMAP_TYPE_VSM )
				vec2 offset = vec2( - 1, 1 ) * shadowRadius * texelSize.y;
				shadow = (
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xyy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yyy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xyx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yyx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xxy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yxy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xxx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yxx, texelSize.y ), dp )
				) * ( 1.0 / 9.0 );
			#else
				shadow = texture2DCompare( shadowMap, cubeToUV( bd3D, texelSize.y ), dp );
			#endif
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
#endif`,xR=`#if NUM_SPOT_LIGHT_COORDS > 0
	uniform mat4 spotLightMatrix[ NUM_SPOT_LIGHT_COORDS ];
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform mat4 directionalShadowMatrix[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform mat4 pointShadowMatrix[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
#endif`,MR=`#if ( defined( USE_SHADOWMAP ) && ( NUM_DIR_LIGHT_SHADOWS > 0 || NUM_POINT_LIGHT_SHADOWS > 0 ) ) || ( NUM_SPOT_LIGHT_COORDS > 0 )
	vec3 shadowWorldNormal = inverseTransformDirection( transformedNormal, viewMatrix );
	vec4 shadowWorldPosition;
#endif
#if defined( USE_SHADOWMAP )
	#if NUM_DIR_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * directionalLightShadows[ i ].shadowNormalBias, 0 );
			vDirectionalShadowCoord[ i ] = directionalShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * pointLightShadows[ i ].shadowNormalBias, 0 );
			vPointShadowCoord[ i ] = pointShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
#endif
#if NUM_SPOT_LIGHT_COORDS > 0
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_COORDS; i ++ ) {
		shadowWorldPosition = worldPosition;
		#if ( defined( USE_SHADOWMAP ) && UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
			shadowWorldPosition.xyz += shadowWorldNormal * spotLightShadows[ i ].shadowNormalBias;
		#endif
		vSpotLightCoord[ i ] = spotLightMatrix[ i ] * shadowWorldPosition;
	}
	#pragma unroll_loop_end
#endif`,ER=`float getShadowMask() {
	float shadow = 1.0;
	#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
		directionalLight = directionalLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( directionalShadowMap[ i ], directionalLight.shadowMapSize, directionalLight.shadowIntensity, directionalLight.shadowBias, directionalLight.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_SHADOWS; i ++ ) {
		spotLight = spotLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( spotShadowMap[ i ], spotLight.shadowMapSize, spotLight.shadowIntensity, spotLight.shadowBias, spotLight.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
		pointLight = pointLightShadows[ i ];
		shadow *= receiveShadow ? getPointShadow( pointShadowMap[ i ], pointLight.shadowMapSize, pointLight.shadowIntensity, pointLight.shadowBias, pointLight.shadowRadius, vPointShadowCoord[ i ], pointLight.shadowCameraNear, pointLight.shadowCameraFar ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#endif
	return shadow;
}`,TR=`#ifdef USE_SKINNING
	mat4 boneMatX = getBoneMatrix( skinIndex.x );
	mat4 boneMatY = getBoneMatrix( skinIndex.y );
	mat4 boneMatZ = getBoneMatrix( skinIndex.z );
	mat4 boneMatW = getBoneMatrix( skinIndex.w );
#endif`,bR=`#ifdef USE_SKINNING
	uniform mat4 bindMatrix;
	uniform mat4 bindMatrixInverse;
	uniform highp sampler2D boneTexture;
	mat4 getBoneMatrix( const in float i ) {
		int size = textureSize( boneTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( boneTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( boneTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( boneTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( boneTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
#endif`,AR=`#ifdef USE_SKINNING
	vec4 skinVertex = bindMatrix * vec4( transformed, 1.0 );
	vec4 skinned = vec4( 0.0 );
	skinned += boneMatX * skinVertex * skinWeight.x;
	skinned += boneMatY * skinVertex * skinWeight.y;
	skinned += boneMatZ * skinVertex * skinWeight.z;
	skinned += boneMatW * skinVertex * skinWeight.w;
	transformed = ( bindMatrixInverse * skinned ).xyz;
#endif`,RR=`#ifdef USE_SKINNING
	mat4 skinMatrix = mat4( 0.0 );
	skinMatrix += skinWeight.x * boneMatX;
	skinMatrix += skinWeight.y * boneMatY;
	skinMatrix += skinWeight.z * boneMatZ;
	skinMatrix += skinWeight.w * boneMatW;
	skinMatrix = bindMatrixInverse * skinMatrix * bindMatrix;
	objectNormal = vec4( skinMatrix * vec4( objectNormal, 0.0 ) ).xyz;
	#ifdef USE_TANGENT
		objectTangent = vec4( skinMatrix * vec4( objectTangent, 0.0 ) ).xyz;
	#endif
#endif`,CR=`float specularStrength;
#ifdef USE_SPECULARMAP
	vec4 texelSpecular = texture2D( specularMap, vSpecularMapUv );
	specularStrength = texelSpecular.r;
#else
	specularStrength = 1.0;
#endif`,wR=`#ifdef USE_SPECULARMAP
	uniform sampler2D specularMap;
#endif`,DR=`#if defined( TONE_MAPPING )
	gl_FragColor.rgb = toneMapping( gl_FragColor.rgb );
#endif`,UR=`#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
uniform float toneMappingExposure;
vec3 LinearToneMapping( vec3 color ) {
	return saturate( toneMappingExposure * color );
}
vec3 ReinhardToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	return saturate( color / ( vec3( 1.0 ) + color ) );
}
vec3 CineonToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	color = max( vec3( 0.0 ), color - 0.004 );
	return pow( ( color * ( 6.2 * color + 0.5 ) ) / ( color * ( 6.2 * color + 1.7 ) + 0.06 ), vec3( 2.2 ) );
}
vec3 RRTAndODTFit( vec3 v ) {
	vec3 a = v * ( v + 0.0245786 ) - 0.000090537;
	vec3 b = v * ( 0.983729 * v + 0.4329510 ) + 0.238081;
	return a / b;
}
vec3 ACESFilmicToneMapping( vec3 color ) {
	const mat3 ACESInputMat = mat3(
		vec3( 0.59719, 0.07600, 0.02840 ),		vec3( 0.35458, 0.90834, 0.13383 ),
		vec3( 0.04823, 0.01566, 0.83777 )
	);
	const mat3 ACESOutputMat = mat3(
		vec3(  1.60475, -0.10208, -0.00327 ),		vec3( -0.53108,  1.10813, -0.07276 ),
		vec3( -0.07367, -0.00605,  1.07602 )
	);
	color *= toneMappingExposure / 0.6;
	color = ACESInputMat * color;
	color = RRTAndODTFit( color );
	color = ACESOutputMat * color;
	return saturate( color );
}
const mat3 LINEAR_REC2020_TO_LINEAR_SRGB = mat3(
	vec3( 1.6605, - 0.1246, - 0.0182 ),
	vec3( - 0.5876, 1.1329, - 0.1006 ),
	vec3( - 0.0728, - 0.0083, 1.1187 )
);
const mat3 LINEAR_SRGB_TO_LINEAR_REC2020 = mat3(
	vec3( 0.6274, 0.0691, 0.0164 ),
	vec3( 0.3293, 0.9195, 0.0880 ),
	vec3( 0.0433, 0.0113, 0.8956 )
);
vec3 agxDefaultContrastApprox( vec3 x ) {
	vec3 x2 = x * x;
	vec3 x4 = x2 * x2;
	return + 15.5 * x4 * x2
		- 40.14 * x4 * x
		+ 31.96 * x4
		- 6.868 * x2 * x
		+ 0.4298 * x2
		+ 0.1191 * x
		- 0.00232;
}
vec3 AgXToneMapping( vec3 color ) {
	const mat3 AgXInsetMatrix = mat3(
		vec3( 0.856627153315983, 0.137318972929847, 0.11189821299995 ),
		vec3( 0.0951212405381588, 0.761241990602591, 0.0767994186031903 ),
		vec3( 0.0482516061458583, 0.101439036467562, 0.811302368396859 )
	);
	const mat3 AgXOutsetMatrix = mat3(
		vec3( 1.1271005818144368, - 0.1413297634984383, - 0.14132976349843826 ),
		vec3( - 0.11060664309660323, 1.157823702216272, - 0.11060664309660294 ),
		vec3( - 0.016493938717834573, - 0.016493938717834257, 1.2519364065950405 )
	);
	const float AgxMinEv = - 12.47393;	const float AgxMaxEv = 4.026069;
	color *= toneMappingExposure;
	color = LINEAR_SRGB_TO_LINEAR_REC2020 * color;
	color = AgXInsetMatrix * color;
	color = max( color, 1e-10 );	color = log2( color );
	color = ( color - AgxMinEv ) / ( AgxMaxEv - AgxMinEv );
	color = clamp( color, 0.0, 1.0 );
	color = agxDefaultContrastApprox( color );
	color = AgXOutsetMatrix * color;
	color = pow( max( vec3( 0.0 ), color ), vec3( 2.2 ) );
	color = LINEAR_REC2020_TO_LINEAR_SRGB * color;
	color = clamp( color, 0.0, 1.0 );
	return color;
}
vec3 NeutralToneMapping( vec3 color ) {
	const float StartCompression = 0.8 - 0.04;
	const float Desaturation = 0.15;
	color *= toneMappingExposure;
	float x = min( color.r, min( color.g, color.b ) );
	float offset = x < 0.08 ? x - 6.25 * x * x : 0.04;
	color -= offset;
	float peak = max( color.r, max( color.g, color.b ) );
	if ( peak < StartCompression ) return color;
	float d = 1. - StartCompression;
	float newPeak = 1. - d * d / ( peak + d - StartCompression );
	color *= newPeak / peak;
	float g = 1. - 1. / ( Desaturation * ( peak - newPeak ) + 1. );
	return mix( color, vec3( newPeak ), g );
}
vec3 CustomToneMapping( vec3 color ) { return color; }`,NR=`#ifdef USE_TRANSMISSION
	material.transmission = transmission;
	material.transmissionAlpha = 1.0;
	material.thickness = thickness;
	material.attenuationDistance = attenuationDistance;
	material.attenuationColor = attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		material.transmission *= texture2D( transmissionMap, vTransmissionMapUv ).r;
	#endif
	#ifdef USE_THICKNESSMAP
		material.thickness *= texture2D( thicknessMap, vThicknessMapUv ).g;
	#endif
	vec3 pos = vWorldPosition;
	vec3 v = normalize( cameraPosition - pos );
	vec3 n = inverseTransformDirection( normal, viewMatrix );
	vec4 transmitted = getIBLVolumeRefraction(
		n, v, material.roughness, material.diffuseColor, material.specularColor, material.specularF90,
		pos, modelMatrix, viewMatrix, projectionMatrix, material.dispersion, material.ior, material.thickness,
		material.attenuationColor, material.attenuationDistance );
	material.transmissionAlpha = mix( material.transmissionAlpha, transmitted.a, material.transmission );
	totalDiffuse = mix( totalDiffuse, transmitted.rgb, material.transmission );
#endif`,LR=`#ifdef USE_TRANSMISSION
	uniform float transmission;
	uniform float thickness;
	uniform float attenuationDistance;
	uniform vec3 attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		uniform sampler2D transmissionMap;
	#endif
	#ifdef USE_THICKNESSMAP
		uniform sampler2D thicknessMap;
	#endif
	uniform vec2 transmissionSamplerSize;
	uniform sampler2D transmissionSamplerMap;
	uniform mat4 modelMatrix;
	uniform mat4 projectionMatrix;
	varying vec3 vWorldPosition;
	float w0( float a ) {
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - a + 3.0 ) - 3.0 ) + 1.0 );
	}
	float w1( float a ) {
		return ( 1.0 / 6.0 ) * ( a *  a * ( 3.0 * a - 6.0 ) + 4.0 );
	}
	float w2( float a ){
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - 3.0 * a + 3.0 ) + 3.0 ) + 1.0 );
	}
	float w3( float a ) {
		return ( 1.0 / 6.0 ) * ( a * a * a );
	}
	float g0( float a ) {
		return w0( a ) + w1( a );
	}
	float g1( float a ) {
		return w2( a ) + w3( a );
	}
	float h0( float a ) {
		return - 1.0 + w1( a ) / ( w0( a ) + w1( a ) );
	}
	float h1( float a ) {
		return 1.0 + w3( a ) / ( w2( a ) + w3( a ) );
	}
	vec4 bicubic( sampler2D tex, vec2 uv, vec4 texelSize, float lod ) {
		uv = uv * texelSize.zw + 0.5;
		vec2 iuv = floor( uv );
		vec2 fuv = fract( uv );
		float g0x = g0( fuv.x );
		float g1x = g1( fuv.x );
		float h0x = h0( fuv.x );
		float h1x = h1( fuv.x );
		float h0y = h0( fuv.y );
		float h1y = h1( fuv.y );
		vec2 p0 = ( vec2( iuv.x + h0x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p1 = ( vec2( iuv.x + h1x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p2 = ( vec2( iuv.x + h0x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		vec2 p3 = ( vec2( iuv.x + h1x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		return g0( fuv.y ) * ( g0x * textureLod( tex, p0, lod ) + g1x * textureLod( tex, p1, lod ) ) +
			g1( fuv.y ) * ( g0x * textureLod( tex, p2, lod ) + g1x * textureLod( tex, p3, lod ) );
	}
	vec4 textureBicubic( sampler2D sampler, vec2 uv, float lod ) {
		vec2 fLodSize = vec2( textureSize( sampler, int( lod ) ) );
		vec2 cLodSize = vec2( textureSize( sampler, int( lod + 1.0 ) ) );
		vec2 fLodSizeInv = 1.0 / fLodSize;
		vec2 cLodSizeInv = 1.0 / cLodSize;
		vec4 fSample = bicubic( sampler, uv, vec4( fLodSizeInv, fLodSize ), floor( lod ) );
		vec4 cSample = bicubic( sampler, uv, vec4( cLodSizeInv, cLodSize ), ceil( lod ) );
		return mix( fSample, cSample, fract( lod ) );
	}
	vec3 getVolumeTransmissionRay( const in vec3 n, const in vec3 v, const in float thickness, const in float ior, const in mat4 modelMatrix ) {
		vec3 refractionVector = refract( - v, normalize( n ), 1.0 / ior );
		vec3 modelScale;
		modelScale.x = length( vec3( modelMatrix[ 0 ].xyz ) );
		modelScale.y = length( vec3( modelMatrix[ 1 ].xyz ) );
		modelScale.z = length( vec3( modelMatrix[ 2 ].xyz ) );
		return normalize( refractionVector ) * thickness * modelScale;
	}
	float applyIorToRoughness( const in float roughness, const in float ior ) {
		return roughness * clamp( ior * 2.0 - 2.0, 0.0, 1.0 );
	}
	vec4 getTransmissionSample( const in vec2 fragCoord, const in float roughness, const in float ior ) {
		float lod = log2( transmissionSamplerSize.x ) * applyIorToRoughness( roughness, ior );
		return textureBicubic( transmissionSamplerMap, fragCoord.xy, lod );
	}
	vec3 volumeAttenuation( const in float transmissionDistance, const in vec3 attenuationColor, const in float attenuationDistance ) {
		if ( isinf( attenuationDistance ) ) {
			return vec3( 1.0 );
		} else {
			vec3 attenuationCoefficient = -log( attenuationColor ) / attenuationDistance;
			vec3 transmittance = exp( - attenuationCoefficient * transmissionDistance );			return transmittance;
		}
	}
	vec4 getIBLVolumeRefraction( const in vec3 n, const in vec3 v, const in float roughness, const in vec3 diffuseColor,
		const in vec3 specularColor, const in float specularF90, const in vec3 position, const in mat4 modelMatrix,
		const in mat4 viewMatrix, const in mat4 projMatrix, const in float dispersion, const in float ior, const in float thickness,
		const in vec3 attenuationColor, const in float attenuationDistance ) {
		vec4 transmittedLight;
		vec3 transmittance;
		#ifdef USE_DISPERSION
			float halfSpread = ( ior - 1.0 ) * 0.025 * dispersion;
			vec3 iors = vec3( ior - halfSpread, ior, ior + halfSpread );
			for ( int i = 0; i < 3; i ++ ) {
				vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, iors[ i ], modelMatrix );
				vec3 refractedRayExit = position + transmissionRay;
		
				vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
				vec2 refractionCoords = ndcPos.xy / ndcPos.w;
				refractionCoords += 1.0;
				refractionCoords /= 2.0;
		
				vec4 transmissionSample = getTransmissionSample( refractionCoords, roughness, iors[ i ] );
				transmittedLight[ i ] = transmissionSample[ i ];
				transmittedLight.a += transmissionSample.a;
				transmittance[ i ] = diffuseColor[ i ] * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance )[ i ];
			}
			transmittedLight.a /= 3.0;
		
		#else
		
			vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, ior, modelMatrix );
			vec3 refractedRayExit = position + transmissionRay;
			vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
			vec2 refractionCoords = ndcPos.xy / ndcPos.w;
			refractionCoords += 1.0;
			refractionCoords /= 2.0;
			transmittedLight = getTransmissionSample( refractionCoords, roughness, ior );
			transmittance = diffuseColor * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance );
		
		#endif
		vec3 attenuatedColor = transmittance * transmittedLight.rgb;
		vec3 F = EnvironmentBRDF( n, v, specularColor, specularF90, roughness );
		float transmittanceFactor = ( transmittance.r + transmittance.g + transmittance.b ) / 3.0;
		return vec4( ( 1.0 - F ) * attenuatedColor, 1.0 - ( 1.0 - transmittedLight.a ) * transmittanceFactor );
	}
#endif`,OR=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_SPECULARMAP
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,PR=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	uniform mat3 mapTransform;
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	uniform mat3 alphaMapTransform;
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	uniform mat3 lightMapTransform;
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	uniform mat3 aoMapTransform;
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	uniform mat3 bumpMapTransform;
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	uniform mat3 normalMapTransform;
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_DISPLACEMENTMAP
	uniform mat3 displacementMapTransform;
	varying vec2 vDisplacementMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	uniform mat3 emissiveMapTransform;
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	uniform mat3 metalnessMapTransform;
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	uniform mat3 roughnessMapTransform;
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	uniform mat3 anisotropyMapTransform;
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	uniform mat3 clearcoatMapTransform;
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform mat3 clearcoatNormalMapTransform;
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform mat3 clearcoatRoughnessMapTransform;
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	uniform mat3 sheenColorMapTransform;
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	uniform mat3 sheenRoughnessMapTransform;
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	uniform mat3 iridescenceMapTransform;
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform mat3 iridescenceThicknessMapTransform;
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SPECULARMAP
	uniform mat3 specularMapTransform;
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	uniform mat3 specularColorMapTransform;
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	uniform mat3 specularIntensityMapTransform;
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,zR=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	vUv = vec3( uv, 1 ).xy;
#endif
#ifdef USE_MAP
	vMapUv = ( mapTransform * vec3( MAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ALPHAMAP
	vAlphaMapUv = ( alphaMapTransform * vec3( ALPHAMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_LIGHTMAP
	vLightMapUv = ( lightMapTransform * vec3( LIGHTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_AOMAP
	vAoMapUv = ( aoMapTransform * vec3( AOMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_BUMPMAP
	vBumpMapUv = ( bumpMapTransform * vec3( BUMPMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_NORMALMAP
	vNormalMapUv = ( normalMapTransform * vec3( NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_DISPLACEMENTMAP
	vDisplacementMapUv = ( displacementMapTransform * vec3( DISPLACEMENTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_EMISSIVEMAP
	vEmissiveMapUv = ( emissiveMapTransform * vec3( EMISSIVEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_METALNESSMAP
	vMetalnessMapUv = ( metalnessMapTransform * vec3( METALNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ROUGHNESSMAP
	vRoughnessMapUv = ( roughnessMapTransform * vec3( ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ANISOTROPYMAP
	vAnisotropyMapUv = ( anisotropyMapTransform * vec3( ANISOTROPYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOATMAP
	vClearcoatMapUv = ( clearcoatMapTransform * vec3( CLEARCOATMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	vClearcoatNormalMapUv = ( clearcoatNormalMapTransform * vec3( CLEARCOAT_NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	vClearcoatRoughnessMapUv = ( clearcoatRoughnessMapTransform * vec3( CLEARCOAT_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCEMAP
	vIridescenceMapUv = ( iridescenceMapTransform * vec3( IRIDESCENCEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	vIridescenceThicknessMapUv = ( iridescenceThicknessMapTransform * vec3( IRIDESCENCE_THICKNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_COLORMAP
	vSheenColorMapUv = ( sheenColorMapTransform * vec3( SHEEN_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	vSheenRoughnessMapUv = ( sheenRoughnessMapTransform * vec3( SHEEN_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULARMAP
	vSpecularMapUv = ( specularMapTransform * vec3( SPECULARMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_COLORMAP
	vSpecularColorMapUv = ( specularColorMapTransform * vec3( SPECULAR_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	vSpecularIntensityMapUv = ( specularIntensityMapTransform * vec3( SPECULAR_INTENSITYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_TRANSMISSIONMAP
	vTransmissionMapUv = ( transmissionMapTransform * vec3( TRANSMISSIONMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_THICKNESSMAP
	vThicknessMapUv = ( thicknessMapTransform * vec3( THICKNESSMAP_UV, 1 ) ).xy;
#endif`,IR=`#if defined( USE_ENVMAP ) || defined( DISTANCE ) || defined ( USE_SHADOWMAP ) || defined ( USE_TRANSMISSION ) || NUM_SPOT_LIGHT_COORDS > 0
	vec4 worldPosition = vec4( transformed, 1.0 );
	#ifdef USE_BATCHING
		worldPosition = batchingMatrix * worldPosition;
	#endif
	#ifdef USE_INSTANCING
		worldPosition = instanceMatrix * worldPosition;
	#endif
	worldPosition = modelMatrix * worldPosition;
#endif`;const BR=`varying vec2 vUv;
uniform mat3 uvTransform;
void main() {
	vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	gl_Position = vec4( position.xy, 1.0, 1.0 );
}`,FR=`uniform sampler2D t2D;
uniform float backgroundIntensity;
varying vec2 vUv;
void main() {
	vec4 texColor = texture2D( t2D, vUv );
	#ifdef DECODE_VIDEO_TEXTURE
		texColor = vec4( mix( pow( texColor.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), texColor.rgb * 0.0773993808, vec3( lessThanEqual( texColor.rgb, vec3( 0.04045 ) ) ) ), texColor.w );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,HR=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,GR=`#ifdef ENVMAP_TYPE_CUBE
	uniform samplerCube envMap;
#elif defined( ENVMAP_TYPE_CUBE_UV )
	uniform sampler2D envMap;
#endif
uniform float flipEnvMap;
uniform float backgroundBlurriness;
uniform float backgroundIntensity;
uniform mat3 backgroundRotation;
varying vec3 vWorldDirection;
#include <cube_uv_reflection_fragment>
void main() {
	#ifdef ENVMAP_TYPE_CUBE
		vec4 texColor = textureCube( envMap, backgroundRotation * vec3( flipEnvMap * vWorldDirection.x, vWorldDirection.yz ) );
	#elif defined( ENVMAP_TYPE_CUBE_UV )
		vec4 texColor = textureCubeUV( envMap, backgroundRotation * vWorldDirection, backgroundBlurriness );
	#else
		vec4 texColor = vec4( 0.0, 0.0, 0.0, 1.0 );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,VR=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,XR=`uniform samplerCube tCube;
uniform float tFlip;
uniform float opacity;
varying vec3 vWorldDirection;
void main() {
	vec4 texColor = textureCube( tCube, vec3( tFlip * vWorldDirection.x, vWorldDirection.yz ) );
	gl_FragColor = texColor;
	gl_FragColor.a *= opacity;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,kR=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
varying vec2 vHighPrecisionZW;
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vHighPrecisionZW = gl_Position.zw;
}`,YR=`#if DEPTH_PACKING == 3200
	uniform float opacity;
#endif
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
varying vec2 vHighPrecisionZW;
void main() {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#if DEPTH_PACKING == 3200
		diffuseColor.a = opacity;
	#endif
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <logdepthbuf_fragment>
	float fragCoordZ = 0.5 * vHighPrecisionZW[0] / vHighPrecisionZW[1] + 0.5;
	#if DEPTH_PACKING == 3200
		gl_FragColor = vec4( vec3( 1.0 - fragCoordZ ), opacity );
	#elif DEPTH_PACKING == 3201
		gl_FragColor = packDepthToRGBA( fragCoordZ );
	#elif DEPTH_PACKING == 3202
		gl_FragColor = vec4( packDepthToRGB( fragCoordZ ), 1.0 );
	#elif DEPTH_PACKING == 3203
		gl_FragColor = vec4( packDepthToRG( fragCoordZ ), 0.0, 1.0 );
	#endif
}`,qR=`#define DISTANCE
varying vec3 vWorldPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <worldpos_vertex>
	#include <clipping_planes_vertex>
	vWorldPosition = worldPosition.xyz;
}`,WR=`#define DISTANCE
uniform vec3 referencePosition;
uniform float nearDistance;
uniform float farDistance;
varying vec3 vWorldPosition;
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <clipping_planes_pars_fragment>
void main () {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	float dist = length( vWorldPosition - referencePosition );
	dist = ( dist - nearDistance ) / ( farDistance - nearDistance );
	dist = saturate( dist );
	gl_FragColor = packDepthToRGBA( dist );
}`,jR=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
}`,ZR=`uniform sampler2D tEquirect;
varying vec3 vWorldDirection;
#include <common>
void main() {
	vec3 direction = normalize( vWorldDirection );
	vec2 sampleUV = equirectUv( direction );
	gl_FragColor = texture2D( tEquirect, sampleUV );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,KR=`uniform float scale;
attribute float lineDistance;
varying float vLineDistance;
#include <common>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	vLineDistance = scale * lineDistance;
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,QR=`uniform vec3 diffuse;
uniform float opacity;
uniform float dashSize;
uniform float totalSize;
varying float vLineDistance;
#include <common>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	if ( mod( vLineDistance, totalSize ) > dashSize ) {
		discard;
	}
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,JR=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#if defined ( USE_ENVMAP ) || defined ( USE_SKINNING )
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinbase_vertex>
		#include <skinnormal_vertex>
		#include <defaultnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <fog_vertex>
}`,$R=`uniform vec3 diffuse;
uniform float opacity;
#ifndef FLAT_SHADED
	varying vec3 vNormal;
#endif
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		reflectedLight.indirectDiffuse += lightMapTexel.rgb * lightMapIntensity * RECIPROCAL_PI;
	#else
		reflectedLight.indirectDiffuse += vec3( 1.0 );
	#endif
	#include <aomap_fragment>
	reflectedLight.indirectDiffuse *= diffuseColor.rgb;
	vec3 outgoingLight = reflectedLight.indirectDiffuse;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,tC=`#define LAMBERT
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,eC=`#define LAMBERT
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_lambert_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_lambert_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,nC=`#define MATCAP
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <displacementmap_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
	vViewPosition = - mvPosition.xyz;
}`,iC=`#define MATCAP
uniform vec3 diffuse;
uniform float opacity;
uniform sampler2D matcap;
varying vec3 vViewPosition;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	vec3 viewDir = normalize( vViewPosition );
	vec3 x = normalize( vec3( viewDir.z, 0.0, - viewDir.x ) );
	vec3 y = cross( viewDir, x );
	vec2 uv = vec2( dot( x, normal ), dot( y, normal ) ) * 0.495 + 0.5;
	#ifdef USE_MATCAP
		vec4 matcapColor = texture2D( matcap, uv );
	#else
		vec4 matcapColor = vec4( vec3( mix( 0.2, 0.8, uv.y ) ), 1.0 );
	#endif
	vec3 outgoingLight = diffuseColor.rgb * matcapColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,aC=`#define NORMAL
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	vViewPosition = - mvPosition.xyz;
#endif
}`,sC=`#define NORMAL
uniform float opacity;
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <packing>
#include <uv_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( 0.0, 0.0, 0.0, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	gl_FragColor = vec4( packNormalToRGB( normal ), diffuseColor.a );
	#ifdef OPAQUE
		gl_FragColor.a = 1.0;
	#endif
}`,rC=`#define PHONG
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,oC=`#define PHONG
uniform vec3 diffuse;
uniform vec3 emissive;
uniform vec3 specular;
uniform float shininess;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_phong_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_phong_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + reflectedLight.directSpecular + reflectedLight.indirectSpecular + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,lC=`#define STANDARD
varying vec3 vViewPosition;
#ifdef USE_TRANSMISSION
	varying vec3 vWorldPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
#ifdef USE_TRANSMISSION
	vWorldPosition = worldPosition.xyz;
#endif
}`,uC=`#define STANDARD
#ifdef PHYSICAL
	#define IOR
	#define USE_SPECULAR
#endif
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float roughness;
uniform float metalness;
uniform float opacity;
#ifdef IOR
	uniform float ior;
#endif
#ifdef USE_SPECULAR
	uniform float specularIntensity;
	uniform vec3 specularColor;
	#ifdef USE_SPECULAR_COLORMAP
		uniform sampler2D specularColorMap;
	#endif
	#ifdef USE_SPECULAR_INTENSITYMAP
		uniform sampler2D specularIntensityMap;
	#endif
#endif
#ifdef USE_CLEARCOAT
	uniform float clearcoat;
	uniform float clearcoatRoughness;
#endif
#ifdef USE_DISPERSION
	uniform float dispersion;
#endif
#ifdef USE_IRIDESCENCE
	uniform float iridescence;
	uniform float iridescenceIOR;
	uniform float iridescenceThicknessMinimum;
	uniform float iridescenceThicknessMaximum;
#endif
#ifdef USE_SHEEN
	uniform vec3 sheenColor;
	uniform float sheenRoughness;
	#ifdef USE_SHEEN_COLORMAP
		uniform sampler2D sheenColorMap;
	#endif
	#ifdef USE_SHEEN_ROUGHNESSMAP
		uniform sampler2D sheenRoughnessMap;
	#endif
#endif
#ifdef USE_ANISOTROPY
	uniform vec2 anisotropyVector;
	#ifdef USE_ANISOTROPYMAP
		uniform sampler2D anisotropyMap;
	#endif
#endif
varying vec3 vViewPosition;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <iridescence_fragment>
#include <cube_uv_reflection_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_physical_pars_fragment>
#include <fog_pars_fragment>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_physical_pars_fragment>
#include <transmission_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <clearcoat_pars_fragment>
#include <iridescence_pars_fragment>
#include <roughnessmap_pars_fragment>
#include <metalnessmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <roughnessmap_fragment>
	#include <metalnessmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <clearcoat_normal_fragment_begin>
	#include <clearcoat_normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_physical_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 totalDiffuse = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse;
	vec3 totalSpecular = reflectedLight.directSpecular + reflectedLight.indirectSpecular;
	#include <transmission_fragment>
	vec3 outgoingLight = totalDiffuse + totalSpecular + totalEmissiveRadiance;
	#ifdef USE_SHEEN
		float sheenEnergyComp = 1.0 - 0.157 * max3( material.sheenColor );
		outgoingLight = outgoingLight * sheenEnergyComp + sheenSpecularDirect + sheenSpecularIndirect;
	#endif
	#ifdef USE_CLEARCOAT
		float dotNVcc = saturate( dot( geometryClearcoatNormal, geometryViewDir ) );
		vec3 Fcc = F_Schlick( material.clearcoatF0, material.clearcoatF90, dotNVcc );
		outgoingLight = outgoingLight * ( 1.0 - material.clearcoat * Fcc ) + ( clearcoatSpecularDirect + clearcoatSpecularIndirect ) * material.clearcoat;
	#endif
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,cC=`#define TOON
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,fC=`#define TOON
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <gradientmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_toon_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_toon_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,hC=`uniform float size;
uniform float scale;
#include <common>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
#ifdef USE_POINTS_UV
	varying vec2 vUv;
	uniform mat3 uvTransform;
#endif
void main() {
	#ifdef USE_POINTS_UV
		vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	#endif
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	gl_PointSize = size;
	#ifdef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) gl_PointSize *= ( scale / - mvPosition.z );
	#endif
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <fog_vertex>
}`,dC=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <color_pars_fragment>
#include <map_particle_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_particle_fragment>
	#include <color_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,pC=`#include <common>
#include <batching_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <shadowmap_pars_vertex>
void main() {
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,mC=`uniform vec3 color;
uniform float opacity;
#include <common>
#include <packing>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <logdepthbuf_pars_fragment>
#include <shadowmap_pars_fragment>
#include <shadowmask_pars_fragment>
void main() {
	#include <logdepthbuf_fragment>
	gl_FragColor = vec4( color, opacity * ( 1.0 - getShadowMask() ) );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,_C=`uniform float rotation;
uniform vec2 center;
#include <common>
#include <uv_pars_vertex>
#include <fog_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	vec4 mvPosition = modelViewMatrix[ 3 ];
	vec2 scale = vec2( length( modelMatrix[ 0 ].xyz ), length( modelMatrix[ 1 ].xyz ) );
	#ifndef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) scale *= - mvPosition.z;
	#endif
	vec2 alignedPosition = ( position.xy - ( center - vec2( 0.5 ) ) ) * scale;
	vec2 rotatedPosition;
	rotatedPosition.x = cos( rotation ) * alignedPosition.x - sin( rotation ) * alignedPosition.y;
	rotatedPosition.y = sin( rotation ) * alignedPosition.x + cos( rotation ) * alignedPosition.y;
	mvPosition.xy += rotatedPosition;
	gl_Position = projectionMatrix * mvPosition;
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,gC=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,Ot={alphahash_fragment:F1,alphahash_pars_fragment:H1,alphamap_fragment:G1,alphamap_pars_fragment:V1,alphatest_fragment:X1,alphatest_pars_fragment:k1,aomap_fragment:Y1,aomap_pars_fragment:q1,batching_pars_vertex:W1,batching_vertex:j1,begin_vertex:Z1,beginnormal_vertex:K1,bsdfs:Q1,iridescence_fragment:J1,bumpmap_pars_fragment:$1,clipping_planes_fragment:tA,clipping_planes_pars_fragment:eA,clipping_planes_pars_vertex:nA,clipping_planes_vertex:iA,color_fragment:aA,color_pars_fragment:sA,color_pars_vertex:rA,color_vertex:oA,common:lA,cube_uv_reflection_fragment:uA,defaultnormal_vertex:cA,displacementmap_pars_vertex:fA,displacementmap_vertex:hA,emissivemap_fragment:dA,emissivemap_pars_fragment:pA,colorspace_fragment:mA,colorspace_pars_fragment:_A,envmap_fragment:gA,envmap_common_pars_fragment:vA,envmap_pars_fragment:SA,envmap_pars_vertex:yA,envmap_physical_pars_fragment:UA,envmap_vertex:xA,fog_vertex:MA,fog_pars_vertex:EA,fog_fragment:TA,fog_pars_fragment:bA,gradientmap_pars_fragment:AA,lightmap_pars_fragment:RA,lights_lambert_fragment:CA,lights_lambert_pars_fragment:wA,lights_pars_begin:DA,lights_toon_fragment:NA,lights_toon_pars_fragment:LA,lights_phong_fragment:OA,lights_phong_pars_fragment:PA,lights_physical_fragment:zA,lights_physical_pars_fragment:IA,lights_fragment_begin:BA,lights_fragment_maps:FA,lights_fragment_end:HA,logdepthbuf_fragment:GA,logdepthbuf_pars_fragment:VA,logdepthbuf_pars_vertex:XA,logdepthbuf_vertex:kA,map_fragment:YA,map_pars_fragment:qA,map_particle_fragment:WA,map_particle_pars_fragment:jA,metalnessmap_fragment:ZA,metalnessmap_pars_fragment:KA,morphinstance_vertex:QA,morphcolor_vertex:JA,morphnormal_vertex:$A,morphtarget_pars_vertex:tR,morphtarget_vertex:eR,normal_fragment_begin:nR,normal_fragment_maps:iR,normal_pars_fragment:aR,normal_pars_vertex:sR,normal_vertex:rR,normalmap_pars_fragment:oR,clearcoat_normal_fragment_begin:lR,clearcoat_normal_fragment_maps:uR,clearcoat_pars_fragment:cR,iridescence_pars_fragment:fR,opaque_fragment:hR,packing:dR,premultiplied_alpha_fragment:pR,project_vertex:mR,dithering_fragment:_R,dithering_pars_fragment:gR,roughnessmap_fragment:vR,roughnessmap_pars_fragment:SR,shadowmap_pars_fragment:yR,shadowmap_pars_vertex:xR,shadowmap_vertex:MR,shadowmask_pars_fragment:ER,skinbase_vertex:TR,skinning_pars_vertex:bR,skinning_vertex:AR,skinnormal_vertex:RR,specularmap_fragment:CR,specularmap_pars_fragment:wR,tonemapping_fragment:DR,tonemapping_pars_fragment:UR,transmission_fragment:NR,transmission_pars_fragment:LR,uv_pars_fragment:OR,uv_pars_vertex:PR,uv_vertex:zR,worldpos_vertex:IR,background_vert:BR,background_frag:FR,backgroundCube_vert:HR,backgroundCube_frag:GR,cube_vert:VR,cube_frag:XR,depth_vert:kR,depth_frag:YR,distanceRGBA_vert:qR,distanceRGBA_frag:WR,equirect_vert:jR,equirect_frag:ZR,linedashed_vert:KR,linedashed_frag:QR,meshbasic_vert:JR,meshbasic_frag:$R,meshlambert_vert:tC,meshlambert_frag:eC,meshmatcap_vert:nC,meshmatcap_frag:iC,meshnormal_vert:aC,meshnormal_frag:sC,meshphong_vert:rC,meshphong_frag:oC,meshphysical_vert:lC,meshphysical_frag:uC,meshtoon_vert:cC,meshtoon_frag:fC,points_vert:hC,points_frag:dC,shadow_vert:pC,shadow_frag:mC,sprite_vert:_C,sprite_frag:gC},at={common:{diffuse:{value:new Ht(16777215)},opacity:{value:1},map:{value:null},mapTransform:{value:new Pt},alphaMap:{value:null},alphaMapTransform:{value:new Pt},alphaTest:{value:0}},specularmap:{specularMap:{value:null},specularMapTransform:{value:new Pt}},envmap:{envMap:{value:null},envMapRotation:{value:new Pt},flipEnvMap:{value:-1},reflectivity:{value:1},ior:{value:1.5},refractionRatio:{value:.98}},aomap:{aoMap:{value:null},aoMapIntensity:{value:1},aoMapTransform:{value:new Pt}},lightmap:{lightMap:{value:null},lightMapIntensity:{value:1},lightMapTransform:{value:new Pt}},bumpmap:{bumpMap:{value:null},bumpMapTransform:{value:new Pt},bumpScale:{value:1}},normalmap:{normalMap:{value:null},normalMapTransform:{value:new Pt},normalScale:{value:new Lt(1,1)}},displacementmap:{displacementMap:{value:null},displacementMapTransform:{value:new Pt},displacementScale:{value:1},displacementBias:{value:0}},emissivemap:{emissiveMap:{value:null},emissiveMapTransform:{value:new Pt}},metalnessmap:{metalnessMap:{value:null},metalnessMapTransform:{value:new Pt}},roughnessmap:{roughnessMap:{value:null},roughnessMapTransform:{value:new Pt}},gradientmap:{gradientMap:{value:null}},fog:{fogDensity:{value:25e-5},fogNear:{value:1},fogFar:{value:2e3},fogColor:{value:new Ht(16777215)}},lights:{ambientLightColor:{value:[]},lightProbe:{value:[]},directionalLights:{value:[],properties:{direction:{},color:{}}},directionalLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},directionalShadowMap:{value:[]},directionalShadowMatrix:{value:[]},spotLights:{value:[],properties:{color:{},position:{},direction:{},distance:{},coneCos:{},penumbraCos:{},decay:{}}},spotLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},spotLightMap:{value:[]},spotShadowMap:{value:[]},spotLightMatrix:{value:[]},pointLights:{value:[],properties:{color:{},position:{},decay:{},distance:{}}},pointLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{},shadowCameraNear:{},shadowCameraFar:{}}},pointShadowMap:{value:[]},pointShadowMatrix:{value:[]},hemisphereLights:{value:[],properties:{direction:{},skyColor:{},groundColor:{}}},rectAreaLights:{value:[],properties:{color:{},position:{},width:{},height:{}}},ltc_1:{value:null},ltc_2:{value:null}},points:{diffuse:{value:new Ht(16777215)},opacity:{value:1},size:{value:1},scale:{value:1},map:{value:null},alphaMap:{value:null},alphaMapTransform:{value:new Pt},alphaTest:{value:0},uvTransform:{value:new Pt}},sprite:{diffuse:{value:new Ht(16777215)},opacity:{value:1},center:{value:new Lt(.5,.5)},rotation:{value:0},map:{value:null},mapTransform:{value:new Pt},alphaMap:{value:null},alphaMapTransform:{value:new Pt},alphaTest:{value:0}}},Ai={basic:{uniforms:cn([at.common,at.specularmap,at.envmap,at.aomap,at.lightmap,at.fog]),vertexShader:Ot.meshbasic_vert,fragmentShader:Ot.meshbasic_frag},lambert:{uniforms:cn([at.common,at.specularmap,at.envmap,at.aomap,at.lightmap,at.emissivemap,at.bumpmap,at.normalmap,at.displacementmap,at.fog,at.lights,{emissive:{value:new Ht(0)}}]),vertexShader:Ot.meshlambert_vert,fragmentShader:Ot.meshlambert_frag},phong:{uniforms:cn([at.common,at.specularmap,at.envmap,at.aomap,at.lightmap,at.emissivemap,at.bumpmap,at.normalmap,at.displacementmap,at.fog,at.lights,{emissive:{value:new Ht(0)},specular:{value:new Ht(1118481)},shininess:{value:30}}]),vertexShader:Ot.meshphong_vert,fragmentShader:Ot.meshphong_frag},standard:{uniforms:cn([at.common,at.envmap,at.aomap,at.lightmap,at.emissivemap,at.bumpmap,at.normalmap,at.displacementmap,at.roughnessmap,at.metalnessmap,at.fog,at.lights,{emissive:{value:new Ht(0)},roughness:{value:1},metalness:{value:0},envMapIntensity:{value:1}}]),vertexShader:Ot.meshphysical_vert,fragmentShader:Ot.meshphysical_frag},toon:{uniforms:cn([at.common,at.aomap,at.lightmap,at.emissivemap,at.bumpmap,at.normalmap,at.displacementmap,at.gradientmap,at.fog,at.lights,{emissive:{value:new Ht(0)}}]),vertexShader:Ot.meshtoon_vert,fragmentShader:Ot.meshtoon_frag},matcap:{uniforms:cn([at.common,at.bumpmap,at.normalmap,at.displacementmap,at.fog,{matcap:{value:null}}]),vertexShader:Ot.meshmatcap_vert,fragmentShader:Ot.meshmatcap_frag},points:{uniforms:cn([at.points,at.fog]),vertexShader:Ot.points_vert,fragmentShader:Ot.points_frag},dashed:{uniforms:cn([at.common,at.fog,{scale:{value:1},dashSize:{value:1},totalSize:{value:2}}]),vertexShader:Ot.linedashed_vert,fragmentShader:Ot.linedashed_frag},depth:{uniforms:cn([at.common,at.displacementmap]),vertexShader:Ot.depth_vert,fragmentShader:Ot.depth_frag},normal:{uniforms:cn([at.common,at.bumpmap,at.normalmap,at.displacementmap,{opacity:{value:1}}]),vertexShader:Ot.meshnormal_vert,fragmentShader:Ot.meshnormal_frag},sprite:{uniforms:cn([at.sprite,at.fog]),vertexShader:Ot.sprite_vert,fragmentShader:Ot.sprite_frag},background:{uniforms:{uvTransform:{value:new Pt},t2D:{value:null},backgroundIntensity:{value:1}},vertexShader:Ot.background_vert,fragmentShader:Ot.background_frag},backgroundCube:{uniforms:{envMap:{value:null},flipEnvMap:{value:-1},backgroundBlurriness:{value:0},backgroundIntensity:{value:1},backgroundRotation:{value:new Pt}},vertexShader:Ot.backgroundCube_vert,fragmentShader:Ot.backgroundCube_frag},cube:{uniforms:{tCube:{value:null},tFlip:{value:-1},opacity:{value:1}},vertexShader:Ot.cube_vert,fragmentShader:Ot.cube_frag},equirect:{uniforms:{tEquirect:{value:null}},vertexShader:Ot.equirect_vert,fragmentShader:Ot.equirect_frag},distanceRGBA:{uniforms:cn([at.common,at.displacementmap,{referencePosition:{value:new P},nearDistance:{value:1},farDistance:{value:1e3}}]),vertexShader:Ot.distanceRGBA_vert,fragmentShader:Ot.distanceRGBA_frag},shadow:{uniforms:cn([at.lights,at.fog,{color:{value:new Ht(0)},opacity:{value:1}}]),vertexShader:Ot.shadow_vert,fragmentShader:Ot.shadow_frag}};Ai.physical={uniforms:cn([Ai.standard.uniforms,{clearcoat:{value:0},clearcoatMap:{value:null},clearcoatMapTransform:{value:new Pt},clearcoatNormalMap:{value:null},clearcoatNormalMapTransform:{value:new Pt},clearcoatNormalScale:{value:new Lt(1,1)},clearcoatRoughness:{value:0},clearcoatRoughnessMap:{value:null},clearcoatRoughnessMapTransform:{value:new Pt},dispersion:{value:0},iridescence:{value:0},iridescenceMap:{value:null},iridescenceMapTransform:{value:new Pt},iridescenceIOR:{value:1.3},iridescenceThicknessMinimum:{value:100},iridescenceThicknessMaximum:{value:400},iridescenceThicknessMap:{value:null},iridescenceThicknessMapTransform:{value:new Pt},sheen:{value:0},sheenColor:{value:new Ht(0)},sheenColorMap:{value:null},sheenColorMapTransform:{value:new Pt},sheenRoughness:{value:1},sheenRoughnessMap:{value:null},sheenRoughnessMapTransform:{value:new Pt},transmission:{value:0},transmissionMap:{value:null},transmissionMapTransform:{value:new Pt},transmissionSamplerSize:{value:new Lt},transmissionSamplerMap:{value:null},thickness:{value:0},thicknessMap:{value:null},thicknessMapTransform:{value:new Pt},attenuationDistance:{value:0},attenuationColor:{value:new Ht(0)},specularColor:{value:new Ht(1,1,1)},specularColorMap:{value:null},specularColorMapTransform:{value:new Pt},specularIntensity:{value:1},specularIntensityMap:{value:null},specularIntensityMapTransform:{value:new Pt},anisotropyVector:{value:new Lt},anisotropyMap:{value:null},anisotropyMapTransform:{value:new Pt}}]),vertexShader:Ot.meshphysical_vert,fragmentShader:Ot.meshphysical_frag};const pu={r:0,b:0,g:0},rs=new sa,vC=new Te;function SC(e,t,n,i,a,s,r){const o=new Ht(0);let l=s===!0?0:1,u,h,p=null,f=0,d=null;function v(_){let g=_.isScene===!0?_.background:null;return g&&g.isTexture&&(g=(_.backgroundBlurriness>0?n:t).get(g)),g}function y(_){let g=!1;const x=v(_);x===null?c(o,l):x&&x.isColor&&(c(x,1),g=!0);const C=e.xr.getEnvironmentBlendMode();C==="additive"?i.buffers.color.setClear(0,0,0,1,r):C==="alpha-blend"&&i.buffers.color.setClear(0,0,0,0,r),(e.autoClear||g)&&(i.buffers.depth.setTest(!0),i.buffers.depth.setMask(!0),i.buffers.color.setMask(!0),e.clear(e.autoClearColor,e.autoClearDepth,e.autoClearStencil))}function m(_,g){const x=v(g);x&&(x.isCubeTexture||x.mapping===$c)?(h===void 0&&(h=new En(new co(1,1,1),new Za({name:"BackgroundCubeMaterial",uniforms:eo(Ai.backgroundCube.uniforms),vertexShader:Ai.backgroundCube.vertexShader,fragmentShader:Ai.backgroundCube.fragmentShader,side:bn,depthTest:!1,depthWrite:!1,fog:!1})),h.geometry.deleteAttribute("normal"),h.geometry.deleteAttribute("uv"),h.onBeforeRender=function(C,R,b){this.matrixWorld.copyPosition(b.matrixWorld)},Object.defineProperty(h.material,"envMap",{get:function(){return this.uniforms.envMap.value}}),a.update(h)),rs.copy(g.backgroundRotation),rs.x*=-1,rs.y*=-1,rs.z*=-1,x.isCubeTexture&&x.isRenderTargetTexture===!1&&(rs.y*=-1,rs.z*=-1),h.material.uniforms.envMap.value=x,h.material.uniforms.flipEnvMap.value=x.isCubeTexture&&x.isRenderTargetTexture===!1?-1:1,h.material.uniforms.backgroundBlurriness.value=g.backgroundBlurriness,h.material.uniforms.backgroundIntensity.value=g.backgroundIntensity,h.material.uniforms.backgroundRotation.value.setFromMatrix4(vC.makeRotationFromEuler(rs)),h.material.toneMapped=ae.getTransfer(x.colorSpace)!==xe,(p!==x||f!==x.version||d!==e.toneMapping)&&(h.material.needsUpdate=!0,p=x,f=x.version,d=e.toneMapping),h.layers.enableAll(),_.unshift(h,h.geometry,h.material,0,0,null)):x&&x.isTexture&&(u===void 0&&(u=new En(new Cl(2,2),new Za({name:"BackgroundMaterial",uniforms:eo(Ai.background.uniforms),vertexShader:Ai.background.vertexShader,fragmentShader:Ai.background.fragmentShader,side:ja,depthTest:!1,depthWrite:!1,fog:!1})),u.geometry.deleteAttribute("normal"),Object.defineProperty(u.material,"map",{get:function(){return this.uniforms.t2D.value}}),a.update(u)),u.material.uniforms.t2D.value=x,u.material.uniforms.backgroundIntensity.value=g.backgroundIntensity,u.material.toneMapped=ae.getTransfer(x.colorSpace)!==xe,x.matrixAutoUpdate===!0&&x.updateMatrix(),u.material.uniforms.uvTransform.value.copy(x.matrix),(p!==x||f!==x.version||d!==e.toneMapping)&&(u.material.needsUpdate=!0,p=x,f=x.version,d=e.toneMapping),u.layers.enableAll(),_.unshift(u,u.geometry,u.material,0,0,null))}function c(_,g){_.getRGB(pu,Ax(e)),i.buffers.color.setClear(pu.r,pu.g,pu.b,g,r)}return{getClearColor:function(){return o},setClearColor:function(_,g=1){o.set(_),l=g,c(o,l)},getClearAlpha:function(){return l},setClearAlpha:function(_){l=_,c(o,l)},render:y,addToRenderList:m}}function yC(e,t){const n=e.getParameter(e.MAX_VERTEX_ATTRIBS),i={},a=f(null);let s=a,r=!1;function o(S,T,F,G,Y){let K=!1;const D=p(G,F,T);s!==D&&(s=D,u(s.object)),K=d(S,G,F,Y),K&&v(S,G,F,Y),Y!==null&&t.update(Y,e.ELEMENT_ARRAY_BUFFER),(K||r)&&(r=!1,x(S,T,F,G),Y!==null&&e.bindBuffer(e.ELEMENT_ARRAY_BUFFER,t.get(Y).buffer))}function l(){return e.createVertexArray()}function u(S){return e.bindVertexArray(S)}function h(S){return e.deleteVertexArray(S)}function p(S,T,F){const G=F.wireframe===!0;let Y=i[S.id];Y===void 0&&(Y={},i[S.id]=Y);let K=Y[T.id];K===void 0&&(K={},Y[T.id]=K);let D=K[G];return D===void 0&&(D=f(l()),K[G]=D),D}function f(S){const T=[],F=[],G=[];for(let Y=0;Y<n;Y++)T[Y]=0,F[Y]=0,G[Y]=0;return{geometry:null,program:null,wireframe:!1,newAttributes:T,enabledAttributes:F,attributeDivisors:G,object:S,attributes:{},index:null}}function d(S,T,F,G){const Y=s.attributes,K=T.attributes;let D=0;const V=F.getAttributes();for(const z in V)if(V[z].location>=0){const it=Y[z];let ht=K[z];if(ht===void 0&&(z==="instanceMatrix"&&S.instanceMatrix&&(ht=S.instanceMatrix),z==="instanceColor"&&S.instanceColor&&(ht=S.instanceColor)),it===void 0||it.attribute!==ht||ht&&it.data!==ht.data)return!0;D++}return s.attributesNum!==D||s.index!==G}function v(S,T,F,G){const Y={},K=T.attributes;let D=0;const V=F.getAttributes();for(const z in V)if(V[z].location>=0){let it=K[z];it===void 0&&(z==="instanceMatrix"&&S.instanceMatrix&&(it=S.instanceMatrix),z==="instanceColor"&&S.instanceColor&&(it=S.instanceColor));const ht={};ht.attribute=it,it&&it.data&&(ht.data=it.data),Y[z]=ht,D++}s.attributes=Y,s.attributesNum=D,s.index=G}function y(){const S=s.newAttributes;for(let T=0,F=S.length;T<F;T++)S[T]=0}function m(S){c(S,0)}function c(S,T){const F=s.newAttributes,G=s.enabledAttributes,Y=s.attributeDivisors;F[S]=1,G[S]===0&&(e.enableVertexAttribArray(S),G[S]=1),Y[S]!==T&&(e.vertexAttribDivisor(S,T),Y[S]=T)}function _(){const S=s.newAttributes,T=s.enabledAttributes;for(let F=0,G=T.length;F<G;F++)T[F]!==S[F]&&(e.disableVertexAttribArray(F),T[F]=0)}function g(S,T,F,G,Y,K,D){D===!0?e.vertexAttribIPointer(S,T,F,Y,K):e.vertexAttribPointer(S,T,F,G,Y,K)}function x(S,T,F,G){y();const Y=G.attributes,K=F.getAttributes(),D=T.defaultAttributeValues;for(const V in K){const z=K[V];if(z.location>=0){let tt=Y[V];if(tt===void 0&&(V==="instanceMatrix"&&S.instanceMatrix&&(tt=S.instanceMatrix),V==="instanceColor"&&S.instanceColor&&(tt=S.instanceColor)),tt!==void 0){const it=tt.normalized,ht=tt.itemSize,Ft=t.get(tt);if(Ft===void 0)continue;const kt=Ft.buffer,k=Ft.type,$=Ft.bytesPerElement,_t=k===e.INT||k===e.UNSIGNED_INT||tt.gpuType===Cm;if(tt.isInterleavedBufferAttribute){const ct=tt.data,Dt=ct.stride,Et=tt.offset;if(ct.isInstancedInterleavedBuffer){for(let Yt=0;Yt<z.locationSize;Yt++)c(z.location+Yt,ct.meshPerAttribute);S.isInstancedMesh!==!0&&G._maxInstanceCount===void 0&&(G._maxInstanceCount=ct.meshPerAttribute*ct.count)}else for(let Yt=0;Yt<z.locationSize;Yt++)m(z.location+Yt);e.bindBuffer(e.ARRAY_BUFFER,kt);for(let Yt=0;Yt<z.locationSize;Yt++)g(z.location+Yt,ht/z.locationSize,k,it,Dt*$,(Et+ht/z.locationSize*Yt)*$,_t)}else{if(tt.isInstancedBufferAttribute){for(let ct=0;ct<z.locationSize;ct++)c(z.location+ct,tt.meshPerAttribute);S.isInstancedMesh!==!0&&G._maxInstanceCount===void 0&&(G._maxInstanceCount=tt.meshPerAttribute*tt.count)}else for(let ct=0;ct<z.locationSize;ct++)m(z.location+ct);e.bindBuffer(e.ARRAY_BUFFER,kt);for(let ct=0;ct<z.locationSize;ct++)g(z.location+ct,ht/z.locationSize,k,it,ht*$,ht/z.locationSize*ct*$,_t)}}else if(D!==void 0){const it=D[V];if(it!==void 0)switch(it.length){case 2:e.vertexAttrib2fv(z.location,it);break;case 3:e.vertexAttrib3fv(z.location,it);break;case 4:e.vertexAttrib4fv(z.location,it);break;default:e.vertexAttrib1fv(z.location,it)}}}}_()}function C(){w();for(const S in i){const T=i[S];for(const F in T){const G=T[F];for(const Y in G)h(G[Y].object),delete G[Y];delete T[F]}delete i[S]}}function R(S){if(i[S.id]===void 0)return;const T=i[S.id];for(const F in T){const G=T[F];for(const Y in G)h(G[Y].object),delete G[Y];delete T[F]}delete i[S.id]}function b(S){for(const T in i){const F=i[T];if(F[S.id]===void 0)continue;const G=F[S.id];for(const Y in G)h(G[Y].object),delete G[Y];delete F[S.id]}}function w(){W(),r=!0,s!==a&&(s=a,u(s.object))}function W(){a.geometry=null,a.program=null,a.wireframe=!1}return{setup:o,reset:w,resetDefaultState:W,dispose:C,releaseStatesOfGeometry:R,releaseStatesOfProgram:b,initAttributes:y,enableAttribute:m,disableUnusedAttributes:_}}function xC(e,t,n){let i;function a(u){i=u}function s(u,h){e.drawArrays(i,u,h),n.update(h,i,1)}function r(u,h,p){p!==0&&(e.drawArraysInstanced(i,u,h,p),n.update(h,i,p))}function o(u,h,p){if(p===0)return;t.get("WEBGL_multi_draw").multiDrawArraysWEBGL(i,u,0,h,0,p);let d=0;for(let v=0;v<p;v++)d+=h[v];n.update(d,i,1)}function l(u,h,p,f){if(p===0)return;const d=t.get("WEBGL_multi_draw");if(d===null)for(let v=0;v<u.length;v++)r(u[v],h[v],f[v]);else{d.multiDrawArraysInstancedWEBGL(i,u,0,h,0,f,0,p);let v=0;for(let y=0;y<p;y++)v+=h[y];for(let y=0;y<f.length;y++)n.update(v,i,f[y])}}this.setMode=a,this.render=s,this.renderInstances=r,this.renderMultiDraw=o,this.renderMultiDrawInstances=l}function MC(e,t,n,i){let a;function s(){if(a!==void 0)return a;if(t.has("EXT_texture_filter_anisotropic")===!0){const b=t.get("EXT_texture_filter_anisotropic");a=e.getParameter(b.MAX_TEXTURE_MAX_ANISOTROPY_EXT)}else a=0;return a}function r(b){return!(b!==vi&&i.convert(b)!==e.getParameter(e.IMPLEMENTATION_COLOR_READ_FORMAT))}function o(b){const w=b===Tl&&(t.has("EXT_color_buffer_half_float")||t.has("EXT_color_buffer_float"));return!(b!==aa&&i.convert(b)!==e.getParameter(e.IMPLEMENTATION_COLOR_READ_TYPE)&&b!==ji&&!w)}function l(b){if(b==="highp"){if(e.getShaderPrecisionFormat(e.VERTEX_SHADER,e.HIGH_FLOAT).precision>0&&e.getShaderPrecisionFormat(e.FRAGMENT_SHADER,e.HIGH_FLOAT).precision>0)return"highp";b="mediump"}return b==="mediump"&&e.getShaderPrecisionFormat(e.VERTEX_SHADER,e.MEDIUM_FLOAT).precision>0&&e.getShaderPrecisionFormat(e.FRAGMENT_SHADER,e.MEDIUM_FLOAT).precision>0?"mediump":"lowp"}let u=n.precision!==void 0?n.precision:"highp";const h=l(u);h!==u&&(console.warn("THREE.WebGLRenderer:",u,"not supported, using",h,"instead."),u=h);const p=n.logarithmicDepthBuffer===!0,f=n.reverseDepthBuffer===!0&&t.has("EXT_clip_control");if(f===!0){const b=t.get("EXT_clip_control");b.clipControlEXT(b.LOWER_LEFT_EXT,b.ZERO_TO_ONE_EXT)}const d=e.getParameter(e.MAX_TEXTURE_IMAGE_UNITS),v=e.getParameter(e.MAX_VERTEX_TEXTURE_IMAGE_UNITS),y=e.getParameter(e.MAX_TEXTURE_SIZE),m=e.getParameter(e.MAX_CUBE_MAP_TEXTURE_SIZE),c=e.getParameter(e.MAX_VERTEX_ATTRIBS),_=e.getParameter(e.MAX_VERTEX_UNIFORM_VECTORS),g=e.getParameter(e.MAX_VARYING_VECTORS),x=e.getParameter(e.MAX_FRAGMENT_UNIFORM_VECTORS),C=v>0,R=e.getParameter(e.MAX_SAMPLES);return{isWebGL2:!0,getMaxAnisotropy:s,getMaxPrecision:l,textureFormatReadable:r,textureTypeReadable:o,precision:u,logarithmicDepthBuffer:p,reverseDepthBuffer:f,maxTextures:d,maxVertexTextures:v,maxTextureSize:y,maxCubemapSize:m,maxAttributes:c,maxVertexUniforms:_,maxVaryings:g,maxFragmentUniforms:x,vertexTextures:C,maxSamples:R}}function EC(e){const t=this;let n=null,i=0,a=!1,s=!1;const r=new Ma,o=new Pt,l={value:null,needsUpdate:!1};this.uniform=l,this.numPlanes=0,this.numIntersection=0,this.init=function(p,f){const d=p.length!==0||f||i!==0||a;return a=f,i=p.length,d},this.beginShadows=function(){s=!0,h(null)},this.endShadows=function(){s=!1},this.setGlobalState=function(p,f){n=h(p,f,0)},this.setState=function(p,f,d){const v=p.clippingPlanes,y=p.clipIntersection,m=p.clipShadows,c=e.get(p);if(!a||v===null||v.length===0||s&&!m)s?h(null):u();else{const _=s?0:i,g=_*4;let x=c.clippingState||null;l.value=x,x=h(v,f,g,d);for(let C=0;C!==g;++C)x[C]=n[C];c.clippingState=x,this.numIntersection=y?this.numPlanes:0,this.numPlanes+=_}};function u(){l.value!==n&&(l.value=n,l.needsUpdate=i>0),t.numPlanes=i,t.numIntersection=0}function h(p,f,d,v){const y=p!==null?p.length:0;let m=null;if(y!==0){if(m=l.value,v!==!0||m===null){const c=d+y*4,_=f.matrixWorldInverse;o.getNormalMatrix(_),(m===null||m.length<c)&&(m=new Float32Array(c));for(let g=0,x=d;g!==y;++g,x+=4)r.copy(p[g]).applyMatrix4(_,o),r.normal.toArray(m,x),m[x+3]=r.constant}l.value=m,l.needsUpdate=!0}return t.numPlanes=y,t.numIntersection=0,m}}function TC(e){let t=new WeakMap;function n(r,o){return o===kd?r.mapping=Qr:o===Yd&&(r.mapping=Jr),r}function i(r){if(r&&r.isTexture){const o=r.mapping;if(o===kd||o===Yd)if(t.has(r)){const l=t.get(r).texture;return n(l,r.mapping)}else{const l=r.image;if(l&&l.height>0){const u=new P1(l.height);return u.fromEquirectangularTexture(e,r),t.set(r,u),r.addEventListener("dispose",a),n(u.texture,r.mapping)}else return null}}return r}function a(r){const o=r.target;o.removeEventListener("dispose",a);const l=t.get(o);l!==void 0&&(t.delete(o),l.dispose())}function s(){t=new WeakMap}return{get:i,dispose:s}}class Dx extends Rx{constructor(t=-1,n=1,i=1,a=-1,s=.1,r=2e3){super(),this.isOrthographicCamera=!0,this.type="OrthographicCamera",this.zoom=1,this.view=null,this.left=t,this.right=n,this.top=i,this.bottom=a,this.near=s,this.far=r,this.updateProjectionMatrix()}copy(t,n){return super.copy(t,n),this.left=t.left,this.right=t.right,this.top=t.top,this.bottom=t.bottom,this.near=t.near,this.far=t.far,this.zoom=t.zoom,this.view=t.view===null?null:Object.assign({},t.view),this}setViewOffset(t,n,i,a,s,r){this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=t,this.view.fullHeight=n,this.view.offsetX=i,this.view.offsetY=a,this.view.width=s,this.view.height=r,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){const t=(this.right-this.left)/(2*this.zoom),n=(this.top-this.bottom)/(2*this.zoom),i=(this.right+this.left)/2,a=(this.top+this.bottom)/2;let s=i-t,r=i+t,o=a+n,l=a-n;if(this.view!==null&&this.view.enabled){const u=(this.right-this.left)/this.view.fullWidth/this.zoom,h=(this.top-this.bottom)/this.view.fullHeight/this.zoom;s+=u*this.view.offsetX,r=s+u*this.view.width,o-=h*this.view.offsetY,l=o-h*this.view.height}this.projectionMatrix.makeOrthographic(s,r,o,l,this.near,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(t){const n=super.toJSON(t);return n.object.zoom=this.zoom,n.object.left=this.left,n.object.right=this.right,n.object.top=this.top,n.object.bottom=this.bottom,n.object.near=this.near,n.object.far=this.far,this.view!==null&&(n.object.view=Object.assign({},this.view)),n}}const Mr=4,l0=[.125,.215,.35,.446,.526,.582],ds=20,dh=new Dx,u0=new Ht;let ph=null,mh=0,_h=0,gh=!1;const fs=(1+Math.sqrt(5))/2,ir=1/fs,c0=[new P(-fs,ir,0),new P(fs,ir,0),new P(-ir,0,fs),new P(ir,0,fs),new P(0,fs,-ir),new P(0,fs,ir),new P(-1,1,-1),new P(1,1,-1),new P(-1,1,1),new P(1,1,1)];class f0{constructor(t){this._renderer=t,this._pingPongRenderTarget=null,this._lodMax=0,this._cubeSize=0,this._lodPlanes=[],this._sizeLods=[],this._sigmas=[],this._blurMaterial=null,this._cubemapMaterial=null,this._equirectMaterial=null,this._compileMaterial(this._blurMaterial)}fromScene(t,n=0,i=.1,a=100){ph=this._renderer.getRenderTarget(),mh=this._renderer.getActiveCubeFace(),_h=this._renderer.getActiveMipmapLevel(),gh=this._renderer.xr.enabled,this._renderer.xr.enabled=!1,this._setSize(256);const s=this._allocateTargets();return s.depthBuffer=!0,this._sceneToCubeUV(t,i,a,s),n>0&&this._blur(s,0,0,n),this._applyPMREM(s),this._cleanup(s),s}fromEquirectangular(t,n=null){return this._fromTexture(t,n)}fromCubemap(t,n=null){return this._fromTexture(t,n)}compileCubemapShader(){this._cubemapMaterial===null&&(this._cubemapMaterial=p0(),this._compileMaterial(this._cubemapMaterial))}compileEquirectangularShader(){this._equirectMaterial===null&&(this._equirectMaterial=d0(),this._compileMaterial(this._equirectMaterial))}dispose(){this._dispose(),this._cubemapMaterial!==null&&this._cubemapMaterial.dispose(),this._equirectMaterial!==null&&this._equirectMaterial.dispose()}_setSize(t){this._lodMax=Math.floor(Math.log2(t)),this._cubeSize=Math.pow(2,this._lodMax)}_dispose(){this._blurMaterial!==null&&this._blurMaterial.dispose(),this._pingPongRenderTarget!==null&&this._pingPongRenderTarget.dispose();for(let t=0;t<this._lodPlanes.length;t++)this._lodPlanes[t].dispose()}_cleanup(t){this._renderer.setRenderTarget(ph,mh,_h),this._renderer.xr.enabled=gh,t.scissorTest=!1,mu(t,0,0,t.width,t.height)}_fromTexture(t,n){t.mapping===Qr||t.mapping===Jr?this._setSize(t.image.length===0?16:t.image[0].width||t.image[0].image.width):this._setSize(t.image.width/4),ph=this._renderer.getRenderTarget(),mh=this._renderer.getActiveCubeFace(),_h=this._renderer.getActiveMipmapLevel(),gh=this._renderer.xr.enabled,this._renderer.xr.enabled=!1;const i=n||this._allocateTargets();return this._textureToCubeUV(t,i),this._applyPMREM(i),this._cleanup(i),i}_allocateTargets(){const t=3*Math.max(this._cubeSize,112),n=4*this._cubeSize,i={magFilter:mi,minFilter:mi,generateMipmaps:!1,type:Tl,format:vi,colorSpace:Ja,depthBuffer:!1},a=h0(t,n,i);if(this._pingPongRenderTarget===null||this._pingPongRenderTarget.width!==t||this._pingPongRenderTarget.height!==n){this._pingPongRenderTarget!==null&&this._dispose(),this._pingPongRenderTarget=h0(t,n,i);const{_lodMax:s}=this;({sizeLods:this._sizeLods,lodPlanes:this._lodPlanes,sigmas:this._sigmas}=bC(s)),this._blurMaterial=AC(s,t,n)}return a}_compileMaterial(t){const n=new En(this._lodPlanes[0],t);this._renderer.compile(n,dh)}_sceneToCubeUV(t,n,i,a){const o=new $n(90,1,n,i),l=[1,-1,1,1,1,1],u=[1,1,1,-1,-1,-1],h=this._renderer,p=h.autoClear,f=h.toneMapping;h.getClearColor(u0),h.toneMapping=Va,h.autoClear=!1;const d=new Os({name:"PMREM.Background",side:bn,depthWrite:!1,depthTest:!1}),v=new En(new co,d);let y=!1;const m=t.background;m?m.isColor&&(d.color.copy(m),t.background=null,y=!0):(d.color.copy(u0),y=!0);for(let c=0;c<6;c++){const _=c%3;_===0?(o.up.set(0,l[c],0),o.lookAt(u[c],0,0)):_===1?(o.up.set(0,0,l[c]),o.lookAt(0,u[c],0)):(o.up.set(0,l[c],0),o.lookAt(0,0,u[c]));const g=this._cubeSize;mu(a,_*g,c>2?g:0,g,g),h.setRenderTarget(a),y&&h.render(v,o),h.render(t,o)}v.geometry.dispose(),v.material.dispose(),h.toneMapping=f,h.autoClear=p,t.background=m}_textureToCubeUV(t,n){const i=this._renderer,a=t.mapping===Qr||t.mapping===Jr;a?(this._cubemapMaterial===null&&(this._cubemapMaterial=p0()),this._cubemapMaterial.uniforms.flipEnvMap.value=t.isRenderTargetTexture===!1?-1:1):this._equirectMaterial===null&&(this._equirectMaterial=d0());const s=a?this._cubemapMaterial:this._equirectMaterial,r=new En(this._lodPlanes[0],s),o=s.uniforms;o.envMap.value=t;const l=this._cubeSize;mu(n,0,0,3*l,2*l),i.setRenderTarget(n),i.render(r,dh)}_applyPMREM(t){const n=this._renderer,i=n.autoClear;n.autoClear=!1;const a=this._lodPlanes.length;for(let s=1;s<a;s++){const r=Math.sqrt(this._sigmas[s]*this._sigmas[s]-this._sigmas[s-1]*this._sigmas[s-1]),o=c0[(a-s-1)%c0.length];this._blur(t,s-1,s,r,o)}n.autoClear=i}_blur(t,n,i,a,s){const r=this._pingPongRenderTarget;this._halfBlur(t,r,n,i,a,"latitudinal",s),this._halfBlur(r,t,i,i,a,"longitudinal",s)}_halfBlur(t,n,i,a,s,r,o){const l=this._renderer,u=this._blurMaterial;r!=="latitudinal"&&r!=="longitudinal"&&console.error("blur direction must be either latitudinal or longitudinal!");const h=3,p=new En(this._lodPlanes[a],u),f=u.uniforms,d=this._sizeLods[i]-1,v=isFinite(s)?Math.PI/(2*d):2*Math.PI/(2*ds-1),y=s/v,m=isFinite(s)?1+Math.floor(h*y):ds;m>ds&&console.warn(`sigmaRadians, ${s}, is too large and will clip, as it requested ${m} samples when the maximum is set to ${ds}`);const c=[];let _=0;for(let b=0;b<ds;++b){const w=b/y,W=Math.exp(-w*w/2);c.push(W),b===0?_+=W:b<m&&(_+=2*W)}for(let b=0;b<c.length;b++)c[b]=c[b]/_;f.envMap.value=t.texture,f.samples.value=m,f.weights.value=c,f.latitudinal.value=r==="latitudinal",o&&(f.poleAxis.value=o);const{_lodMax:g}=this;f.dTheta.value=v,f.mipInt.value=g-i;const x=this._sizeLods[a],C=3*x*(a>g-Mr?a-g+Mr:0),R=4*(this._cubeSize-x);mu(n,C,R,3*x,2*x),l.setRenderTarget(n),l.render(p,dh)}}function bC(e){const t=[],n=[],i=[];let a=e;const s=e-Mr+1+l0.length;for(let r=0;r<s;r++){const o=Math.pow(2,a);n.push(o);let l=1/o;r>e-Mr?l=l0[r-e+Mr-1]:r===0&&(l=0),i.push(l);const u=1/(o-2),h=-u,p=1+u,f=[h,h,p,h,p,p,h,h,p,p,h,p],d=6,v=6,y=3,m=2,c=1,_=new Float32Array(y*v*d),g=new Float32Array(m*v*d),x=new Float32Array(c*v*d);for(let R=0;R<d;R++){const b=R%3*2/3-1,w=R>2?0:-1,W=[b,w,0,b+2/3,w,0,b+2/3,w+1,0,b,w,0,b+2/3,w+1,0,b,w+1,0];_.set(W,y*v*R),g.set(f,m*v*R);const S=[R,R,R,R,R,R];x.set(S,c*v*R)}const C=new wn;C.setAttribute("position",new si(_,y)),C.setAttribute("uv",new si(g,m)),C.setAttribute("faceIndex",new si(x,c)),t.push(C),a>Mr&&a--}return{lodPlanes:t,sizeLods:n,sigmas:i}}function h0(e,t,n){const i=new Ns(e,t,n);return i.texture.mapping=$c,i.texture.name="PMREM.cubeUv",i.scissorTest=!0,i}function mu(e,t,n,i,a){e.viewport.set(t,n,i,a),e.scissor.set(t,n,i,a)}function AC(e,t,n){const i=new Float32Array(ds),a=new P(0,1,0);return new Za({name:"SphericalGaussianBlur",defines:{n:ds,CUBEUV_TEXEL_WIDTH:1/t,CUBEUV_TEXEL_HEIGHT:1/n,CUBEUV_MAX_MIP:`${e}.0`},uniforms:{envMap:{value:null},samples:{value:1},weights:{value:i},latitudinal:{value:!1},dTheta:{value:0},mipInt:{value:0},poleAxis:{value:a}},vertexShader:Im(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			varying vec3 vOutputDirection;

			uniform sampler2D envMap;
			uniform int samples;
			uniform float weights[ n ];
			uniform bool latitudinal;
			uniform float dTheta;
			uniform float mipInt;
			uniform vec3 poleAxis;

			#define ENVMAP_TYPE_CUBE_UV
			#include <cube_uv_reflection_fragment>

			vec3 getSample( float theta, vec3 axis ) {

				float cosTheta = cos( theta );
				// Rodrigues' axis-angle rotation
				vec3 sampleDirection = vOutputDirection * cosTheta
					+ cross( axis, vOutputDirection ) * sin( theta )
					+ axis * dot( axis, vOutputDirection ) * ( 1.0 - cosTheta );

				return bilinearCubeUV( envMap, sampleDirection, mipInt );

			}

			void main() {

				vec3 axis = latitudinal ? poleAxis : cross( poleAxis, vOutputDirection );

				if ( all( equal( axis, vec3( 0.0 ) ) ) ) {

					axis = vec3( vOutputDirection.z, 0.0, - vOutputDirection.x );

				}

				axis = normalize( axis );

				gl_FragColor = vec4( 0.0, 0.0, 0.0, 1.0 );
				gl_FragColor.rgb += weights[ 0 ] * getSample( 0.0, axis );

				for ( int i = 1; i < n; i++ ) {

					if ( i >= samples ) {

						break;

					}

					float theta = dTheta * float( i );
					gl_FragColor.rgb += weights[ i ] * getSample( -1.0 * theta, axis );
					gl_FragColor.rgb += weights[ i ] * getSample( theta, axis );

				}

			}
		`,blending:Ga,depthTest:!1,depthWrite:!1})}function d0(){return new Za({name:"EquirectangularToCubeUV",uniforms:{envMap:{value:null}},vertexShader:Im(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			varying vec3 vOutputDirection;

			uniform sampler2D envMap;

			#include <common>

			void main() {

				vec3 outputDirection = normalize( vOutputDirection );
				vec2 uv = equirectUv( outputDirection );

				gl_FragColor = vec4( texture2D ( envMap, uv ).rgb, 1.0 );

			}
		`,blending:Ga,depthTest:!1,depthWrite:!1})}function p0(){return new Za({name:"CubemapToCubeUV",uniforms:{envMap:{value:null},flipEnvMap:{value:-1}},vertexShader:Im(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			uniform float flipEnvMap;

			varying vec3 vOutputDirection;

			uniform samplerCube envMap;

			void main() {

				gl_FragColor = textureCube( envMap, vec3( flipEnvMap * vOutputDirection.x, vOutputDirection.yz ) );

			}
		`,blending:Ga,depthTest:!1,depthWrite:!1})}function Im(){return`

		precision mediump float;
		precision mediump int;

		attribute float faceIndex;

		varying vec3 vOutputDirection;

		// RH coordinate system; PMREM face-indexing convention
		vec3 getDirection( vec2 uv, float face ) {

			uv = 2.0 * uv - 1.0;

			vec3 direction = vec3( uv, 1.0 );

			if ( face == 0.0 ) {

				direction = direction.zyx; // ( 1, v, u ) pos x

			} else if ( face == 1.0 ) {

				direction = direction.xzy;
				direction.xz *= -1.0; // ( -u, 1, -v ) pos y

			} else if ( face == 2.0 ) {

				direction.x *= -1.0; // ( -u, v, 1 ) pos z

			} else if ( face == 3.0 ) {

				direction = direction.zyx;
				direction.xz *= -1.0; // ( -1, v, -u ) neg x

			} else if ( face == 4.0 ) {

				direction = direction.xzy;
				direction.xy *= -1.0; // ( -u, -1, v ) neg y

			} else if ( face == 5.0 ) {

				direction.z *= -1.0; // ( u, v, -1 ) neg z

			}

			return direction;

		}

		void main() {

			vOutputDirection = getDirection( uv, faceIndex );
			gl_Position = vec4( position, 1.0 );

		}
	`}function RC(e){let t=new WeakMap,n=null;function i(o){if(o&&o.isTexture){const l=o.mapping,u=l===kd||l===Yd,h=l===Qr||l===Jr;if(u||h){let p=t.get(o);const f=p!==void 0?p.texture.pmremVersion:0;if(o.isRenderTargetTexture&&o.pmremVersion!==f)return n===null&&(n=new f0(e)),p=u?n.fromEquirectangular(o,p):n.fromCubemap(o,p),p.texture.pmremVersion=o.pmremVersion,t.set(o,p),p.texture;if(p!==void 0)return p.texture;{const d=o.image;return u&&d&&d.height>0||h&&d&&a(d)?(n===null&&(n=new f0(e)),p=u?n.fromEquirectangular(o):n.fromCubemap(o),p.texture.pmremVersion=o.pmremVersion,t.set(o,p),o.addEventListener("dispose",s),p.texture):null}}}return o}function a(o){let l=0;const u=6;for(let h=0;h<u;h++)o[h]!==void 0&&l++;return l===u}function s(o){const l=o.target;l.removeEventListener("dispose",s);const u=t.get(l);u!==void 0&&(t.delete(l),u.dispose())}function r(){t=new WeakMap,n!==null&&(n.dispose(),n=null)}return{get:i,dispose:r}}function CC(e){const t={};function n(i){if(t[i]!==void 0)return t[i];let a;switch(i){case"WEBGL_depth_texture":a=e.getExtension("WEBGL_depth_texture")||e.getExtension("MOZ_WEBGL_depth_texture")||e.getExtension("WEBKIT_WEBGL_depth_texture");break;case"EXT_texture_filter_anisotropic":a=e.getExtension("EXT_texture_filter_anisotropic")||e.getExtension("MOZ_EXT_texture_filter_anisotropic")||e.getExtension("WEBKIT_EXT_texture_filter_anisotropic");break;case"WEBGL_compressed_texture_s3tc":a=e.getExtension("WEBGL_compressed_texture_s3tc")||e.getExtension("MOZ_WEBGL_compressed_texture_s3tc")||e.getExtension("WEBKIT_WEBGL_compressed_texture_s3tc");break;case"WEBGL_compressed_texture_pvrtc":a=e.getExtension("WEBGL_compressed_texture_pvrtc")||e.getExtension("WEBKIT_WEBGL_compressed_texture_pvrtc");break;default:a=e.getExtension(i)}return t[i]=a,a}return{has:function(i){return n(i)!==null},init:function(){n("EXT_color_buffer_float"),n("WEBGL_clip_cull_distance"),n("OES_texture_float_linear"),n("EXT_color_buffer_half_float"),n("WEBGL_multisampled_render_to_texture"),n("WEBGL_render_shared_exponent")},get:function(i){const a=n(i);return a===null&&Wu("THREE.WebGLRenderer: "+i+" extension not supported."),a}}}function wC(e,t,n,i){const a={},s=new WeakMap;function r(p){const f=p.target;f.index!==null&&t.remove(f.index);for(const v in f.attributes)t.remove(f.attributes[v]);for(const v in f.morphAttributes){const y=f.morphAttributes[v];for(let m=0,c=y.length;m<c;m++)t.remove(y[m])}f.removeEventListener("dispose",r),delete a[f.id];const d=s.get(f);d&&(t.remove(d),s.delete(f)),i.releaseStatesOfGeometry(f),f.isInstancedBufferGeometry===!0&&delete f._maxInstanceCount,n.memory.geometries--}function o(p,f){return a[f.id]===!0||(f.addEventListener("dispose",r),a[f.id]=!0,n.memory.geometries++),f}function l(p){const f=p.attributes;for(const v in f)t.update(f[v],e.ARRAY_BUFFER);const d=p.morphAttributes;for(const v in d){const y=d[v];for(let m=0,c=y.length;m<c;m++)t.update(y[m],e.ARRAY_BUFFER)}}function u(p){const f=[],d=p.index,v=p.attributes.position;let y=0;if(d!==null){const _=d.array;y=d.version;for(let g=0,x=_.length;g<x;g+=3){const C=_[g+0],R=_[g+1],b=_[g+2];f.push(C,R,R,b,b,C)}}else if(v!==void 0){const _=v.array;y=v.version;for(let g=0,x=_.length/3-1;g<x;g+=3){const C=g+0,R=g+1,b=g+2;f.push(C,R,R,b,b,C)}}else return;const m=new(Sx(f)?bx:Tx)(f,1);m.version=y;const c=s.get(p);c&&t.remove(c),s.set(p,m)}function h(p){const f=s.get(p);if(f){const d=p.index;d!==null&&f.version<d.version&&u(p)}else u(p);return s.get(p)}return{get:o,update:l,getWireframeAttribute:h}}function DC(e,t,n){let i;function a(f){i=f}let s,r;function o(f){s=f.type,r=f.bytesPerElement}function l(f,d){e.drawElements(i,d,s,f*r),n.update(d,i,1)}function u(f,d,v){v!==0&&(e.drawElementsInstanced(i,d,s,f*r,v),n.update(d,i,v))}function h(f,d,v){if(v===0)return;t.get("WEBGL_multi_draw").multiDrawElementsWEBGL(i,d,0,s,f,0,v);let m=0;for(let c=0;c<v;c++)m+=d[c];n.update(m,i,1)}function p(f,d,v,y){if(v===0)return;const m=t.get("WEBGL_multi_draw");if(m===null)for(let c=0;c<f.length;c++)u(f[c]/r,d[c],y[c]);else{m.multiDrawElementsInstancedWEBGL(i,d,0,s,f,0,y,0,v);let c=0;for(let _=0;_<v;_++)c+=d[_];for(let _=0;_<y.length;_++)n.update(c,i,y[_])}}this.setMode=a,this.setIndex=o,this.render=l,this.renderInstances=u,this.renderMultiDraw=h,this.renderMultiDrawInstances=p}function UC(e){const t={geometries:0,textures:0},n={frame:0,calls:0,triangles:0,points:0,lines:0};function i(s,r,o){switch(n.calls++,r){case e.TRIANGLES:n.triangles+=o*(s/3);break;case e.LINES:n.lines+=o*(s/2);break;case e.LINE_STRIP:n.lines+=o*(s-1);break;case e.LINE_LOOP:n.lines+=o*s;break;case e.POINTS:n.points+=o*s;break;default:console.error("THREE.WebGLInfo: Unknown draw mode:",r);break}}function a(){n.calls=0,n.triangles=0,n.points=0,n.lines=0}return{memory:t,render:n,programs:null,autoReset:!0,reset:a,update:i}}function NC(e,t,n){const i=new WeakMap,a=new Ce;function s(r,o,l){const u=r.morphTargetInfluences,h=o.morphAttributes.position||o.morphAttributes.normal||o.morphAttributes.color,p=h!==void 0?h.length:0;let f=i.get(o);if(f===void 0||f.count!==p){let S=function(){w.dispose(),i.delete(o),o.removeEventListener("dispose",S)};var d=S;f!==void 0&&f.texture.dispose();const v=o.morphAttributes.position!==void 0,y=o.morphAttributes.normal!==void 0,m=o.morphAttributes.color!==void 0,c=o.morphAttributes.position||[],_=o.morphAttributes.normal||[],g=o.morphAttributes.color||[];let x=0;v===!0&&(x=1),y===!0&&(x=2),m===!0&&(x=3);let C=o.attributes.position.count*x,R=1;C>t.maxTextureSize&&(R=Math.ceil(C/t.maxTextureSize),C=t.maxTextureSize);const b=new Float32Array(C*R*4*p),w=new xx(b,C,R,p);w.type=ji,w.needsUpdate=!0;const W=x*4;for(let T=0;T<p;T++){const F=c[T],G=_[T],Y=g[T],K=C*R*4*T;for(let D=0;D<F.count;D++){const V=D*W;v===!0&&(a.fromBufferAttribute(F,D),b[K+V+0]=a.x,b[K+V+1]=a.y,b[K+V+2]=a.z,b[K+V+3]=0),y===!0&&(a.fromBufferAttribute(G,D),b[K+V+4]=a.x,b[K+V+5]=a.y,b[K+V+6]=a.z,b[K+V+7]=0),m===!0&&(a.fromBufferAttribute(Y,D),b[K+V+8]=a.x,b[K+V+9]=a.y,b[K+V+10]=a.z,b[K+V+11]=Y.itemSize===4?a.w:1)}}f={count:p,texture:w,size:new Lt(C,R)},i.set(o,f),o.addEventListener("dispose",S)}if(r.isInstancedMesh===!0&&r.morphTexture!==null)l.getUniforms().setValue(e,"morphTexture",r.morphTexture,n);else{let v=0;for(let m=0;m<u.length;m++)v+=u[m];const y=o.morphTargetsRelative?1:1-v;l.getUniforms().setValue(e,"morphTargetBaseInfluence",y),l.getUniforms().setValue(e,"morphTargetInfluences",u)}l.getUniforms().setValue(e,"morphTargetsTexture",f.texture,n),l.getUniforms().setValue(e,"morphTargetsTextureSize",f.size)}return{update:s}}function LC(e,t,n,i){let a=new WeakMap;function s(l){const u=i.render.frame,h=l.geometry,p=t.get(l,h);if(a.get(p)!==u&&(t.update(p),a.set(p,u)),l.isInstancedMesh&&(l.hasEventListener("dispose",o)===!1&&l.addEventListener("dispose",o),a.get(l)!==u&&(n.update(l.instanceMatrix,e.ARRAY_BUFFER),l.instanceColor!==null&&n.update(l.instanceColor,e.ARRAY_BUFFER),a.set(l,u))),l.isSkinnedMesh){const f=l.skeleton;a.get(f)!==u&&(f.update(),a.set(f,u))}return p}function r(){a=new WeakMap}function o(l){const u=l.target;u.removeEventListener("dispose",o),n.remove(u.instanceMatrix),u.instanceColor!==null&&n.remove(u.instanceColor)}return{update:s,dispose:r}}class Ux extends An{constructor(t,n,i,a,s,r,o,l,u,h=Pr){if(h!==Pr&&h!==to)throw new Error("DepthTexture format must be either THREE.DepthFormat or THREE.DepthStencilFormat");i===void 0&&h===Pr&&(i=Us),i===void 0&&h===to&&(i=$r),super(null,a,s,r,o,l,h,i,u),this.isDepthTexture=!0,this.image={width:t,height:n},this.magFilter=o!==void 0?o:ii,this.minFilter=l!==void 0?l:ii,this.flipY=!1,this.generateMipmaps=!1,this.compareFunction=null}copy(t){return super.copy(t),this.compareFunction=t.compareFunction,this}toJSON(t){const n=super.toJSON(t);return this.compareFunction!==null&&(n.compareFunction=this.compareFunction),n}}const Nx=new An,m0=new Ux(1,1),Lx=new xx,Ox=new S1,Px=new Cx,_0=[],g0=[],v0=new Float32Array(16),S0=new Float32Array(9),y0=new Float32Array(4);function fo(e,t,n){const i=e[0];if(i<=0||i>0)return e;const a=t*n;let s=_0[a];if(s===void 0&&(s=new Float32Array(a),_0[a]=s),t!==0){i.toArray(s,0);for(let r=1,o=0;r!==t;++r)o+=n,e[r].toArray(s,o)}return s}function He(e,t){if(e.length!==t.length)return!1;for(let n=0,i=e.length;n<i;n++)if(e[n]!==t[n])return!1;return!0}function Ge(e,t){for(let n=0,i=t.length;n<i;n++)e[n]=t[n]}function nf(e,t){let n=g0[t];n===void 0&&(n=new Int32Array(t),g0[t]=n);for(let i=0;i!==t;++i)n[i]=e.allocateTextureUnit();return n}function OC(e,t){const n=this.cache;n[0]!==t&&(e.uniform1f(this.addr,t),n[0]=t)}function PC(e,t){const n=this.cache;if(t.x!==void 0)(n[0]!==t.x||n[1]!==t.y)&&(e.uniform2f(this.addr,t.x,t.y),n[0]=t.x,n[1]=t.y);else{if(He(n,t))return;e.uniform2fv(this.addr,t),Ge(n,t)}}function zC(e,t){const n=this.cache;if(t.x!==void 0)(n[0]!==t.x||n[1]!==t.y||n[2]!==t.z)&&(e.uniform3f(this.addr,t.x,t.y,t.z),n[0]=t.x,n[1]=t.y,n[2]=t.z);else if(t.r!==void 0)(n[0]!==t.r||n[1]!==t.g||n[2]!==t.b)&&(e.uniform3f(this.addr,t.r,t.g,t.b),n[0]=t.r,n[1]=t.g,n[2]=t.b);else{if(He(n,t))return;e.uniform3fv(this.addr,t),Ge(n,t)}}function IC(e,t){const n=this.cache;if(t.x!==void 0)(n[0]!==t.x||n[1]!==t.y||n[2]!==t.z||n[3]!==t.w)&&(e.uniform4f(this.addr,t.x,t.y,t.z,t.w),n[0]=t.x,n[1]=t.y,n[2]=t.z,n[3]=t.w);else{if(He(n,t))return;e.uniform4fv(this.addr,t),Ge(n,t)}}function BC(e,t){const n=this.cache,i=t.elements;if(i===void 0){if(He(n,t))return;e.uniformMatrix2fv(this.addr,!1,t),Ge(n,t)}else{if(He(n,i))return;y0.set(i),e.uniformMatrix2fv(this.addr,!1,y0),Ge(n,i)}}function FC(e,t){const n=this.cache,i=t.elements;if(i===void 0){if(He(n,t))return;e.uniformMatrix3fv(this.addr,!1,t),Ge(n,t)}else{if(He(n,i))return;S0.set(i),e.uniformMatrix3fv(this.addr,!1,S0),Ge(n,i)}}function HC(e,t){const n=this.cache,i=t.elements;if(i===void 0){if(He(n,t))return;e.uniformMatrix4fv(this.addr,!1,t),Ge(n,t)}else{if(He(n,i))return;v0.set(i),e.uniformMatrix4fv(this.addr,!1,v0),Ge(n,i)}}function GC(e,t){const n=this.cache;n[0]!==t&&(e.uniform1i(this.addr,t),n[0]=t)}function VC(e,t){const n=this.cache;if(t.x!==void 0)(n[0]!==t.x||n[1]!==t.y)&&(e.uniform2i(this.addr,t.x,t.y),n[0]=t.x,n[1]=t.y);else{if(He(n,t))return;e.uniform2iv(this.addr,t),Ge(n,t)}}function XC(e,t){const n=this.cache;if(t.x!==void 0)(n[0]!==t.x||n[1]!==t.y||n[2]!==t.z)&&(e.uniform3i(this.addr,t.x,t.y,t.z),n[0]=t.x,n[1]=t.y,n[2]=t.z);else{if(He(n,t))return;e.uniform3iv(this.addr,t),Ge(n,t)}}function kC(e,t){const n=this.cache;if(t.x!==void 0)(n[0]!==t.x||n[1]!==t.y||n[2]!==t.z||n[3]!==t.w)&&(e.uniform4i(this.addr,t.x,t.y,t.z,t.w),n[0]=t.x,n[1]=t.y,n[2]=t.z,n[3]=t.w);else{if(He(n,t))return;e.uniform4iv(this.addr,t),Ge(n,t)}}function YC(e,t){const n=this.cache;n[0]!==t&&(e.uniform1ui(this.addr,t),n[0]=t)}function qC(e,t){const n=this.cache;if(t.x!==void 0)(n[0]!==t.x||n[1]!==t.y)&&(e.uniform2ui(this.addr,t.x,t.y),n[0]=t.x,n[1]=t.y);else{if(He(n,t))return;e.uniform2uiv(this.addr,t),Ge(n,t)}}function WC(e,t){const n=this.cache;if(t.x!==void 0)(n[0]!==t.x||n[1]!==t.y||n[2]!==t.z)&&(e.uniform3ui(this.addr,t.x,t.y,t.z),n[0]=t.x,n[1]=t.y,n[2]=t.z);else{if(He(n,t))return;e.uniform3uiv(this.addr,t),Ge(n,t)}}function jC(e,t){const n=this.cache;if(t.x!==void 0)(n[0]!==t.x||n[1]!==t.y||n[2]!==t.z||n[3]!==t.w)&&(e.uniform4ui(this.addr,t.x,t.y,t.z,t.w),n[0]=t.x,n[1]=t.y,n[2]=t.z,n[3]=t.w);else{if(He(n,t))return;e.uniform4uiv(this.addr,t),Ge(n,t)}}function ZC(e,t,n){const i=this.cache,a=n.allocateTextureUnit();i[0]!==a&&(e.uniform1i(this.addr,a),i[0]=a);let s;this.type===e.SAMPLER_2D_SHADOW?(m0.compareFunction=vx,s=m0):s=Nx,n.setTexture2D(t||s,a)}function KC(e,t,n){const i=this.cache,a=n.allocateTextureUnit();i[0]!==a&&(e.uniform1i(this.addr,a),i[0]=a),n.setTexture3D(t||Ox,a)}function QC(e,t,n){const i=this.cache,a=n.allocateTextureUnit();i[0]!==a&&(e.uniform1i(this.addr,a),i[0]=a),n.setTextureCube(t||Px,a)}function JC(e,t,n){const i=this.cache,a=n.allocateTextureUnit();i[0]!==a&&(e.uniform1i(this.addr,a),i[0]=a),n.setTexture2DArray(t||Lx,a)}function $C(e){switch(e){case 5126:return OC;case 35664:return PC;case 35665:return zC;case 35666:return IC;case 35674:return BC;case 35675:return FC;case 35676:return HC;case 5124:case 35670:return GC;case 35667:case 35671:return VC;case 35668:case 35672:return XC;case 35669:case 35673:return kC;case 5125:return YC;case 36294:return qC;case 36295:return WC;case 36296:return jC;case 35678:case 36198:case 36298:case 36306:case 35682:return ZC;case 35679:case 36299:case 36307:return KC;case 35680:case 36300:case 36308:case 36293:return QC;case 36289:case 36303:case 36311:case 36292:return JC}}function t2(e,t){e.uniform1fv(this.addr,t)}function e2(e,t){const n=fo(t,this.size,2);e.uniform2fv(this.addr,n)}function n2(e,t){const n=fo(t,this.size,3);e.uniform3fv(this.addr,n)}function i2(e,t){const n=fo(t,this.size,4);e.uniform4fv(this.addr,n)}function a2(e,t){const n=fo(t,this.size,4);e.uniformMatrix2fv(this.addr,!1,n)}function s2(e,t){const n=fo(t,this.size,9);e.uniformMatrix3fv(this.addr,!1,n)}function r2(e,t){const n=fo(t,this.size,16);e.uniformMatrix4fv(this.addr,!1,n)}function o2(e,t){e.uniform1iv(this.addr,t)}function l2(e,t){e.uniform2iv(this.addr,t)}function u2(e,t){e.uniform3iv(this.addr,t)}function c2(e,t){e.uniform4iv(this.addr,t)}function f2(e,t){e.uniform1uiv(this.addr,t)}function h2(e,t){e.uniform2uiv(this.addr,t)}function d2(e,t){e.uniform3uiv(this.addr,t)}function p2(e,t){e.uniform4uiv(this.addr,t)}function m2(e,t,n){const i=this.cache,a=t.length,s=nf(n,a);He(i,s)||(e.uniform1iv(this.addr,s),Ge(i,s));for(let r=0;r!==a;++r)n.setTexture2D(t[r]||Nx,s[r])}function _2(e,t,n){const i=this.cache,a=t.length,s=nf(n,a);He(i,s)||(e.uniform1iv(this.addr,s),Ge(i,s));for(let r=0;r!==a;++r)n.setTexture3D(t[r]||Ox,s[r])}function g2(e,t,n){const i=this.cache,a=t.length,s=nf(n,a);He(i,s)||(e.uniform1iv(this.addr,s),Ge(i,s));for(let r=0;r!==a;++r)n.setTextureCube(t[r]||Px,s[r])}function v2(e,t,n){const i=this.cache,a=t.length,s=nf(n,a);He(i,s)||(e.uniform1iv(this.addr,s),Ge(i,s));for(let r=0;r!==a;++r)n.setTexture2DArray(t[r]||Lx,s[r])}function S2(e){switch(e){case 5126:return t2;case 35664:return e2;case 35665:return n2;case 35666:return i2;case 35674:return a2;case 35675:return s2;case 35676:return r2;case 5124:case 35670:return o2;case 35667:case 35671:return l2;case 35668:case 35672:return u2;case 35669:case 35673:return c2;case 5125:return f2;case 36294:return h2;case 36295:return d2;case 36296:return p2;case 35678:case 36198:case 36298:case 36306:case 35682:return m2;case 35679:case 36299:case 36307:return _2;case 35680:case 36300:case 36308:case 36293:return g2;case 36289:case 36303:case 36311:case 36292:return v2}}class y2{constructor(t,n,i){this.id=t,this.addr=i,this.cache=[],this.type=n.type,this.setValue=$C(n.type)}}class x2{constructor(t,n,i){this.id=t,this.addr=i,this.cache=[],this.type=n.type,this.size=n.size,this.setValue=S2(n.type)}}class M2{constructor(t){this.id=t,this.seq=[],this.map={}}setValue(t,n,i){const a=this.seq;for(let s=0,r=a.length;s!==r;++s){const o=a[s];o.setValue(t,n[o.id],i)}}}const vh=/(\w+)(\])?(\[|\.)?/g;function x0(e,t){e.seq.push(t),e.map[t.id]=t}function E2(e,t,n){const i=e.name,a=i.length;for(vh.lastIndex=0;;){const s=vh.exec(i),r=vh.lastIndex;let o=s[1];const l=s[2]==="]",u=s[3];if(l&&(o=o|0),u===void 0||u==="["&&r+2===a){x0(n,u===void 0?new y2(o,e,t):new x2(o,e,t));break}else{let p=n.map[o];p===void 0&&(p=new M2(o),x0(n,p)),n=p}}}class ju{constructor(t,n){this.seq=[],this.map={};const i=t.getProgramParameter(n,t.ACTIVE_UNIFORMS);for(let a=0;a<i;++a){const s=t.getActiveUniform(n,a),r=t.getUniformLocation(n,s.name);E2(s,r,this)}}setValue(t,n,i,a){const s=this.map[n];s!==void 0&&s.setValue(t,i,a)}setOptional(t,n,i){const a=n[i];a!==void 0&&this.setValue(t,i,a)}static upload(t,n,i,a){for(let s=0,r=n.length;s!==r;++s){const o=n[s],l=i[o.id];l.needsUpdate!==!1&&o.setValue(t,l.value,a)}}static seqWithValue(t,n){const i=[];for(let a=0,s=t.length;a!==s;++a){const r=t[a];r.id in n&&i.push(r)}return i}}function M0(e,t,n){const i=e.createShader(t);return e.shaderSource(i,n),e.compileShader(i),i}const T2=37297;let b2=0;function A2(e,t){const n=e.split(`
`),i=[],a=Math.max(t-6,0),s=Math.min(t+6,n.length);for(let r=a;r<s;r++){const o=r+1;i.push(`${o===t?">":" "} ${o}: ${n[r]}`)}return i.join(`
`)}function R2(e){const t=ae.getPrimaries(ae.workingColorSpace),n=ae.getPrimaries(e);let i;switch(t===n?i="":t===Ac&&n===bc?i="LinearDisplayP3ToLinearSRGB":t===bc&&n===Ac&&(i="LinearSRGBToLinearDisplayP3"),e){case Ja:case tf:return[i,"LinearTransferOETF"];case Ti:case Om:return[i,"sRGBTransferOETF"];default:return console.warn("THREE.WebGLProgram: Unsupported color space:",e),[i,"LinearTransferOETF"]}}function E0(e,t,n){const i=e.getShaderParameter(t,e.COMPILE_STATUS),a=e.getShaderInfoLog(t).trim();if(i&&a==="")return"";const s=/ERROR: 0:(\d+)/.exec(a);if(s){const r=parseInt(s[1]);return n.toUpperCase()+`

`+a+`

`+A2(e.getShaderSource(t),r)}else return a}function C2(e,t){const n=R2(t);return`vec4 ${e}( vec4 value ) { return ${n[0]}( ${n[1]}( value ) ); }`}function w2(e,t){let n;switch(t){case Xb:n="Linear";break;case kb:n="Reinhard";break;case Yb:n="Cineon";break;case qb:n="ACESFilmic";break;case jb:n="AgX";break;case Zb:n="Neutral";break;case Wb:n="Custom";break;default:console.warn("THREE.WebGLProgram: Unsupported toneMapping:",t),n="Linear"}return"vec3 "+e+"( vec3 color ) { return "+n+"ToneMapping( color ); }"}const _u=new P;function D2(){ae.getLuminanceCoefficients(_u);const e=_u.x.toFixed(4),t=_u.y.toFixed(4),n=_u.z.toFixed(4);return["float luminance( const in vec3 rgb ) {",`	const vec3 weights = vec3( ${e}, ${t}, ${n} );`,"	return dot( weights, rgb );","}"].join(`
`)}function U2(e){return[e.extensionClipCullDistance?"#extension GL_ANGLE_clip_cull_distance : require":"",e.extensionMultiDraw?"#extension GL_ANGLE_multi_draw : require":""].filter(No).join(`
`)}function N2(e){const t=[];for(const n in e){const i=e[n];i!==!1&&t.push("#define "+n+" "+i)}return t.join(`
`)}function L2(e,t){const n={},i=e.getProgramParameter(t,e.ACTIVE_ATTRIBUTES);for(let a=0;a<i;a++){const s=e.getActiveAttrib(t,a),r=s.name;let o=1;s.type===e.FLOAT_MAT2&&(o=2),s.type===e.FLOAT_MAT3&&(o=3),s.type===e.FLOAT_MAT4&&(o=4),n[r]={type:s.type,location:e.getAttribLocation(t,r),locationSize:o}}return n}function No(e){return e!==""}function T0(e,t){const n=t.numSpotLightShadows+t.numSpotLightMaps-t.numSpotLightShadowsWithMaps;return e.replace(/NUM_DIR_LIGHTS/g,t.numDirLights).replace(/NUM_SPOT_LIGHTS/g,t.numSpotLights).replace(/NUM_SPOT_LIGHT_MAPS/g,t.numSpotLightMaps).replace(/NUM_SPOT_LIGHT_COORDS/g,n).replace(/NUM_RECT_AREA_LIGHTS/g,t.numRectAreaLights).replace(/NUM_POINT_LIGHTS/g,t.numPointLights).replace(/NUM_HEMI_LIGHTS/g,t.numHemiLights).replace(/NUM_DIR_LIGHT_SHADOWS/g,t.numDirLightShadows).replace(/NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS/g,t.numSpotLightShadowsWithMaps).replace(/NUM_SPOT_LIGHT_SHADOWS/g,t.numSpotLightShadows).replace(/NUM_POINT_LIGHT_SHADOWS/g,t.numPointLightShadows)}function b0(e,t){return e.replace(/NUM_CLIPPING_PLANES/g,t.numClippingPlanes).replace(/UNION_CLIPPING_PLANES/g,t.numClippingPlanes-t.numClipIntersection)}const O2=/^[ \t]*#include +<([\w\d./]+)>/gm;function xp(e){return e.replace(O2,z2)}const P2=new Map;function z2(e,t){let n=Ot[t];if(n===void 0){const i=P2.get(t);if(i!==void 0)n=Ot[i],console.warn('THREE.WebGLRenderer: Shader chunk "%s" has been deprecated. Use "%s" instead.',t,i);else throw new Error("Can not resolve #include <"+t+">")}return xp(n)}const I2=/#pragma unroll_loop_start\s+for\s*\(\s*int\s+i\s*=\s*(\d+)\s*;\s*i\s*<\s*(\d+)\s*;\s*i\s*\+\+\s*\)\s*{([\s\S]+?)}\s+#pragma unroll_loop_end/g;function A0(e){return e.replace(I2,B2)}function B2(e,t,n,i){let a="";for(let s=parseInt(t);s<parseInt(n);s++)a+=i.replace(/\[\s*i\s*\]/g,"[ "+s+" ]").replace(/UNROLLED_LOOP_INDEX/g,s);return a}function R0(e){let t=`precision ${e.precision} float;
	precision ${e.precision} int;
	precision ${e.precision} sampler2D;
	precision ${e.precision} samplerCube;
	precision ${e.precision} sampler3D;
	precision ${e.precision} sampler2DArray;
	precision ${e.precision} sampler2DShadow;
	precision ${e.precision} samplerCubeShadow;
	precision ${e.precision} sampler2DArrayShadow;
	precision ${e.precision} isampler2D;
	precision ${e.precision} isampler3D;
	precision ${e.precision} isamplerCube;
	precision ${e.precision} isampler2DArray;
	precision ${e.precision} usampler2D;
	precision ${e.precision} usampler3D;
	precision ${e.precision} usamplerCube;
	precision ${e.precision} usampler2DArray;
	`;return e.precision==="highp"?t+=`
#define HIGH_PRECISION`:e.precision==="mediump"?t+=`
#define MEDIUM_PRECISION`:e.precision==="lowp"&&(t+=`
#define LOW_PRECISION`),t}function F2(e){let t="SHADOWMAP_TYPE_BASIC";return e.shadowMapType===sx?t="SHADOWMAP_TYPE_PCF":e.shadowMapType===Mb?t="SHADOWMAP_TYPE_PCF_SOFT":e.shadowMapType===Yi&&(t="SHADOWMAP_TYPE_VSM"),t}function H2(e){let t="ENVMAP_TYPE_CUBE";if(e.envMap)switch(e.envMapMode){case Qr:case Jr:t="ENVMAP_TYPE_CUBE";break;case $c:t="ENVMAP_TYPE_CUBE_UV";break}return t}function G2(e){let t="ENVMAP_MODE_REFLECTION";if(e.envMap)switch(e.envMapMode){case Jr:t="ENVMAP_MODE_REFRACTION";break}return t}function V2(e){let t="ENVMAP_BLENDING_NONE";if(e.envMap)switch(e.combine){case rx:t="ENVMAP_BLENDING_MULTIPLY";break;case Gb:t="ENVMAP_BLENDING_MIX";break;case Vb:t="ENVMAP_BLENDING_ADD";break}return t}function X2(e){const t=e.envMapCubeUVHeight;if(t===null)return null;const n=Math.log2(t)-2,i=1/t;return{texelWidth:1/(3*Math.max(Math.pow(2,n),7*16)),texelHeight:i,maxMip:n}}function k2(e,t,n,i){const a=e.getContext(),s=n.defines;let r=n.vertexShader,o=n.fragmentShader;const l=F2(n),u=H2(n),h=G2(n),p=V2(n),f=X2(n),d=U2(n),v=N2(s),y=a.createProgram();let m,c,_=n.glslVersion?"#version "+n.glslVersion+`
`:"";n.isRawShaderMaterial?(m=["#define SHADER_TYPE "+n.shaderType,"#define SHADER_NAME "+n.shaderName,v].filter(No).join(`
`),m.length>0&&(m+=`
`),c=["#define SHADER_TYPE "+n.shaderType,"#define SHADER_NAME "+n.shaderName,v].filter(No).join(`
`),c.length>0&&(c+=`
`)):(m=[R0(n),"#define SHADER_TYPE "+n.shaderType,"#define SHADER_NAME "+n.shaderName,v,n.extensionClipCullDistance?"#define USE_CLIP_DISTANCE":"",n.batching?"#define USE_BATCHING":"",n.batchingColor?"#define USE_BATCHING_COLOR":"",n.instancing?"#define USE_INSTANCING":"",n.instancingColor?"#define USE_INSTANCING_COLOR":"",n.instancingMorph?"#define USE_INSTANCING_MORPH":"",n.useFog&&n.fog?"#define USE_FOG":"",n.useFog&&n.fogExp2?"#define FOG_EXP2":"",n.map?"#define USE_MAP":"",n.envMap?"#define USE_ENVMAP":"",n.envMap?"#define "+h:"",n.lightMap?"#define USE_LIGHTMAP":"",n.aoMap?"#define USE_AOMAP":"",n.bumpMap?"#define USE_BUMPMAP":"",n.normalMap?"#define USE_NORMALMAP":"",n.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",n.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",n.displacementMap?"#define USE_DISPLACEMENTMAP":"",n.emissiveMap?"#define USE_EMISSIVEMAP":"",n.anisotropy?"#define USE_ANISOTROPY":"",n.anisotropyMap?"#define USE_ANISOTROPYMAP":"",n.clearcoatMap?"#define USE_CLEARCOATMAP":"",n.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",n.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",n.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",n.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",n.specularMap?"#define USE_SPECULARMAP":"",n.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",n.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",n.roughnessMap?"#define USE_ROUGHNESSMAP":"",n.metalnessMap?"#define USE_METALNESSMAP":"",n.alphaMap?"#define USE_ALPHAMAP":"",n.alphaHash?"#define USE_ALPHAHASH":"",n.transmission?"#define USE_TRANSMISSION":"",n.transmissionMap?"#define USE_TRANSMISSIONMAP":"",n.thicknessMap?"#define USE_THICKNESSMAP":"",n.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",n.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",n.mapUv?"#define MAP_UV "+n.mapUv:"",n.alphaMapUv?"#define ALPHAMAP_UV "+n.alphaMapUv:"",n.lightMapUv?"#define LIGHTMAP_UV "+n.lightMapUv:"",n.aoMapUv?"#define AOMAP_UV "+n.aoMapUv:"",n.emissiveMapUv?"#define EMISSIVEMAP_UV "+n.emissiveMapUv:"",n.bumpMapUv?"#define BUMPMAP_UV "+n.bumpMapUv:"",n.normalMapUv?"#define NORMALMAP_UV "+n.normalMapUv:"",n.displacementMapUv?"#define DISPLACEMENTMAP_UV "+n.displacementMapUv:"",n.metalnessMapUv?"#define METALNESSMAP_UV "+n.metalnessMapUv:"",n.roughnessMapUv?"#define ROUGHNESSMAP_UV "+n.roughnessMapUv:"",n.anisotropyMapUv?"#define ANISOTROPYMAP_UV "+n.anisotropyMapUv:"",n.clearcoatMapUv?"#define CLEARCOATMAP_UV "+n.clearcoatMapUv:"",n.clearcoatNormalMapUv?"#define CLEARCOAT_NORMALMAP_UV "+n.clearcoatNormalMapUv:"",n.clearcoatRoughnessMapUv?"#define CLEARCOAT_ROUGHNESSMAP_UV "+n.clearcoatRoughnessMapUv:"",n.iridescenceMapUv?"#define IRIDESCENCEMAP_UV "+n.iridescenceMapUv:"",n.iridescenceThicknessMapUv?"#define IRIDESCENCE_THICKNESSMAP_UV "+n.iridescenceThicknessMapUv:"",n.sheenColorMapUv?"#define SHEEN_COLORMAP_UV "+n.sheenColorMapUv:"",n.sheenRoughnessMapUv?"#define SHEEN_ROUGHNESSMAP_UV "+n.sheenRoughnessMapUv:"",n.specularMapUv?"#define SPECULARMAP_UV "+n.specularMapUv:"",n.specularColorMapUv?"#define SPECULAR_COLORMAP_UV "+n.specularColorMapUv:"",n.specularIntensityMapUv?"#define SPECULAR_INTENSITYMAP_UV "+n.specularIntensityMapUv:"",n.transmissionMapUv?"#define TRANSMISSIONMAP_UV "+n.transmissionMapUv:"",n.thicknessMapUv?"#define THICKNESSMAP_UV "+n.thicknessMapUv:"",n.vertexTangents&&n.flatShading===!1?"#define USE_TANGENT":"",n.vertexColors?"#define USE_COLOR":"",n.vertexAlphas?"#define USE_COLOR_ALPHA":"",n.vertexUv1s?"#define USE_UV1":"",n.vertexUv2s?"#define USE_UV2":"",n.vertexUv3s?"#define USE_UV3":"",n.pointsUvs?"#define USE_POINTS_UV":"",n.flatShading?"#define FLAT_SHADED":"",n.skinning?"#define USE_SKINNING":"",n.morphTargets?"#define USE_MORPHTARGETS":"",n.morphNormals&&n.flatShading===!1?"#define USE_MORPHNORMALS":"",n.morphColors?"#define USE_MORPHCOLORS":"",n.morphTargetsCount>0?"#define MORPHTARGETS_TEXTURE_STRIDE "+n.morphTextureStride:"",n.morphTargetsCount>0?"#define MORPHTARGETS_COUNT "+n.morphTargetsCount:"",n.doubleSided?"#define DOUBLE_SIDED":"",n.flipSided?"#define FLIP_SIDED":"",n.shadowMapEnabled?"#define USE_SHADOWMAP":"",n.shadowMapEnabled?"#define "+l:"",n.sizeAttenuation?"#define USE_SIZEATTENUATION":"",n.numLightProbes>0?"#define USE_LIGHT_PROBES":"",n.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",n.reverseDepthBuffer?"#define USE_REVERSEDEPTHBUF":"","uniform mat4 modelMatrix;","uniform mat4 modelViewMatrix;","uniform mat4 projectionMatrix;","uniform mat4 viewMatrix;","uniform mat3 normalMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;","#ifdef USE_INSTANCING","	attribute mat4 instanceMatrix;","#endif","#ifdef USE_INSTANCING_COLOR","	attribute vec3 instanceColor;","#endif","#ifdef USE_INSTANCING_MORPH","	uniform sampler2D morphTexture;","#endif","attribute vec3 position;","attribute vec3 normal;","attribute vec2 uv;","#ifdef USE_UV1","	attribute vec2 uv1;","#endif","#ifdef USE_UV2","	attribute vec2 uv2;","#endif","#ifdef USE_UV3","	attribute vec2 uv3;","#endif","#ifdef USE_TANGENT","	attribute vec4 tangent;","#endif","#if defined( USE_COLOR_ALPHA )","	attribute vec4 color;","#elif defined( USE_COLOR )","	attribute vec3 color;","#endif","#ifdef USE_SKINNING","	attribute vec4 skinIndex;","	attribute vec4 skinWeight;","#endif",`
`].filter(No).join(`
`),c=[R0(n),"#define SHADER_TYPE "+n.shaderType,"#define SHADER_NAME "+n.shaderName,v,n.useFog&&n.fog?"#define USE_FOG":"",n.useFog&&n.fogExp2?"#define FOG_EXP2":"",n.alphaToCoverage?"#define ALPHA_TO_COVERAGE":"",n.map?"#define USE_MAP":"",n.matcap?"#define USE_MATCAP":"",n.envMap?"#define USE_ENVMAP":"",n.envMap?"#define "+u:"",n.envMap?"#define "+h:"",n.envMap?"#define "+p:"",f?"#define CUBEUV_TEXEL_WIDTH "+f.texelWidth:"",f?"#define CUBEUV_TEXEL_HEIGHT "+f.texelHeight:"",f?"#define CUBEUV_MAX_MIP "+f.maxMip+".0":"",n.lightMap?"#define USE_LIGHTMAP":"",n.aoMap?"#define USE_AOMAP":"",n.bumpMap?"#define USE_BUMPMAP":"",n.normalMap?"#define USE_NORMALMAP":"",n.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",n.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",n.emissiveMap?"#define USE_EMISSIVEMAP":"",n.anisotropy?"#define USE_ANISOTROPY":"",n.anisotropyMap?"#define USE_ANISOTROPYMAP":"",n.clearcoat?"#define USE_CLEARCOAT":"",n.clearcoatMap?"#define USE_CLEARCOATMAP":"",n.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",n.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",n.dispersion?"#define USE_DISPERSION":"",n.iridescence?"#define USE_IRIDESCENCE":"",n.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",n.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",n.specularMap?"#define USE_SPECULARMAP":"",n.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",n.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",n.roughnessMap?"#define USE_ROUGHNESSMAP":"",n.metalnessMap?"#define USE_METALNESSMAP":"",n.alphaMap?"#define USE_ALPHAMAP":"",n.alphaTest?"#define USE_ALPHATEST":"",n.alphaHash?"#define USE_ALPHAHASH":"",n.sheen?"#define USE_SHEEN":"",n.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",n.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",n.transmission?"#define USE_TRANSMISSION":"",n.transmissionMap?"#define USE_TRANSMISSIONMAP":"",n.thicknessMap?"#define USE_THICKNESSMAP":"",n.vertexTangents&&n.flatShading===!1?"#define USE_TANGENT":"",n.vertexColors||n.instancingColor||n.batchingColor?"#define USE_COLOR":"",n.vertexAlphas?"#define USE_COLOR_ALPHA":"",n.vertexUv1s?"#define USE_UV1":"",n.vertexUv2s?"#define USE_UV2":"",n.vertexUv3s?"#define USE_UV3":"",n.pointsUvs?"#define USE_POINTS_UV":"",n.gradientMap?"#define USE_GRADIENTMAP":"",n.flatShading?"#define FLAT_SHADED":"",n.doubleSided?"#define DOUBLE_SIDED":"",n.flipSided?"#define FLIP_SIDED":"",n.shadowMapEnabled?"#define USE_SHADOWMAP":"",n.shadowMapEnabled?"#define "+l:"",n.premultipliedAlpha?"#define PREMULTIPLIED_ALPHA":"",n.numLightProbes>0?"#define USE_LIGHT_PROBES":"",n.decodeVideoTexture?"#define DECODE_VIDEO_TEXTURE":"",n.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",n.reverseDepthBuffer?"#define USE_REVERSEDEPTHBUF":"","uniform mat4 viewMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;",n.toneMapping!==Va?"#define TONE_MAPPING":"",n.toneMapping!==Va?Ot.tonemapping_pars_fragment:"",n.toneMapping!==Va?w2("toneMapping",n.toneMapping):"",n.dithering?"#define DITHERING":"",n.opaque?"#define OPAQUE":"",Ot.colorspace_pars_fragment,C2("linearToOutputTexel",n.outputColorSpace),D2(),n.useDepthPacking?"#define DEPTH_PACKING "+n.depthPacking:"",`
`].filter(No).join(`
`)),r=xp(r),r=T0(r,n),r=b0(r,n),o=xp(o),o=T0(o,n),o=b0(o,n),r=A0(r),o=A0(o),n.isRawShaderMaterial!==!0&&(_=`#version 300 es
`,m=[d,"#define attribute in","#define varying out","#define texture2D texture"].join(`
`)+`
`+m,c=["#define varying in",n.glslVersion===kg?"":"layout(location = 0) out highp vec4 pc_fragColor;",n.glslVersion===kg?"":"#define gl_FragColor pc_fragColor","#define gl_FragDepthEXT gl_FragDepth","#define texture2D texture","#define textureCube texture","#define texture2DProj textureProj","#define texture2DLodEXT textureLod","#define texture2DProjLodEXT textureProjLod","#define textureCubeLodEXT textureLod","#define texture2DGradEXT textureGrad","#define texture2DProjGradEXT textureProjGrad","#define textureCubeGradEXT textureGrad"].join(`
`)+`
`+c);const g=_+m+r,x=_+c+o,C=M0(a,a.VERTEX_SHADER,g),R=M0(a,a.FRAGMENT_SHADER,x);a.attachShader(y,C),a.attachShader(y,R),n.index0AttributeName!==void 0?a.bindAttribLocation(y,0,n.index0AttributeName):n.morphTargets===!0&&a.bindAttribLocation(y,0,"position"),a.linkProgram(y);function b(T){if(e.debug.checkShaderErrors){const F=a.getProgramInfoLog(y).trim(),G=a.getShaderInfoLog(C).trim(),Y=a.getShaderInfoLog(R).trim();let K=!0,D=!0;if(a.getProgramParameter(y,a.LINK_STATUS)===!1)if(K=!1,typeof e.debug.onShaderError=="function")e.debug.onShaderError(a,y,C,R);else{const V=E0(a,C,"vertex"),z=E0(a,R,"fragment");console.error("THREE.WebGLProgram: Shader Error "+a.getError()+" - VALIDATE_STATUS "+a.getProgramParameter(y,a.VALIDATE_STATUS)+`

Material Name: `+T.name+`
Material Type: `+T.type+`

Program Info Log: `+F+`
`+V+`
`+z)}else F!==""?console.warn("THREE.WebGLProgram: Program Info Log:",F):(G===""||Y==="")&&(D=!1);D&&(T.diagnostics={runnable:K,programLog:F,vertexShader:{log:G,prefix:m},fragmentShader:{log:Y,prefix:c}})}a.deleteShader(C),a.deleteShader(R),w=new ju(a,y),W=L2(a,y)}let w;this.getUniforms=function(){return w===void 0&&b(this),w};let W;this.getAttributes=function(){return W===void 0&&b(this),W};let S=n.rendererExtensionParallelShaderCompile===!1;return this.isReady=function(){return S===!1&&(S=a.getProgramParameter(y,T2)),S},this.destroy=function(){i.releaseStatesOfProgram(this),a.deleteProgram(y),this.program=void 0},this.type=n.shaderType,this.name=n.shaderName,this.id=b2++,this.cacheKey=t,this.usedTimes=1,this.program=y,this.vertexShader=C,this.fragmentShader=R,this}let Y2=0;class q2{constructor(){this.shaderCache=new Map,this.materialCache=new Map}update(t){const n=t.vertexShader,i=t.fragmentShader,a=this._getShaderStage(n),s=this._getShaderStage(i),r=this._getShaderCacheForMaterial(t);return r.has(a)===!1&&(r.add(a),a.usedTimes++),r.has(s)===!1&&(r.add(s),s.usedTimes++),this}remove(t){const n=this.materialCache.get(t);for(const i of n)i.usedTimes--,i.usedTimes===0&&this.shaderCache.delete(i.code);return this.materialCache.delete(t),this}getVertexShaderID(t){return this._getShaderStage(t.vertexShader).id}getFragmentShaderID(t){return this._getShaderStage(t.fragmentShader).id}dispose(){this.shaderCache.clear(),this.materialCache.clear()}_getShaderCacheForMaterial(t){const n=this.materialCache;let i=n.get(t);return i===void 0&&(i=new Set,n.set(t,i)),i}_getShaderStage(t){const n=this.shaderCache;let i=n.get(t);return i===void 0&&(i=new W2(t),n.set(t,i)),i}}class W2{constructor(t){this.id=Y2++,this.code=t,this.usedTimes=0}}function j2(e,t,n,i,a,s,r){const o=new Mx,l=new q2,u=new Set,h=[],p=a.logarithmicDepthBuffer,f=a.reverseDepthBuffer,d=a.vertexTextures;let v=a.precision;const y={MeshDepthMaterial:"depth",MeshDistanceMaterial:"distanceRGBA",MeshNormalMaterial:"normal",MeshBasicMaterial:"basic",MeshLambertMaterial:"lambert",MeshPhongMaterial:"phong",MeshToonMaterial:"toon",MeshStandardMaterial:"physical",MeshPhysicalMaterial:"physical",MeshMatcapMaterial:"matcap",LineBasicMaterial:"basic",LineDashedMaterial:"dashed",PointsMaterial:"points",ShadowMaterial:"shadow",SpriteMaterial:"sprite"};function m(S){return u.add(S),S===0?"uv":`uv${S}`}function c(S,T,F,G,Y){const K=G.fog,D=Y.geometry,V=S.isMeshStandardMaterial?G.environment:null,z=(S.isMeshStandardMaterial?n:t).get(S.envMap||V),tt=z&&z.mapping===$c?z.image.height:null,it=y[S.type];S.precision!==null&&(v=a.getMaxPrecision(S.precision),v!==S.precision&&console.warn("THREE.WebGLProgram.getParameters:",S.precision,"not supported, using",v,"instead."));const ht=D.morphAttributes.position||D.morphAttributes.normal||D.morphAttributes.color,Ft=ht!==void 0?ht.length:0;let kt=0;D.morphAttributes.position!==void 0&&(kt=1),D.morphAttributes.normal!==void 0&&(kt=2),D.morphAttributes.color!==void 0&&(kt=3);let k,$,_t,ct;if(it){const _n=Ai[it];k=_n.vertexShader,$=_n.fragmentShader}else k=S.vertexShader,$=S.fragmentShader,l.update(S),_t=l.getVertexShaderID(S),ct=l.getFragmentShaderID(S);const Dt=e.getRenderTarget(),Et=Y.isInstancedMesh===!0,Yt=Y.isBatchedMesh===!0,ue=!!S.map,qt=!!S.matcap,U=!!z,Dn=!!S.aoMap,Vt=!!S.lightMap,jt=!!S.bumpMap,bt=!!S.normalMap,Se=!!S.displacementMap,wt=!!S.emissiveMap,A=!!S.metalnessMap,M=!!S.roughnessMap,I=S.anisotropy>0,Z=S.clearcoat>0,J=S.dispersion>0,j=S.iridescence>0,vt=S.sheen>0,st=S.transmission>0,ft=I&&!!S.anisotropyMap,Zt=Z&&!!S.clearcoatMap,et=Z&&!!S.clearcoatNormalMap,dt=Z&&!!S.clearcoatRoughnessMap,At=j&&!!S.iridescenceMap,Rt=j&&!!S.iridescenceThicknessMap,pt=vt&&!!S.sheenColorMap,Xt=vt&&!!S.sheenRoughnessMap,Ut=!!S.specularMap,pe=!!S.specularColorMap,N=!!S.specularIntensityMap,lt=st&&!!S.transmissionMap,X=st&&!!S.thicknessMap,Q=!!S.gradientMap,rt=!!S.alphaMap,ut=S.alphaTest>0,Wt=!!S.alphaHash,Ue=!!S.extensions;let mn=Va;S.toneMapped&&(Dt===null||Dt.isXRRenderTarget===!0)&&(mn=e.toneMapping);const Jt={shaderID:it,shaderType:S.type,shaderName:S.name,vertexShader:k,fragmentShader:$,defines:S.defines,customVertexShaderID:_t,customFragmentShaderID:ct,isRawShaderMaterial:S.isRawShaderMaterial===!0,glslVersion:S.glslVersion,precision:v,batching:Yt,batchingColor:Yt&&Y._colorsTexture!==null,instancing:Et,instancingColor:Et&&Y.instanceColor!==null,instancingMorph:Et&&Y.morphTexture!==null,supportsVertexTextures:d,outputColorSpace:Dt===null?e.outputColorSpace:Dt.isXRRenderTarget===!0?Dt.texture.colorSpace:Ja,alphaToCoverage:!!S.alphaToCoverage,map:ue,matcap:qt,envMap:U,envMapMode:U&&z.mapping,envMapCubeUVHeight:tt,aoMap:Dn,lightMap:Vt,bumpMap:jt,normalMap:bt,displacementMap:d&&Se,emissiveMap:wt,normalMapObjectSpace:bt&&S.normalMapType===t1,normalMapTangentSpace:bt&&S.normalMapType===$b,metalnessMap:A,roughnessMap:M,anisotropy:I,anisotropyMap:ft,clearcoat:Z,clearcoatMap:Zt,clearcoatNormalMap:et,clearcoatRoughnessMap:dt,dispersion:J,iridescence:j,iridescenceMap:At,iridescenceThicknessMap:Rt,sheen:vt,sheenColorMap:pt,sheenRoughnessMap:Xt,specularMap:Ut,specularColorMap:pe,specularIntensityMap:N,transmission:st,transmissionMap:lt,thicknessMap:X,gradientMap:Q,opaque:S.transparent===!1&&S.blending===Or&&S.alphaToCoverage===!1,alphaMap:rt,alphaTest:ut,alphaHash:Wt,combine:S.combine,mapUv:ue&&m(S.map.channel),aoMapUv:Dn&&m(S.aoMap.channel),lightMapUv:Vt&&m(S.lightMap.channel),bumpMapUv:jt&&m(S.bumpMap.channel),normalMapUv:bt&&m(S.normalMap.channel),displacementMapUv:Se&&m(S.displacementMap.channel),emissiveMapUv:wt&&m(S.emissiveMap.channel),metalnessMapUv:A&&m(S.metalnessMap.channel),roughnessMapUv:M&&m(S.roughnessMap.channel),anisotropyMapUv:ft&&m(S.anisotropyMap.channel),clearcoatMapUv:Zt&&m(S.clearcoatMap.channel),clearcoatNormalMapUv:et&&m(S.clearcoatNormalMap.channel),clearcoatRoughnessMapUv:dt&&m(S.clearcoatRoughnessMap.channel),iridescenceMapUv:At&&m(S.iridescenceMap.channel),iridescenceThicknessMapUv:Rt&&m(S.iridescenceThicknessMap.channel),sheenColorMapUv:pt&&m(S.sheenColorMap.channel),sheenRoughnessMapUv:Xt&&m(S.sheenRoughnessMap.channel),specularMapUv:Ut&&m(S.specularMap.channel),specularColorMapUv:pe&&m(S.specularColorMap.channel),specularIntensityMapUv:N&&m(S.specularIntensityMap.channel),transmissionMapUv:lt&&m(S.transmissionMap.channel),thicknessMapUv:X&&m(S.thicknessMap.channel),alphaMapUv:rt&&m(S.alphaMap.channel),vertexTangents:!!D.attributes.tangent&&(bt||I),vertexColors:S.vertexColors,vertexAlphas:S.vertexColors===!0&&!!D.attributes.color&&D.attributes.color.itemSize===4,pointsUvs:Y.isPoints===!0&&!!D.attributes.uv&&(ue||rt),fog:!!K,useFog:S.fog===!0,fogExp2:!!K&&K.isFogExp2,flatShading:S.flatShading===!0,sizeAttenuation:S.sizeAttenuation===!0,logarithmicDepthBuffer:p,reverseDepthBuffer:f,skinning:Y.isSkinnedMesh===!0,morphTargets:D.morphAttributes.position!==void 0,morphNormals:D.morphAttributes.normal!==void 0,morphColors:D.morphAttributes.color!==void 0,morphTargetsCount:Ft,morphTextureStride:kt,numDirLights:T.directional.length,numPointLights:T.point.length,numSpotLights:T.spot.length,numSpotLightMaps:T.spotLightMap.length,numRectAreaLights:T.rectArea.length,numHemiLights:T.hemi.length,numDirLightShadows:T.directionalShadowMap.length,numPointLightShadows:T.pointShadowMap.length,numSpotLightShadows:T.spotShadowMap.length,numSpotLightShadowsWithMaps:T.numSpotLightShadowsWithMaps,numLightProbes:T.numLightProbes,numClippingPlanes:r.numPlanes,numClipIntersection:r.numIntersection,dithering:S.dithering,shadowMapEnabled:e.shadowMap.enabled&&F.length>0,shadowMapType:e.shadowMap.type,toneMapping:mn,decodeVideoTexture:ue&&S.map.isVideoTexture===!0&&ae.getTransfer(S.map.colorSpace)===xe,premultipliedAlpha:S.premultipliedAlpha,doubleSided:S.side===pi,flipSided:S.side===bn,useDepthPacking:S.depthPacking>=0,depthPacking:S.depthPacking||0,index0AttributeName:S.index0AttributeName,extensionClipCullDistance:Ue&&S.extensions.clipCullDistance===!0&&i.has("WEBGL_clip_cull_distance"),extensionMultiDraw:(Ue&&S.extensions.multiDraw===!0||Yt)&&i.has("WEBGL_multi_draw"),rendererExtensionParallelShaderCompile:i.has("KHR_parallel_shader_compile"),customProgramCacheKey:S.customProgramCacheKey()};return Jt.vertexUv1s=u.has(1),Jt.vertexUv2s=u.has(2),Jt.vertexUv3s=u.has(3),u.clear(),Jt}function _(S){const T=[];if(S.shaderID?T.push(S.shaderID):(T.push(S.customVertexShaderID),T.push(S.customFragmentShaderID)),S.defines!==void 0)for(const F in S.defines)T.push(F),T.push(S.defines[F]);return S.isRawShaderMaterial===!1&&(g(T,S),x(T,S),T.push(e.outputColorSpace)),T.push(S.customProgramCacheKey),T.join()}function g(S,T){S.push(T.precision),S.push(T.outputColorSpace),S.push(T.envMapMode),S.push(T.envMapCubeUVHeight),S.push(T.mapUv),S.push(T.alphaMapUv),S.push(T.lightMapUv),S.push(T.aoMapUv),S.push(T.bumpMapUv),S.push(T.normalMapUv),S.push(T.displacementMapUv),S.push(T.emissiveMapUv),S.push(T.metalnessMapUv),S.push(T.roughnessMapUv),S.push(T.anisotropyMapUv),S.push(T.clearcoatMapUv),S.push(T.clearcoatNormalMapUv),S.push(T.clearcoatRoughnessMapUv),S.push(T.iridescenceMapUv),S.push(T.iridescenceThicknessMapUv),S.push(T.sheenColorMapUv),S.push(T.sheenRoughnessMapUv),S.push(T.specularMapUv),S.push(T.specularColorMapUv),S.push(T.specularIntensityMapUv),S.push(T.transmissionMapUv),S.push(T.thicknessMapUv),S.push(T.combine),S.push(T.fogExp2),S.push(T.sizeAttenuation),S.push(T.morphTargetsCount),S.push(T.morphAttributeCount),S.push(T.numDirLights),S.push(T.numPointLights),S.push(T.numSpotLights),S.push(T.numSpotLightMaps),S.push(T.numHemiLights),S.push(T.numRectAreaLights),S.push(T.numDirLightShadows),S.push(T.numPointLightShadows),S.push(T.numSpotLightShadows),S.push(T.numSpotLightShadowsWithMaps),S.push(T.numLightProbes),S.push(T.shadowMapType),S.push(T.toneMapping),S.push(T.numClippingPlanes),S.push(T.numClipIntersection),S.push(T.depthPacking)}function x(S,T){o.disableAll(),T.supportsVertexTextures&&o.enable(0),T.instancing&&o.enable(1),T.instancingColor&&o.enable(2),T.instancingMorph&&o.enable(3),T.matcap&&o.enable(4),T.envMap&&o.enable(5),T.normalMapObjectSpace&&o.enable(6),T.normalMapTangentSpace&&o.enable(7),T.clearcoat&&o.enable(8),T.iridescence&&o.enable(9),T.alphaTest&&o.enable(10),T.vertexColors&&o.enable(11),T.vertexAlphas&&o.enable(12),T.vertexUv1s&&o.enable(13),T.vertexUv2s&&o.enable(14),T.vertexUv3s&&o.enable(15),T.vertexTangents&&o.enable(16),T.anisotropy&&o.enable(17),T.alphaHash&&o.enable(18),T.batching&&o.enable(19),T.dispersion&&o.enable(20),T.batchingColor&&o.enable(21),S.push(o.mask),o.disableAll(),T.fog&&o.enable(0),T.useFog&&o.enable(1),T.flatShading&&o.enable(2),T.logarithmicDepthBuffer&&o.enable(3),T.reverseDepthBuffer&&o.enable(4),T.skinning&&o.enable(5),T.morphTargets&&o.enable(6),T.morphNormals&&o.enable(7),T.morphColors&&o.enable(8),T.premultipliedAlpha&&o.enable(9),T.shadowMapEnabled&&o.enable(10),T.doubleSided&&o.enable(11),T.flipSided&&o.enable(12),T.useDepthPacking&&o.enable(13),T.dithering&&o.enable(14),T.transmission&&o.enable(15),T.sheen&&o.enable(16),T.opaque&&o.enable(17),T.pointsUvs&&o.enable(18),T.decodeVideoTexture&&o.enable(19),T.alphaToCoverage&&o.enable(20),S.push(o.mask)}function C(S){const T=y[S.type];let F;if(T){const G=Ai[T];F=U1.clone(G.uniforms)}else F=S.uniforms;return F}function R(S,T){let F;for(let G=0,Y=h.length;G<Y;G++){const K=h[G];if(K.cacheKey===T){F=K,++F.usedTimes;break}}return F===void 0&&(F=new k2(e,T,S,s),h.push(F)),F}function b(S){if(--S.usedTimes===0){const T=h.indexOf(S);h[T]=h[h.length-1],h.pop(),S.destroy()}}function w(S){l.remove(S)}function W(){l.dispose()}return{getParameters:c,getProgramCacheKey:_,getUniforms:C,acquireProgram:R,releaseProgram:b,releaseShaderCache:w,programs:h,dispose:W}}function Z2(){let e=new WeakMap;function t(r){return e.has(r)}function n(r){let o=e.get(r);return o===void 0&&(o={},e.set(r,o)),o}function i(r){e.delete(r)}function a(r,o,l){e.get(r)[o]=l}function s(){e=new WeakMap}return{has:t,get:n,remove:i,update:a,dispose:s}}function K2(e,t){return e.groupOrder!==t.groupOrder?e.groupOrder-t.groupOrder:e.renderOrder!==t.renderOrder?e.renderOrder-t.renderOrder:e.material.id!==t.material.id?e.material.id-t.material.id:e.z!==t.z?e.z-t.z:e.id-t.id}function C0(e,t){return e.groupOrder!==t.groupOrder?e.groupOrder-t.groupOrder:e.renderOrder!==t.renderOrder?e.renderOrder-t.renderOrder:e.z!==t.z?t.z-e.z:e.id-t.id}function w0(){const e=[];let t=0;const n=[],i=[],a=[];function s(){t=0,n.length=0,i.length=0,a.length=0}function r(p,f,d,v,y,m){let c=e[t];return c===void 0?(c={id:p.id,object:p,geometry:f,material:d,groupOrder:v,renderOrder:p.renderOrder,z:y,group:m},e[t]=c):(c.id=p.id,c.object=p,c.geometry=f,c.material=d,c.groupOrder=v,c.renderOrder=p.renderOrder,c.z=y,c.group=m),t++,c}function o(p,f,d,v,y,m){const c=r(p,f,d,v,y,m);d.transmission>0?i.push(c):d.transparent===!0?a.push(c):n.push(c)}function l(p,f,d,v,y,m){const c=r(p,f,d,v,y,m);d.transmission>0?i.unshift(c):d.transparent===!0?a.unshift(c):n.unshift(c)}function u(p,f){n.length>1&&n.sort(p||K2),i.length>1&&i.sort(f||C0),a.length>1&&a.sort(f||C0)}function h(){for(let p=t,f=e.length;p<f;p++){const d=e[p];if(d.id===null)break;d.id=null,d.object=null,d.geometry=null,d.material=null,d.group=null}}return{opaque:n,transmissive:i,transparent:a,init:s,push:o,unshift:l,finish:h,sort:u}}function Q2(){let e=new WeakMap;function t(i,a){const s=e.get(i);let r;return s===void 0?(r=new w0,e.set(i,[r])):a>=s.length?(r=new w0,s.push(r)):r=s[a],r}function n(){e=new WeakMap}return{get:t,dispose:n}}function J2(){const e={};return{get:function(t){if(e[t.id]!==void 0)return e[t.id];let n;switch(t.type){case"DirectionalLight":n={direction:new P,color:new Ht};break;case"SpotLight":n={position:new P,direction:new P,color:new Ht,distance:0,coneCos:0,penumbraCos:0,decay:0};break;case"PointLight":n={position:new P,color:new Ht,distance:0,decay:0};break;case"HemisphereLight":n={direction:new P,skyColor:new Ht,groundColor:new Ht};break;case"RectAreaLight":n={color:new Ht,position:new P,halfWidth:new P,halfHeight:new P};break}return e[t.id]=n,n}}}function $2(){const e={};return{get:function(t){if(e[t.id]!==void 0)return e[t.id];let n;switch(t.type){case"DirectionalLight":n={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new Lt};break;case"SpotLight":n={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new Lt};break;case"PointLight":n={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new Lt,shadowCameraNear:1,shadowCameraFar:1e3};break}return e[t.id]=n,n}}}let tw=0;function ew(e,t){return(t.castShadow?2:0)-(e.castShadow?2:0)+(t.map?1:0)-(e.map?1:0)}function nw(e){const t=new J2,n=$2(),i={version:0,hash:{directionalLength:-1,pointLength:-1,spotLength:-1,rectAreaLength:-1,hemiLength:-1,numDirectionalShadows:-1,numPointShadows:-1,numSpotShadows:-1,numSpotMaps:-1,numLightProbes:-1},ambient:[0,0,0],probe:[],directional:[],directionalShadow:[],directionalShadowMap:[],directionalShadowMatrix:[],spot:[],spotLightMap:[],spotShadow:[],spotShadowMap:[],spotLightMatrix:[],rectArea:[],rectAreaLTC1:null,rectAreaLTC2:null,point:[],pointShadow:[],pointShadowMap:[],pointShadowMatrix:[],hemi:[],numSpotLightShadowsWithMaps:0,numLightProbes:0};for(let u=0;u<9;u++)i.probe.push(new P);const a=new P,s=new Te,r=new Te;function o(u){let h=0,p=0,f=0;for(let W=0;W<9;W++)i.probe[W].set(0,0,0);let d=0,v=0,y=0,m=0,c=0,_=0,g=0,x=0,C=0,R=0,b=0;u.sort(ew);for(let W=0,S=u.length;W<S;W++){const T=u[W],F=T.color,G=T.intensity,Y=T.distance,K=T.shadow&&T.shadow.map?T.shadow.map.texture:null;if(T.isAmbientLight)h+=F.r*G,p+=F.g*G,f+=F.b*G;else if(T.isLightProbe){for(let D=0;D<9;D++)i.probe[D].addScaledVector(T.sh.coefficients[D],G);b++}else if(T.isDirectionalLight){const D=t.get(T);if(D.color.copy(T.color).multiplyScalar(T.intensity),T.castShadow){const V=T.shadow,z=n.get(T);z.shadowIntensity=V.intensity,z.shadowBias=V.bias,z.shadowNormalBias=V.normalBias,z.shadowRadius=V.radius,z.shadowMapSize=V.mapSize,i.directionalShadow[d]=z,i.directionalShadowMap[d]=K,i.directionalShadowMatrix[d]=T.shadow.matrix,_++}i.directional[d]=D,d++}else if(T.isSpotLight){const D=t.get(T);D.position.setFromMatrixPosition(T.matrixWorld),D.color.copy(F).multiplyScalar(G),D.distance=Y,D.coneCos=Math.cos(T.angle),D.penumbraCos=Math.cos(T.angle*(1-T.penumbra)),D.decay=T.decay,i.spot[y]=D;const V=T.shadow;if(T.map&&(i.spotLightMap[C]=T.map,C++,V.updateMatrices(T),T.castShadow&&R++),i.spotLightMatrix[y]=V.matrix,T.castShadow){const z=n.get(T);z.shadowIntensity=V.intensity,z.shadowBias=V.bias,z.shadowNormalBias=V.normalBias,z.shadowRadius=V.radius,z.shadowMapSize=V.mapSize,i.spotShadow[y]=z,i.spotShadowMap[y]=K,x++}y++}else if(T.isRectAreaLight){const D=t.get(T);D.color.copy(F).multiplyScalar(G),D.halfWidth.set(T.width*.5,0,0),D.halfHeight.set(0,T.height*.5,0),i.rectArea[m]=D,m++}else if(T.isPointLight){const D=t.get(T);if(D.color.copy(T.color).multiplyScalar(T.intensity),D.distance=T.distance,D.decay=T.decay,T.castShadow){const V=T.shadow,z=n.get(T);z.shadowIntensity=V.intensity,z.shadowBias=V.bias,z.shadowNormalBias=V.normalBias,z.shadowRadius=V.radius,z.shadowMapSize=V.mapSize,z.shadowCameraNear=V.camera.near,z.shadowCameraFar=V.camera.far,i.pointShadow[v]=z,i.pointShadowMap[v]=K,i.pointShadowMatrix[v]=T.shadow.matrix,g++}i.point[v]=D,v++}else if(T.isHemisphereLight){const D=t.get(T);D.skyColor.copy(T.color).multiplyScalar(G),D.groundColor.copy(T.groundColor).multiplyScalar(G),i.hemi[c]=D,c++}}m>0&&(e.has("OES_texture_float_linear")===!0?(i.rectAreaLTC1=at.LTC_FLOAT_1,i.rectAreaLTC2=at.LTC_FLOAT_2):(i.rectAreaLTC1=at.LTC_HALF_1,i.rectAreaLTC2=at.LTC_HALF_2)),i.ambient[0]=h,i.ambient[1]=p,i.ambient[2]=f;const w=i.hash;(w.directionalLength!==d||w.pointLength!==v||w.spotLength!==y||w.rectAreaLength!==m||w.hemiLength!==c||w.numDirectionalShadows!==_||w.numPointShadows!==g||w.numSpotShadows!==x||w.numSpotMaps!==C||w.numLightProbes!==b)&&(i.directional.length=d,i.spot.length=y,i.rectArea.length=m,i.point.length=v,i.hemi.length=c,i.directionalShadow.length=_,i.directionalShadowMap.length=_,i.pointShadow.length=g,i.pointShadowMap.length=g,i.spotShadow.length=x,i.spotShadowMap.length=x,i.directionalShadowMatrix.length=_,i.pointShadowMatrix.length=g,i.spotLightMatrix.length=x+C-R,i.spotLightMap.length=C,i.numSpotLightShadowsWithMaps=R,i.numLightProbes=b,w.directionalLength=d,w.pointLength=v,w.spotLength=y,w.rectAreaLength=m,w.hemiLength=c,w.numDirectionalShadows=_,w.numPointShadows=g,w.numSpotShadows=x,w.numSpotMaps=C,w.numLightProbes=b,i.version=tw++)}function l(u,h){let p=0,f=0,d=0,v=0,y=0;const m=h.matrixWorldInverse;for(let c=0,_=u.length;c<_;c++){const g=u[c];if(g.isDirectionalLight){const x=i.directional[p];x.direction.setFromMatrixPosition(g.matrixWorld),a.setFromMatrixPosition(g.target.matrixWorld),x.direction.sub(a),x.direction.transformDirection(m),p++}else if(g.isSpotLight){const x=i.spot[d];x.position.setFromMatrixPosition(g.matrixWorld),x.position.applyMatrix4(m),x.direction.setFromMatrixPosition(g.matrixWorld),a.setFromMatrixPosition(g.target.matrixWorld),x.direction.sub(a),x.direction.transformDirection(m),d++}else if(g.isRectAreaLight){const x=i.rectArea[v];x.position.setFromMatrixPosition(g.matrixWorld),x.position.applyMatrix4(m),r.identity(),s.copy(g.matrixWorld),s.premultiply(m),r.extractRotation(s),x.halfWidth.set(g.width*.5,0,0),x.halfHeight.set(0,g.height*.5,0),x.halfWidth.applyMatrix4(r),x.halfHeight.applyMatrix4(r),v++}else if(g.isPointLight){const x=i.point[f];x.position.setFromMatrixPosition(g.matrixWorld),x.position.applyMatrix4(m),f++}else if(g.isHemisphereLight){const x=i.hemi[y];x.direction.setFromMatrixPosition(g.matrixWorld),x.direction.transformDirection(m),y++}}}return{setup:o,setupView:l,state:i}}function D0(e){const t=new nw(e),n=[],i=[];function a(h){u.camera=h,n.length=0,i.length=0}function s(h){n.push(h)}function r(h){i.push(h)}function o(){t.setup(n)}function l(h){t.setupView(n,h)}const u={lightsArray:n,shadowsArray:i,camera:null,lights:t,transmissionRenderTarget:{}};return{init:a,state:u,setupLights:o,setupLightsView:l,pushLight:s,pushShadow:r}}function iw(e){let t=new WeakMap;function n(a,s=0){const r=t.get(a);let o;return r===void 0?(o=new D0(e),t.set(a,[o])):s>=r.length?(o=new D0(e),r.push(o)):o=r[s],o}function i(){t=new WeakMap}return{get:n,dispose:i}}class aw extends Rl{constructor(t){super(),this.isMeshDepthMaterial=!0,this.type="MeshDepthMaterial",this.depthPacking=Qb,this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.wireframe=!1,this.wireframeLinewidth=1,this.setValues(t)}copy(t){return super.copy(t),this.depthPacking=t.depthPacking,this.map=t.map,this.alphaMap=t.alphaMap,this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this}}class sw extends Rl{constructor(t){super(),this.isMeshDistanceMaterial=!0,this.type="MeshDistanceMaterial",this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.setValues(t)}copy(t){return super.copy(t),this.map=t.map,this.alphaMap=t.alphaMap,this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this}}const rw=`void main() {
	gl_Position = vec4( position, 1.0 );
}`,ow=`uniform sampler2D shadow_pass;
uniform vec2 resolution;
uniform float radius;
#include <packing>
void main() {
	const float samples = float( VSM_SAMPLES );
	float mean = 0.0;
	float squared_mean = 0.0;
	float uvStride = samples <= 1.0 ? 0.0 : 2.0 / ( samples - 1.0 );
	float uvStart = samples <= 1.0 ? 0.0 : - 1.0;
	for ( float i = 0.0; i < samples; i ++ ) {
		float uvOffset = uvStart + i * uvStride;
		#ifdef HORIZONTAL_PASS
			vec2 distribution = unpackRGBATo2Half( texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( uvOffset, 0.0 ) * radius ) / resolution ) );
			mean += distribution.x;
			squared_mean += distribution.y * distribution.y + distribution.x * distribution.x;
		#else
			float depth = unpackRGBAToDepth( texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( 0.0, uvOffset ) * radius ) / resolution ) );
			mean += depth;
			squared_mean += depth * depth;
		#endif
	}
	mean = mean / samples;
	squared_mean = squared_mean / samples;
	float std_dev = sqrt( squared_mean - mean * mean );
	gl_FragColor = pack2HalfToRGBA( vec2( mean, std_dev ) );
}`;function lw(e,t,n){let i=new zm;const a=new Lt,s=new Lt,r=new Ce,o=new aw({depthPacking:Jb}),l=new sw,u={},h=n.maxTextureSize,p={[ja]:bn,[bn]:ja,[pi]:pi},f=new Za({defines:{VSM_SAMPLES:8},uniforms:{shadow_pass:{value:null},resolution:{value:new Lt},radius:{value:4}},vertexShader:rw,fragmentShader:ow}),d=f.clone();d.defines.HORIZONTAL_PASS=1;const v=new wn;v.setAttribute("position",new si(new Float32Array([-1,-1,.5,3,-1,.5,-1,3,.5]),3));const y=new En(v,f),m=this;this.enabled=!1,this.autoUpdate=!0,this.needsUpdate=!1,this.type=sx;let c=this.type;this.render=function(R,b,w){if(m.enabled===!1||m.autoUpdate===!1&&m.needsUpdate===!1||R.length===0)return;const W=e.getRenderTarget(),S=e.getActiveCubeFace(),T=e.getActiveMipmapLevel(),F=e.state;F.setBlending(Ga),F.buffers.color.setClear(1,1,1,1),F.buffers.depth.setTest(!0),F.setScissorTest(!1);const G=c!==Yi&&this.type===Yi,Y=c===Yi&&this.type!==Yi;for(let K=0,D=R.length;K<D;K++){const V=R[K],z=V.shadow;if(z===void 0){console.warn("THREE.WebGLShadowMap:",V,"has no shadow.");continue}if(z.autoUpdate===!1&&z.needsUpdate===!1)continue;a.copy(z.mapSize);const tt=z.getFrameExtents();if(a.multiply(tt),s.copy(z.mapSize),(a.x>h||a.y>h)&&(a.x>h&&(s.x=Math.floor(h/tt.x),a.x=s.x*tt.x,z.mapSize.x=s.x),a.y>h&&(s.y=Math.floor(h/tt.y),a.y=s.y*tt.y,z.mapSize.y=s.y)),z.map===null||G===!0||Y===!0){const ht=this.type!==Yi?{minFilter:ii,magFilter:ii}:{};z.map!==null&&z.map.dispose(),z.map=new Ns(a.x,a.y,ht),z.map.texture.name=V.name+".shadowMap",z.camera.updateProjectionMatrix()}e.setRenderTarget(z.map),e.clear();const it=z.getViewportCount();for(let ht=0;ht<it;ht++){const Ft=z.getViewport(ht);r.set(s.x*Ft.x,s.y*Ft.y,s.x*Ft.z,s.y*Ft.w),F.viewport(r),z.updateMatrices(V,ht),i=z.getFrustum(),x(b,w,z.camera,V,this.type)}z.isPointLightShadow!==!0&&this.type===Yi&&_(z,w),z.needsUpdate=!1}c=this.type,m.needsUpdate=!1,e.setRenderTarget(W,S,T)};function _(R,b){const w=t.update(y);f.defines.VSM_SAMPLES!==R.blurSamples&&(f.defines.VSM_SAMPLES=R.blurSamples,d.defines.VSM_SAMPLES=R.blurSamples,f.needsUpdate=!0,d.needsUpdate=!0),R.mapPass===null&&(R.mapPass=new Ns(a.x,a.y)),f.uniforms.shadow_pass.value=R.map.texture,f.uniforms.resolution.value=R.mapSize,f.uniforms.radius.value=R.radius,e.setRenderTarget(R.mapPass),e.clear(),e.renderBufferDirect(b,null,w,f,y,null),d.uniforms.shadow_pass.value=R.mapPass.texture,d.uniforms.resolution.value=R.mapSize,d.uniforms.radius.value=R.radius,e.setRenderTarget(R.map),e.clear(),e.renderBufferDirect(b,null,w,d,y,null)}function g(R,b,w,W){let S=null;const T=w.isPointLight===!0?R.customDistanceMaterial:R.customDepthMaterial;if(T!==void 0)S=T;else if(S=w.isPointLight===!0?l:o,e.localClippingEnabled&&b.clipShadows===!0&&Array.isArray(b.clippingPlanes)&&b.clippingPlanes.length!==0||b.displacementMap&&b.displacementScale!==0||b.alphaMap&&b.alphaTest>0||b.map&&b.alphaTest>0){const F=S.uuid,G=b.uuid;let Y=u[F];Y===void 0&&(Y={},u[F]=Y);let K=Y[G];K===void 0&&(K=S.clone(),Y[G]=K,b.addEventListener("dispose",C)),S=K}if(S.visible=b.visible,S.wireframe=b.wireframe,W===Yi?S.side=b.shadowSide!==null?b.shadowSide:b.side:S.side=b.shadowSide!==null?b.shadowSide:p[b.side],S.alphaMap=b.alphaMap,S.alphaTest=b.alphaTest,S.map=b.map,S.clipShadows=b.clipShadows,S.clippingPlanes=b.clippingPlanes,S.clipIntersection=b.clipIntersection,S.displacementMap=b.displacementMap,S.displacementScale=b.displacementScale,S.displacementBias=b.displacementBias,S.wireframeLinewidth=b.wireframeLinewidth,S.linewidth=b.linewidth,w.isPointLight===!0&&S.isMeshDistanceMaterial===!0){const F=e.properties.get(S);F.light=w}return S}function x(R,b,w,W,S){if(R.visible===!1)return;if(R.layers.test(b.layers)&&(R.isMesh||R.isLine||R.isPoints)&&(R.castShadow||R.receiveShadow&&S===Yi)&&(!R.frustumCulled||i.intersectsObject(R))){R.modelViewMatrix.multiplyMatrices(w.matrixWorldInverse,R.matrixWorld);const G=t.update(R),Y=R.material;if(Array.isArray(Y)){const K=G.groups;for(let D=0,V=K.length;D<V;D++){const z=K[D],tt=Y[z.materialIndex];if(tt&&tt.visible){const it=g(R,tt,W,S);R.onBeforeShadow(e,R,b,w,G,it,z),e.renderBufferDirect(w,null,G,it,R,z),R.onAfterShadow(e,R,b,w,G,it,z)}}}else if(Y.visible){const K=g(R,Y,W,S);R.onBeforeShadow(e,R,b,w,G,K,null),e.renderBufferDirect(w,null,G,K,R,null),R.onAfterShadow(e,R,b,w,G,K,null)}}const F=R.children;for(let G=0,Y=F.length;G<Y;G++)x(F[G],b,w,W,S)}function C(R){R.target.removeEventListener("dispose",C);for(const w in u){const W=u[w],S=R.target.uuid;S in W&&(W[S].dispose(),delete W[S])}}}const uw={[Id]:Bd,[Fd]:Vd,[Hd]:Xd,[Kr]:Gd,[Bd]:Id,[Vd]:Fd,[Xd]:Hd,[Gd]:Kr};function cw(e){function t(){let N=!1;const lt=new Ce;let X=null;const Q=new Ce(0,0,0,0);return{setMask:function(rt){X!==rt&&!N&&(e.colorMask(rt,rt,rt,rt),X=rt)},setLocked:function(rt){N=rt},setClear:function(rt,ut,Wt,Ue,mn){mn===!0&&(rt*=Ue,ut*=Ue,Wt*=Ue),lt.set(rt,ut,Wt,Ue),Q.equals(lt)===!1&&(e.clearColor(rt,ut,Wt,Ue),Q.copy(lt))},reset:function(){N=!1,X=null,Q.set(-1,0,0,0)}}}function n(){let N=!1,lt=!1,X=null,Q=null,rt=null;return{setReversed:function(ut){lt=ut},setTest:function(ut){ut?_t(e.DEPTH_TEST):ct(e.DEPTH_TEST)},setMask:function(ut){X!==ut&&!N&&(e.depthMask(ut),X=ut)},setFunc:function(ut){if(lt&&(ut=uw[ut]),Q!==ut){switch(ut){case Id:e.depthFunc(e.NEVER);break;case Bd:e.depthFunc(e.ALWAYS);break;case Fd:e.depthFunc(e.LESS);break;case Kr:e.depthFunc(e.LEQUAL);break;case Hd:e.depthFunc(e.EQUAL);break;case Gd:e.depthFunc(e.GEQUAL);break;case Vd:e.depthFunc(e.GREATER);break;case Xd:e.depthFunc(e.NOTEQUAL);break;default:e.depthFunc(e.LEQUAL)}Q=ut}},setLocked:function(ut){N=ut},setClear:function(ut){rt!==ut&&(e.clearDepth(ut),rt=ut)},reset:function(){N=!1,X=null,Q=null,rt=null}}}function i(){let N=!1,lt=null,X=null,Q=null,rt=null,ut=null,Wt=null,Ue=null,mn=null;return{setTest:function(Jt){N||(Jt?_t(e.STENCIL_TEST):ct(e.STENCIL_TEST))},setMask:function(Jt){lt!==Jt&&!N&&(e.stencilMask(Jt),lt=Jt)},setFunc:function(Jt,_n,Ii){(X!==Jt||Q!==_n||rt!==Ii)&&(e.stencilFunc(Jt,_n,Ii),X=Jt,Q=_n,rt=Ii)},setOp:function(Jt,_n,Ii){(ut!==Jt||Wt!==_n||Ue!==Ii)&&(e.stencilOp(Jt,_n,Ii),ut=Jt,Wt=_n,Ue=Ii)},setLocked:function(Jt){N=Jt},setClear:function(Jt){mn!==Jt&&(e.clearStencil(Jt),mn=Jt)},reset:function(){N=!1,lt=null,X=null,Q=null,rt=null,ut=null,Wt=null,Ue=null,mn=null}}}const a=new t,s=new n,r=new i,o=new WeakMap,l=new WeakMap;let u={},h={},p=new WeakMap,f=[],d=null,v=!1,y=null,m=null,c=null,_=null,g=null,x=null,C=null,R=new Ht(0,0,0),b=0,w=!1,W=null,S=null,T=null,F=null,G=null;const Y=e.getParameter(e.MAX_COMBINED_TEXTURE_IMAGE_UNITS);let K=!1,D=0;const V=e.getParameter(e.VERSION);V.indexOf("WebGL")!==-1?(D=parseFloat(/^WebGL (\d)/.exec(V)[1]),K=D>=1):V.indexOf("OpenGL ES")!==-1&&(D=parseFloat(/^OpenGL ES (\d)/.exec(V)[1]),K=D>=2);let z=null,tt={};const it=e.getParameter(e.SCISSOR_BOX),ht=e.getParameter(e.VIEWPORT),Ft=new Ce().fromArray(it),kt=new Ce().fromArray(ht);function k(N,lt,X,Q){const rt=new Uint8Array(4),ut=e.createTexture();e.bindTexture(N,ut),e.texParameteri(N,e.TEXTURE_MIN_FILTER,e.NEAREST),e.texParameteri(N,e.TEXTURE_MAG_FILTER,e.NEAREST);for(let Wt=0;Wt<X;Wt++)N===e.TEXTURE_3D||N===e.TEXTURE_2D_ARRAY?e.texImage3D(lt,0,e.RGBA,1,1,Q,0,e.RGBA,e.UNSIGNED_BYTE,rt):e.texImage2D(lt+Wt,0,e.RGBA,1,1,0,e.RGBA,e.UNSIGNED_BYTE,rt);return ut}const $={};$[e.TEXTURE_2D]=k(e.TEXTURE_2D,e.TEXTURE_2D,1),$[e.TEXTURE_CUBE_MAP]=k(e.TEXTURE_CUBE_MAP,e.TEXTURE_CUBE_MAP_POSITIVE_X,6),$[e.TEXTURE_2D_ARRAY]=k(e.TEXTURE_2D_ARRAY,e.TEXTURE_2D_ARRAY,1,1),$[e.TEXTURE_3D]=k(e.TEXTURE_3D,e.TEXTURE_3D,1,1),a.setClear(0,0,0,1),s.setClear(1),r.setClear(0),_t(e.DEPTH_TEST),s.setFunc(Kr),Vt(!1),jt(Bg),_t(e.CULL_FACE),U(Ga);function _t(N){u[N]!==!0&&(e.enable(N),u[N]=!0)}function ct(N){u[N]!==!1&&(e.disable(N),u[N]=!1)}function Dt(N,lt){return h[N]!==lt?(e.bindFramebuffer(N,lt),h[N]=lt,N===e.DRAW_FRAMEBUFFER&&(h[e.FRAMEBUFFER]=lt),N===e.FRAMEBUFFER&&(h[e.DRAW_FRAMEBUFFER]=lt),!0):!1}function Et(N,lt){let X=f,Q=!1;if(N){X=p.get(lt),X===void 0&&(X=[],p.set(lt,X));const rt=N.textures;if(X.length!==rt.length||X[0]!==e.COLOR_ATTACHMENT0){for(let ut=0,Wt=rt.length;ut<Wt;ut++)X[ut]=e.COLOR_ATTACHMENT0+ut;X.length=rt.length,Q=!0}}else X[0]!==e.BACK&&(X[0]=e.BACK,Q=!0);Q&&e.drawBuffers(X)}function Yt(N){return d!==N?(e.useProgram(N),d=N,!0):!1}const ue={[hs]:e.FUNC_ADD,[Tb]:e.FUNC_SUBTRACT,[bb]:e.FUNC_REVERSE_SUBTRACT};ue[Ab]=e.MIN,ue[Rb]=e.MAX;const qt={[Cb]:e.ZERO,[wb]:e.ONE,[Db]:e.SRC_COLOR,[Pd]:e.SRC_ALPHA,[zb]:e.SRC_ALPHA_SATURATE,[Ob]:e.DST_COLOR,[Nb]:e.DST_ALPHA,[Ub]:e.ONE_MINUS_SRC_COLOR,[zd]:e.ONE_MINUS_SRC_ALPHA,[Pb]:e.ONE_MINUS_DST_COLOR,[Lb]:e.ONE_MINUS_DST_ALPHA,[Ib]:e.CONSTANT_COLOR,[Bb]:e.ONE_MINUS_CONSTANT_COLOR,[Fb]:e.CONSTANT_ALPHA,[Hb]:e.ONE_MINUS_CONSTANT_ALPHA};function U(N,lt,X,Q,rt,ut,Wt,Ue,mn,Jt){if(N===Ga){v===!0&&(ct(e.BLEND),v=!1);return}if(v===!1&&(_t(e.BLEND),v=!0),N!==Eb){if(N!==y||Jt!==w){if((m!==hs||g!==hs)&&(e.blendEquation(e.FUNC_ADD),m=hs,g=hs),Jt)switch(N){case Or:e.blendFuncSeparate(e.ONE,e.ONE_MINUS_SRC_ALPHA,e.ONE,e.ONE_MINUS_SRC_ALPHA);break;case Fg:e.blendFunc(e.ONE,e.ONE);break;case Hg:e.blendFuncSeparate(e.ZERO,e.ONE_MINUS_SRC_COLOR,e.ZERO,e.ONE);break;case Gg:e.blendFuncSeparate(e.ZERO,e.SRC_COLOR,e.ZERO,e.SRC_ALPHA);break;default:console.error("THREE.WebGLState: Invalid blending: ",N);break}else switch(N){case Or:e.blendFuncSeparate(e.SRC_ALPHA,e.ONE_MINUS_SRC_ALPHA,e.ONE,e.ONE_MINUS_SRC_ALPHA);break;case Fg:e.blendFunc(e.SRC_ALPHA,e.ONE);break;case Hg:e.blendFuncSeparate(e.ZERO,e.ONE_MINUS_SRC_COLOR,e.ZERO,e.ONE);break;case Gg:e.blendFunc(e.ZERO,e.SRC_COLOR);break;default:console.error("THREE.WebGLState: Invalid blending: ",N);break}c=null,_=null,x=null,C=null,R.set(0,0,0),b=0,y=N,w=Jt}return}rt=rt||lt,ut=ut||X,Wt=Wt||Q,(lt!==m||rt!==g)&&(e.blendEquationSeparate(ue[lt],ue[rt]),m=lt,g=rt),(X!==c||Q!==_||ut!==x||Wt!==C)&&(e.blendFuncSeparate(qt[X],qt[Q],qt[ut],qt[Wt]),c=X,_=Q,x=ut,C=Wt),(Ue.equals(R)===!1||mn!==b)&&(e.blendColor(Ue.r,Ue.g,Ue.b,mn),R.copy(Ue),b=mn),y=N,w=!1}function Dn(N,lt){N.side===pi?ct(e.CULL_FACE):_t(e.CULL_FACE);let X=N.side===bn;lt&&(X=!X),Vt(X),N.blending===Or&&N.transparent===!1?U(Ga):U(N.blending,N.blendEquation,N.blendSrc,N.blendDst,N.blendEquationAlpha,N.blendSrcAlpha,N.blendDstAlpha,N.blendColor,N.blendAlpha,N.premultipliedAlpha),s.setFunc(N.depthFunc),s.setTest(N.depthTest),s.setMask(N.depthWrite),a.setMask(N.colorWrite);const Q=N.stencilWrite;r.setTest(Q),Q&&(r.setMask(N.stencilWriteMask),r.setFunc(N.stencilFunc,N.stencilRef,N.stencilFuncMask),r.setOp(N.stencilFail,N.stencilZFail,N.stencilZPass)),Se(N.polygonOffset,N.polygonOffsetFactor,N.polygonOffsetUnits),N.alphaToCoverage===!0?_t(e.SAMPLE_ALPHA_TO_COVERAGE):ct(e.SAMPLE_ALPHA_TO_COVERAGE)}function Vt(N){W!==N&&(N?e.frontFace(e.CW):e.frontFace(e.CCW),W=N)}function jt(N){N!==yb?(_t(e.CULL_FACE),N!==S&&(N===Bg?e.cullFace(e.BACK):N===xb?e.cullFace(e.FRONT):e.cullFace(e.FRONT_AND_BACK))):ct(e.CULL_FACE),S=N}function bt(N){N!==T&&(K&&e.lineWidth(N),T=N)}function Se(N,lt,X){N?(_t(e.POLYGON_OFFSET_FILL),(F!==lt||G!==X)&&(e.polygonOffset(lt,X),F=lt,G=X)):ct(e.POLYGON_OFFSET_FILL)}function wt(N){N?_t(e.SCISSOR_TEST):ct(e.SCISSOR_TEST)}function A(N){N===void 0&&(N=e.TEXTURE0+Y-1),z!==N&&(e.activeTexture(N),z=N)}function M(N,lt,X){X===void 0&&(z===null?X=e.TEXTURE0+Y-1:X=z);let Q=tt[X];Q===void 0&&(Q={type:void 0,texture:void 0},tt[X]=Q),(Q.type!==N||Q.texture!==lt)&&(z!==X&&(e.activeTexture(X),z=X),e.bindTexture(N,lt||$[N]),Q.type=N,Q.texture=lt)}function I(){const N=tt[z];N!==void 0&&N.type!==void 0&&(e.bindTexture(N.type,null),N.type=void 0,N.texture=void 0)}function Z(){try{e.compressedTexImage2D.apply(e,arguments)}catch(N){console.error("THREE.WebGLState:",N)}}function J(){try{e.compressedTexImage3D.apply(e,arguments)}catch(N){console.error("THREE.WebGLState:",N)}}function j(){try{e.texSubImage2D.apply(e,arguments)}catch(N){console.error("THREE.WebGLState:",N)}}function vt(){try{e.texSubImage3D.apply(e,arguments)}catch(N){console.error("THREE.WebGLState:",N)}}function st(){try{e.compressedTexSubImage2D.apply(e,arguments)}catch(N){console.error("THREE.WebGLState:",N)}}function ft(){try{e.compressedTexSubImage3D.apply(e,arguments)}catch(N){console.error("THREE.WebGLState:",N)}}function Zt(){try{e.texStorage2D.apply(e,arguments)}catch(N){console.error("THREE.WebGLState:",N)}}function et(){try{e.texStorage3D.apply(e,arguments)}catch(N){console.error("THREE.WebGLState:",N)}}function dt(){try{e.texImage2D.apply(e,arguments)}catch(N){console.error("THREE.WebGLState:",N)}}function At(){try{e.texImage3D.apply(e,arguments)}catch(N){console.error("THREE.WebGLState:",N)}}function Rt(N){Ft.equals(N)===!1&&(e.scissor(N.x,N.y,N.z,N.w),Ft.copy(N))}function pt(N){kt.equals(N)===!1&&(e.viewport(N.x,N.y,N.z,N.w),kt.copy(N))}function Xt(N,lt){let X=l.get(lt);X===void 0&&(X=new WeakMap,l.set(lt,X));let Q=X.get(N);Q===void 0&&(Q=e.getUniformBlockIndex(lt,N.name),X.set(N,Q))}function Ut(N,lt){const Q=l.get(lt).get(N);o.get(lt)!==Q&&(e.uniformBlockBinding(lt,Q,N.__bindingPointIndex),o.set(lt,Q))}function pe(){e.disable(e.BLEND),e.disable(e.CULL_FACE),e.disable(e.DEPTH_TEST),e.disable(e.POLYGON_OFFSET_FILL),e.disable(e.SCISSOR_TEST),e.disable(e.STENCIL_TEST),e.disable(e.SAMPLE_ALPHA_TO_COVERAGE),e.blendEquation(e.FUNC_ADD),e.blendFunc(e.ONE,e.ZERO),e.blendFuncSeparate(e.ONE,e.ZERO,e.ONE,e.ZERO),e.blendColor(0,0,0,0),e.colorMask(!0,!0,!0,!0),e.clearColor(0,0,0,0),e.depthMask(!0),e.depthFunc(e.LESS),e.clearDepth(1),e.stencilMask(4294967295),e.stencilFunc(e.ALWAYS,0,4294967295),e.stencilOp(e.KEEP,e.KEEP,e.KEEP),e.clearStencil(0),e.cullFace(e.BACK),e.frontFace(e.CCW),e.polygonOffset(0,0),e.activeTexture(e.TEXTURE0),e.bindFramebuffer(e.FRAMEBUFFER,null),e.bindFramebuffer(e.DRAW_FRAMEBUFFER,null),e.bindFramebuffer(e.READ_FRAMEBUFFER,null),e.useProgram(null),e.lineWidth(1),e.scissor(0,0,e.canvas.width,e.canvas.height),e.viewport(0,0,e.canvas.width,e.canvas.height),u={},z=null,tt={},h={},p=new WeakMap,f=[],d=null,v=!1,y=null,m=null,c=null,_=null,g=null,x=null,C=null,R=new Ht(0,0,0),b=0,w=!1,W=null,S=null,T=null,F=null,G=null,Ft.set(0,0,e.canvas.width,e.canvas.height),kt.set(0,0,e.canvas.width,e.canvas.height),a.reset(),s.reset(),r.reset()}return{buffers:{color:a,depth:s,stencil:r},enable:_t,disable:ct,bindFramebuffer:Dt,drawBuffers:Et,useProgram:Yt,setBlending:U,setMaterial:Dn,setFlipSided:Vt,setCullFace:jt,setLineWidth:bt,setPolygonOffset:Se,setScissorTest:wt,activeTexture:A,bindTexture:M,unbindTexture:I,compressedTexImage2D:Z,compressedTexImage3D:J,texImage2D:dt,texImage3D:At,updateUBOMapping:Xt,uniformBlockBinding:Ut,texStorage2D:Zt,texStorage3D:et,texSubImage2D:j,texSubImage3D:vt,compressedTexSubImage2D:st,compressedTexSubImage3D:ft,scissor:Rt,viewport:pt,reset:pe}}function U0(e,t,n,i){const a=fw(i);switch(n){case fx:return e*t;case dx:return e*t;case px:return e*t*2;case mx:return e*t/a.components*a.byteLength;case Um:return e*t/a.components*a.byteLength;case _x:return e*t*2/a.components*a.byteLength;case Nm:return e*t*2/a.components*a.byteLength;case hx:return e*t*3/a.components*a.byteLength;case vi:return e*t*4/a.components*a.byteLength;case Lm:return e*t*4/a.components*a.byteLength;case Gu:case Vu:return Math.floor((e+3)/4)*Math.floor((t+3)/4)*8;case Xu:case ku:return Math.floor((e+3)/4)*Math.floor((t+3)/4)*16;case Zd:case Qd:return Math.max(e,16)*Math.max(t,8)/4;case jd:case Kd:return Math.max(e,8)*Math.max(t,8)/2;case Jd:case $d:return Math.floor((e+3)/4)*Math.floor((t+3)/4)*8;case tp:return Math.floor((e+3)/4)*Math.floor((t+3)/4)*16;case ep:return Math.floor((e+3)/4)*Math.floor((t+3)/4)*16;case np:return Math.floor((e+4)/5)*Math.floor((t+3)/4)*16;case ip:return Math.floor((e+4)/5)*Math.floor((t+4)/5)*16;case ap:return Math.floor((e+5)/6)*Math.floor((t+4)/5)*16;case sp:return Math.floor((e+5)/6)*Math.floor((t+5)/6)*16;case rp:return Math.floor((e+7)/8)*Math.floor((t+4)/5)*16;case op:return Math.floor((e+7)/8)*Math.floor((t+5)/6)*16;case lp:return Math.floor((e+7)/8)*Math.floor((t+7)/8)*16;case up:return Math.floor((e+9)/10)*Math.floor((t+4)/5)*16;case cp:return Math.floor((e+9)/10)*Math.floor((t+5)/6)*16;case fp:return Math.floor((e+9)/10)*Math.floor((t+7)/8)*16;case hp:return Math.floor((e+9)/10)*Math.floor((t+9)/10)*16;case dp:return Math.floor((e+11)/12)*Math.floor((t+9)/10)*16;case pp:return Math.floor((e+11)/12)*Math.floor((t+11)/12)*16;case Yu:case mp:case _p:return Math.ceil(e/4)*Math.ceil(t/4)*16;case gx:case gp:return Math.ceil(e/4)*Math.ceil(t/4)*8;case vp:case Sp:return Math.ceil(e/4)*Math.ceil(t/4)*16}throw new Error(`Unable to determine texture byte length for ${n} format.`)}function fw(e){switch(e){case aa:case lx:return{byteLength:1,components:1};case fl:case ux:case Tl:return{byteLength:2,components:1};case wm:case Dm:return{byteLength:2,components:4};case Us:case Cm:case ji:return{byteLength:4,components:1};case cx:return{byteLength:4,components:3}}throw new Error(`Unknown texture type ${e}.`)}function hw(e,t,n,i,a,s,r){const o=t.has("WEBGL_multisampled_render_to_texture")?t.get("WEBGL_multisampled_render_to_texture"):null,l=typeof navigator>"u"?!1:/OculusBrowser/g.test(navigator.userAgent),u=new Lt,h=new WeakMap;let p;const f=new WeakMap;let d=!1;try{d=typeof OffscreenCanvas<"u"&&new OffscreenCanvas(1,1).getContext("2d")!==null}catch{}function v(A,M){return d?new OffscreenCanvas(A,M):Cc("canvas")}function y(A,M,I){let Z=1;const J=wt(A);if((J.width>I||J.height>I)&&(Z=I/Math.max(J.width,J.height)),Z<1)if(typeof HTMLImageElement<"u"&&A instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&A instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&A instanceof ImageBitmap||typeof VideoFrame<"u"&&A instanceof VideoFrame){const j=Math.floor(Z*J.width),vt=Math.floor(Z*J.height);p===void 0&&(p=v(j,vt));const st=M?v(j,vt):p;return st.width=j,st.height=vt,st.getContext("2d").drawImage(A,0,0,j,vt),console.warn("THREE.WebGLRenderer: Texture has been resized from ("+J.width+"x"+J.height+") to ("+j+"x"+vt+")."),st}else return"data"in A&&console.warn("THREE.WebGLRenderer: Image in DataTexture is too big ("+J.width+"x"+J.height+")."),A;return A}function m(A){return A.generateMipmaps&&A.minFilter!==ii&&A.minFilter!==mi}function c(A){e.generateMipmap(A)}function _(A,M,I,Z,J=!1){if(A!==null){if(e[A]!==void 0)return e[A];console.warn("THREE.WebGLRenderer: Attempt to use non-existing WebGL internal format '"+A+"'")}let j=M;if(M===e.RED&&(I===e.FLOAT&&(j=e.R32F),I===e.HALF_FLOAT&&(j=e.R16F),I===e.UNSIGNED_BYTE&&(j=e.R8)),M===e.RED_INTEGER&&(I===e.UNSIGNED_BYTE&&(j=e.R8UI),I===e.UNSIGNED_SHORT&&(j=e.R16UI),I===e.UNSIGNED_INT&&(j=e.R32UI),I===e.BYTE&&(j=e.R8I),I===e.SHORT&&(j=e.R16I),I===e.INT&&(j=e.R32I)),M===e.RG&&(I===e.FLOAT&&(j=e.RG32F),I===e.HALF_FLOAT&&(j=e.RG16F),I===e.UNSIGNED_BYTE&&(j=e.RG8)),M===e.RG_INTEGER&&(I===e.UNSIGNED_BYTE&&(j=e.RG8UI),I===e.UNSIGNED_SHORT&&(j=e.RG16UI),I===e.UNSIGNED_INT&&(j=e.RG32UI),I===e.BYTE&&(j=e.RG8I),I===e.SHORT&&(j=e.RG16I),I===e.INT&&(j=e.RG32I)),M===e.RGB_INTEGER&&(I===e.UNSIGNED_BYTE&&(j=e.RGB8UI),I===e.UNSIGNED_SHORT&&(j=e.RGB16UI),I===e.UNSIGNED_INT&&(j=e.RGB32UI),I===e.BYTE&&(j=e.RGB8I),I===e.SHORT&&(j=e.RGB16I),I===e.INT&&(j=e.RGB32I)),M===e.RGBA_INTEGER&&(I===e.UNSIGNED_BYTE&&(j=e.RGBA8UI),I===e.UNSIGNED_SHORT&&(j=e.RGBA16UI),I===e.UNSIGNED_INT&&(j=e.RGBA32UI),I===e.BYTE&&(j=e.RGBA8I),I===e.SHORT&&(j=e.RGBA16I),I===e.INT&&(j=e.RGBA32I)),M===e.RGB&&I===e.UNSIGNED_INT_5_9_9_9_REV&&(j=e.RGB9_E5),M===e.RGBA){const vt=J?Tc:ae.getTransfer(Z);I===e.FLOAT&&(j=e.RGBA32F),I===e.HALF_FLOAT&&(j=e.RGBA16F),I===e.UNSIGNED_BYTE&&(j=vt===xe?e.SRGB8_ALPHA8:e.RGBA8),I===e.UNSIGNED_SHORT_4_4_4_4&&(j=e.RGBA4),I===e.UNSIGNED_SHORT_5_5_5_1&&(j=e.RGB5_A1)}return(j===e.R16F||j===e.R32F||j===e.RG16F||j===e.RG32F||j===e.RGBA16F||j===e.RGBA32F)&&t.get("EXT_color_buffer_float"),j}function g(A,M){let I;return A?M===null||M===Us||M===$r?I=e.DEPTH24_STENCIL8:M===ji?I=e.DEPTH32F_STENCIL8:M===fl&&(I=e.DEPTH24_STENCIL8,console.warn("DepthTexture: 16 bit depth attachment is not supported with stencil. Using 24-bit attachment.")):M===null||M===Us||M===$r?I=e.DEPTH_COMPONENT24:M===ji?I=e.DEPTH_COMPONENT32F:M===fl&&(I=e.DEPTH_COMPONENT16),I}function x(A,M){return m(A)===!0||A.isFramebufferTexture&&A.minFilter!==ii&&A.minFilter!==mi?Math.log2(Math.max(M.width,M.height))+1:A.mipmaps!==void 0&&A.mipmaps.length>0?A.mipmaps.length:A.isCompressedTexture&&Array.isArray(A.image)?M.mipmaps.length:1}function C(A){const M=A.target;M.removeEventListener("dispose",C),b(M),M.isVideoTexture&&h.delete(M)}function R(A){const M=A.target;M.removeEventListener("dispose",R),W(M)}function b(A){const M=i.get(A);if(M.__webglInit===void 0)return;const I=A.source,Z=f.get(I);if(Z){const J=Z[M.__cacheKey];J.usedTimes--,J.usedTimes===0&&w(A),Object.keys(Z).length===0&&f.delete(I)}i.remove(A)}function w(A){const M=i.get(A);e.deleteTexture(M.__webglTexture);const I=A.source,Z=f.get(I);delete Z[M.__cacheKey],r.memory.textures--}function W(A){const M=i.get(A);if(A.depthTexture&&A.depthTexture.dispose(),A.isWebGLCubeRenderTarget)for(let Z=0;Z<6;Z++){if(Array.isArray(M.__webglFramebuffer[Z]))for(let J=0;J<M.__webglFramebuffer[Z].length;J++)e.deleteFramebuffer(M.__webglFramebuffer[Z][J]);else e.deleteFramebuffer(M.__webglFramebuffer[Z]);M.__webglDepthbuffer&&e.deleteRenderbuffer(M.__webglDepthbuffer[Z])}else{if(Array.isArray(M.__webglFramebuffer))for(let Z=0;Z<M.__webglFramebuffer.length;Z++)e.deleteFramebuffer(M.__webglFramebuffer[Z]);else e.deleteFramebuffer(M.__webglFramebuffer);if(M.__webglDepthbuffer&&e.deleteRenderbuffer(M.__webglDepthbuffer),M.__webglMultisampledFramebuffer&&e.deleteFramebuffer(M.__webglMultisampledFramebuffer),M.__webglColorRenderbuffer)for(let Z=0;Z<M.__webglColorRenderbuffer.length;Z++)M.__webglColorRenderbuffer[Z]&&e.deleteRenderbuffer(M.__webglColorRenderbuffer[Z]);M.__webglDepthRenderbuffer&&e.deleteRenderbuffer(M.__webglDepthRenderbuffer)}const I=A.textures;for(let Z=0,J=I.length;Z<J;Z++){const j=i.get(I[Z]);j.__webglTexture&&(e.deleteTexture(j.__webglTexture),r.memory.textures--),i.remove(I[Z])}i.remove(A)}let S=0;function T(){S=0}function F(){const A=S;return A>=a.maxTextures&&console.warn("THREE.WebGLTextures: Trying to use "+A+" texture units while this GPU supports only "+a.maxTextures),S+=1,A}function G(A){const M=[];return M.push(A.wrapS),M.push(A.wrapT),M.push(A.wrapR||0),M.push(A.magFilter),M.push(A.minFilter),M.push(A.anisotropy),M.push(A.internalFormat),M.push(A.format),M.push(A.type),M.push(A.generateMipmaps),M.push(A.premultiplyAlpha),M.push(A.flipY),M.push(A.unpackAlignment),M.push(A.colorSpace),M.join()}function Y(A,M){const I=i.get(A);if(A.isVideoTexture&&bt(A),A.isRenderTargetTexture===!1&&A.version>0&&I.__version!==A.version){const Z=A.image;if(Z===null)console.warn("THREE.WebGLRenderer: Texture marked for update but no image data found.");else if(Z.complete===!1)console.warn("THREE.WebGLRenderer: Texture marked for update but image is incomplete");else{kt(I,A,M);return}}n.bindTexture(e.TEXTURE_2D,I.__webglTexture,e.TEXTURE0+M)}function K(A,M){const I=i.get(A);if(A.version>0&&I.__version!==A.version){kt(I,A,M);return}n.bindTexture(e.TEXTURE_2D_ARRAY,I.__webglTexture,e.TEXTURE0+M)}function D(A,M){const I=i.get(A);if(A.version>0&&I.__version!==A.version){kt(I,A,M);return}n.bindTexture(e.TEXTURE_3D,I.__webglTexture,e.TEXTURE0+M)}function V(A,M){const I=i.get(A);if(A.version>0&&I.__version!==A.version){k(I,A,M);return}n.bindTexture(e.TEXTURE_CUBE_MAP,I.__webglTexture,e.TEXTURE0+M)}const z={[qd]:e.REPEAT,[_s]:e.CLAMP_TO_EDGE,[Wd]:e.MIRRORED_REPEAT},tt={[ii]:e.NEAREST,[Kb]:e.NEAREST_MIPMAP_NEAREST,[Kl]:e.NEAREST_MIPMAP_LINEAR,[mi]:e.LINEAR,[kf]:e.LINEAR_MIPMAP_NEAREST,[gs]:e.LINEAR_MIPMAP_LINEAR},it={[e1]:e.NEVER,[o1]:e.ALWAYS,[n1]:e.LESS,[vx]:e.LEQUAL,[i1]:e.EQUAL,[r1]:e.GEQUAL,[a1]:e.GREATER,[s1]:e.NOTEQUAL};function ht(A,M){if(M.type===ji&&t.has("OES_texture_float_linear")===!1&&(M.magFilter===mi||M.magFilter===kf||M.magFilter===Kl||M.magFilter===gs||M.minFilter===mi||M.minFilter===kf||M.minFilter===Kl||M.minFilter===gs)&&console.warn("THREE.WebGLRenderer: Unable to use linear filtering with floating point textures. OES_texture_float_linear not supported on this device."),e.texParameteri(A,e.TEXTURE_WRAP_S,z[M.wrapS]),e.texParameteri(A,e.TEXTURE_WRAP_T,z[M.wrapT]),(A===e.TEXTURE_3D||A===e.TEXTURE_2D_ARRAY)&&e.texParameteri(A,e.TEXTURE_WRAP_R,z[M.wrapR]),e.texParameteri(A,e.TEXTURE_MAG_FILTER,tt[M.magFilter]),e.texParameteri(A,e.TEXTURE_MIN_FILTER,tt[M.minFilter]),M.compareFunction&&(e.texParameteri(A,e.TEXTURE_COMPARE_MODE,e.COMPARE_REF_TO_TEXTURE),e.texParameteri(A,e.TEXTURE_COMPARE_FUNC,it[M.compareFunction])),t.has("EXT_texture_filter_anisotropic")===!0){if(M.magFilter===ii||M.minFilter!==Kl&&M.minFilter!==gs||M.type===ji&&t.has("OES_texture_float_linear")===!1)return;if(M.anisotropy>1||i.get(M).__currentAnisotropy){const I=t.get("EXT_texture_filter_anisotropic");e.texParameterf(A,I.TEXTURE_MAX_ANISOTROPY_EXT,Math.min(M.anisotropy,a.getMaxAnisotropy())),i.get(M).__currentAnisotropy=M.anisotropy}}}function Ft(A,M){let I=!1;A.__webglInit===void 0&&(A.__webglInit=!0,M.addEventListener("dispose",C));const Z=M.source;let J=f.get(Z);J===void 0&&(J={},f.set(Z,J));const j=G(M);if(j!==A.__cacheKey){J[j]===void 0&&(J[j]={texture:e.createTexture(),usedTimes:0},r.memory.textures++,I=!0),J[j].usedTimes++;const vt=J[A.__cacheKey];vt!==void 0&&(J[A.__cacheKey].usedTimes--,vt.usedTimes===0&&w(M)),A.__cacheKey=j,A.__webglTexture=J[j].texture}return I}function kt(A,M,I){let Z=e.TEXTURE_2D;(M.isDataArrayTexture||M.isCompressedArrayTexture)&&(Z=e.TEXTURE_2D_ARRAY),M.isData3DTexture&&(Z=e.TEXTURE_3D);const J=Ft(A,M),j=M.source;n.bindTexture(Z,A.__webglTexture,e.TEXTURE0+I);const vt=i.get(j);if(j.version!==vt.__version||J===!0){n.activeTexture(e.TEXTURE0+I);const st=ae.getPrimaries(ae.workingColorSpace),ft=M.colorSpace===Ta?null:ae.getPrimaries(M.colorSpace),Zt=M.colorSpace===Ta||st===ft?e.NONE:e.BROWSER_DEFAULT_WEBGL;e.pixelStorei(e.UNPACK_FLIP_Y_WEBGL,M.flipY),e.pixelStorei(e.UNPACK_PREMULTIPLY_ALPHA_WEBGL,M.premultiplyAlpha),e.pixelStorei(e.UNPACK_ALIGNMENT,M.unpackAlignment),e.pixelStorei(e.UNPACK_COLORSPACE_CONVERSION_WEBGL,Zt);let et=y(M.image,!1,a.maxTextureSize);et=Se(M,et);const dt=s.convert(M.format,M.colorSpace),At=s.convert(M.type);let Rt=_(M.internalFormat,dt,At,M.colorSpace,M.isVideoTexture);ht(Z,M);let pt;const Xt=M.mipmaps,Ut=M.isVideoTexture!==!0,pe=vt.__version===void 0||J===!0,N=j.dataReady,lt=x(M,et);if(M.isDepthTexture)Rt=g(M.format===to,M.type),pe&&(Ut?n.texStorage2D(e.TEXTURE_2D,1,Rt,et.width,et.height):n.texImage2D(e.TEXTURE_2D,0,Rt,et.width,et.height,0,dt,At,null));else if(M.isDataTexture)if(Xt.length>0){Ut&&pe&&n.texStorage2D(e.TEXTURE_2D,lt,Rt,Xt[0].width,Xt[0].height);for(let X=0,Q=Xt.length;X<Q;X++)pt=Xt[X],Ut?N&&n.texSubImage2D(e.TEXTURE_2D,X,0,0,pt.width,pt.height,dt,At,pt.data):n.texImage2D(e.TEXTURE_2D,X,Rt,pt.width,pt.height,0,dt,At,pt.data);M.generateMipmaps=!1}else Ut?(pe&&n.texStorage2D(e.TEXTURE_2D,lt,Rt,et.width,et.height),N&&n.texSubImage2D(e.TEXTURE_2D,0,0,0,et.width,et.height,dt,At,et.data)):n.texImage2D(e.TEXTURE_2D,0,Rt,et.width,et.height,0,dt,At,et.data);else if(M.isCompressedTexture)if(M.isCompressedArrayTexture){Ut&&pe&&n.texStorage3D(e.TEXTURE_2D_ARRAY,lt,Rt,Xt[0].width,Xt[0].height,et.depth);for(let X=0,Q=Xt.length;X<Q;X++)if(pt=Xt[X],M.format!==vi)if(dt!==null)if(Ut){if(N)if(M.layerUpdates.size>0){const rt=U0(pt.width,pt.height,M.format,M.type);for(const ut of M.layerUpdates){const Wt=pt.data.subarray(ut*rt/pt.data.BYTES_PER_ELEMENT,(ut+1)*rt/pt.data.BYTES_PER_ELEMENT);n.compressedTexSubImage3D(e.TEXTURE_2D_ARRAY,X,0,0,ut,pt.width,pt.height,1,dt,Wt,0,0)}M.clearLayerUpdates()}else n.compressedTexSubImage3D(e.TEXTURE_2D_ARRAY,X,0,0,0,pt.width,pt.height,et.depth,dt,pt.data,0,0)}else n.compressedTexImage3D(e.TEXTURE_2D_ARRAY,X,Rt,pt.width,pt.height,et.depth,0,pt.data,0,0);else console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()");else Ut?N&&n.texSubImage3D(e.TEXTURE_2D_ARRAY,X,0,0,0,pt.width,pt.height,et.depth,dt,At,pt.data):n.texImage3D(e.TEXTURE_2D_ARRAY,X,Rt,pt.width,pt.height,et.depth,0,dt,At,pt.data)}else{Ut&&pe&&n.texStorage2D(e.TEXTURE_2D,lt,Rt,Xt[0].width,Xt[0].height);for(let X=0,Q=Xt.length;X<Q;X++)pt=Xt[X],M.format!==vi?dt!==null?Ut?N&&n.compressedTexSubImage2D(e.TEXTURE_2D,X,0,0,pt.width,pt.height,dt,pt.data):n.compressedTexImage2D(e.TEXTURE_2D,X,Rt,pt.width,pt.height,0,pt.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()"):Ut?N&&n.texSubImage2D(e.TEXTURE_2D,X,0,0,pt.width,pt.height,dt,At,pt.data):n.texImage2D(e.TEXTURE_2D,X,Rt,pt.width,pt.height,0,dt,At,pt.data)}else if(M.isDataArrayTexture)if(Ut){if(pe&&n.texStorage3D(e.TEXTURE_2D_ARRAY,lt,Rt,et.width,et.height,et.depth),N)if(M.layerUpdates.size>0){const X=U0(et.width,et.height,M.format,M.type);for(const Q of M.layerUpdates){const rt=et.data.subarray(Q*X/et.data.BYTES_PER_ELEMENT,(Q+1)*X/et.data.BYTES_PER_ELEMENT);n.texSubImage3D(e.TEXTURE_2D_ARRAY,0,0,0,Q,et.width,et.height,1,dt,At,rt)}M.clearLayerUpdates()}else n.texSubImage3D(e.TEXTURE_2D_ARRAY,0,0,0,0,et.width,et.height,et.depth,dt,At,et.data)}else n.texImage3D(e.TEXTURE_2D_ARRAY,0,Rt,et.width,et.height,et.depth,0,dt,At,et.data);else if(M.isData3DTexture)Ut?(pe&&n.texStorage3D(e.TEXTURE_3D,lt,Rt,et.width,et.height,et.depth),N&&n.texSubImage3D(e.TEXTURE_3D,0,0,0,0,et.width,et.height,et.depth,dt,At,et.data)):n.texImage3D(e.TEXTURE_3D,0,Rt,et.width,et.height,et.depth,0,dt,At,et.data);else if(M.isFramebufferTexture){if(pe)if(Ut)n.texStorage2D(e.TEXTURE_2D,lt,Rt,et.width,et.height);else{let X=et.width,Q=et.height;for(let rt=0;rt<lt;rt++)n.texImage2D(e.TEXTURE_2D,rt,Rt,X,Q,0,dt,At,null),X>>=1,Q>>=1}}else if(Xt.length>0){if(Ut&&pe){const X=wt(Xt[0]);n.texStorage2D(e.TEXTURE_2D,lt,Rt,X.width,X.height)}for(let X=0,Q=Xt.length;X<Q;X++)pt=Xt[X],Ut?N&&n.texSubImage2D(e.TEXTURE_2D,X,0,0,dt,At,pt):n.texImage2D(e.TEXTURE_2D,X,Rt,dt,At,pt);M.generateMipmaps=!1}else if(Ut){if(pe){const X=wt(et);n.texStorage2D(e.TEXTURE_2D,lt,Rt,X.width,X.height)}N&&n.texSubImage2D(e.TEXTURE_2D,0,0,0,dt,At,et)}else n.texImage2D(e.TEXTURE_2D,0,Rt,dt,At,et);m(M)&&c(Z),vt.__version=j.version,M.onUpdate&&M.onUpdate(M)}A.__version=M.version}function k(A,M,I){if(M.image.length!==6)return;const Z=Ft(A,M),J=M.source;n.bindTexture(e.TEXTURE_CUBE_MAP,A.__webglTexture,e.TEXTURE0+I);const j=i.get(J);if(J.version!==j.__version||Z===!0){n.activeTexture(e.TEXTURE0+I);const vt=ae.getPrimaries(ae.workingColorSpace),st=M.colorSpace===Ta?null:ae.getPrimaries(M.colorSpace),ft=M.colorSpace===Ta||vt===st?e.NONE:e.BROWSER_DEFAULT_WEBGL;e.pixelStorei(e.UNPACK_FLIP_Y_WEBGL,M.flipY),e.pixelStorei(e.UNPACK_PREMULTIPLY_ALPHA_WEBGL,M.premultiplyAlpha),e.pixelStorei(e.UNPACK_ALIGNMENT,M.unpackAlignment),e.pixelStorei(e.UNPACK_COLORSPACE_CONVERSION_WEBGL,ft);const Zt=M.isCompressedTexture||M.image[0].isCompressedTexture,et=M.image[0]&&M.image[0].isDataTexture,dt=[];for(let Q=0;Q<6;Q++)!Zt&&!et?dt[Q]=y(M.image[Q],!0,a.maxCubemapSize):dt[Q]=et?M.image[Q].image:M.image[Q],dt[Q]=Se(M,dt[Q]);const At=dt[0],Rt=s.convert(M.format,M.colorSpace),pt=s.convert(M.type),Xt=_(M.internalFormat,Rt,pt,M.colorSpace),Ut=M.isVideoTexture!==!0,pe=j.__version===void 0||Z===!0,N=J.dataReady;let lt=x(M,At);ht(e.TEXTURE_CUBE_MAP,M);let X;if(Zt){Ut&&pe&&n.texStorage2D(e.TEXTURE_CUBE_MAP,lt,Xt,At.width,At.height);for(let Q=0;Q<6;Q++){X=dt[Q].mipmaps;for(let rt=0;rt<X.length;rt++){const ut=X[rt];M.format!==vi?Rt!==null?Ut?N&&n.compressedTexSubImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,rt,0,0,ut.width,ut.height,Rt,ut.data):n.compressedTexImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,rt,Xt,ut.width,ut.height,0,ut.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .setTextureCube()"):Ut?N&&n.texSubImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,rt,0,0,ut.width,ut.height,Rt,pt,ut.data):n.texImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,rt,Xt,ut.width,ut.height,0,Rt,pt,ut.data)}}}else{if(X=M.mipmaps,Ut&&pe){X.length>0&&lt++;const Q=wt(dt[0]);n.texStorage2D(e.TEXTURE_CUBE_MAP,lt,Xt,Q.width,Q.height)}for(let Q=0;Q<6;Q++)if(et){Ut?N&&n.texSubImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,0,0,0,dt[Q].width,dt[Q].height,Rt,pt,dt[Q].data):n.texImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,0,Xt,dt[Q].width,dt[Q].height,0,Rt,pt,dt[Q].data);for(let rt=0;rt<X.length;rt++){const Wt=X[rt].image[Q].image;Ut?N&&n.texSubImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,rt+1,0,0,Wt.width,Wt.height,Rt,pt,Wt.data):n.texImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,rt+1,Xt,Wt.width,Wt.height,0,Rt,pt,Wt.data)}}else{Ut?N&&n.texSubImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,0,0,0,Rt,pt,dt[Q]):n.texImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,0,Xt,Rt,pt,dt[Q]);for(let rt=0;rt<X.length;rt++){const ut=X[rt];Ut?N&&n.texSubImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,rt+1,0,0,Rt,pt,ut.image[Q]):n.texImage2D(e.TEXTURE_CUBE_MAP_POSITIVE_X+Q,rt+1,Xt,Rt,pt,ut.image[Q])}}}m(M)&&c(e.TEXTURE_CUBE_MAP),j.__version=J.version,M.onUpdate&&M.onUpdate(M)}A.__version=M.version}function $(A,M,I,Z,J,j){const vt=s.convert(I.format,I.colorSpace),st=s.convert(I.type),ft=_(I.internalFormat,vt,st,I.colorSpace);if(!i.get(M).__hasExternalTextures){const et=Math.max(1,M.width>>j),dt=Math.max(1,M.height>>j);J===e.TEXTURE_3D||J===e.TEXTURE_2D_ARRAY?n.texImage3D(J,j,ft,et,dt,M.depth,0,vt,st,null):n.texImage2D(J,j,ft,et,dt,0,vt,st,null)}n.bindFramebuffer(e.FRAMEBUFFER,A),jt(M)?o.framebufferTexture2DMultisampleEXT(e.FRAMEBUFFER,Z,J,i.get(I).__webglTexture,0,Vt(M)):(J===e.TEXTURE_2D||J>=e.TEXTURE_CUBE_MAP_POSITIVE_X&&J<=e.TEXTURE_CUBE_MAP_NEGATIVE_Z)&&e.framebufferTexture2D(e.FRAMEBUFFER,Z,J,i.get(I).__webglTexture,j),n.bindFramebuffer(e.FRAMEBUFFER,null)}function _t(A,M,I){if(e.bindRenderbuffer(e.RENDERBUFFER,A),M.depthBuffer){const Z=M.depthTexture,J=Z&&Z.isDepthTexture?Z.type:null,j=g(M.stencilBuffer,J),vt=M.stencilBuffer?e.DEPTH_STENCIL_ATTACHMENT:e.DEPTH_ATTACHMENT,st=Vt(M);jt(M)?o.renderbufferStorageMultisampleEXT(e.RENDERBUFFER,st,j,M.width,M.height):I?e.renderbufferStorageMultisample(e.RENDERBUFFER,st,j,M.width,M.height):e.renderbufferStorage(e.RENDERBUFFER,j,M.width,M.height),e.framebufferRenderbuffer(e.FRAMEBUFFER,vt,e.RENDERBUFFER,A)}else{const Z=M.textures;for(let J=0;J<Z.length;J++){const j=Z[J],vt=s.convert(j.format,j.colorSpace),st=s.convert(j.type),ft=_(j.internalFormat,vt,st,j.colorSpace),Zt=Vt(M);I&&jt(M)===!1?e.renderbufferStorageMultisample(e.RENDERBUFFER,Zt,ft,M.width,M.height):jt(M)?o.renderbufferStorageMultisampleEXT(e.RENDERBUFFER,Zt,ft,M.width,M.height):e.renderbufferStorage(e.RENDERBUFFER,ft,M.width,M.height)}}e.bindRenderbuffer(e.RENDERBUFFER,null)}function ct(A,M){if(M&&M.isWebGLCubeRenderTarget)throw new Error("Depth Texture with cube render targets is not supported");if(n.bindFramebuffer(e.FRAMEBUFFER,A),!(M.depthTexture&&M.depthTexture.isDepthTexture))throw new Error("renderTarget.depthTexture must be an instance of THREE.DepthTexture");(!i.get(M.depthTexture).__webglTexture||M.depthTexture.image.width!==M.width||M.depthTexture.image.height!==M.height)&&(M.depthTexture.image.width=M.width,M.depthTexture.image.height=M.height,M.depthTexture.needsUpdate=!0),Y(M.depthTexture,0);const Z=i.get(M.depthTexture).__webglTexture,J=Vt(M);if(M.depthTexture.format===Pr)jt(M)?o.framebufferTexture2DMultisampleEXT(e.FRAMEBUFFER,e.DEPTH_ATTACHMENT,e.TEXTURE_2D,Z,0,J):e.framebufferTexture2D(e.FRAMEBUFFER,e.DEPTH_ATTACHMENT,e.TEXTURE_2D,Z,0);else if(M.depthTexture.format===to)jt(M)?o.framebufferTexture2DMultisampleEXT(e.FRAMEBUFFER,e.DEPTH_STENCIL_ATTACHMENT,e.TEXTURE_2D,Z,0,J):e.framebufferTexture2D(e.FRAMEBUFFER,e.DEPTH_STENCIL_ATTACHMENT,e.TEXTURE_2D,Z,0);else throw new Error("Unknown depthTexture format")}function Dt(A){const M=i.get(A),I=A.isWebGLCubeRenderTarget===!0;if(M.__boundDepthTexture!==A.depthTexture){const Z=A.depthTexture;if(M.__depthDisposeCallback&&M.__depthDisposeCallback(),Z){const J=()=>{delete M.__boundDepthTexture,delete M.__depthDisposeCallback,Z.removeEventListener("dispose",J)};Z.addEventListener("dispose",J),M.__depthDisposeCallback=J}M.__boundDepthTexture=Z}if(A.depthTexture&&!M.__autoAllocateDepthBuffer){if(I)throw new Error("target.depthTexture not supported in Cube render targets");ct(M.__webglFramebuffer,A)}else if(I){M.__webglDepthbuffer=[];for(let Z=0;Z<6;Z++)if(n.bindFramebuffer(e.FRAMEBUFFER,M.__webglFramebuffer[Z]),M.__webglDepthbuffer[Z]===void 0)M.__webglDepthbuffer[Z]=e.createRenderbuffer(),_t(M.__webglDepthbuffer[Z],A,!1);else{const J=A.stencilBuffer?e.DEPTH_STENCIL_ATTACHMENT:e.DEPTH_ATTACHMENT,j=M.__webglDepthbuffer[Z];e.bindRenderbuffer(e.RENDERBUFFER,j),e.framebufferRenderbuffer(e.FRAMEBUFFER,J,e.RENDERBUFFER,j)}}else if(n.bindFramebuffer(e.FRAMEBUFFER,M.__webglFramebuffer),M.__webglDepthbuffer===void 0)M.__webglDepthbuffer=e.createRenderbuffer(),_t(M.__webglDepthbuffer,A,!1);else{const Z=A.stencilBuffer?e.DEPTH_STENCIL_ATTACHMENT:e.DEPTH_ATTACHMENT,J=M.__webglDepthbuffer;e.bindRenderbuffer(e.RENDERBUFFER,J),e.framebufferRenderbuffer(e.FRAMEBUFFER,Z,e.RENDERBUFFER,J)}n.bindFramebuffer(e.FRAMEBUFFER,null)}function Et(A,M,I){const Z=i.get(A);M!==void 0&&$(Z.__webglFramebuffer,A,A.texture,e.COLOR_ATTACHMENT0,e.TEXTURE_2D,0),I!==void 0&&Dt(A)}function Yt(A){const M=A.texture,I=i.get(A),Z=i.get(M);A.addEventListener("dispose",R);const J=A.textures,j=A.isWebGLCubeRenderTarget===!0,vt=J.length>1;if(vt||(Z.__webglTexture===void 0&&(Z.__webglTexture=e.createTexture()),Z.__version=M.version,r.memory.textures++),j){I.__webglFramebuffer=[];for(let st=0;st<6;st++)if(M.mipmaps&&M.mipmaps.length>0){I.__webglFramebuffer[st]=[];for(let ft=0;ft<M.mipmaps.length;ft++)I.__webglFramebuffer[st][ft]=e.createFramebuffer()}else I.__webglFramebuffer[st]=e.createFramebuffer()}else{if(M.mipmaps&&M.mipmaps.length>0){I.__webglFramebuffer=[];for(let st=0;st<M.mipmaps.length;st++)I.__webglFramebuffer[st]=e.createFramebuffer()}else I.__webglFramebuffer=e.createFramebuffer();if(vt)for(let st=0,ft=J.length;st<ft;st++){const Zt=i.get(J[st]);Zt.__webglTexture===void 0&&(Zt.__webglTexture=e.createTexture(),r.memory.textures++)}if(A.samples>0&&jt(A)===!1){I.__webglMultisampledFramebuffer=e.createFramebuffer(),I.__webglColorRenderbuffer=[],n.bindFramebuffer(e.FRAMEBUFFER,I.__webglMultisampledFramebuffer);for(let st=0;st<J.length;st++){const ft=J[st];I.__webglColorRenderbuffer[st]=e.createRenderbuffer(),e.bindRenderbuffer(e.RENDERBUFFER,I.__webglColorRenderbuffer[st]);const Zt=s.convert(ft.format,ft.colorSpace),et=s.convert(ft.type),dt=_(ft.internalFormat,Zt,et,ft.colorSpace,A.isXRRenderTarget===!0),At=Vt(A);e.renderbufferStorageMultisample(e.RENDERBUFFER,At,dt,A.width,A.height),e.framebufferRenderbuffer(e.FRAMEBUFFER,e.COLOR_ATTACHMENT0+st,e.RENDERBUFFER,I.__webglColorRenderbuffer[st])}e.bindRenderbuffer(e.RENDERBUFFER,null),A.depthBuffer&&(I.__webglDepthRenderbuffer=e.createRenderbuffer(),_t(I.__webglDepthRenderbuffer,A,!0)),n.bindFramebuffer(e.FRAMEBUFFER,null)}}if(j){n.bindTexture(e.TEXTURE_CUBE_MAP,Z.__webglTexture),ht(e.TEXTURE_CUBE_MAP,M);for(let st=0;st<6;st++)if(M.mipmaps&&M.mipmaps.length>0)for(let ft=0;ft<M.mipmaps.length;ft++)$(I.__webglFramebuffer[st][ft],A,M,e.COLOR_ATTACHMENT0,e.TEXTURE_CUBE_MAP_POSITIVE_X+st,ft);else $(I.__webglFramebuffer[st],A,M,e.COLOR_ATTACHMENT0,e.TEXTURE_CUBE_MAP_POSITIVE_X+st,0);m(M)&&c(e.TEXTURE_CUBE_MAP),n.unbindTexture()}else if(vt){for(let st=0,ft=J.length;st<ft;st++){const Zt=J[st],et=i.get(Zt);n.bindTexture(e.TEXTURE_2D,et.__webglTexture),ht(e.TEXTURE_2D,Zt),$(I.__webglFramebuffer,A,Zt,e.COLOR_ATTACHMENT0+st,e.TEXTURE_2D,0),m(Zt)&&c(e.TEXTURE_2D)}n.unbindTexture()}else{let st=e.TEXTURE_2D;if((A.isWebGL3DRenderTarget||A.isWebGLArrayRenderTarget)&&(st=A.isWebGL3DRenderTarget?e.TEXTURE_3D:e.TEXTURE_2D_ARRAY),n.bindTexture(st,Z.__webglTexture),ht(st,M),M.mipmaps&&M.mipmaps.length>0)for(let ft=0;ft<M.mipmaps.length;ft++)$(I.__webglFramebuffer[ft],A,M,e.COLOR_ATTACHMENT0,st,ft);else $(I.__webglFramebuffer,A,M,e.COLOR_ATTACHMENT0,st,0);m(M)&&c(st),n.unbindTexture()}A.depthBuffer&&Dt(A)}function ue(A){const M=A.textures;for(let I=0,Z=M.length;I<Z;I++){const J=M[I];if(m(J)){const j=A.isWebGLCubeRenderTarget?e.TEXTURE_CUBE_MAP:e.TEXTURE_2D,vt=i.get(J).__webglTexture;n.bindTexture(j,vt),c(j),n.unbindTexture()}}}const qt=[],U=[];function Dn(A){if(A.samples>0){if(jt(A)===!1){const M=A.textures,I=A.width,Z=A.height;let J=e.COLOR_BUFFER_BIT;const j=A.stencilBuffer?e.DEPTH_STENCIL_ATTACHMENT:e.DEPTH_ATTACHMENT,vt=i.get(A),st=M.length>1;if(st)for(let ft=0;ft<M.length;ft++)n.bindFramebuffer(e.FRAMEBUFFER,vt.__webglMultisampledFramebuffer),e.framebufferRenderbuffer(e.FRAMEBUFFER,e.COLOR_ATTACHMENT0+ft,e.RENDERBUFFER,null),n.bindFramebuffer(e.FRAMEBUFFER,vt.__webglFramebuffer),e.framebufferTexture2D(e.DRAW_FRAMEBUFFER,e.COLOR_ATTACHMENT0+ft,e.TEXTURE_2D,null,0);n.bindFramebuffer(e.READ_FRAMEBUFFER,vt.__webglMultisampledFramebuffer),n.bindFramebuffer(e.DRAW_FRAMEBUFFER,vt.__webglFramebuffer);for(let ft=0;ft<M.length;ft++){if(A.resolveDepthBuffer&&(A.depthBuffer&&(J|=e.DEPTH_BUFFER_BIT),A.stencilBuffer&&A.resolveStencilBuffer&&(J|=e.STENCIL_BUFFER_BIT)),st){e.framebufferRenderbuffer(e.READ_FRAMEBUFFER,e.COLOR_ATTACHMENT0,e.RENDERBUFFER,vt.__webglColorRenderbuffer[ft]);const Zt=i.get(M[ft]).__webglTexture;e.framebufferTexture2D(e.DRAW_FRAMEBUFFER,e.COLOR_ATTACHMENT0,e.TEXTURE_2D,Zt,0)}e.blitFramebuffer(0,0,I,Z,0,0,I,Z,J,e.NEAREST),l===!0&&(qt.length=0,U.length=0,qt.push(e.COLOR_ATTACHMENT0+ft),A.depthBuffer&&A.resolveDepthBuffer===!1&&(qt.push(j),U.push(j),e.invalidateFramebuffer(e.DRAW_FRAMEBUFFER,U)),e.invalidateFramebuffer(e.READ_FRAMEBUFFER,qt))}if(n.bindFramebuffer(e.READ_FRAMEBUFFER,null),n.bindFramebuffer(e.DRAW_FRAMEBUFFER,null),st)for(let ft=0;ft<M.length;ft++){n.bindFramebuffer(e.FRAMEBUFFER,vt.__webglMultisampledFramebuffer),e.framebufferRenderbuffer(e.FRAMEBUFFER,e.COLOR_ATTACHMENT0+ft,e.RENDERBUFFER,vt.__webglColorRenderbuffer[ft]);const Zt=i.get(M[ft]).__webglTexture;n.bindFramebuffer(e.FRAMEBUFFER,vt.__webglFramebuffer),e.framebufferTexture2D(e.DRAW_FRAMEBUFFER,e.COLOR_ATTACHMENT0+ft,e.TEXTURE_2D,Zt,0)}n.bindFramebuffer(e.DRAW_FRAMEBUFFER,vt.__webglMultisampledFramebuffer)}else if(A.depthBuffer&&A.resolveDepthBuffer===!1&&l){const M=A.stencilBuffer?e.DEPTH_STENCIL_ATTACHMENT:e.DEPTH_ATTACHMENT;e.invalidateFramebuffer(e.DRAW_FRAMEBUFFER,[M])}}}function Vt(A){return Math.min(a.maxSamples,A.samples)}function jt(A){const M=i.get(A);return A.samples>0&&t.has("WEBGL_multisampled_render_to_texture")===!0&&M.__useRenderToTexture!==!1}function bt(A){const M=r.render.frame;h.get(A)!==M&&(h.set(A,M),A.update())}function Se(A,M){const I=A.colorSpace,Z=A.format,J=A.type;return A.isCompressedTexture===!0||A.isVideoTexture===!0||I!==Ja&&I!==Ta&&(ae.getTransfer(I)===xe?(Z!==vi||J!==aa)&&console.warn("THREE.WebGLTextures: sRGB encoded textures have to use RGBAFormat and UnsignedByteType."):console.error("THREE.WebGLTextures: Unsupported texture color space:",I)),M}function wt(A){return typeof HTMLImageElement<"u"&&A instanceof HTMLImageElement?(u.width=A.naturalWidth||A.width,u.height=A.naturalHeight||A.height):typeof VideoFrame<"u"&&A instanceof VideoFrame?(u.width=A.displayWidth,u.height=A.displayHeight):(u.width=A.width,u.height=A.height),u}this.allocateTextureUnit=F,this.resetTextureUnits=T,this.setTexture2D=Y,this.setTexture2DArray=K,this.setTexture3D=D,this.setTextureCube=V,this.rebindTextures=Et,this.setupRenderTarget=Yt,this.updateRenderTargetMipmap=ue,this.updateMultisampleRenderTarget=Dn,this.setupDepthRenderbuffer=Dt,this.setupFrameBufferTexture=$,this.useMultisampledRTT=jt}function dw(e,t){function n(i,a=Ta){let s;const r=ae.getTransfer(a);if(i===aa)return e.UNSIGNED_BYTE;if(i===wm)return e.UNSIGNED_SHORT_4_4_4_4;if(i===Dm)return e.UNSIGNED_SHORT_5_5_5_1;if(i===cx)return e.UNSIGNED_INT_5_9_9_9_REV;if(i===lx)return e.BYTE;if(i===ux)return e.SHORT;if(i===fl)return e.UNSIGNED_SHORT;if(i===Cm)return e.INT;if(i===Us)return e.UNSIGNED_INT;if(i===ji)return e.FLOAT;if(i===Tl)return e.HALF_FLOAT;if(i===fx)return e.ALPHA;if(i===hx)return e.RGB;if(i===vi)return e.RGBA;if(i===dx)return e.LUMINANCE;if(i===px)return e.LUMINANCE_ALPHA;if(i===Pr)return e.DEPTH_COMPONENT;if(i===to)return e.DEPTH_STENCIL;if(i===mx)return e.RED;if(i===Um)return e.RED_INTEGER;if(i===_x)return e.RG;if(i===Nm)return e.RG_INTEGER;if(i===Lm)return e.RGBA_INTEGER;if(i===Gu||i===Vu||i===Xu||i===ku)if(r===xe)if(s=t.get("WEBGL_compressed_texture_s3tc_srgb"),s!==null){if(i===Gu)return s.COMPRESSED_SRGB_S3TC_DXT1_EXT;if(i===Vu)return s.COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT;if(i===Xu)return s.COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT;if(i===ku)return s.COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT}else return null;else if(s=t.get("WEBGL_compressed_texture_s3tc"),s!==null){if(i===Gu)return s.COMPRESSED_RGB_S3TC_DXT1_EXT;if(i===Vu)return s.COMPRESSED_RGBA_S3TC_DXT1_EXT;if(i===Xu)return s.COMPRESSED_RGBA_S3TC_DXT3_EXT;if(i===ku)return s.COMPRESSED_RGBA_S3TC_DXT5_EXT}else return null;if(i===jd||i===Zd||i===Kd||i===Qd)if(s=t.get("WEBGL_compressed_texture_pvrtc"),s!==null){if(i===jd)return s.COMPRESSED_RGB_PVRTC_4BPPV1_IMG;if(i===Zd)return s.COMPRESSED_RGB_PVRTC_2BPPV1_IMG;if(i===Kd)return s.COMPRESSED_RGBA_PVRTC_4BPPV1_IMG;if(i===Qd)return s.COMPRESSED_RGBA_PVRTC_2BPPV1_IMG}else return null;if(i===Jd||i===$d||i===tp)if(s=t.get("WEBGL_compressed_texture_etc"),s!==null){if(i===Jd||i===$d)return r===xe?s.COMPRESSED_SRGB8_ETC2:s.COMPRESSED_RGB8_ETC2;if(i===tp)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ETC2_EAC:s.COMPRESSED_RGBA8_ETC2_EAC}else return null;if(i===ep||i===np||i===ip||i===ap||i===sp||i===rp||i===op||i===lp||i===up||i===cp||i===fp||i===hp||i===dp||i===pp)if(s=t.get("WEBGL_compressed_texture_astc"),s!==null){if(i===ep)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR:s.COMPRESSED_RGBA_ASTC_4x4_KHR;if(i===np)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR:s.COMPRESSED_RGBA_ASTC_5x4_KHR;if(i===ip)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR:s.COMPRESSED_RGBA_ASTC_5x5_KHR;if(i===ap)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR:s.COMPRESSED_RGBA_ASTC_6x5_KHR;if(i===sp)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR:s.COMPRESSED_RGBA_ASTC_6x6_KHR;if(i===rp)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR:s.COMPRESSED_RGBA_ASTC_8x5_KHR;if(i===op)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR:s.COMPRESSED_RGBA_ASTC_8x6_KHR;if(i===lp)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR:s.COMPRESSED_RGBA_ASTC_8x8_KHR;if(i===up)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR:s.COMPRESSED_RGBA_ASTC_10x5_KHR;if(i===cp)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR:s.COMPRESSED_RGBA_ASTC_10x6_KHR;if(i===fp)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR:s.COMPRESSED_RGBA_ASTC_10x8_KHR;if(i===hp)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR:s.COMPRESSED_RGBA_ASTC_10x10_KHR;if(i===dp)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR:s.COMPRESSED_RGBA_ASTC_12x10_KHR;if(i===pp)return r===xe?s.COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR:s.COMPRESSED_RGBA_ASTC_12x12_KHR}else return null;if(i===Yu||i===mp||i===_p)if(s=t.get("EXT_texture_compression_bptc"),s!==null){if(i===Yu)return r===xe?s.COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT:s.COMPRESSED_RGBA_BPTC_UNORM_EXT;if(i===mp)return s.COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT;if(i===_p)return s.COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT}else return null;if(i===gx||i===gp||i===vp||i===Sp)if(s=t.get("EXT_texture_compression_rgtc"),s!==null){if(i===Yu)return s.COMPRESSED_RED_RGTC1_EXT;if(i===gp)return s.COMPRESSED_SIGNED_RED_RGTC1_EXT;if(i===vp)return s.COMPRESSED_RED_GREEN_RGTC2_EXT;if(i===Sp)return s.COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT}else return null;return i===$r?e.UNSIGNED_INT_24_8:e[i]!==void 0?e[i]:null}return{convert:n}}class pw extends $n{constructor(t=[]){super(),this.isArrayCamera=!0,this.cameras=t}}class Lo extends en{constructor(){super(),this.isGroup=!0,this.type="Group"}}const mw={type:"move"};class Sh{constructor(){this._targetRay=null,this._grip=null,this._hand=null}getHandSpace(){return this._hand===null&&(this._hand=new Lo,this._hand.matrixAutoUpdate=!1,this._hand.visible=!1,this._hand.joints={},this._hand.inputState={pinching:!1}),this._hand}getTargetRaySpace(){return this._targetRay===null&&(this._targetRay=new Lo,this._targetRay.matrixAutoUpdate=!1,this._targetRay.visible=!1,this._targetRay.hasLinearVelocity=!1,this._targetRay.linearVelocity=new P,this._targetRay.hasAngularVelocity=!1,this._targetRay.angularVelocity=new P),this._targetRay}getGripSpace(){return this._grip===null&&(this._grip=new Lo,this._grip.matrixAutoUpdate=!1,this._grip.visible=!1,this._grip.hasLinearVelocity=!1,this._grip.linearVelocity=new P,this._grip.hasAngularVelocity=!1,this._grip.angularVelocity=new P),this._grip}dispatchEvent(t){return this._targetRay!==null&&this._targetRay.dispatchEvent(t),this._grip!==null&&this._grip.dispatchEvent(t),this._hand!==null&&this._hand.dispatchEvent(t),this}connect(t){if(t&&t.hand){const n=this._hand;if(n)for(const i of t.hand.values())this._getHandJoint(n,i)}return this.dispatchEvent({type:"connected",data:t}),this}disconnect(t){return this.dispatchEvent({type:"disconnected",data:t}),this._targetRay!==null&&(this._targetRay.visible=!1),this._grip!==null&&(this._grip.visible=!1),this._hand!==null&&(this._hand.visible=!1),this}update(t,n,i){let a=null,s=null,r=null;const o=this._targetRay,l=this._grip,u=this._hand;if(t&&n.session.visibilityState!=="visible-blurred"){if(u&&t.hand){r=!0;for(const y of t.hand.values()){const m=n.getJointPose(y,i),c=this._getHandJoint(u,y);m!==null&&(c.matrix.fromArray(m.transform.matrix),c.matrix.decompose(c.position,c.rotation,c.scale),c.matrixWorldNeedsUpdate=!0,c.jointRadius=m.radius),c.visible=m!==null}const h=u.joints["index-finger-tip"],p=u.joints["thumb-tip"],f=h.position.distanceTo(p.position),d=.02,v=.005;u.inputState.pinching&&f>d+v?(u.inputState.pinching=!1,this.dispatchEvent({type:"pinchend",handedness:t.handedness,target:this})):!u.inputState.pinching&&f<=d-v&&(u.inputState.pinching=!0,this.dispatchEvent({type:"pinchstart",handedness:t.handedness,target:this}))}else l!==null&&t.gripSpace&&(s=n.getPose(t.gripSpace,i),s!==null&&(l.matrix.fromArray(s.transform.matrix),l.matrix.decompose(l.position,l.rotation,l.scale),l.matrixWorldNeedsUpdate=!0,s.linearVelocity?(l.hasLinearVelocity=!0,l.linearVelocity.copy(s.linearVelocity)):l.hasLinearVelocity=!1,s.angularVelocity?(l.hasAngularVelocity=!0,l.angularVelocity.copy(s.angularVelocity)):l.hasAngularVelocity=!1));o!==null&&(a=n.getPose(t.targetRaySpace,i),a===null&&s!==null&&(a=s),a!==null&&(o.matrix.fromArray(a.transform.matrix),o.matrix.decompose(o.position,o.rotation,o.scale),o.matrixWorldNeedsUpdate=!0,a.linearVelocity?(o.hasLinearVelocity=!0,o.linearVelocity.copy(a.linearVelocity)):o.hasLinearVelocity=!1,a.angularVelocity?(o.hasAngularVelocity=!0,o.angularVelocity.copy(a.angularVelocity)):o.hasAngularVelocity=!1,this.dispatchEvent(mw)))}return o!==null&&(o.visible=a!==null),l!==null&&(l.visible=s!==null),u!==null&&(u.visible=r!==null),this}_getHandJoint(t,n){if(t.joints[n.jointName]===void 0){const i=new Lo;i.matrixAutoUpdate=!1,i.visible=!1,t.joints[n.jointName]=i,t.add(i)}return t.joints[n.jointName]}}const _w=`
void main() {

	gl_Position = vec4( position, 1.0 );

}`,gw=`
uniform sampler2DArray depthColor;
uniform float depthWidth;
uniform float depthHeight;

void main() {

	vec2 coord = vec2( gl_FragCoord.x / depthWidth, gl_FragCoord.y / depthHeight );

	if ( coord.x >= 1.0 ) {

		gl_FragDepth = texture( depthColor, vec3( coord.x - 1.0, coord.y, 1 ) ).r;

	} else {

		gl_FragDepth = texture( depthColor, vec3( coord.x, coord.y, 0 ) ).r;

	}

}`;class vw{constructor(){this.texture=null,this.mesh=null,this.depthNear=0,this.depthFar=0}init(t,n,i){if(this.texture===null){const a=new An,s=t.properties.get(a);s.__webglTexture=n.texture,(n.depthNear!=i.depthNear||n.depthFar!=i.depthFar)&&(this.depthNear=n.depthNear,this.depthFar=n.depthFar),this.texture=a}}getMesh(t){if(this.texture!==null&&this.mesh===null){const n=t.cameras[0].viewport,i=new Za({vertexShader:_w,fragmentShader:gw,uniforms:{depthColor:{value:this.texture},depthWidth:{value:n.z},depthHeight:{value:n.w}}});this.mesh=new En(new Cl(20,20),i)}return this.mesh}reset(){this.texture=null,this.mesh=null}getDepthTexture(){return this.texture}}class Sw extends Hs{constructor(t,n){super();const i=this;let a=null,s=1,r=null,o="local-floor",l=1,u=null,h=null,p=null,f=null,d=null,v=null;const y=new vw,m=n.getContextAttributes();let c=null,_=null;const g=[],x=[],C=new Lt;let R=null;const b=new $n;b.layers.enable(1),b.viewport=new Ce;const w=new $n;w.layers.enable(2),w.viewport=new Ce;const W=[b,w],S=new pw;S.layers.enable(1),S.layers.enable(2);let T=null,F=null;this.cameraAutoUpdate=!0,this.enabled=!1,this.isPresenting=!1,this.getController=function(k){let $=g[k];return $===void 0&&($=new Sh,g[k]=$),$.getTargetRaySpace()},this.getControllerGrip=function(k){let $=g[k];return $===void 0&&($=new Sh,g[k]=$),$.getGripSpace()},this.getHand=function(k){let $=g[k];return $===void 0&&($=new Sh,g[k]=$),$.getHandSpace()};function G(k){const $=x.indexOf(k.inputSource);if($===-1)return;const _t=g[$];_t!==void 0&&(_t.update(k.inputSource,k.frame,u||r),_t.dispatchEvent({type:k.type,data:k.inputSource}))}function Y(){a.removeEventListener("select",G),a.removeEventListener("selectstart",G),a.removeEventListener("selectend",G),a.removeEventListener("squeeze",G),a.removeEventListener("squeezestart",G),a.removeEventListener("squeezeend",G),a.removeEventListener("end",Y),a.removeEventListener("inputsourceschange",K);for(let k=0;k<g.length;k++){const $=x[k];$!==null&&(x[k]=null,g[k].disconnect($))}T=null,F=null,y.reset(),t.setRenderTarget(c),d=null,f=null,p=null,a=null,_=null,kt.stop(),i.isPresenting=!1,t.setPixelRatio(R),t.setSize(C.width,C.height,!1),i.dispatchEvent({type:"sessionend"})}this.setFramebufferScaleFactor=function(k){s=k,i.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change framebuffer scale while presenting.")},this.setReferenceSpaceType=function(k){o=k,i.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change reference space type while presenting.")},this.getReferenceSpace=function(){return u||r},this.setReferenceSpace=function(k){u=k},this.getBaseLayer=function(){return f!==null?f:d},this.getBinding=function(){return p},this.getFrame=function(){return v},this.getSession=function(){return a},this.setSession=async function(k){if(a=k,a!==null){if(c=t.getRenderTarget(),a.addEventListener("select",G),a.addEventListener("selectstart",G),a.addEventListener("selectend",G),a.addEventListener("squeeze",G),a.addEventListener("squeezestart",G),a.addEventListener("squeezeend",G),a.addEventListener("end",Y),a.addEventListener("inputsourceschange",K),m.xrCompatible!==!0&&await n.makeXRCompatible(),R=t.getPixelRatio(),t.getSize(C),a.renderState.layers===void 0){const $={antialias:m.antialias,alpha:!0,depth:m.depth,stencil:m.stencil,framebufferScaleFactor:s};d=new XRWebGLLayer(a,n,$),a.updateRenderState({baseLayer:d}),t.setPixelRatio(1),t.setSize(d.framebufferWidth,d.framebufferHeight,!1),_=new Ns(d.framebufferWidth,d.framebufferHeight,{format:vi,type:aa,colorSpace:t.outputColorSpace,stencilBuffer:m.stencil})}else{let $=null,_t=null,ct=null;m.depth&&(ct=m.stencil?n.DEPTH24_STENCIL8:n.DEPTH_COMPONENT24,$=m.stencil?to:Pr,_t=m.stencil?$r:Us);const Dt={colorFormat:n.RGBA8,depthFormat:ct,scaleFactor:s};p=new XRWebGLBinding(a,n),f=p.createProjectionLayer(Dt),a.updateRenderState({layers:[f]}),t.setPixelRatio(1),t.setSize(f.textureWidth,f.textureHeight,!1),_=new Ns(f.textureWidth,f.textureHeight,{format:vi,type:aa,depthTexture:new Ux(f.textureWidth,f.textureHeight,_t,void 0,void 0,void 0,void 0,void 0,void 0,$),stencilBuffer:m.stencil,colorSpace:t.outputColorSpace,samples:m.antialias?4:0,resolveDepthBuffer:f.ignoreDepthValues===!1})}_.isXRRenderTarget=!0,this.setFoveation(l),u=null,r=await a.requestReferenceSpace(o),kt.setContext(a),kt.start(),i.isPresenting=!0,i.dispatchEvent({type:"sessionstart"})}},this.getEnvironmentBlendMode=function(){if(a!==null)return a.environmentBlendMode},this.getDepthTexture=function(){return y.getDepthTexture()};function K(k){for(let $=0;$<k.removed.length;$++){const _t=k.removed[$],ct=x.indexOf(_t);ct>=0&&(x[ct]=null,g[ct].disconnect(_t))}for(let $=0;$<k.added.length;$++){const _t=k.added[$];let ct=x.indexOf(_t);if(ct===-1){for(let Et=0;Et<g.length;Et++)if(Et>=x.length){x.push(_t),ct=Et;break}else if(x[Et]===null){x[Et]=_t,ct=Et;break}if(ct===-1)break}const Dt=g[ct];Dt&&Dt.connect(_t)}}const D=new P,V=new P;function z(k,$,_t){D.setFromMatrixPosition($.matrixWorld),V.setFromMatrixPosition(_t.matrixWorld);const ct=D.distanceTo(V),Dt=$.projectionMatrix.elements,Et=_t.projectionMatrix.elements,Yt=Dt[14]/(Dt[10]-1),ue=Dt[14]/(Dt[10]+1),qt=(Dt[9]+1)/Dt[5],U=(Dt[9]-1)/Dt[5],Dn=(Dt[8]-1)/Dt[0],Vt=(Et[8]+1)/Et[0],jt=Yt*Dn,bt=Yt*Vt,Se=ct/(-Dn+Vt),wt=Se*-Dn;if($.matrixWorld.decompose(k.position,k.quaternion,k.scale),k.translateX(wt),k.translateZ(Se),k.matrixWorld.compose(k.position,k.quaternion,k.scale),k.matrixWorldInverse.copy(k.matrixWorld).invert(),Dt[10]===-1)k.projectionMatrix.copy($.projectionMatrix),k.projectionMatrixInverse.copy($.projectionMatrixInverse);else{const A=Yt+Se,M=ue+Se,I=jt-wt,Z=bt+(ct-wt),J=qt*ue/M*A,j=U*ue/M*A;k.projectionMatrix.makePerspective(I,Z,J,j,A,M),k.projectionMatrixInverse.copy(k.projectionMatrix).invert()}}function tt(k,$){$===null?k.matrixWorld.copy(k.matrix):k.matrixWorld.multiplyMatrices($.matrixWorld,k.matrix),k.matrixWorldInverse.copy(k.matrixWorld).invert()}this.updateCamera=function(k){if(a===null)return;let $=k.near,_t=k.far;y.texture!==null&&(y.depthNear>0&&($=y.depthNear),y.depthFar>0&&(_t=y.depthFar)),S.near=w.near=b.near=$,S.far=w.far=b.far=_t,(T!==S.near||F!==S.far)&&(a.updateRenderState({depthNear:S.near,depthFar:S.far}),T=S.near,F=S.far);const ct=k.parent,Dt=S.cameras;tt(S,ct);for(let Et=0;Et<Dt.length;Et++)tt(Dt[Et],ct);Dt.length===2?z(S,b,w):S.projectionMatrix.copy(b.projectionMatrix),it(k,S,ct)};function it(k,$,_t){_t===null?k.matrix.copy($.matrixWorld):(k.matrix.copy(_t.matrixWorld),k.matrix.invert(),k.matrix.multiply($.matrixWorld)),k.matrix.decompose(k.position,k.quaternion,k.scale),k.updateMatrixWorld(!0),k.projectionMatrix.copy($.projectionMatrix),k.projectionMatrixInverse.copy($.projectionMatrixInverse),k.isPerspectiveCamera&&(k.fov=yp*2*Math.atan(1/k.projectionMatrix.elements[5]),k.zoom=1)}this.getCamera=function(){return S},this.getFoveation=function(){if(!(f===null&&d===null))return l},this.setFoveation=function(k){l=k,f!==null&&(f.fixedFoveation=k),d!==null&&d.fixedFoveation!==void 0&&(d.fixedFoveation=k)},this.hasDepthSensing=function(){return y.texture!==null},this.getDepthSensingMesh=function(){return y.getMesh(S)};let ht=null;function Ft(k,$){if(h=$.getViewerPose(u||r),v=$,h!==null){const _t=h.views;d!==null&&(t.setRenderTargetFramebuffer(_,d.framebuffer),t.setRenderTarget(_));let ct=!1;_t.length!==S.cameras.length&&(S.cameras.length=0,ct=!0);for(let Et=0;Et<_t.length;Et++){const Yt=_t[Et];let ue=null;if(d!==null)ue=d.getViewport(Yt);else{const U=p.getViewSubImage(f,Yt);ue=U.viewport,Et===0&&(t.setRenderTargetTextures(_,U.colorTexture,f.ignoreDepthValues?void 0:U.depthStencilTexture),t.setRenderTarget(_))}let qt=W[Et];qt===void 0&&(qt=new $n,qt.layers.enable(Et),qt.viewport=new Ce,W[Et]=qt),qt.matrix.fromArray(Yt.transform.matrix),qt.matrix.decompose(qt.position,qt.quaternion,qt.scale),qt.projectionMatrix.fromArray(Yt.projectionMatrix),qt.projectionMatrixInverse.copy(qt.projectionMatrix).invert(),qt.viewport.set(ue.x,ue.y,ue.width,ue.height),Et===0&&(S.matrix.copy(qt.matrix),S.matrix.decompose(S.position,S.quaternion,S.scale)),ct===!0&&S.cameras.push(qt)}const Dt=a.enabledFeatures;if(Dt&&Dt.includes("depth-sensing")){const Et=p.getDepthInformation(_t[0]);Et&&Et.isValid&&Et.texture&&y.init(t,Et,a.renderState)}}for(let _t=0;_t<g.length;_t++){const ct=x[_t],Dt=g[_t];ct!==null&&Dt!==void 0&&Dt.update(ct,$,u||r)}ht&&ht(k,$),$.detectedPlanes&&i.dispatchEvent({type:"planesdetected",data:$}),v=null}const kt=new wx;kt.setAnimationLoop(Ft),this.setAnimationLoop=function(k){ht=k},this.dispose=function(){}}}const os=new sa,yw=new Te;function xw(e,t){function n(m,c){m.matrixAutoUpdate===!0&&m.updateMatrix(),c.value.copy(m.matrix)}function i(m,c){c.color.getRGB(m.fogColor.value,Ax(e)),c.isFog?(m.fogNear.value=c.near,m.fogFar.value=c.far):c.isFogExp2&&(m.fogDensity.value=c.density)}function a(m,c,_,g,x){c.isMeshBasicMaterial||c.isMeshLambertMaterial?s(m,c):c.isMeshToonMaterial?(s(m,c),p(m,c)):c.isMeshPhongMaterial?(s(m,c),h(m,c)):c.isMeshStandardMaterial?(s(m,c),f(m,c),c.isMeshPhysicalMaterial&&d(m,c,x)):c.isMeshMatcapMaterial?(s(m,c),v(m,c)):c.isMeshDepthMaterial?s(m,c):c.isMeshDistanceMaterial?(s(m,c),y(m,c)):c.isMeshNormalMaterial?s(m,c):c.isLineBasicMaterial?(r(m,c),c.isLineDashedMaterial&&o(m,c)):c.isPointsMaterial?l(m,c,_,g):c.isSpriteMaterial?u(m,c):c.isShadowMaterial?(m.color.value.copy(c.color),m.opacity.value=c.opacity):c.isShaderMaterial&&(c.uniformsNeedUpdate=!1)}function s(m,c){m.opacity.value=c.opacity,c.color&&m.diffuse.value.copy(c.color),c.emissive&&m.emissive.value.copy(c.emissive).multiplyScalar(c.emissiveIntensity),c.map&&(m.map.value=c.map,n(c.map,m.mapTransform)),c.alphaMap&&(m.alphaMap.value=c.alphaMap,n(c.alphaMap,m.alphaMapTransform)),c.bumpMap&&(m.bumpMap.value=c.bumpMap,n(c.bumpMap,m.bumpMapTransform),m.bumpScale.value=c.bumpScale,c.side===bn&&(m.bumpScale.value*=-1)),c.normalMap&&(m.normalMap.value=c.normalMap,n(c.normalMap,m.normalMapTransform),m.normalScale.value.copy(c.normalScale),c.side===bn&&m.normalScale.value.negate()),c.displacementMap&&(m.displacementMap.value=c.displacementMap,n(c.displacementMap,m.displacementMapTransform),m.displacementScale.value=c.displacementScale,m.displacementBias.value=c.displacementBias),c.emissiveMap&&(m.emissiveMap.value=c.emissiveMap,n(c.emissiveMap,m.emissiveMapTransform)),c.specularMap&&(m.specularMap.value=c.specularMap,n(c.specularMap,m.specularMapTransform)),c.alphaTest>0&&(m.alphaTest.value=c.alphaTest);const _=t.get(c),g=_.envMap,x=_.envMapRotation;g&&(m.envMap.value=g,os.copy(x),os.x*=-1,os.y*=-1,os.z*=-1,g.isCubeTexture&&g.isRenderTargetTexture===!1&&(os.y*=-1,os.z*=-1),m.envMapRotation.value.setFromMatrix4(yw.makeRotationFromEuler(os)),m.flipEnvMap.value=g.isCubeTexture&&g.isRenderTargetTexture===!1?-1:1,m.reflectivity.value=c.reflectivity,m.ior.value=c.ior,m.refractionRatio.value=c.refractionRatio),c.lightMap&&(m.lightMap.value=c.lightMap,m.lightMapIntensity.value=c.lightMapIntensity,n(c.lightMap,m.lightMapTransform)),c.aoMap&&(m.aoMap.value=c.aoMap,m.aoMapIntensity.value=c.aoMapIntensity,n(c.aoMap,m.aoMapTransform))}function r(m,c){m.diffuse.value.copy(c.color),m.opacity.value=c.opacity,c.map&&(m.map.value=c.map,n(c.map,m.mapTransform))}function o(m,c){m.dashSize.value=c.dashSize,m.totalSize.value=c.dashSize+c.gapSize,m.scale.value=c.scale}function l(m,c,_,g){m.diffuse.value.copy(c.color),m.opacity.value=c.opacity,m.size.value=c.size*_,m.scale.value=g*.5,c.map&&(m.map.value=c.map,n(c.map,m.uvTransform)),c.alphaMap&&(m.alphaMap.value=c.alphaMap,n(c.alphaMap,m.alphaMapTransform)),c.alphaTest>0&&(m.alphaTest.value=c.alphaTest)}function u(m,c){m.diffuse.value.copy(c.color),m.opacity.value=c.opacity,m.rotation.value=c.rotation,c.map&&(m.map.value=c.map,n(c.map,m.mapTransform)),c.alphaMap&&(m.alphaMap.value=c.alphaMap,n(c.alphaMap,m.alphaMapTransform)),c.alphaTest>0&&(m.alphaTest.value=c.alphaTest)}function h(m,c){m.specular.value.copy(c.specular),m.shininess.value=Math.max(c.shininess,1e-4)}function p(m,c){c.gradientMap&&(m.gradientMap.value=c.gradientMap)}function f(m,c){m.metalness.value=c.metalness,c.metalnessMap&&(m.metalnessMap.value=c.metalnessMap,n(c.metalnessMap,m.metalnessMapTransform)),m.roughness.value=c.roughness,c.roughnessMap&&(m.roughnessMap.value=c.roughnessMap,n(c.roughnessMap,m.roughnessMapTransform)),c.envMap&&(m.envMapIntensity.value=c.envMapIntensity)}function d(m,c,_){m.ior.value=c.ior,c.sheen>0&&(m.sheenColor.value.copy(c.sheenColor).multiplyScalar(c.sheen),m.sheenRoughness.value=c.sheenRoughness,c.sheenColorMap&&(m.sheenColorMap.value=c.sheenColorMap,n(c.sheenColorMap,m.sheenColorMapTransform)),c.sheenRoughnessMap&&(m.sheenRoughnessMap.value=c.sheenRoughnessMap,n(c.sheenRoughnessMap,m.sheenRoughnessMapTransform))),c.clearcoat>0&&(m.clearcoat.value=c.clearcoat,m.clearcoatRoughness.value=c.clearcoatRoughness,c.clearcoatMap&&(m.clearcoatMap.value=c.clearcoatMap,n(c.clearcoatMap,m.clearcoatMapTransform)),c.clearcoatRoughnessMap&&(m.clearcoatRoughnessMap.value=c.clearcoatRoughnessMap,n(c.clearcoatRoughnessMap,m.clearcoatRoughnessMapTransform)),c.clearcoatNormalMap&&(m.clearcoatNormalMap.value=c.clearcoatNormalMap,n(c.clearcoatNormalMap,m.clearcoatNormalMapTransform),m.clearcoatNormalScale.value.copy(c.clearcoatNormalScale),c.side===bn&&m.clearcoatNormalScale.value.negate())),c.dispersion>0&&(m.dispersion.value=c.dispersion),c.iridescence>0&&(m.iridescence.value=c.iridescence,m.iridescenceIOR.value=c.iridescenceIOR,m.iridescenceThicknessMinimum.value=c.iridescenceThicknessRange[0],m.iridescenceThicknessMaximum.value=c.iridescenceThicknessRange[1],c.iridescenceMap&&(m.iridescenceMap.value=c.iridescenceMap,n(c.iridescenceMap,m.iridescenceMapTransform)),c.iridescenceThicknessMap&&(m.iridescenceThicknessMap.value=c.iridescenceThicknessMap,n(c.iridescenceThicknessMap,m.iridescenceThicknessMapTransform))),c.transmission>0&&(m.transmission.value=c.transmission,m.transmissionSamplerMap.value=_.texture,m.transmissionSamplerSize.value.set(_.width,_.height),c.transmissionMap&&(m.transmissionMap.value=c.transmissionMap,n(c.transmissionMap,m.transmissionMapTransform)),m.thickness.value=c.thickness,c.thicknessMap&&(m.thicknessMap.value=c.thicknessMap,n(c.thicknessMap,m.thicknessMapTransform)),m.attenuationDistance.value=c.attenuationDistance,m.attenuationColor.value.copy(c.attenuationColor)),c.anisotropy>0&&(m.anisotropyVector.value.set(c.anisotropy*Math.cos(c.anisotropyRotation),c.anisotropy*Math.sin(c.anisotropyRotation)),c.anisotropyMap&&(m.anisotropyMap.value=c.anisotropyMap,n(c.anisotropyMap,m.anisotropyMapTransform))),m.specularIntensity.value=c.specularIntensity,m.specularColor.value.copy(c.specularColor),c.specularColorMap&&(m.specularColorMap.value=c.specularColorMap,n(c.specularColorMap,m.specularColorMapTransform)),c.specularIntensityMap&&(m.specularIntensityMap.value=c.specularIntensityMap,n(c.specularIntensityMap,m.specularIntensityMapTransform))}function v(m,c){c.matcap&&(m.matcap.value=c.matcap)}function y(m,c){const _=t.get(c).light;m.referencePosition.value.setFromMatrixPosition(_.matrixWorld),m.nearDistance.value=_.shadow.camera.near,m.farDistance.value=_.shadow.camera.far}return{refreshFogUniforms:i,refreshMaterialUniforms:a}}function Mw(e,t,n,i){let a={},s={},r=[];const o=e.getParameter(e.MAX_UNIFORM_BUFFER_BINDINGS);function l(_,g){const x=g.program;i.uniformBlockBinding(_,x)}function u(_,g){let x=a[_.id];x===void 0&&(v(_),x=h(_),a[_.id]=x,_.addEventListener("dispose",m));const C=g.program;i.updateUBOMapping(_,C);const R=t.render.frame;s[_.id]!==R&&(f(_),s[_.id]=R)}function h(_){const g=p();_.__bindingPointIndex=g;const x=e.createBuffer(),C=_.__size,R=_.usage;return e.bindBuffer(e.UNIFORM_BUFFER,x),e.bufferData(e.UNIFORM_BUFFER,C,R),e.bindBuffer(e.UNIFORM_BUFFER,null),e.bindBufferBase(e.UNIFORM_BUFFER,g,x),x}function p(){for(let _=0;_<o;_++)if(r.indexOf(_)===-1)return r.push(_),_;return console.error("THREE.WebGLRenderer: Maximum number of simultaneously usable uniforms groups reached."),0}function f(_){const g=a[_.id],x=_.uniforms,C=_.__cache;e.bindBuffer(e.UNIFORM_BUFFER,g);for(let R=0,b=x.length;R<b;R++){const w=Array.isArray(x[R])?x[R]:[x[R]];for(let W=0,S=w.length;W<S;W++){const T=w[W];if(d(T,R,W,C)===!0){const F=T.__offset,G=Array.isArray(T.value)?T.value:[T.value];let Y=0;for(let K=0;K<G.length;K++){const D=G[K],V=y(D);typeof D=="number"||typeof D=="boolean"?(T.__data[0]=D,e.bufferSubData(e.UNIFORM_BUFFER,F+Y,T.__data)):D.isMatrix3?(T.__data[0]=D.elements[0],T.__data[1]=D.elements[1],T.__data[2]=D.elements[2],T.__data[3]=0,T.__data[4]=D.elements[3],T.__data[5]=D.elements[4],T.__data[6]=D.elements[5],T.__data[7]=0,T.__data[8]=D.elements[6],T.__data[9]=D.elements[7],T.__data[10]=D.elements[8],T.__data[11]=0):(D.toArray(T.__data,Y),Y+=V.storage/Float32Array.BYTES_PER_ELEMENT)}e.bufferSubData(e.UNIFORM_BUFFER,F,T.__data)}}}e.bindBuffer(e.UNIFORM_BUFFER,null)}function d(_,g,x,C){const R=_.value,b=g+"_"+x;if(C[b]===void 0)return typeof R=="number"||typeof R=="boolean"?C[b]=R:C[b]=R.clone(),!0;{const w=C[b];if(typeof R=="number"||typeof R=="boolean"){if(w!==R)return C[b]=R,!0}else if(w.equals(R)===!1)return w.copy(R),!0}return!1}function v(_){const g=_.uniforms;let x=0;const C=16;for(let b=0,w=g.length;b<w;b++){const W=Array.isArray(g[b])?g[b]:[g[b]];for(let S=0,T=W.length;S<T;S++){const F=W[S],G=Array.isArray(F.value)?F.value:[F.value];for(let Y=0,K=G.length;Y<K;Y++){const D=G[Y],V=y(D),z=x%C,tt=z%V.boundary,it=z+tt;x+=tt,it!==0&&C-it<V.storage&&(x+=C-it),F.__data=new Float32Array(V.storage/Float32Array.BYTES_PER_ELEMENT),F.__offset=x,x+=V.storage}}}const R=x%C;return R>0&&(x+=C-R),_.__size=x,_.__cache={},this}function y(_){const g={boundary:0,storage:0};return typeof _=="number"||typeof _=="boolean"?(g.boundary=4,g.storage=4):_.isVector2?(g.boundary=8,g.storage=8):_.isVector3||_.isColor?(g.boundary=16,g.storage=12):_.isVector4?(g.boundary=16,g.storage=16):_.isMatrix3?(g.boundary=48,g.storage=48):_.isMatrix4?(g.boundary=64,g.storage=64):_.isTexture?console.warn("THREE.WebGLRenderer: Texture samplers can not be part of an uniforms group."):console.warn("THREE.WebGLRenderer: Unsupported uniform value type.",_),g}function m(_){const g=_.target;g.removeEventListener("dispose",m);const x=r.indexOf(g.__bindingPointIndex);r.splice(x,1),e.deleteBuffer(a[g.id]),delete a[g.id],delete s[g.id]}function c(){for(const _ in a)e.deleteBuffer(a[_]);r=[],a={},s={}}return{bind:l,update:u,dispose:c}}class Ew{constructor(t={}){const{canvas:n=c1(),context:i=null,depth:a=!0,stencil:s=!1,alpha:r=!1,antialias:o=!1,premultipliedAlpha:l=!0,preserveDrawingBuffer:u=!1,powerPreference:h="default",failIfMajorPerformanceCaveat:p=!1}=t;this.isWebGLRenderer=!0;let f;if(i!==null){if(typeof WebGLRenderingContext<"u"&&i instanceof WebGLRenderingContext)throw new Error("THREE.WebGLRenderer: WebGL 1 is not supported since r163.");f=i.getContextAttributes().alpha}else f=r;const d=new Uint32Array(4),v=new Int32Array(4);let y=null,m=null;const c=[],_=[];this.domElement=n,this.debug={checkShaderErrors:!0,onShaderError:null},this.autoClear=!0,this.autoClearColor=!0,this.autoClearDepth=!0,this.autoClearStencil=!0,this.sortObjects=!0,this.clippingPlanes=[],this.localClippingEnabled=!1,this._outputColorSpace=Ti,this.toneMapping=Va,this.toneMappingExposure=1;const g=this;let x=!1,C=0,R=0,b=null,w=-1,W=null;const S=new Ce,T=new Ce;let F=null;const G=new Ht(0);let Y=0,K=n.width,D=n.height,V=1,z=null,tt=null;const it=new Ce(0,0,K,D),ht=new Ce(0,0,K,D);let Ft=!1;const kt=new zm;let k=!1,$=!1;const _t=new Te,ct=new Te,Dt=new P,Et=new Ce,Yt={background:null,fog:null,environment:null,overrideMaterial:null,isScene:!0};let ue=!1;function qt(){return b===null?V:1}let U=i;function Dn(E,L){return n.getContext(E,L)}try{const E={alpha:!0,depth:a,stencil:s,antialias:o,premultipliedAlpha:l,preserveDrawingBuffer:u,powerPreference:h,failIfMajorPerformanceCaveat:p};if("setAttribute"in n&&n.setAttribute("data-engine",`three.js r${Rm}`),n.addEventListener("webglcontextlost",Q,!1),n.addEventListener("webglcontextrestored",rt,!1),n.addEventListener("webglcontextcreationerror",ut,!1),U===null){const L="webgl2";if(U=Dn(L,E),U===null)throw Dn(L)?new Error("Error creating WebGL context with your selected attributes."):new Error("Error creating WebGL context.")}}catch(E){throw console.error("THREE.WebGLRenderer: "+E.message),E}let Vt,jt,bt,Se,wt,A,M,I,Z,J,j,vt,st,ft,Zt,et,dt,At,Rt,pt,Xt,Ut,pe,N;function lt(){Vt=new CC(U),Vt.init(),Ut=new dw(U,Vt),jt=new MC(U,Vt,t,Ut),bt=new cw(U),jt.reverseDepthBuffer&&bt.buffers.depth.setReversed(!0),Se=new UC(U),wt=new Z2,A=new hw(U,Vt,bt,wt,jt,Ut,Se),M=new TC(g),I=new RC(g),Z=new B1(U),pe=new yC(U,Z),J=new wC(U,Z,Se,pe),j=new LC(U,J,Z,Se),Rt=new NC(U,jt,A),et=new EC(wt),vt=new j2(g,M,I,Vt,jt,pe,et),st=new xw(g,wt),ft=new Q2,Zt=new iw(Vt),At=new SC(g,M,I,bt,j,f,l),dt=new lw(g,j,jt),N=new Mw(U,Se,jt,bt),pt=new xC(U,Vt,Se),Xt=new DC(U,Vt,Se),Se.programs=vt.programs,g.capabilities=jt,g.extensions=Vt,g.properties=wt,g.renderLists=ft,g.shadowMap=dt,g.state=bt,g.info=Se}lt();const X=new Sw(g,U);this.xr=X,this.getContext=function(){return U},this.getContextAttributes=function(){return U.getContextAttributes()},this.forceContextLoss=function(){const E=Vt.get("WEBGL_lose_context");E&&E.loseContext()},this.forceContextRestore=function(){const E=Vt.get("WEBGL_lose_context");E&&E.restoreContext()},this.getPixelRatio=function(){return V},this.setPixelRatio=function(E){E!==void 0&&(V=E,this.setSize(K,D,!1))},this.getSize=function(E){return E.set(K,D)},this.setSize=function(E,L,B=!0){if(X.isPresenting){console.warn("THREE.WebGLRenderer: Can't change size while VR device is presenting.");return}K=E,D=L,n.width=Math.floor(E*V),n.height=Math.floor(L*V),B===!0&&(n.style.width=E+"px",n.style.height=L+"px"),this.setViewport(0,0,E,L)},this.getDrawingBufferSize=function(E){return E.set(K*V,D*V).floor()},this.setDrawingBufferSize=function(E,L,B){K=E,D=L,V=B,n.width=Math.floor(E*B),n.height=Math.floor(L*B),this.setViewport(0,0,E,L)},this.getCurrentViewport=function(E){return E.copy(S)},this.getViewport=function(E){return E.copy(it)},this.setViewport=function(E,L,B,H){E.isVector4?it.set(E.x,E.y,E.z,E.w):it.set(E,L,B,H),bt.viewport(S.copy(it).multiplyScalar(V).round())},this.getScissor=function(E){return E.copy(ht)},this.setScissor=function(E,L,B,H){E.isVector4?ht.set(E.x,E.y,E.z,E.w):ht.set(E,L,B,H),bt.scissor(T.copy(ht).multiplyScalar(V).round())},this.getScissorTest=function(){return Ft},this.setScissorTest=function(E){bt.setScissorTest(Ft=E)},this.setOpaqueSort=function(E){z=E},this.setTransparentSort=function(E){tt=E},this.getClearColor=function(E){return E.copy(At.getClearColor())},this.setClearColor=function(){At.setClearColor.apply(At,arguments)},this.getClearAlpha=function(){return At.getClearAlpha()},this.setClearAlpha=function(){At.setClearAlpha.apply(At,arguments)},this.clear=function(E=!0,L=!0,B=!0){let H=0;if(E){let O=!1;if(b!==null){const nt=b.texture.format;O=nt===Lm||nt===Nm||nt===Um}if(O){const nt=b.texture.type,ot=nt===aa||nt===Us||nt===fl||nt===$r||nt===wm||nt===Dm,mt=At.getClearColor(),gt=At.getClearAlpha(),Mt=mt.r,Tt=mt.g,St=mt.b;ot?(d[0]=Mt,d[1]=Tt,d[2]=St,d[3]=gt,U.clearBufferuiv(U.COLOR,0,d)):(v[0]=Mt,v[1]=Tt,v[2]=St,v[3]=gt,U.clearBufferiv(U.COLOR,0,v))}else H|=U.COLOR_BUFFER_BIT}L&&(H|=U.DEPTH_BUFFER_BIT,U.clearDepth(this.capabilities.reverseDepthBuffer?0:1)),B&&(H|=U.STENCIL_BUFFER_BIT,this.state.buffers.stencil.setMask(4294967295)),U.clear(H)},this.clearColor=function(){this.clear(!0,!1,!1)},this.clearDepth=function(){this.clear(!1,!0,!1)},this.clearStencil=function(){this.clear(!1,!1,!0)},this.dispose=function(){n.removeEventListener("webglcontextlost",Q,!1),n.removeEventListener("webglcontextrestored",rt,!1),n.removeEventListener("webglcontextcreationerror",ut,!1),ft.dispose(),Zt.dispose(),wt.dispose(),M.dispose(),I.dispose(),j.dispose(),pe.dispose(),N.dispose(),vt.dispose(),X.dispose(),X.removeEventListener("sessionstart",Vm),X.removeEventListener("sessionend",Xm),$a.stop()};function Q(E){E.preventDefault(),console.log("THREE.WebGLRenderer: Context Lost."),x=!0}function rt(){console.log("THREE.WebGLRenderer: Context Restored."),x=!1;const E=Se.autoReset,L=dt.enabled,B=dt.autoUpdate,H=dt.needsUpdate,O=dt.type;lt(),Se.autoReset=E,dt.enabled=L,dt.autoUpdate=B,dt.needsUpdate=H,dt.type=O}function ut(E){console.error("THREE.WebGLRenderer: A WebGL context could not be created. Reason: ",E.statusMessage)}function Wt(E){const L=E.target;L.removeEventListener("dispose",Wt),Ue(L)}function Ue(E){mn(E),wt.remove(E)}function mn(E){const L=wt.get(E).programs;L!==void 0&&(L.forEach(function(B){vt.releaseProgram(B)}),E.isShaderMaterial&&vt.releaseShaderCache(E))}this.renderBufferDirect=function(E,L,B,H,O,nt){L===null&&(L=Yt);const ot=O.isMesh&&O.matrixWorld.determinant()<0,mt=Hx(E,L,B,H,O);bt.setMaterial(H,ot);let gt=B.index,Mt=1;if(H.wireframe===!0){if(gt=J.getWireframeAttribute(B),gt===void 0)return;Mt=2}const Tt=B.drawRange,St=B.attributes.position;let se=Tt.start*Mt,ye=(Tt.start+Tt.count)*Mt;nt!==null&&(se=Math.max(se,nt.start*Mt),ye=Math.min(ye,(nt.start+nt.count)*Mt)),gt!==null?(se=Math.max(se,0),ye=Math.min(ye,gt.count)):St!=null&&(se=Math.max(se,0),ye=Math.min(ye,St.count));const be=ye-se;if(be<0||be===1/0)return;pe.setup(O,H,mt,B,gt);let Un,ee=pt;if(gt!==null&&(Un=Z.get(gt),ee=Xt,ee.setIndex(Un)),O.isMesh)H.wireframe===!0?(bt.setLineWidth(H.wireframeLinewidth*qt()),ee.setMode(U.LINES)):ee.setMode(U.TRIANGLES);else if(O.isLine){let yt=H.linewidth;yt===void 0&&(yt=1),bt.setLineWidth(yt*qt()),O.isLineSegments?ee.setMode(U.LINES):O.isLineLoop?ee.setMode(U.LINE_LOOP):ee.setMode(U.LINE_STRIP)}else O.isPoints?ee.setMode(U.POINTS):O.isSprite&&ee.setMode(U.TRIANGLES);if(O.isBatchedMesh)if(O._multiDrawInstances!==null)ee.renderMultiDrawInstances(O._multiDrawStarts,O._multiDrawCounts,O._multiDrawCount,O._multiDrawInstances);else if(Vt.get("WEBGL_multi_draw"))ee.renderMultiDraw(O._multiDrawStarts,O._multiDrawCounts,O._multiDrawCount);else{const yt=O._multiDrawStarts,je=O._multiDrawCounts,ne=O._multiDrawCount,oi=gt?Z.get(gt).bytesPerElement:1,Gs=wt.get(H).currentProgram.getUniforms();for(let Nn=0;Nn<ne;Nn++)Gs.setValue(U,"_gl_DrawID",Nn),ee.render(yt[Nn]/oi,je[Nn])}else if(O.isInstancedMesh)ee.renderInstances(se,be,O.count);else if(B.isInstancedBufferGeometry){const yt=B._maxInstanceCount!==void 0?B._maxInstanceCount:1/0,je=Math.min(B.instanceCount,yt);ee.renderInstances(se,be,je)}else ee.render(se,be)};function Jt(E,L,B){E.transparent===!0&&E.side===pi&&E.forceSinglePass===!1?(E.side=bn,E.needsUpdate=!0,Dl(E,L,B),E.side=ja,E.needsUpdate=!0,Dl(E,L,B),E.side=pi):Dl(E,L,B)}this.compile=function(E,L,B=null){B===null&&(B=E),m=Zt.get(B),m.init(L),_.push(m),B.traverseVisible(function(O){O.isLight&&O.layers.test(L.layers)&&(m.pushLight(O),O.castShadow&&m.pushShadow(O))}),E!==B&&E.traverseVisible(function(O){O.isLight&&O.layers.test(L.layers)&&(m.pushLight(O),O.castShadow&&m.pushShadow(O))}),m.setupLights();const H=new Set;return E.traverse(function(O){if(!(O.isMesh||O.isPoints||O.isLine||O.isSprite))return;const nt=O.material;if(nt)if(Array.isArray(nt))for(let ot=0;ot<nt.length;ot++){const mt=nt[ot];Jt(mt,B,O),H.add(mt)}else Jt(nt,B,O),H.add(nt)}),_.pop(),m=null,H},this.compileAsync=function(E,L,B=null){const H=this.compile(E,L,B);return new Promise(O=>{function nt(){if(H.forEach(function(ot){wt.get(ot).currentProgram.isReady()&&H.delete(ot)}),H.size===0){O(E);return}setTimeout(nt,10)}Vt.get("KHR_parallel_shader_compile")!==null?nt():setTimeout(nt,10)})};let _n=null;function Ii(E){_n&&_n(E)}function Vm(){$a.stop()}function Xm(){$a.start()}const $a=new wx;$a.setAnimationLoop(Ii),typeof self<"u"&&$a.setContext(self),this.setAnimationLoop=function(E){_n=E,X.setAnimationLoop(E),E===null?$a.stop():$a.start()},X.addEventListener("sessionstart",Vm),X.addEventListener("sessionend",Xm),this.render=function(E,L){if(L!==void 0&&L.isCamera!==!0){console.error("THREE.WebGLRenderer.render: camera is not an instance of THREE.Camera.");return}if(x===!0)return;if(E.matrixWorldAutoUpdate===!0&&E.updateMatrixWorld(),L.parent===null&&L.matrixWorldAutoUpdate===!0&&L.updateMatrixWorld(),X.enabled===!0&&X.isPresenting===!0&&(X.cameraAutoUpdate===!0&&X.updateCamera(L),L=X.getCamera()),E.isScene===!0&&E.onBeforeRender(g,E,L,b),m=Zt.get(E,_.length),m.init(L),_.push(m),ct.multiplyMatrices(L.projectionMatrix,L.matrixWorldInverse),kt.setFromProjectionMatrix(ct),$=this.localClippingEnabled,k=et.init(this.clippingPlanes,$),y=ft.get(E,c.length),y.init(),c.push(y),X.enabled===!0&&X.isPresenting===!0){const nt=g.xr.getDepthSensingMesh();nt!==null&&sf(nt,L,-1/0,g.sortObjects)}sf(E,L,0,g.sortObjects),y.finish(),g.sortObjects===!0&&y.sort(z,tt),ue=X.enabled===!1||X.isPresenting===!1||X.hasDepthSensing()===!1,ue&&At.addToRenderList(y,E),this.info.render.frame++,k===!0&&et.beginShadows();const B=m.state.shadowsArray;dt.render(B,E,L),k===!0&&et.endShadows(),this.info.autoReset===!0&&this.info.reset();const H=y.opaque,O=y.transmissive;if(m.setupLights(),L.isArrayCamera){const nt=L.cameras;if(O.length>0)for(let ot=0,mt=nt.length;ot<mt;ot++){const gt=nt[ot];Ym(H,O,E,gt)}ue&&At.render(E);for(let ot=0,mt=nt.length;ot<mt;ot++){const gt=nt[ot];km(y,E,gt,gt.viewport)}}else O.length>0&&Ym(H,O,E,L),ue&&At.render(E),km(y,E,L);b!==null&&(A.updateMultisampleRenderTarget(b),A.updateRenderTargetMipmap(b)),E.isScene===!0&&E.onAfterRender(g,E,L),pe.resetDefaultState(),w=-1,W=null,_.pop(),_.length>0?(m=_[_.length-1],k===!0&&et.setGlobalState(g.clippingPlanes,m.state.camera)):m=null,c.pop(),c.length>0?y=c[c.length-1]:y=null};function sf(E,L,B,H){if(E.visible===!1)return;if(E.layers.test(L.layers)){if(E.isGroup)B=E.renderOrder;else if(E.isLOD)E.autoUpdate===!0&&E.update(L);else if(E.isLight)m.pushLight(E),E.castShadow&&m.pushShadow(E);else if(E.isSprite){if(!E.frustumCulled||kt.intersectsSprite(E)){H&&Et.setFromMatrixPosition(E.matrixWorld).applyMatrix4(ct);const ot=j.update(E),mt=E.material;mt.visible&&y.push(E,ot,mt,B,Et.z,null)}}else if((E.isMesh||E.isLine||E.isPoints)&&(!E.frustumCulled||kt.intersectsObject(E))){const ot=j.update(E),mt=E.material;if(H&&(E.boundingSphere!==void 0?(E.boundingSphere===null&&E.computeBoundingSphere(),Et.copy(E.boundingSphere.center)):(ot.boundingSphere===null&&ot.computeBoundingSphere(),Et.copy(ot.boundingSphere.center)),Et.applyMatrix4(E.matrixWorld).applyMatrix4(ct)),Array.isArray(mt)){const gt=ot.groups;for(let Mt=0,Tt=gt.length;Mt<Tt;Mt++){const St=gt[Mt],se=mt[St.materialIndex];se&&se.visible&&y.push(E,ot,se,B,Et.z,St)}}else mt.visible&&y.push(E,ot,mt,B,Et.z,null)}}const nt=E.children;for(let ot=0,mt=nt.length;ot<mt;ot++)sf(nt[ot],L,B,H)}function km(E,L,B,H){const O=E.opaque,nt=E.transmissive,ot=E.transparent;m.setupLightsView(B),k===!0&&et.setGlobalState(g.clippingPlanes,B),H&&bt.viewport(S.copy(H)),O.length>0&&wl(O,L,B),nt.length>0&&wl(nt,L,B),ot.length>0&&wl(ot,L,B),bt.buffers.depth.setTest(!0),bt.buffers.depth.setMask(!0),bt.buffers.color.setMask(!0),bt.setPolygonOffset(!1)}function Ym(E,L,B,H){if((B.isScene===!0?B.overrideMaterial:null)!==null)return;m.state.transmissionRenderTarget[H.id]===void 0&&(m.state.transmissionRenderTarget[H.id]=new Ns(1,1,{generateMipmaps:!0,type:Vt.has("EXT_color_buffer_half_float")||Vt.has("EXT_color_buffer_float")?Tl:aa,minFilter:gs,samples:4,stencilBuffer:s,resolveDepthBuffer:!1,resolveStencilBuffer:!1,colorSpace:ae.workingColorSpace}));const nt=m.state.transmissionRenderTarget[H.id],ot=H.viewport||S;nt.setSize(ot.z,ot.w);const mt=g.getRenderTarget();g.setRenderTarget(nt),g.getClearColor(G),Y=g.getClearAlpha(),Y<1&&g.setClearColor(16777215,.5),g.clear(),ue&&At.render(B);const gt=g.toneMapping;g.toneMapping=Va;const Mt=H.viewport;if(H.viewport!==void 0&&(H.viewport=void 0),m.setupLightsView(H),k===!0&&et.setGlobalState(g.clippingPlanes,H),wl(E,B,H),A.updateMultisampleRenderTarget(nt),A.updateRenderTargetMipmap(nt),Vt.has("WEBGL_multisampled_render_to_texture")===!1){let Tt=!1;for(let St=0,se=L.length;St<se;St++){const ye=L[St],be=ye.object,Un=ye.geometry,ee=ye.material,yt=ye.group;if(ee.side===pi&&be.layers.test(H.layers)){const je=ee.side;ee.side=bn,ee.needsUpdate=!0,qm(be,B,H,Un,ee,yt),ee.side=je,ee.needsUpdate=!0,Tt=!0}}Tt===!0&&(A.updateMultisampleRenderTarget(nt),A.updateRenderTargetMipmap(nt))}g.setRenderTarget(mt),g.setClearColor(G,Y),Mt!==void 0&&(H.viewport=Mt),g.toneMapping=gt}function wl(E,L,B){const H=L.isScene===!0?L.overrideMaterial:null;for(let O=0,nt=E.length;O<nt;O++){const ot=E[O],mt=ot.object,gt=ot.geometry,Mt=H===null?ot.material:H,Tt=ot.group;mt.layers.test(B.layers)&&qm(mt,L,B,gt,Mt,Tt)}}function qm(E,L,B,H,O,nt){E.onBeforeRender(g,L,B,H,O,nt),E.modelViewMatrix.multiplyMatrices(B.matrixWorldInverse,E.matrixWorld),E.normalMatrix.getNormalMatrix(E.modelViewMatrix),O.onBeforeRender(g,L,B,H,E,nt),O.transparent===!0&&O.side===pi&&O.forceSinglePass===!1?(O.side=bn,O.needsUpdate=!0,g.renderBufferDirect(B,L,H,O,E,nt),O.side=ja,O.needsUpdate=!0,g.renderBufferDirect(B,L,H,O,E,nt),O.side=pi):g.renderBufferDirect(B,L,H,O,E,nt),E.onAfterRender(g,L,B,H,O,nt)}function Dl(E,L,B){L.isScene!==!0&&(L=Yt);const H=wt.get(E),O=m.state.lights,nt=m.state.shadowsArray,ot=O.state.version,mt=vt.getParameters(E,O.state,nt,L,B),gt=vt.getProgramCacheKey(mt);let Mt=H.programs;H.environment=E.isMeshStandardMaterial?L.environment:null,H.fog=L.fog,H.envMap=(E.isMeshStandardMaterial?I:M).get(E.envMap||H.environment),H.envMapRotation=H.environment!==null&&E.envMap===null?L.environmentRotation:E.envMapRotation,Mt===void 0&&(E.addEventListener("dispose",Wt),Mt=new Map,H.programs=Mt);let Tt=Mt.get(gt);if(Tt!==void 0){if(H.currentProgram===Tt&&H.lightsStateVersion===ot)return jm(E,mt),Tt}else mt.uniforms=vt.getUniforms(E),E.onBeforeCompile(mt,g),Tt=vt.acquireProgram(mt,gt),Mt.set(gt,Tt),H.uniforms=mt.uniforms;const St=H.uniforms;return(!E.isShaderMaterial&&!E.isRawShaderMaterial||E.clipping===!0)&&(St.clippingPlanes=et.uniform),jm(E,mt),H.needsLights=Vx(E),H.lightsStateVersion=ot,H.needsLights&&(St.ambientLightColor.value=O.state.ambient,St.lightProbe.value=O.state.probe,St.directionalLights.value=O.state.directional,St.directionalLightShadows.value=O.state.directionalShadow,St.spotLights.value=O.state.spot,St.spotLightShadows.value=O.state.spotShadow,St.rectAreaLights.value=O.state.rectArea,St.ltc_1.value=O.state.rectAreaLTC1,St.ltc_2.value=O.state.rectAreaLTC2,St.pointLights.value=O.state.point,St.pointLightShadows.value=O.state.pointShadow,St.hemisphereLights.value=O.state.hemi,St.directionalShadowMap.value=O.state.directionalShadowMap,St.directionalShadowMatrix.value=O.state.directionalShadowMatrix,St.spotShadowMap.value=O.state.spotShadowMap,St.spotLightMatrix.value=O.state.spotLightMatrix,St.spotLightMap.value=O.state.spotLightMap,St.pointShadowMap.value=O.state.pointShadowMap,St.pointShadowMatrix.value=O.state.pointShadowMatrix),H.currentProgram=Tt,H.uniformsList=null,Tt}function Wm(E){if(E.uniformsList===null){const L=E.currentProgram.getUniforms();E.uniformsList=ju.seqWithValue(L.seq,E.uniforms)}return E.uniformsList}function jm(E,L){const B=wt.get(E);B.outputColorSpace=L.outputColorSpace,B.batching=L.batching,B.batchingColor=L.batchingColor,B.instancing=L.instancing,B.instancingColor=L.instancingColor,B.instancingMorph=L.instancingMorph,B.skinning=L.skinning,B.morphTargets=L.morphTargets,B.morphNormals=L.morphNormals,B.morphColors=L.morphColors,B.morphTargetsCount=L.morphTargetsCount,B.numClippingPlanes=L.numClippingPlanes,B.numIntersection=L.numClipIntersection,B.vertexAlphas=L.vertexAlphas,B.vertexTangents=L.vertexTangents,B.toneMapping=L.toneMapping}function Hx(E,L,B,H,O){L.isScene!==!0&&(L=Yt),A.resetTextureUnits();const nt=L.fog,ot=H.isMeshStandardMaterial?L.environment:null,mt=b===null?g.outputColorSpace:b.isXRRenderTarget===!0?b.texture.colorSpace:Ja,gt=(H.isMeshStandardMaterial?I:M).get(H.envMap||ot),Mt=H.vertexColors===!0&&!!B.attributes.color&&B.attributes.color.itemSize===4,Tt=!!B.attributes.tangent&&(!!H.normalMap||H.anisotropy>0),St=!!B.morphAttributes.position,se=!!B.morphAttributes.normal,ye=!!B.morphAttributes.color;let be=Va;H.toneMapped&&(b===null||b.isXRRenderTarget===!0)&&(be=g.toneMapping);const Un=B.morphAttributes.position||B.morphAttributes.normal||B.morphAttributes.color,ee=Un!==void 0?Un.length:0,yt=wt.get(H),je=m.state.lights;if(k===!0&&($===!0||E!==W)){const Wn=E===W&&H.id===w;et.setState(H,E,Wn)}let ne=!1;H.version===yt.__version?(yt.needsLights&&yt.lightsStateVersion!==je.state.version||yt.outputColorSpace!==mt||O.isBatchedMesh&&yt.batching===!1||!O.isBatchedMesh&&yt.batching===!0||O.isBatchedMesh&&yt.batchingColor===!0&&O.colorTexture===null||O.isBatchedMesh&&yt.batchingColor===!1&&O.colorTexture!==null||O.isInstancedMesh&&yt.instancing===!1||!O.isInstancedMesh&&yt.instancing===!0||O.isSkinnedMesh&&yt.skinning===!1||!O.isSkinnedMesh&&yt.skinning===!0||O.isInstancedMesh&&yt.instancingColor===!0&&O.instanceColor===null||O.isInstancedMesh&&yt.instancingColor===!1&&O.instanceColor!==null||O.isInstancedMesh&&yt.instancingMorph===!0&&O.morphTexture===null||O.isInstancedMesh&&yt.instancingMorph===!1&&O.morphTexture!==null||yt.envMap!==gt||H.fog===!0&&yt.fog!==nt||yt.numClippingPlanes!==void 0&&(yt.numClippingPlanes!==et.numPlanes||yt.numIntersection!==et.numIntersection)||yt.vertexAlphas!==Mt||yt.vertexTangents!==Tt||yt.morphTargets!==St||yt.morphNormals!==se||yt.morphColors!==ye||yt.toneMapping!==be||yt.morphTargetsCount!==ee)&&(ne=!0):(ne=!0,yt.__version=H.version);let oi=yt.currentProgram;ne===!0&&(oi=Dl(H,L,O));let Gs=!1,Nn=!1,rf=!1;const we=oi.getUniforms(),ua=yt.uniforms;if(bt.useProgram(oi.program)&&(Gs=!0,Nn=!0,rf=!0),H.id!==w&&(w=H.id,Nn=!0),Gs||W!==E){jt.reverseDepthBuffer?(_t.copy(E.projectionMatrix),h1(_t),d1(_t),we.setValue(U,"projectionMatrix",_t)):we.setValue(U,"projectionMatrix",E.projectionMatrix),we.setValue(U,"viewMatrix",E.matrixWorldInverse);const Wn=we.map.cameraPosition;Wn!==void 0&&Wn.setValue(U,Dt.setFromMatrixPosition(E.matrixWorld)),jt.logarithmicDepthBuffer&&we.setValue(U,"logDepthBufFC",2/(Math.log(E.far+1)/Math.LN2)),(H.isMeshPhongMaterial||H.isMeshToonMaterial||H.isMeshLambertMaterial||H.isMeshBasicMaterial||H.isMeshStandardMaterial||H.isShaderMaterial)&&we.setValue(U,"isOrthographic",E.isOrthographicCamera===!0),W!==E&&(W=E,Nn=!0,rf=!0)}if(O.isSkinnedMesh){we.setOptional(U,O,"bindMatrix"),we.setOptional(U,O,"bindMatrixInverse");const Wn=O.skeleton;Wn&&(Wn.boneTexture===null&&Wn.computeBoneTexture(),we.setValue(U,"boneTexture",Wn.boneTexture,A))}O.isBatchedMesh&&(we.setOptional(U,O,"batchingTexture"),we.setValue(U,"batchingTexture",O._matricesTexture,A),we.setOptional(U,O,"batchingIdTexture"),we.setValue(U,"batchingIdTexture",O._indirectTexture,A),we.setOptional(U,O,"batchingColorTexture"),O._colorsTexture!==null&&we.setValue(U,"batchingColorTexture",O._colorsTexture,A));const of=B.morphAttributes;if((of.position!==void 0||of.normal!==void 0||of.color!==void 0)&&Rt.update(O,B,oi),(Nn||yt.receiveShadow!==O.receiveShadow)&&(yt.receiveShadow=O.receiveShadow,we.setValue(U,"receiveShadow",O.receiveShadow)),H.isMeshGouraudMaterial&&H.envMap!==null&&(ua.envMap.value=gt,ua.flipEnvMap.value=gt.isCubeTexture&&gt.isRenderTargetTexture===!1?-1:1),H.isMeshStandardMaterial&&H.envMap===null&&L.environment!==null&&(ua.envMapIntensity.value=L.environmentIntensity),Nn&&(we.setValue(U,"toneMappingExposure",g.toneMappingExposure),yt.needsLights&&Gx(ua,rf),nt&&H.fog===!0&&st.refreshFogUniforms(ua,nt),st.refreshMaterialUniforms(ua,H,V,D,m.state.transmissionRenderTarget[E.id]),ju.upload(U,Wm(yt),ua,A)),H.isShaderMaterial&&H.uniformsNeedUpdate===!0&&(ju.upload(U,Wm(yt),ua,A),H.uniformsNeedUpdate=!1),H.isSpriteMaterial&&we.setValue(U,"center",O.center),we.setValue(U,"modelViewMatrix",O.modelViewMatrix),we.setValue(U,"normalMatrix",O.normalMatrix),we.setValue(U,"modelMatrix",O.matrixWorld),H.isShaderMaterial||H.isRawShaderMaterial){const Wn=H.uniformsGroups;for(let lf=0,Xx=Wn.length;lf<Xx;lf++){const Zm=Wn[lf];N.update(Zm,oi),N.bind(Zm,oi)}}return oi}function Gx(E,L){E.ambientLightColor.needsUpdate=L,E.lightProbe.needsUpdate=L,E.directionalLights.needsUpdate=L,E.directionalLightShadows.needsUpdate=L,E.pointLights.needsUpdate=L,E.pointLightShadows.needsUpdate=L,E.spotLights.needsUpdate=L,E.spotLightShadows.needsUpdate=L,E.rectAreaLights.needsUpdate=L,E.hemisphereLights.needsUpdate=L}function Vx(E){return E.isMeshLambertMaterial||E.isMeshToonMaterial||E.isMeshPhongMaterial||E.isMeshStandardMaterial||E.isShadowMaterial||E.isShaderMaterial&&E.lights===!0}this.getActiveCubeFace=function(){return C},this.getActiveMipmapLevel=function(){return R},this.getRenderTarget=function(){return b},this.setRenderTargetTextures=function(E,L,B){wt.get(E.texture).__webglTexture=L,wt.get(E.depthTexture).__webglTexture=B;const H=wt.get(E);H.__hasExternalTextures=!0,H.__autoAllocateDepthBuffer=B===void 0,H.__autoAllocateDepthBuffer||Vt.has("WEBGL_multisampled_render_to_texture")===!0&&(console.warn("THREE.WebGLRenderer: Render-to-texture extension was disabled because an external texture was provided"),H.__useRenderToTexture=!1)},this.setRenderTargetFramebuffer=function(E,L){const B=wt.get(E);B.__webglFramebuffer=L,B.__useDefaultFramebuffer=L===void 0},this.setRenderTarget=function(E,L=0,B=0){b=E,C=L,R=B;let H=!0,O=null,nt=!1,ot=!1;if(E){const gt=wt.get(E);if(gt.__useDefaultFramebuffer!==void 0)bt.bindFramebuffer(U.FRAMEBUFFER,null),H=!1;else if(gt.__webglFramebuffer===void 0)A.setupRenderTarget(E);else if(gt.__hasExternalTextures)A.rebindTextures(E,wt.get(E.texture).__webglTexture,wt.get(E.depthTexture).__webglTexture);else if(E.depthBuffer){const St=E.depthTexture;if(gt.__boundDepthTexture!==St){if(St!==null&&wt.has(St)&&(E.width!==St.image.width||E.height!==St.image.height))throw new Error("WebGLRenderTarget: Attached DepthTexture is initialized to the incorrect size.");A.setupDepthRenderbuffer(E)}}const Mt=E.texture;(Mt.isData3DTexture||Mt.isDataArrayTexture||Mt.isCompressedArrayTexture)&&(ot=!0);const Tt=wt.get(E).__webglFramebuffer;E.isWebGLCubeRenderTarget?(Array.isArray(Tt[L])?O=Tt[L][B]:O=Tt[L],nt=!0):E.samples>0&&A.useMultisampledRTT(E)===!1?O=wt.get(E).__webglMultisampledFramebuffer:Array.isArray(Tt)?O=Tt[B]:O=Tt,S.copy(E.viewport),T.copy(E.scissor),F=E.scissorTest}else S.copy(it).multiplyScalar(V).floor(),T.copy(ht).multiplyScalar(V).floor(),F=Ft;if(bt.bindFramebuffer(U.FRAMEBUFFER,O)&&H&&bt.drawBuffers(E,O),bt.viewport(S),bt.scissor(T),bt.setScissorTest(F),nt){const gt=wt.get(E.texture);U.framebufferTexture2D(U.FRAMEBUFFER,U.COLOR_ATTACHMENT0,U.TEXTURE_CUBE_MAP_POSITIVE_X+L,gt.__webglTexture,B)}else if(ot){const gt=wt.get(E.texture),Mt=L||0;U.framebufferTextureLayer(U.FRAMEBUFFER,U.COLOR_ATTACHMENT0,gt.__webglTexture,B||0,Mt)}w=-1},this.readRenderTargetPixels=function(E,L,B,H,O,nt,ot){if(!(E&&E.isWebGLRenderTarget)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");return}let mt=wt.get(E).__webglFramebuffer;if(E.isWebGLCubeRenderTarget&&ot!==void 0&&(mt=mt[ot]),mt){bt.bindFramebuffer(U.FRAMEBUFFER,mt);try{const gt=E.texture,Mt=gt.format,Tt=gt.type;if(!jt.textureFormatReadable(Mt)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in RGBA or implementation defined format.");return}if(!jt.textureTypeReadable(Tt)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in UnsignedByteType or implementation defined type.");return}L>=0&&L<=E.width-H&&B>=0&&B<=E.height-O&&U.readPixels(L,B,H,O,Ut.convert(Mt),Ut.convert(Tt),nt)}finally{const gt=b!==null?wt.get(b).__webglFramebuffer:null;bt.bindFramebuffer(U.FRAMEBUFFER,gt)}}},this.readRenderTargetPixelsAsync=async function(E,L,B,H,O,nt,ot){if(!(E&&E.isWebGLRenderTarget))throw new Error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");let mt=wt.get(E).__webglFramebuffer;if(E.isWebGLCubeRenderTarget&&ot!==void 0&&(mt=mt[ot]),mt){const gt=E.texture,Mt=gt.format,Tt=gt.type;if(!jt.textureFormatReadable(Mt))throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in RGBA or implementation defined format.");if(!jt.textureTypeReadable(Tt))throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in UnsignedByteType or implementation defined type.");if(L>=0&&L<=E.width-H&&B>=0&&B<=E.height-O){bt.bindFramebuffer(U.FRAMEBUFFER,mt);const St=U.createBuffer();U.bindBuffer(U.PIXEL_PACK_BUFFER,St),U.bufferData(U.PIXEL_PACK_BUFFER,nt.byteLength,U.STREAM_READ),U.readPixels(L,B,H,O,Ut.convert(Mt),Ut.convert(Tt),0);const se=b!==null?wt.get(b).__webglFramebuffer:null;bt.bindFramebuffer(U.FRAMEBUFFER,se);const ye=U.fenceSync(U.SYNC_GPU_COMMANDS_COMPLETE,0);return U.flush(),await f1(U,ye,4),U.bindBuffer(U.PIXEL_PACK_BUFFER,St),U.getBufferSubData(U.PIXEL_PACK_BUFFER,0,nt),U.deleteBuffer(St),U.deleteSync(ye),nt}else throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: requested read bounds are out of range.")}},this.copyFramebufferToTexture=function(E,L=null,B=0){E.isTexture!==!0&&(Wu("WebGLRenderer: copyFramebufferToTexture function signature has changed."),L=arguments[0]||null,E=arguments[1]);const H=Math.pow(2,-B),O=Math.floor(E.image.width*H),nt=Math.floor(E.image.height*H),ot=L!==null?L.x:0,mt=L!==null?L.y:0;A.setTexture2D(E,0),U.copyTexSubImage2D(U.TEXTURE_2D,B,0,0,ot,mt,O,nt),bt.unbindTexture()},this.copyTextureToTexture=function(E,L,B=null,H=null,O=0){E.isTexture!==!0&&(Wu("WebGLRenderer: copyTextureToTexture function signature has changed."),H=arguments[0]||null,E=arguments[1],L=arguments[2],O=arguments[3]||0,B=null);let nt,ot,mt,gt,Mt,Tt;B!==null?(nt=B.max.x-B.min.x,ot=B.max.y-B.min.y,mt=B.min.x,gt=B.min.y):(nt=E.image.width,ot=E.image.height,mt=0,gt=0),H!==null?(Mt=H.x,Tt=H.y):(Mt=0,Tt=0);const St=Ut.convert(L.format),se=Ut.convert(L.type);A.setTexture2D(L,0),U.pixelStorei(U.UNPACK_FLIP_Y_WEBGL,L.flipY),U.pixelStorei(U.UNPACK_PREMULTIPLY_ALPHA_WEBGL,L.premultiplyAlpha),U.pixelStorei(U.UNPACK_ALIGNMENT,L.unpackAlignment);const ye=U.getParameter(U.UNPACK_ROW_LENGTH),be=U.getParameter(U.UNPACK_IMAGE_HEIGHT),Un=U.getParameter(U.UNPACK_SKIP_PIXELS),ee=U.getParameter(U.UNPACK_SKIP_ROWS),yt=U.getParameter(U.UNPACK_SKIP_IMAGES),je=E.isCompressedTexture?E.mipmaps[O]:E.image;U.pixelStorei(U.UNPACK_ROW_LENGTH,je.width),U.pixelStorei(U.UNPACK_IMAGE_HEIGHT,je.height),U.pixelStorei(U.UNPACK_SKIP_PIXELS,mt),U.pixelStorei(U.UNPACK_SKIP_ROWS,gt),E.isDataTexture?U.texSubImage2D(U.TEXTURE_2D,O,Mt,Tt,nt,ot,St,se,je.data):E.isCompressedTexture?U.compressedTexSubImage2D(U.TEXTURE_2D,O,Mt,Tt,je.width,je.height,St,je.data):U.texSubImage2D(U.TEXTURE_2D,O,Mt,Tt,nt,ot,St,se,je),U.pixelStorei(U.UNPACK_ROW_LENGTH,ye),U.pixelStorei(U.UNPACK_IMAGE_HEIGHT,be),U.pixelStorei(U.UNPACK_SKIP_PIXELS,Un),U.pixelStorei(U.UNPACK_SKIP_ROWS,ee),U.pixelStorei(U.UNPACK_SKIP_IMAGES,yt),O===0&&L.generateMipmaps&&U.generateMipmap(U.TEXTURE_2D),bt.unbindTexture()},this.copyTextureToTexture3D=function(E,L,B=null,H=null,O=0){E.isTexture!==!0&&(Wu("WebGLRenderer: copyTextureToTexture3D function signature has changed."),B=arguments[0]||null,H=arguments[1]||null,E=arguments[2],L=arguments[3],O=arguments[4]||0);let nt,ot,mt,gt,Mt,Tt,St,se,ye;const be=E.isCompressedTexture?E.mipmaps[O]:E.image;B!==null?(nt=B.max.x-B.min.x,ot=B.max.y-B.min.y,mt=B.max.z-B.min.z,gt=B.min.x,Mt=B.min.y,Tt=B.min.z):(nt=be.width,ot=be.height,mt=be.depth,gt=0,Mt=0,Tt=0),H!==null?(St=H.x,se=H.y,ye=H.z):(St=0,se=0,ye=0);const Un=Ut.convert(L.format),ee=Ut.convert(L.type);let yt;if(L.isData3DTexture)A.setTexture3D(L,0),yt=U.TEXTURE_3D;else if(L.isDataArrayTexture||L.isCompressedArrayTexture)A.setTexture2DArray(L,0),yt=U.TEXTURE_2D_ARRAY;else{console.warn("THREE.WebGLRenderer.copyTextureToTexture3D: only supports THREE.DataTexture3D and THREE.DataTexture2DArray.");return}U.pixelStorei(U.UNPACK_FLIP_Y_WEBGL,L.flipY),U.pixelStorei(U.UNPACK_PREMULTIPLY_ALPHA_WEBGL,L.premultiplyAlpha),U.pixelStorei(U.UNPACK_ALIGNMENT,L.unpackAlignment);const je=U.getParameter(U.UNPACK_ROW_LENGTH),ne=U.getParameter(U.UNPACK_IMAGE_HEIGHT),oi=U.getParameter(U.UNPACK_SKIP_PIXELS),Gs=U.getParameter(U.UNPACK_SKIP_ROWS),Nn=U.getParameter(U.UNPACK_SKIP_IMAGES);U.pixelStorei(U.UNPACK_ROW_LENGTH,be.width),U.pixelStorei(U.UNPACK_IMAGE_HEIGHT,be.height),U.pixelStorei(U.UNPACK_SKIP_PIXELS,gt),U.pixelStorei(U.UNPACK_SKIP_ROWS,Mt),U.pixelStorei(U.UNPACK_SKIP_IMAGES,Tt),E.isDataTexture||E.isData3DTexture?U.texSubImage3D(yt,O,St,se,ye,nt,ot,mt,Un,ee,be.data):L.isCompressedArrayTexture?U.compressedTexSubImage3D(yt,O,St,se,ye,nt,ot,mt,Un,be.data):U.texSubImage3D(yt,O,St,se,ye,nt,ot,mt,Un,ee,be),U.pixelStorei(U.UNPACK_ROW_LENGTH,je),U.pixelStorei(U.UNPACK_IMAGE_HEIGHT,ne),U.pixelStorei(U.UNPACK_SKIP_PIXELS,oi),U.pixelStorei(U.UNPACK_SKIP_ROWS,Gs),U.pixelStorei(U.UNPACK_SKIP_IMAGES,Nn),O===0&&L.generateMipmaps&&U.generateMipmap(yt),bt.unbindTexture()},this.initRenderTarget=function(E){wt.get(E).__webglFramebuffer===void 0&&A.setupRenderTarget(E)},this.initTexture=function(E){E.isCubeTexture?A.setTextureCube(E,0):E.isData3DTexture?A.setTexture3D(E,0):E.isDataArrayTexture||E.isCompressedArrayTexture?A.setTexture2DArray(E,0):A.setTexture2D(E,0),bt.unbindTexture()},this.resetState=function(){C=0,R=0,b=null,bt.reset(),pe.reset()},typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}get coordinateSystem(){return Zi}get outputColorSpace(){return this._outputColorSpace}set outputColorSpace(t){this._outputColorSpace=t;const n=this.getContext();n.drawingBufferColorSpace=t===Om?"display-p3":"srgb",n.unpackColorSpace=ae.workingColorSpace===tf?"display-p3":"srgb"}}class Tw extends en{constructor(){super(),this.isScene=!0,this.type="Scene",this.background=null,this.environment=null,this.fog=null,this.backgroundBlurriness=0,this.backgroundIntensity=1,this.backgroundRotation=new sa,this.environmentIntensity=1,this.environmentRotation=new sa,this.overrideMaterial=null,typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}copy(t,n){return super.copy(t,n),t.background!==null&&(this.background=t.background.clone()),t.environment!==null&&(this.environment=t.environment.clone()),t.fog!==null&&(this.fog=t.fog.clone()),this.backgroundBlurriness=t.backgroundBlurriness,this.backgroundIntensity=t.backgroundIntensity,this.backgroundRotation.copy(t.backgroundRotation),this.environmentIntensity=t.environmentIntensity,this.environmentRotation.copy(t.environmentRotation),t.overrideMaterial!==null&&(this.overrideMaterial=t.overrideMaterial.clone()),this.matrixAutoUpdate=t.matrixAutoUpdate,this}toJSON(t){const n=super.toJSON(t);return this.fog!==null&&(n.object.fog=this.fog.toJSON()),this.backgroundBlurriness>0&&(n.object.backgroundBlurriness=this.backgroundBlurriness),this.backgroundIntensity!==1&&(n.object.backgroundIntensity=this.backgroundIntensity),n.object.backgroundRotation=this.backgroundRotation.toArray(),this.environmentIntensity!==1&&(n.object.environmentIntensity=this.environmentIntensity),n.object.environmentRotation=this.environmentRotation.toArray(),n}}class af extends Rl{constructor(t){super(),this.isLineBasicMaterial=!0,this.type="LineBasicMaterial",this.color=new Ht(16777215),this.map=null,this.linewidth=1,this.linecap="round",this.linejoin="round",this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.color.copy(t.color),this.map=t.map,this.linewidth=t.linewidth,this.linecap=t.linecap,this.linejoin=t.linejoin,this.fog=t.fog,this}}const wc=new P,Dc=new P,N0=new Te,bo=new Pm,gu=new ef,yh=new P,L0=new P;class zx extends en{constructor(t=new wn,n=new af){super(),this.isLine=!0,this.type="Line",this.geometry=t,this.material=n,this.updateMorphTargets()}copy(t,n){return super.copy(t,n),this.material=Array.isArray(t.material)?t.material.slice():t.material,this.geometry=t.geometry,this}computeLineDistances(){const t=this.geometry;if(t.index===null){const n=t.attributes.position,i=[0];for(let a=1,s=n.count;a<s;a++)wc.fromBufferAttribute(n,a-1),Dc.fromBufferAttribute(n,a),i[a]=i[a-1],i[a]+=wc.distanceTo(Dc);t.setAttribute("lineDistance",new We(i,1))}else console.warn("THREE.Line.computeLineDistances(): Computation only possible with non-indexed BufferGeometry.");return this}raycast(t,n){const i=this.geometry,a=this.matrixWorld,s=t.params.Line.threshold,r=i.drawRange;if(i.boundingSphere===null&&i.computeBoundingSphere(),gu.copy(i.boundingSphere),gu.applyMatrix4(a),gu.radius+=s,t.ray.intersectsSphere(gu)===!1)return;N0.copy(a).invert(),bo.copy(t.ray).applyMatrix4(N0);const o=s/((this.scale.x+this.scale.y+this.scale.z)/3),l=o*o,u=this.isLineSegments?2:1,h=i.index,f=i.attributes.position;if(h!==null){const d=Math.max(0,r.start),v=Math.min(h.count,r.start+r.count);for(let y=d,m=v-1;y<m;y+=u){const c=h.getX(y),_=h.getX(y+1),g=vu(this,t,bo,l,c,_);g&&n.push(g)}if(this.isLineLoop){const y=h.getX(v-1),m=h.getX(d),c=vu(this,t,bo,l,y,m);c&&n.push(c)}}else{const d=Math.max(0,r.start),v=Math.min(f.count,r.start+r.count);for(let y=d,m=v-1;y<m;y+=u){const c=vu(this,t,bo,l,y,y+1);c&&n.push(c)}if(this.isLineLoop){const y=vu(this,t,bo,l,v-1,d);y&&n.push(y)}}}updateMorphTargets(){const n=this.geometry.morphAttributes,i=Object.keys(n);if(i.length>0){const a=n[i[0]];if(a!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let s=0,r=a.length;s<r;s++){const o=a[s].name||String(s);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=s}}}}}function vu(e,t,n,i,a,s){const r=e.geometry.attributes.position;if(wc.fromBufferAttribute(r,a),Dc.fromBufferAttribute(r,s),n.distanceSqToSegment(wc,Dc,yh,L0)>i)return;yh.applyMatrix4(e.matrixWorld);const l=t.ray.origin.distanceTo(yh);if(!(l<t.near||l>t.far))return{distance:l,point:L0.clone().applyMatrix4(e.matrixWorld),index:a,face:null,faceIndex:null,barycoord:null,object:e}}const O0=new P,P0=new P;class Ix extends zx{constructor(t,n){super(t,n),this.isLineSegments=!0,this.type="LineSegments"}computeLineDistances(){const t=this.geometry;if(t.index===null){const n=t.attributes.position,i=[];for(let a=0,s=n.count;a<s;a+=2)O0.fromBufferAttribute(n,a),P0.fromBufferAttribute(n,a+1),i[a]=a===0?0:i[a-1],i[a+1]=i[a]+O0.distanceTo(P0);t.setAttribute("lineDistance",new We(i,1))}else console.warn("THREE.LineSegments.computeLineDistances(): Computation only possible with non-indexed BufferGeometry.");return this}}class Bm extends wn{constructor(t=1,n=1,i=1,a=32,s=1,r=!1,o=0,l=Math.PI*2){super(),this.type="CylinderGeometry",this.parameters={radiusTop:t,radiusBottom:n,height:i,radialSegments:a,heightSegments:s,openEnded:r,thetaStart:o,thetaLength:l};const u=this;a=Math.floor(a),s=Math.floor(s);const h=[],p=[],f=[],d=[];let v=0;const y=[],m=i/2;let c=0;_(),r===!1&&(t>0&&g(!0),n>0&&g(!1)),this.setIndex(h),this.setAttribute("position",new We(p,3)),this.setAttribute("normal",new We(f,3)),this.setAttribute("uv",new We(d,2));function _(){const x=new P,C=new P;let R=0;const b=(n-t)/i;for(let w=0;w<=s;w++){const W=[],S=w/s,T=S*(n-t)+t;for(let F=0;F<=a;F++){const G=F/a,Y=G*l+o,K=Math.sin(Y),D=Math.cos(Y);C.x=T*K,C.y=-S*i+m,C.z=T*D,p.push(C.x,C.y,C.z),x.set(K,b,D).normalize(),f.push(x.x,x.y,x.z),d.push(G,1-S),W.push(v++)}y.push(W)}for(let w=0;w<a;w++)for(let W=0;W<s;W++){const S=y[W][w],T=y[W+1][w],F=y[W+1][w+1],G=y[W][w+1];t>0&&(h.push(S,T,G),R+=3),n>0&&(h.push(T,F,G),R+=3)}u.addGroup(c,R,0),c+=R}function g(x){const C=v,R=new Lt,b=new P;let w=0;const W=x===!0?t:n,S=x===!0?1:-1;for(let F=1;F<=a;F++)p.push(0,m*S,0),f.push(0,S,0),d.push(.5,.5),v++;const T=v;for(let F=0;F<=a;F++){const Y=F/a*l+o,K=Math.cos(Y),D=Math.sin(Y);b.x=W*D,b.y=m*S,b.z=W*K,p.push(b.x,b.y,b.z),f.push(0,S,0),R.x=K*.5+.5,R.y=D*.5*S+.5,d.push(R.x,R.y),v++}for(let F=0;F<a;F++){const G=C+F,Y=T+F;x===!0?h.push(Y,Y+1,G):h.push(Y+1,Y,G),w+=3}u.addGroup(c,w,x===!0?1:2),c+=w}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new Bm(t.radiusTop,t.radiusBottom,t.height,t.radialSegments,t.heightSegments,t.openEnded,t.thetaStart,t.thetaLength)}}class Fm extends Bm{constructor(t=1,n=1,i=32,a=1,s=!1,r=0,o=Math.PI*2){super(0,t,n,i,a,s,r,o),this.type="ConeGeometry",this.parameters={radius:t,height:n,radialSegments:i,heightSegments:a,openEnded:s,thetaStart:r,thetaLength:o}}static fromJSON(t){return new Fm(t.radius,t.height,t.radialSegments,t.heightSegments,t.openEnded,t.thetaStart,t.thetaLength)}}class Hm extends wn{constructor(t=1,n=32,i=16,a=0,s=Math.PI*2,r=0,o=Math.PI){super(),this.type="SphereGeometry",this.parameters={radius:t,widthSegments:n,heightSegments:i,phiStart:a,phiLength:s,thetaStart:r,thetaLength:o},n=Math.max(3,Math.floor(n)),i=Math.max(2,Math.floor(i));const l=Math.min(r+o,Math.PI);let u=0;const h=[],p=new P,f=new P,d=[],v=[],y=[],m=[];for(let c=0;c<=i;c++){const _=[],g=c/i;let x=0;c===0&&r===0?x=.5/n:c===i&&l===Math.PI&&(x=-.5/n);for(let C=0;C<=n;C++){const R=C/n;p.x=-t*Math.cos(a+R*s)*Math.sin(r+g*o),p.y=t*Math.cos(r+g*o),p.z=t*Math.sin(a+R*s)*Math.sin(r+g*o),v.push(p.x,p.y,p.z),f.copy(p).normalize(),y.push(f.x,f.y,f.z),m.push(R+x,1-g),_.push(u++)}h.push(_)}for(let c=0;c<i;c++)for(let _=0;_<n;_++){const g=h[c][_+1],x=h[c][_],C=h[c+1][_],R=h[c+1][_+1];(c!==0||r>0)&&d.push(g,x,R),(c!==i-1||l<Math.PI)&&d.push(x,C,R)}this.setIndex(d),this.setAttribute("position",new We(v,3)),this.setAttribute("normal",new We(y,3)),this.setAttribute("uv",new We(m,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new Hm(t.radius,t.widthSegments,t.heightSegments,t.phiStart,t.phiLength,t.thetaStart,t.thetaLength)}}class Bx extends en{constructor(t,n=1){super(),this.isLight=!0,this.type="Light",this.color=new Ht(t),this.intensity=n}dispose(){}copy(t,n){return super.copy(t,n),this.color.copy(t.color),this.intensity=t.intensity,this}toJSON(t){const n=super.toJSON(t);return n.object.color=this.color.getHex(),n.object.intensity=this.intensity,this.groundColor!==void 0&&(n.object.groundColor=this.groundColor.getHex()),this.distance!==void 0&&(n.object.distance=this.distance),this.angle!==void 0&&(n.object.angle=this.angle),this.decay!==void 0&&(n.object.decay=this.decay),this.penumbra!==void 0&&(n.object.penumbra=this.penumbra),this.shadow!==void 0&&(n.object.shadow=this.shadow.toJSON()),this.target!==void 0&&(n.object.target=this.target.uuid),n}}const xh=new Te,z0=new P,I0=new P;class bw{constructor(t){this.camera=t,this.intensity=1,this.bias=0,this.normalBias=0,this.radius=1,this.blurSamples=8,this.mapSize=new Lt(512,512),this.map=null,this.mapPass=null,this.matrix=new Te,this.autoUpdate=!0,this.needsUpdate=!1,this._frustum=new zm,this._frameExtents=new Lt(1,1),this._viewportCount=1,this._viewports=[new Ce(0,0,1,1)]}getViewportCount(){return this._viewportCount}getFrustum(){return this._frustum}updateMatrices(t){const n=this.camera,i=this.matrix;z0.setFromMatrixPosition(t.matrixWorld),n.position.copy(z0),I0.setFromMatrixPosition(t.target.matrixWorld),n.lookAt(I0),n.updateMatrixWorld(),xh.multiplyMatrices(n.projectionMatrix,n.matrixWorldInverse),this._frustum.setFromProjectionMatrix(xh),i.set(.5,0,0,.5,0,.5,0,.5,0,0,.5,.5,0,0,0,1),i.multiply(xh)}getViewport(t){return this._viewports[t]}getFrameExtents(){return this._frameExtents}dispose(){this.map&&this.map.dispose(),this.mapPass&&this.mapPass.dispose()}copy(t){return this.camera=t.camera.clone(),this.intensity=t.intensity,this.bias=t.bias,this.radius=t.radius,this.mapSize.copy(t.mapSize),this}clone(){return new this.constructor().copy(this)}toJSON(){const t={};return this.intensity!==1&&(t.intensity=this.intensity),this.bias!==0&&(t.bias=this.bias),this.normalBias!==0&&(t.normalBias=this.normalBias),this.radius!==1&&(t.radius=this.radius),(this.mapSize.x!==512||this.mapSize.y!==512)&&(t.mapSize=this.mapSize.toArray()),t.camera=this.camera.toJSON(!1).object,delete t.camera.matrix,t}}class Aw extends bw{constructor(){super(new Dx(-5,5,5,-5,.5,500)),this.isDirectionalLightShadow=!0}}class Rw extends Bx{constructor(t,n){super(t,n),this.isDirectionalLight=!0,this.type="DirectionalLight",this.position.copy(en.DEFAULT_UP),this.updateMatrix(),this.target=new en,this.shadow=new Aw}dispose(){this.shadow.dispose()}copy(t){return super.copy(t),this.target=t.target.clone(),this.shadow=t.shadow.clone(),this}}class Cw extends Bx{constructor(t,n){super(t,n),this.isAmbientLight=!0,this.type="AmbientLight"}}class B0{constructor(t=1,n=0,i=0){return this.radius=t,this.phi=n,this.theta=i,this}set(t,n,i){return this.radius=t,this.phi=n,this.theta=i,this}copy(t){return this.radius=t.radius,this.phi=t.phi,this.theta=t.theta,this}makeSafe(){return this.phi=Math.max(1e-6,Math.min(Math.PI-1e-6,this.phi)),this}setFromVector3(t){return this.setFromCartesianCoords(t.x,t.y,t.z)}setFromCartesianCoords(t,n,i){return this.radius=Math.sqrt(t*t+n*n+i*i),this.radius===0?(this.theta=0,this.phi=0):(this.theta=Math.atan2(t,i),this.phi=Math.acos(hn(n/this.radius,-1,1))),this}clone(){return new this.constructor().copy(this)}}class ww extends Ix{constructor(t=10,n=10,i=4473924,a=8947848){i=new Ht(i),a=new Ht(a);const s=n/2,r=t/n,o=t/2,l=[],u=[];for(let f=0,d=0,v=-o;f<=n;f++,v+=r){l.push(-o,0,v,o,0,v),l.push(v,0,-o,v,0,o);const y=f===s?i:a;y.toArray(u,d),d+=3,y.toArray(u,d),d+=3,y.toArray(u,d),d+=3,y.toArray(u,d),d+=3}const h=new wn;h.setAttribute("position",new We(l,3)),h.setAttribute("color",new We(u,3));const p=new af({vertexColors:!0,toneMapped:!1});super(h,p),this.type="GridHelper"}dispose(){this.geometry.dispose(),this.material.dispose()}}class Dw extends Hs{constructor(t,n=null){super(),this.object=t,this.domElement=n,this.enabled=!0,this.state=-1,this.keys={},this.mouseButtons={LEFT:null,MIDDLE:null,RIGHT:null},this.touches={ONE:null,TWO:null}}connect(){}disconnect(){}dispose(){}update(){}}typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("register",{detail:{revision:Rm}}));typeof window<"u"&&(window.__THREE__?console.warn("WARNING: Multiple instances of Three.js being imported."):window.__THREE__=Rm);const F0={type:"change"},Gm={type:"start"},Fx={type:"end"},Su=new Pm,H0=new Ma,Uw=Math.cos(70*u1.DEG2RAD),ze=new P,vn=2*Math.PI,fe={NONE:-1,ROTATE:0,DOLLY:1,PAN:2,TOUCH_ROTATE:3,TOUCH_PAN:4,TOUCH_DOLLY_PAN:5,TOUCH_DOLLY_ROTATE:6},Mh=1e-6;class Nw extends Dw{constructor(t,n=null){super(t,n),this.state=fe.NONE,this.enabled=!0,this.target=new P,this.cursor=new P,this.minDistance=0,this.maxDistance=1/0,this.minZoom=0,this.maxZoom=1/0,this.minTargetRadius=0,this.maxTargetRadius=1/0,this.minPolarAngle=0,this.maxPolarAngle=Math.PI,this.minAzimuthAngle=-1/0,this.maxAzimuthAngle=1/0,this.enableDamping=!1,this.dampingFactor=.05,this.enableZoom=!0,this.zoomSpeed=1,this.enableRotate=!0,this.rotateSpeed=1,this.enablePan=!0,this.panSpeed=1,this.screenSpacePanning=!0,this.keyPanSpeed=7,this.zoomToCursor=!1,this.autoRotate=!1,this.autoRotateSpeed=2,this.keys={LEFT:"ArrowLeft",UP:"ArrowUp",RIGHT:"ArrowRight",BOTTOM:"ArrowDown"},this.mouseButtons={LEFT:Lr.ROTATE,MIDDLE:Lr.DOLLY,RIGHT:Lr.PAN},this.touches={ONE:xr.ROTATE,TWO:xr.DOLLY_PAN},this.target0=this.target.clone(),this.position0=this.object.position.clone(),this.zoom0=this.object.zoom,this._domElementKeyEvents=null,this._lastPosition=new P,this._lastQuaternion=new Ls,this._lastTargetPosition=new P,this._quat=new Ls().setFromUnitVectors(t.up,new P(0,1,0)),this._quatInverse=this._quat.clone().invert(),this._spherical=new B0,this._sphericalDelta=new B0,this._scale=1,this._panOffset=new P,this._rotateStart=new Lt,this._rotateEnd=new Lt,this._rotateDelta=new Lt,this._panStart=new Lt,this._panEnd=new Lt,this._panDelta=new Lt,this._dollyStart=new Lt,this._dollyEnd=new Lt,this._dollyDelta=new Lt,this._dollyDirection=new P,this._mouse=new Lt,this._performCursorZoom=!1,this._pointers=[],this._pointerPositions={},this._controlActive=!1,this._onPointerMove=Ow.bind(this),this._onPointerDown=Lw.bind(this),this._onPointerUp=Pw.bind(this),this._onContextMenu=Vw.bind(this),this._onMouseWheel=Bw.bind(this),this._onKeyDown=Fw.bind(this),this._onTouchStart=Hw.bind(this),this._onTouchMove=Gw.bind(this),this._onMouseDown=zw.bind(this),this._onMouseMove=Iw.bind(this),this._interceptControlDown=Xw.bind(this),this._interceptControlUp=kw.bind(this),this.domElement!==null&&this.connect(),this.update()}connect(){this.domElement.addEventListener("pointerdown",this._onPointerDown),this.domElement.addEventListener("pointercancel",this._onPointerUp),this.domElement.addEventListener("contextmenu",this._onContextMenu),this.domElement.addEventListener("wheel",this._onMouseWheel,{passive:!1}),this.domElement.getRootNode().addEventListener("keydown",this._interceptControlDown,{passive:!0,capture:!0}),this.domElement.style.touchAction="none"}disconnect(){this.domElement.removeEventListener("pointerdown",this._onPointerDown),this.domElement.removeEventListener("pointermove",this._onPointerMove),this.domElement.removeEventListener("pointerup",this._onPointerUp),this.domElement.removeEventListener("pointercancel",this._onPointerUp),this.domElement.removeEventListener("wheel",this._onMouseWheel),this.domElement.removeEventListener("contextmenu",this._onContextMenu),this.stopListenToKeyEvents(),this.domElement.getRootNode().removeEventListener("keydown",this._interceptControlDown,{capture:!0}),this.domElement.style.touchAction="auto"}dispose(){this.disconnect()}getPolarAngle(){return this._spherical.phi}getAzimuthalAngle(){return this._spherical.theta}getDistance(){return this.object.position.distanceTo(this.target)}listenToKeyEvents(t){t.addEventListener("keydown",this._onKeyDown),this._domElementKeyEvents=t}stopListenToKeyEvents(){this._domElementKeyEvents!==null&&(this._domElementKeyEvents.removeEventListener("keydown",this._onKeyDown),this._domElementKeyEvents=null)}saveState(){this.target0.copy(this.target),this.position0.copy(this.object.position),this.zoom0=this.object.zoom}reset(){this.target.copy(this.target0),this.object.position.copy(this.position0),this.object.zoom=this.zoom0,this.object.updateProjectionMatrix(),this.dispatchEvent(F0),this.update(),this.state=fe.NONE}update(t=null){const n=this.object.position;ze.copy(n).sub(this.target),ze.applyQuaternion(this._quat),this._spherical.setFromVector3(ze),this.autoRotate&&this.state===fe.NONE&&this._rotateLeft(this._getAutoRotationAngle(t)),this.enableDamping?(this._spherical.theta+=this._sphericalDelta.theta*this.dampingFactor,this._spherical.phi+=this._sphericalDelta.phi*this.dampingFactor):(this._spherical.theta+=this._sphericalDelta.theta,this._spherical.phi+=this._sphericalDelta.phi);let i=this.minAzimuthAngle,a=this.maxAzimuthAngle;isFinite(i)&&isFinite(a)&&(i<-Math.PI?i+=vn:i>Math.PI&&(i-=vn),a<-Math.PI?a+=vn:a>Math.PI&&(a-=vn),i<=a?this._spherical.theta=Math.max(i,Math.min(a,this._spherical.theta)):this._spherical.theta=this._spherical.theta>(i+a)/2?Math.max(i,this._spherical.theta):Math.min(a,this._spherical.theta)),this._spherical.phi=Math.max(this.minPolarAngle,Math.min(this.maxPolarAngle,this._spherical.phi)),this._spherical.makeSafe(),this.enableDamping===!0?this.target.addScaledVector(this._panOffset,this.dampingFactor):this.target.add(this._panOffset),this.target.sub(this.cursor),this.target.clampLength(this.minTargetRadius,this.maxTargetRadius),this.target.add(this.cursor);let s=!1;if(this.zoomToCursor&&this._performCursorZoom||this.object.isOrthographicCamera)this._spherical.radius=this._clampDistance(this._spherical.radius);else{const r=this._spherical.radius;this._spherical.radius=this._clampDistance(this._spherical.radius*this._scale),s=r!=this._spherical.radius}if(ze.setFromSpherical(this._spherical),ze.applyQuaternion(this._quatInverse),n.copy(this.target).add(ze),this.object.lookAt(this.target),this.enableDamping===!0?(this._sphericalDelta.theta*=1-this.dampingFactor,this._sphericalDelta.phi*=1-this.dampingFactor,this._panOffset.multiplyScalar(1-this.dampingFactor)):(this._sphericalDelta.set(0,0,0),this._panOffset.set(0,0,0)),this.zoomToCursor&&this._performCursorZoom){let r=null;if(this.object.isPerspectiveCamera){const o=ze.length();r=this._clampDistance(o*this._scale);const l=o-r;this.object.position.addScaledVector(this._dollyDirection,l),this.object.updateMatrixWorld(),s=!!l}else if(this.object.isOrthographicCamera){const o=new P(this._mouse.x,this._mouse.y,0);o.unproject(this.object);const l=this.object.zoom;this.object.zoom=Math.max(this.minZoom,Math.min(this.maxZoom,this.object.zoom/this._scale)),this.object.updateProjectionMatrix(),s=l!==this.object.zoom;const u=new P(this._mouse.x,this._mouse.y,0);u.unproject(this.object),this.object.position.sub(u).add(o),this.object.updateMatrixWorld(),r=ze.length()}else console.warn("WARNING: OrbitControls.js encountered an unknown camera type - zoom to cursor disabled."),this.zoomToCursor=!1;r!==null&&(this.screenSpacePanning?this.target.set(0,0,-1).transformDirection(this.object.matrix).multiplyScalar(r).add(this.object.position):(Su.origin.copy(this.object.position),Su.direction.set(0,0,-1).transformDirection(this.object.matrix),Math.abs(this.object.up.dot(Su.direction))<Uw?this.object.lookAt(this.target):(H0.setFromNormalAndCoplanarPoint(this.object.up,this.target),Su.intersectPlane(H0,this.target))))}else if(this.object.isOrthographicCamera){const r=this.object.zoom;this.object.zoom=Math.max(this.minZoom,Math.min(this.maxZoom,this.object.zoom/this._scale)),r!==this.object.zoom&&(this.object.updateProjectionMatrix(),s=!0)}return this._scale=1,this._performCursorZoom=!1,s||this._lastPosition.distanceToSquared(this.object.position)>Mh||8*(1-this._lastQuaternion.dot(this.object.quaternion))>Mh||this._lastTargetPosition.distanceToSquared(this.target)>Mh?(this.dispatchEvent(F0),this._lastPosition.copy(this.object.position),this._lastQuaternion.copy(this.object.quaternion),this._lastTargetPosition.copy(this.target),!0):!1}_getAutoRotationAngle(t){return t!==null?vn/60*this.autoRotateSpeed*t:vn/60/60*this.autoRotateSpeed}_getZoomScale(t){const n=Math.abs(t*.01);return Math.pow(.95,this.zoomSpeed*n)}_rotateLeft(t){this._sphericalDelta.theta-=t}_rotateUp(t){this._sphericalDelta.phi-=t}_panLeft(t,n){ze.setFromMatrixColumn(n,0),ze.multiplyScalar(-t),this._panOffset.add(ze)}_panUp(t,n){this.screenSpacePanning===!0?ze.setFromMatrixColumn(n,1):(ze.setFromMatrixColumn(n,0),ze.crossVectors(this.object.up,ze)),ze.multiplyScalar(t),this._panOffset.add(ze)}_pan(t,n){const i=this.domElement;if(this.object.isPerspectiveCamera){const a=this.object.position;ze.copy(a).sub(this.target);let s=ze.length();s*=Math.tan(this.object.fov/2*Math.PI/180),this._panLeft(2*t*s/i.clientHeight,this.object.matrix),this._panUp(2*n*s/i.clientHeight,this.object.matrix)}else this.object.isOrthographicCamera?(this._panLeft(t*(this.object.right-this.object.left)/this.object.zoom/i.clientWidth,this.object.matrix),this._panUp(n*(this.object.top-this.object.bottom)/this.object.zoom/i.clientHeight,this.object.matrix)):(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - pan disabled."),this.enablePan=!1)}_dollyOut(t){this.object.isPerspectiveCamera||this.object.isOrthographicCamera?this._scale/=t:(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled."),this.enableZoom=!1)}_dollyIn(t){this.object.isPerspectiveCamera||this.object.isOrthographicCamera?this._scale*=t:(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled."),this.enableZoom=!1)}_updateZoomParameters(t,n){if(!this.zoomToCursor)return;this._performCursorZoom=!0;const i=this.domElement.getBoundingClientRect(),a=t-i.left,s=n-i.top,r=i.width,o=i.height;this._mouse.x=a/r*2-1,this._mouse.y=-(s/o)*2+1,this._dollyDirection.set(this._mouse.x,this._mouse.y,1).unproject(this.object).sub(this.object.position).normalize()}_clampDistance(t){return Math.max(this.minDistance,Math.min(this.maxDistance,t))}_handleMouseDownRotate(t){this._rotateStart.set(t.clientX,t.clientY)}_handleMouseDownDolly(t){this._updateZoomParameters(t.clientX,t.clientX),this._dollyStart.set(t.clientX,t.clientY)}_handleMouseDownPan(t){this._panStart.set(t.clientX,t.clientY)}_handleMouseMoveRotate(t){this._rotateEnd.set(t.clientX,t.clientY),this._rotateDelta.subVectors(this._rotateEnd,this._rotateStart).multiplyScalar(this.rotateSpeed);const n=this.domElement;this._rotateLeft(vn*this._rotateDelta.x/n.clientHeight),this._rotateUp(vn*this._rotateDelta.y/n.clientHeight),this._rotateStart.copy(this._rotateEnd),this.update()}_handleMouseMoveDolly(t){this._dollyEnd.set(t.clientX,t.clientY),this._dollyDelta.subVectors(this._dollyEnd,this._dollyStart),this._dollyDelta.y>0?this._dollyOut(this._getZoomScale(this._dollyDelta.y)):this._dollyDelta.y<0&&this._dollyIn(this._getZoomScale(this._dollyDelta.y)),this._dollyStart.copy(this._dollyEnd),this.update()}_handleMouseMovePan(t){this._panEnd.set(t.clientX,t.clientY),this._panDelta.subVectors(this._panEnd,this._panStart).multiplyScalar(this.panSpeed),this._pan(this._panDelta.x,this._panDelta.y),this._panStart.copy(this._panEnd),this.update()}_handleMouseWheel(t){this._updateZoomParameters(t.clientX,t.clientY),t.deltaY<0?this._dollyIn(this._getZoomScale(t.deltaY)):t.deltaY>0&&this._dollyOut(this._getZoomScale(t.deltaY)),this.update()}_handleKeyDown(t){let n=!1;switch(t.code){case this.keys.UP:t.ctrlKey||t.metaKey||t.shiftKey?this._rotateUp(vn*this.rotateSpeed/this.domElement.clientHeight):this._pan(0,this.keyPanSpeed),n=!0;break;case this.keys.BOTTOM:t.ctrlKey||t.metaKey||t.shiftKey?this._rotateUp(-vn*this.rotateSpeed/this.domElement.clientHeight):this._pan(0,-this.keyPanSpeed),n=!0;break;case this.keys.LEFT:t.ctrlKey||t.metaKey||t.shiftKey?this._rotateLeft(vn*this.rotateSpeed/this.domElement.clientHeight):this._pan(this.keyPanSpeed,0),n=!0;break;case this.keys.RIGHT:t.ctrlKey||t.metaKey||t.shiftKey?this._rotateLeft(-vn*this.rotateSpeed/this.domElement.clientHeight):this._pan(-this.keyPanSpeed,0),n=!0;break}n&&(t.preventDefault(),this.update())}_handleTouchStartRotate(t){if(this._pointers.length===1)this._rotateStart.set(t.pageX,t.pageY);else{const n=this._getSecondPointerPosition(t),i=.5*(t.pageX+n.x),a=.5*(t.pageY+n.y);this._rotateStart.set(i,a)}}_handleTouchStartPan(t){if(this._pointers.length===1)this._panStart.set(t.pageX,t.pageY);else{const n=this._getSecondPointerPosition(t),i=.5*(t.pageX+n.x),a=.5*(t.pageY+n.y);this._panStart.set(i,a)}}_handleTouchStartDolly(t){const n=this._getSecondPointerPosition(t),i=t.pageX-n.x,a=t.pageY-n.y,s=Math.sqrt(i*i+a*a);this._dollyStart.set(0,s)}_handleTouchStartDollyPan(t){this.enableZoom&&this._handleTouchStartDolly(t),this.enablePan&&this._handleTouchStartPan(t)}_handleTouchStartDollyRotate(t){this.enableZoom&&this._handleTouchStartDolly(t),this.enableRotate&&this._handleTouchStartRotate(t)}_handleTouchMoveRotate(t){if(this._pointers.length==1)this._rotateEnd.set(t.pageX,t.pageY);else{const i=this._getSecondPointerPosition(t),a=.5*(t.pageX+i.x),s=.5*(t.pageY+i.y);this._rotateEnd.set(a,s)}this._rotateDelta.subVectors(this._rotateEnd,this._rotateStart).multiplyScalar(this.rotateSpeed);const n=this.domElement;this._rotateLeft(vn*this._rotateDelta.x/n.clientHeight),this._rotateUp(vn*this._rotateDelta.y/n.clientHeight),this._rotateStart.copy(this._rotateEnd)}_handleTouchMovePan(t){if(this._pointers.length===1)this._panEnd.set(t.pageX,t.pageY);else{const n=this._getSecondPointerPosition(t),i=.5*(t.pageX+n.x),a=.5*(t.pageY+n.y);this._panEnd.set(i,a)}this._panDelta.subVectors(this._panEnd,this._panStart).multiplyScalar(this.panSpeed),this._pan(this._panDelta.x,this._panDelta.y),this._panStart.copy(this._panEnd)}_handleTouchMoveDolly(t){const n=this._getSecondPointerPosition(t),i=t.pageX-n.x,a=t.pageY-n.y,s=Math.sqrt(i*i+a*a);this._dollyEnd.set(0,s),this._dollyDelta.set(0,Math.pow(this._dollyEnd.y/this._dollyStart.y,this.zoomSpeed)),this._dollyOut(this._dollyDelta.y),this._dollyStart.copy(this._dollyEnd);const r=(t.pageX+n.x)*.5,o=(t.pageY+n.y)*.5;this._updateZoomParameters(r,o)}_handleTouchMoveDollyPan(t){this.enableZoom&&this._handleTouchMoveDolly(t),this.enablePan&&this._handleTouchMovePan(t)}_handleTouchMoveDollyRotate(t){this.enableZoom&&this._handleTouchMoveDolly(t),this.enableRotate&&this._handleTouchMoveRotate(t)}_addPointer(t){this._pointers.push(t.pointerId)}_removePointer(t){delete this._pointerPositions[t.pointerId];for(let n=0;n<this._pointers.length;n++)if(this._pointers[n]==t.pointerId){this._pointers.splice(n,1);return}}_isTrackingPointer(t){for(let n=0;n<this._pointers.length;n++)if(this._pointers[n]==t.pointerId)return!0;return!1}_trackPointer(t){let n=this._pointerPositions[t.pointerId];n===void 0&&(n=new Lt,this._pointerPositions[t.pointerId]=n),n.set(t.pageX,t.pageY)}_getSecondPointerPosition(t){const n=t.pointerId===this._pointers[0]?this._pointers[1]:this._pointers[0];return this._pointerPositions[n]}_customWheelEvent(t){const n=t.deltaMode,i={clientX:t.clientX,clientY:t.clientY,deltaY:t.deltaY};switch(n){case 1:i.deltaY*=16;break;case 2:i.deltaY*=100;break}return t.ctrlKey&&!this._controlActive&&(i.deltaY*=10),i}}function Lw(e){this.enabled!==!1&&(this._pointers.length===0&&(this.domElement.setPointerCapture(e.pointerId),this.domElement.addEventListener("pointermove",this._onPointerMove),this.domElement.addEventListener("pointerup",this._onPointerUp)),!this._isTrackingPointer(e)&&(this._addPointer(e),e.pointerType==="touch"?this._onTouchStart(e):this._onMouseDown(e)))}function Ow(e){this.enabled!==!1&&(e.pointerType==="touch"?this._onTouchMove(e):this._onMouseMove(e))}function Pw(e){switch(this._removePointer(e),this._pointers.length){case 0:this.domElement.releasePointerCapture(e.pointerId),this.domElement.removeEventListener("pointermove",this._onPointerMove),this.domElement.removeEventListener("pointerup",this._onPointerUp),this.dispatchEvent(Fx),this.state=fe.NONE;break;case 1:const t=this._pointers[0],n=this._pointerPositions[t];this._onTouchStart({pointerId:t,pageX:n.x,pageY:n.y});break}}function zw(e){let t;switch(e.button){case 0:t=this.mouseButtons.LEFT;break;case 1:t=this.mouseButtons.MIDDLE;break;case 2:t=this.mouseButtons.RIGHT;break;default:t=-1}switch(t){case Lr.DOLLY:if(this.enableZoom===!1)return;this._handleMouseDownDolly(e),this.state=fe.DOLLY;break;case Lr.ROTATE:if(e.ctrlKey||e.metaKey||e.shiftKey){if(this.enablePan===!1)return;this._handleMouseDownPan(e),this.state=fe.PAN}else{if(this.enableRotate===!1)return;this._handleMouseDownRotate(e),this.state=fe.ROTATE}break;case Lr.PAN:if(e.ctrlKey||e.metaKey||e.shiftKey){if(this.enableRotate===!1)return;this._handleMouseDownRotate(e),this.state=fe.ROTATE}else{if(this.enablePan===!1)return;this._handleMouseDownPan(e),this.state=fe.PAN}break;default:this.state=fe.NONE}this.state!==fe.NONE&&this.dispatchEvent(Gm)}function Iw(e){switch(this.state){case fe.ROTATE:if(this.enableRotate===!1)return;this._handleMouseMoveRotate(e);break;case fe.DOLLY:if(this.enableZoom===!1)return;this._handleMouseMoveDolly(e);break;case fe.PAN:if(this.enablePan===!1)return;this._handleMouseMovePan(e);break}}function Bw(e){this.enabled===!1||this.enableZoom===!1||this.state!==fe.NONE||(e.preventDefault(),this.dispatchEvent(Gm),this._handleMouseWheel(this._customWheelEvent(e)),this.dispatchEvent(Fx))}function Fw(e){this.enabled===!1||this.enablePan===!1||this._handleKeyDown(e)}function Hw(e){switch(this._trackPointer(e),this._pointers.length){case 1:switch(this.touches.ONE){case xr.ROTATE:if(this.enableRotate===!1)return;this._handleTouchStartRotate(e),this.state=fe.TOUCH_ROTATE;break;case xr.PAN:if(this.enablePan===!1)return;this._handleTouchStartPan(e),this.state=fe.TOUCH_PAN;break;default:this.state=fe.NONE}break;case 2:switch(this.touches.TWO){case xr.DOLLY_PAN:if(this.enableZoom===!1&&this.enablePan===!1)return;this._handleTouchStartDollyPan(e),this.state=fe.TOUCH_DOLLY_PAN;break;case xr.DOLLY_ROTATE:if(this.enableZoom===!1&&this.enableRotate===!1)return;this._handleTouchStartDollyRotate(e),this.state=fe.TOUCH_DOLLY_ROTATE;break;default:this.state=fe.NONE}break;default:this.state=fe.NONE}this.state!==fe.NONE&&this.dispatchEvent(Gm)}function Gw(e){switch(this._trackPointer(e),this.state){case fe.TOUCH_ROTATE:if(this.enableRotate===!1)return;this._handleTouchMoveRotate(e),this.update();break;case fe.TOUCH_PAN:if(this.enablePan===!1)return;this._handleTouchMovePan(e),this.update();break;case fe.TOUCH_DOLLY_PAN:if(this.enableZoom===!1&&this.enablePan===!1)return;this._handleTouchMoveDollyPan(e),this.update();break;case fe.TOUCH_DOLLY_ROTATE:if(this.enableZoom===!1&&this.enableRotate===!1)return;this._handleTouchMoveDollyRotate(e),this.update();break;default:this.state=fe.NONE}}function Vw(e){this.enabled!==!1&&e.preventDefault()}function Xw(e){e.key==="Control"&&(this._controlActive=!0,this.domElement.getRootNode().addEventListener("keyup",this._interceptControlUp,{passive:!0,capture:!0}))}function kw(e){e.key==="Control"&&(this._controlActive=!1,this.domElement.getRootNode().removeEventListener("keyup",this._interceptControlUp,{passive:!0,capture:!0}))}function Ao(e,t){return[e[0]+t[0],e[1]+t[1]]}function ar(e,t){return[e[0]*t[0]-e[1]*t[1],e[0]*t[1]+e[1]*t[0]]}function Yw(e){return Math.hypot(e[0],e[1])}function yu(e,t){const n=Math.hypot(e[0],e[1]);if(n===0)return[0,0];const i=Math.atan2(e[1],e[0]),a=Math.log(n),s=t[0]*a-t[1]*i,r=t[1]*a+t[0]*i,o=Math.exp(s);return[o*Math.cos(r),o*Math.sin(r)]}const xu=[1];function qw(e){for(let t=xu.length;t<=e;t++)xu[t]=xu[t-1]*t;return xu[e]}const Ww=[1,-.5,1/6,0,-1/30,0,1/42,0,-1/30,0,5/66,0,-691/2730,0,7/6,0,-3617/510];function Oo(e){let i=[0,0];for(let h=1;h<40;h++)i=Ao(i,yu([h,0],[-e[0],-e[1]]));const a=[40,0],s=(e[0]-1)*(e[0]-1)+e[1]*e[1];if(s===0)return[1/0,0];const r=[(e[0]-1)/s,-e[1]/s];let o=ar(r,yu(a,[1-e[0],-e[1]]));o=Ao(o,ar([.5,0],yu(a,[-e[0],-e[1]])));let l=[1,0],u=[0,0];for(let h=1;h<=8;h++){l=ar(l,[e[0]+2*h-2,e[1]]),l=ar(l,[e[0]+2*h-1,e[1]]);const p=Ww[2*h]/qw(2*h);u=Ao(u,ar([p,0],ar(l,yu(a,[1-e[0]-2*h,-e[1]]))))}return Ao(i,Ao(o,u))}function jw(){const e=Oo([2,0]),t=Oo([4,0]),n=Oo([.5,0]),i=Oo([.5,14.134725142]);return{z2:e[0],z2err:Math.abs(e[0]-Math.PI*Math.PI/6),z4:t[0],z4err:Math.abs(t[0]-Math.pow(Math.PI,4)/90),zh:n[0],zherr:Math.abs(n[0]+1.4603545088095868),zcrit:Yw(i)}}const Zw=[14.134725142,21.022039639,25.01085758,30.424876126,32.935061588,37.586178159,40.918719012,43.327073281,48.005150881,49.773832478,52.970321478,56.446247697,59.347044003,60.831778525,65.112544048];function Kw(e){const t=e.clientWidth||800,n=e.clientHeight||600,i=new Tw;i.background=new Ht(0);const a=new $n(50,t/n,.1,500);a.position.set(26,20,30);const s=new Ew({antialias:!0});s.setSize(t,n),s.setPixelRatio(Math.min(window.devicePixelRatio||1,2)),e.appendChild(s.domElement);const r=m=>{m.preventDefault()},o=()=>{s.render(i,a)};s.domElement.addEventListener("webglcontextlost",r),s.domElement.addEventListener("webglcontextrestored",o);const l=new Nw(a,s.domElement);l.enableDamping=!0;const u=new Cw(16777215,.55);i.add(u);const h=new Rw(16777215,1.1);h.position.set(30,40,25),i.add(h);let p=0;const f=()=>{p=requestAnimationFrame(f),l.update(),s.render(i,a)};f();const d=new Set([u,h]),v=()=>{const m=e.clientWidth,c=e.clientHeight;m>0&&c>0&&(a.aspect=m/c,a.updateProjectionMatrix(),s.setSize(m,c))};window.addEventListener("resize",v);const y=m=>{var c;(c=m.traverse)==null||c.call(m,_=>{var g,x,C,R;(x=(g=_.geometry)==null?void 0:g.dispose)==null||x.call(g),Array.isArray(_.material)?_.material.forEach(b=>{var w;return(w=b.dispose)==null?void 0:w.call(b)}):(R=(C=_.material)==null?void 0:C.dispose)==null||R.call(C)})};return{scene:i,camera:a,renderer:s,controls:l,clear(){for(let m=i.children.length-1;m>=0;m--){const c=i.children[m];d.has(c)||(i.remove(c),y(c))}},dispose(){var m,c;cancelAnimationFrame(p),window.removeEventListener("resize",v),this.clear(),l.dispose(),s.domElement.removeEventListener("webglcontextlost",r),s.domElement.removeEventListener("webglcontextrestored",o),s.dispose(),(m=s.forceContextLoss)==null||m.call(s),(c=s.domElement.parentNode)==null||c.removeChild(s.domElement)}}}function Qw(e,t=18,n=.5,i=4,a=96){e.clear();let s=a;const r=()=>(s=(s*1103515245+12345)%2147483648)/2147483648,o=[];for(let d=0;d<i;d++)o.push([1+r()*(t-1),1+r()*(t-1)]);const l=new Lo,u=new af({color:2899558}),h=[];for(let d=0;d<t;d++)for(let v=0;v<t;v++)h.push(new P(d,0,v),new P(d+1,0,v)),h.push(new P(d,0,v),new P(d,0,v+1));l.add(new Ix(new wn().setFromPoints(h),u));const p=new co(.22,1,.22);for(let d=0;d<t;d++)for(let v=0;v<t;v++){const y=2*Math.PI*n*(v+1)%(2*Math.PI),m=y/(2*Math.PI),c=new Os({color:new Ht().setHSL(m,.75,.55)}),_=.4+.9*Math.abs(Math.sin(y)),g=new En(p,c);g.position.set(v,_/2,d),g.scale.y=_,l.add(g)}const f=new Fm(.5,1.6,20);for(const[d,v]of o){const y=new En(f,new Os({color:16733491}));y.position.set(v,1.4,d),l.add(y)}return e.scene.add(l),e.camera.position.set(t*1.3,t,t*1.5),e.controls.target.set(t/2,0,t/2),{vortices:o}}function Jw(e,t=6,n=1.9){e.clear();const i=72,a=new Cl(2*t,2*t,i,i);a.rotateX(-Math.PI/2);const s=a.attributes.position,r=[];for(let u=0;u<s.count;u++){const h=s.getX(u),p=s.getZ(u),f=Math.hypot(h,p),d=n*f*(f<=t?1:0);s.setY(u,d);const v=Math.min(1,Math.abs(d)/(n*t)),y=new Ht().setHSL(d>=0?.58:0,.8,.35+.35*v);r.push(y.r,y.g,y.b)}a.setAttribute("color",new We(r,3)),a.computeVertexNormals();const o=new En(a,new Os({vertexColors:!0,side:pi,wireframe:!1,transparent:!0,opacity:.92}));e.scene.add(o);const l=new ww(2*t,12,2241365,1713216);l.position.y=-.01,e.scene.add(l),e.camera.position.set(9,7,11),e.controls.target.set(0,0,0)}function $w(e,t=40,n=81,i=240){e.clear();let a=0;const s=n*i,r=new wn,o=new Float32Array(s*3),l=new Float32Array(s*3),u=[],h=[],p=[],f=[];for(let c=0;c<n;c++)for(let _=0;_<i;_++){const g=c/(n-1)*1.2,x=_/(i-1)*t,C=Oo([g,x]),R=Math.hypot(C[0],C[1]);a=Math.max(a,R),h.push(g),p.push(x),f.push(R)}for(let c=0;c<h.length;c++){o[3*c]=h[c]-.6,o[3*c+1]=Math.min(f[c],6),o[3*c+2]=p[c]-t/2;const _=Math.min(.85,f[c]/3),g=new Ht().setHSL(.62-.62*_,.85,.28+.4*_);l[3*c]=g.r,l[3*c+1]=g.g,l[3*c+2]=g.b}for(let c=0;c<n-1;c++)for(let _=0;_<i-1;_++){const g=c*i+_,x=g+1,C=g+i,R=C+1;u.push(g,C,x,x,C,R)}r.setAttribute("position",new si(o,3)),r.setAttribute("color",new si(l,3)),r.setIndex(u),r.computeVertexNormals();const d=new En(r,new Os({vertexColors:!0,side:pi}));e.scene.add(d);const v=new af({color:16766282}),y=[new P(-.1,0,-t/2),new P(-.1,0,t/2)];e.scene.add(new zx(new wn().setFromPoints(y),v));const m=new Hm(.22,16,16);for(const c of Zw){if(c>t)break;const _=new En(m,new Os({color:16724821}));_.position.set(-.1,.05,c-t/2),e.scene.add(_)}return e.camera.position.set(4.5,7,22),e.controls.target.set(-.1,1.2,0),{eMax:a}}const t3=[["hofstadter","Hofstadter lattice"],["dirac","Dirac cone"],["zeta","ζ critical strip"]];function e3(){try{const e=document.createElement("canvas");return!!(window.WebGLRenderingContext&&(e.getContext("webgl2")||e.getContext("webgl")))}catch{return!1}}function n3(){const e=Pn.useRef(null),t=Pn.useRef(null),[n,i]=Pn.useState("hofstadter"),[a,s]=Pn.useState(.5),[r,o]=Pn.useState(4),[l,u]=Pn.useState(""),[h,p]=Pn.useState(null),[f,d]=Pn.useState("");return Pn.useEffect(()=>{p(jw())},[]),Pn.useEffect(()=>{if(e.current){if(!e3()){d("WebGL is not available in this browser or environment. The 3D laboratory needs hardware (or software) WebGL — try Chrome, Firefox or Safari with hardware acceleration enabled.");return}try{t.current=Kw(e.current)}catch(v){d(`Failed to initialize the WebGL renderer — ${v.message}`);return}return()=>{t.current&&t.current.dispose(),t.current=null}}},[]),Pn.useEffect(()=>{const v=t.current;if(!(!v||f))try{if(n==="hofstadter"){const{vortices:y}=Qw(v,18,a,r);u(`Lattice 18×18, α = ${a}, ${y.length} vortices (red cones, q=+1). Site bars are colored by the Landau phase 2πα·j — the GUE mechanism of the suite is the vortex phase field (:monumental gauge).`)}else n==="dirac"?(Jw(v,6,1.9),u("Dirac cone E(k) = v_F·|k| at α = 1/2 (vortex q=+1): the chiral tower of suite tests 19/30, v_F(2π) = 1.9.")):($w(v,40,61,200),u(`|ζ(σ+it)| for σ ∈ [0, 1.2], t ∈ [0, 40] — the critical strip (3D-34). Yellow line: Re s = 1/2; red spheres: embedded zeros γ₁..γ₁₅. JS ζ-evaluator self-check: |ζ(2)−π²/6| = ${h?h.z2err.toExponential(2):"…"}.`))}catch(y){d(`Failed to build the "${n}" scene — ${(y==null?void 0:y.message)||y}. Reload the page; if it persists, try another browser.`)}},[n,a,r,h,f]),Kt.jsxs("div",{className:"app",children:[Kt.jsx("a",{className:"skip-link",href:"#main",children:"Skip to content"}),Kt.jsxs("header",{className:"hero",children:[Kt.jsx("p",{className:"kicker",children:"AB-Cloud · 3D laboratory"}),Kt.jsx("h1",{children:Kt.jsxs("span",{className:"grad",children:["The lattice, the cone and the strip:",Kt.jsx("br",{}),"experiments 3D-1…3D-34, live"]})}),Kt.jsxs("p",{className:"sub",children:["Hofstadter lattice with vortices · Dirac cone · ζ critical strip —",Kt.jsx("b",{children:" WebGL and Three.js, computed in real time"}),". Every scene is procedural: no prebaked pictures, no server."]})]}),Kt.jsx("div",{className:"tabbar-wrap",children:Kt.jsx("nav",{className:"tabbar","aria-label":"Scenes",children:t3.map(([v,y])=>Kt.jsx("button",{className:n===v?"btn active":"btn","aria-current":n===v?"true":void 0,onClick:()=>i(v),children:y},v))})}),n==="hofstadter"&&Kt.jsxs("div",{className:"controls",children:[Kt.jsxs("label",{children:["α = ",Kt.jsx("span",{className:"val",children:a.toFixed(2)}),Kt.jsx("input",{type:"range",min:"0",max:"1",step:"0.05",value:a,onChange:v=>s(+v.target.value)})]}),Kt.jsxs("label",{children:["vortices = ",Kt.jsx("span",{className:"val",children:r}),Kt.jsx("input",{type:"range",min:"0",max:"12",value:r,onChange:v=>o(+v.target.value)})]})]}),Kt.jsxs("main",{id:"main",children:[Kt.jsx("div",{ref:e,className:"canvas-host"}),f&&Kt.jsx("p",{className:"gl-error",role:"alert",children:f}),!f&&Kt.jsx("p",{className:"info",children:l})]}),Kt.jsxs("footer",{children:[Kt.jsxs("div",{className:"links",children:[Kt.jsx("a",{href:"https://github.com/wild8highlander/ab-cloud-research",target:"_blank",rel:"noopener",children:"GitHub repository"}),Kt.jsx("a",{href:"https://github.com/wild8highlander/ab-cloud-research/blob/main/LICENSE",target:"_blank",rel:"noopener",children:"License"}),Kt.jsx("a",{href:"https://doi.org/10.5281/zenodo.21825394",target:"_blank",rel:"noopener",children:"Zenodo DOI"}),Kt.jsx("a",{href:"/",children:"Portal home"})]}),Kt.jsxs("div",{children:["Source: ",Kt.jsx("code",{children:"apps/ab-cloud-lab3d/"})," (React 19 + Vite + Three.js). ζ evaluator: self-anchored Euler–Maclaurin (port of 3D-34); check anchors ζ(2)=π²/6, ζ(4)=π⁴/90, ζ(1/2)≈−1.4603545."]})]})]})}Sb.createRoot(document.getElementById("root")).render(Kt.jsx(n3,{}));
